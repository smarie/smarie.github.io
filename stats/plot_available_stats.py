from dataclasses import dataclass
from pathlib import Path

import pandas as pd

import plotly.graph_objects as go
import matplotlib.pyplot as plt


STATS_DIR = Path(__file__).parent
DOCS_DIR = STATS_DIR.parent / "docs"
STATS_DATA_DIR = STATS_DIR / "data"
_DOCS_STATIC_DIR = DOCS_DIR / "_static"
PLOTLY_JSONS_DIR = _DOCS_STATIC_DIR / "plotly"
PLOTLY_PNGS_DIR = _DOCS_STATIC_DIR / "pngs"

ALL_PROJECTS = [
    # TODO pydantic-tables ? pydocquery?
    'm5py',
    'mkdocs-gallery',
    'qdscreen',
    'genbadge',
    'pytest-cases',
    'pytest-harvest',
    'pytest-steps',
    'pytest-pilot',
    'doit-api',
    'fprules',
    'odsclient',
    'azmlclient',
    'getversion',
    'mixture',
    'pyfields',
    'marshmallow-pyfields',
    'autoclass',
    'vtypes',
    'valid8',
    'yamlable',
    'mini-lambda',
    'makefun',
    'decopatch',
    'spawny',
    'parsyfiles',
    'envswitch',
]
OBSOLETES = {
    'pyoad': 'spawny',
    'classtools-autocode': 'autoclass',
    'sficopaf': 'parsyfiles'
}
ALL_PROJECTS_INCL_OBSOLETES = ALL_PROJECTS + list(OBSOLETES.keys())
assert len(ALL_PROJECTS_INCL_OBSOLETES) == 29


def plot_stats():
    all_dfs_lst = []
    for f in STATS_DATA_DIR.glob("all*.csv"):
        df = pd.read_csv(f, index_col=[0])
        all_dfs_lst.append(df)

    all_dfs  = pd.concat(all_dfs_lst, axis=0)
    all_dfs['date'] = pd.to_datetime(all_dfs['yyyymm'], format="%Y-%m")  # + pd.offsets.MonthEnd(0)

    # remove last month since it is incomplete
    not_last_month = all_dfs['date'] < all_dfs['date'].max()
    all_dfs = all_dfs.loc[not_last_month]

    del all_dfs['yyyymm']
    # def map_obsoletes(val):
    #     try:
    #         return OBSOLETES[val]
    #     except KeyError:
    #         return val
    # all_dfs['project'] = all_dfs['project'].apply(map_obsoletes)
    all_dfs2 = all_dfs.set_index(['date', 'project']).unstack().sort_index()

    # merge OBSOLETES to actual name: NO, this can be used to check "phantom" downloads
    # for kpi in all_dfs2.columns.levels[0]:
    #     for p_old, p_new in OBSOLETES.items():
    #         all_dfs2[(kpi, p_new)] = all_dfs2[(kpi, p_new)] + all_dfs2[(kpi, p_old)]
    #         del all_dfs2[(kpi, p_old)]

    percent3_df = all_dfs2['percent_3'].copy()
    downloads_df = all_dfs2['download_count'].copy()
    downloads_df_legacy_merged = downloads_df.copy()
    for p_old, p_new in OBSOLETES.items():
        downloads_df_legacy_merged[p_new] += downloads_df_legacy_merged[p_old]
        del downloads_df_legacy_merged[p_old]

    # total download by year
    downloads_yearly_df = downloads_df.copy()
    downloads_yearly_df["Year"] = downloads_yearly_df.index.year
    downloads_yearly_df = downloads_yearly_df.groupby("Year").sum()


    # total downloads overall since 2016
    downloads_totals = downloads_df.sum(axis=0).sort_values(ascending=False)

    # names of 'own' and 'reference'
    all_projects_incl_refs_and_obsoletes_sorted = list(downloads_totals.index)
    all_projects_incl_obsoletes_sorted = [p for p in all_projects_incl_refs_and_obsoletes_sorted if
                                          p in ALL_PROJECTS_INCL_OBSOLETES]
    assert set(all_projects_incl_obsoletes_sorted) == set(ALL_PROJECTS_INCL_OBSOLETES)
    all_ref_projects_sorted = [p for p in all_projects_incl_refs_and_obsoletes_sorted if p not in
                               ALL_PROJECTS_INCL_OBSOLETES]
    pkg_names = PkgNames(
        all_sorted=all_projects_incl_refs_and_obsoletes_sorted,
        refs_sorted=all_ref_projects_sorted,
        own_sorted=all_projects_incl_obsoletes_sorted
    )

    # Plot 1 - totals per package since 2016
    plot1_totals_per_pkg_since_2016(downloads_totals, pkg_names=pkg_names)

    # Plot 2a - totals per year (all pkgs together)
    downloads_yearly_total = downloads_yearly_df[all_projects_incl_obsoletes_sorted].sum(axis=1)
    # Remove last (incomplete) year
    downloads_yearly_total = downloads_yearly_total.iloc[:-1]
    plot2_yearly_totals(downloads_yearly_total)

    # html_str = fig.to_html(DOCS_STATIC_DIR / "YearlyTotals.html")  # for us to check the plotly.js version
    # use this print to check that the version is still v3.0.1
    # where_idx = html_str.index("plotly.js")
    # print(html_str[where_idx-100:where_idx+100])
    # assert "plotly.js v3.0.1" in html_str
    # download and store to https://cdn.plot.ly/plotly-3.0.1.min.js

    # Plot 2b - totals per year - detailed per package
    nb_proj_highlighted = 15
    plot2b_yearly_per_pkg(downloads_yearly_df, pkg_names=pkg_names, nb_proj_highlighted=nb_proj_highlighted)

    # Plot 3 - cumulative timeseries of downloads
    downloads_cumulative = downloads_df.cumsum()
    # verify that this cumulative sum gives the same numbers per packages as our initial downloads totals
    _downloads_totals2 = downloads_cumulative.iloc[-1,:].sort_values(ascending=False)
    _downloads_totals2.name = None
    pd.testing.assert_series_equal(downloads_totals, _downloads_totals2)
    # last_date = downloads_totals2.name
    # projects_by_tot_download_desc2 = list(downloads_totals2.index)

    downloads_cumulative.iloc[:, 2:].plot()
    downloads_cumulative[all_projects_incl_obsoletes_sorted].plot()
    # plt.title("Cumulative nb downloads over time - per package")
    # better would be to have the text on the last point of the curve
    # for proj in all_projects_incl_obsoletes_sorted:
    #     plt.text(last_date, downloads_totals2[proj], proj)

    # fig = go.Figure()
    # fig.add_trace(go.Scatter(
    #     x=
    # ))

    # Plot 3bis same but not cumulated
    downloads_df[all_projects_incl_obsoletes_sorted].plot()
    plt.title("Monthly nb downloads - per package")
    last_month_dwnload = downloads_df.iloc[-1,:].sort_values(ascending=False)
    last_date = last_month_dwnload.name
    # better would be to have the text on the last point of the curve
    for proj in all_projects_incl_obsoletes_sorted:
        plt.text(last_date, last_month_dwnload[proj], proj)
    plt.savefig(_DOCS_STATIC_DIR / "MonthlyPerPkgTotals.png")

    # Plot 4 -----
    downloads_cumulative[all_projects_incl_obsoletes_sorted].plot.area()
    plt.title("Overall Cumulative nb downloads over time")
    val = 0
    for proj in all_projects_incl_obsoletes_sorted:
        val += downloads_totals[proj]
        plt.text(last_date, val, proj)

    plt.show()


@dataclass
class PkgNames:
    refs_sorted: list[str]
    own_sorted: list[str]
    all_sorted: list[str]


def plot1_totals_per_pkg_since_2016(downloads_totals, pkg_names: PkgNames):
    # Plot 1 total download
    # plt.figure()
    # plt.title("Total nb downloads per package since 2016")


    all_years_total = downloads_totals[pkg_names.own_sorted]
    all_years_total_refs = downloads_totals[pkg_names.refs_sorted]
    # ax = all_years_total.plot.bar(rot=45)
    # plt.xticks(ha='right')
    # for scope, _filter in ((all_projects_incl_obsoletes_sorted, True),
    #                       (all_projects_incl_refs_and_obsoletes_sorted, False)):
    #   all_years_total = downloads_totals[scope]
    fig = go.Figure()
    fig.add_trace(
        go.Bar(
            x=all_years_total.index,
            y=all_years_total.tolist(),
            hovertemplate="<br>".join([
                "Package: %{x}",
                "Nb downloads: %{y:d}",
            ]),
            name="own packages"
        )
    )
    fig.add_trace(
        go.Bar(
            x=all_years_total_refs.index,
            y=all_years_total_refs.tolist(),
            hovertemplate="<br>".join([
                "Package: %{x}",
                "Nb downloads: %{y:d}",
            ]),
            name="reference packages",
            visible='legendonly'
        )
    )
    _filter = True
    suffix = "" if _filter else " (compared to reference projects)"
    fig.update_layout(
        title_text=f"Total nb downloads per package since 2016{suffix}",
        yaxis_title_text="Nb downloads",
        xaxis_title_text="Package",
        xaxis={"categoryarray": pkg_names.all_sorted}
    )
    fig.show("browser")
    suffix = "" if _filter else "_WithRefs"
    fig.write_json(PLOTLY_JSONS_DIR / f"OverallTotals{suffix}.json", pretty=False)
    fig.write_image(PLOTLY_PNGS_DIR / f"OverallTotals{suffix}.png")


def plot2_yearly_totals(downloads_yearly_total):
    fig = go.Figure()
    fig.add_trace(go.Bar(
        # Convert to string to avoid the issue with xticks not displaying in the mkdocs final html
        x=downloads_yearly_total.index.astype(str),
        y=downloads_yearly_total.tolist(),
        hovertemplate="<br>".join([
            "Year: %{x}",
            "Nb downloads: %{y:d}",
        ])
    ))
    fig.update_layout(
        title_text="Python packages downloads per year",
        yaxis_title_text="Nb downloads",
        xaxis_title_text="Year",
    )
    fig.show("browser")
    fig.write_json(PLOTLY_JSONS_DIR / "YearlyTotals.json", pretty=False)
    fig.write_image(PLOTLY_PNGS_DIR / "YearlyTotals.png")


def plot2b_yearly_per_pkg(downloads_yearly_df, pkg_names: PkgNames, nb_proj_highlighted):
    highlighted_pkgs = pkg_names.own_sorted[:nb_proj_highlighted]
    rest_names = pkg_names.own_sorted[nb_proj_highlighted:]
    nb_rest_pkgs = len(rest_names)

    fig = go.Figure()
    for p in highlighted_pkgs:
        _proj_yearly_series = downloads_yearly_df[p].iloc[:-1]
        fig.add_trace(go.Bar(
            name=p,
            # Convert to string to avoid the issue with xticks not displaying in the mkdocs final html
            x=_proj_yearly_series.index.astype(str),
            y=_proj_yearly_series.tolist(),
            hovertemplate="<br>".join([
                f"Package name: {p}",
                "Year: %{x}",
                "Nb downloads: %{y:d}",
            ])
        ))

    rest_data = downloads_yearly_df[rest_names].sum(axis=1).iloc[:-1]
    fig.add_trace(go.Bar(
        name=f"Other {nb_rest_pkgs} pkgs",
        x=rest_data.index,
        y=rest_data.tolist(),
        hovertemplate="<br>".join([
            f"Package names: ({nb_rest_pkgs}) {rest_names}",
            "Year: %{x}",
            "Nb downloads: %{y:d}",
        ])
    ))
    fig.update_layout(
        barmode='stack',
        title_text="Python packages downloads per year",
        yaxis_title_text="Nb downloads",
        xaxis_title_text="Year",
    )
    fig.show("browser")
    fig.write_json(PLOTLY_JSONS_DIR / "YearlyTotalsDetails.json", pretty=False)
    fig.write_image(PLOTLY_PNGS_DIR / "YearlyTotalsDetails.png")


if __name__ == '__main__':
    plot_stats()
