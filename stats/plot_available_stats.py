from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt

STATS_DIR = Path(__file__).parent
DOCS_DIR = STATS_DIR.parent / "docs"
STATS_DATA_DIR = STATS_DIR / "data"
DOCS_STATIC_DIR = DOCS_DIR / "_static"

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


    # =====================================================

    # Plot 1 total download
    plt.figure()
    plt.title("Total nb downloads per package since 2016")
    downloads_totals = downloads_df.sum(axis=0).sort_values(ascending=False)
    # for p_old, p_new in OBSOLETES.items():
    #     downloads_totals[p_new] += downloads_totals[p_old]
    #     del downloads_totals[p_old]
    all_projects_incl_refs_and_obsoletes_sorted = list(downloads_totals.index)
    all_projects_incl_obsoletes_sorted = [p for p in all_projects_incl_refs_and_obsoletes_sorted if p in ALL_PROJECTS_INCL_OBSOLETES]
    assert set(all_projects_incl_obsoletes_sorted) == set(ALL_PROJECTS_INCL_OBSOLETES)
    ax = downloads_totals[all_projects_incl_obsoletes_sorted].plot.bar(rot=45)
    plt.xticks(ha='right')

    # Plot 2 yearly totals
    plt.figure()
    plt.title("Open Source Libs - Total nb downloads per year")
    downloads_yearly_total = downloads_yearly_df[all_projects_incl_obsoletes_sorted].sum(axis=1)
    # Remove last (incomplete) year
    downloads_yearly_total = downloads_yearly_total.iloc[:-1]
    downloads_yearly_total.plot.bar(rot=0)
    plt.savefig(DOCS_STATIC_DIR / "YearlyTotals.png")

    # Plot 3 ----------
    # cumulative timeseries of downloads
    downloads_cumulative = downloads_df.cumsum()
    # for p_old, p_new in OBSOLETES.items():
    #     downloads_cumulative[p_new] += downloads_cumulative[p_old]
    #     del downloads_cumulative[p_old]
    downloads_totals2 = downloads_cumulative.iloc[-1,:].sort_values(ascending=False)
    last_date = downloads_totals2.name
    downloads_totals2.name = None
    pd.testing.assert_series_equal(downloads_totals, downloads_totals2)

    projects_by_tot_download_desc2 = list(downloads_totals2.index)

    # downloads_cumulative.iloc[:, 2:].plot()
    downloads_cumulative[all_projects_incl_obsoletes_sorted].plot()
    plt.title("Cumulative nb downloads over time - per package")
    # better would be to have the text on the last point of the curve
    for proj in all_projects_incl_obsoletes_sorted:
        plt.text(last_date, downloads_totals2[proj], proj)

    # Plot 3bis same but not cumulated
    downloads_df[all_projects_incl_obsoletes_sorted].plot()
    plt.title("Monthly nb downloads - per package")
    last_month_dwnload = downloads_df.iloc[-1,:].sort_values(ascending=False)
    last_date = last_month_dwnload.name
    # better would be to have the text on the last point of the curve
    for proj in all_projects_incl_obsoletes_sorted:
        plt.text(last_date, last_month_dwnload[proj], proj)
    plt.savefig(DOCS_STATIC_DIR / "MonthlyPerPkgTotals.png")

    # Plot 4 -----
    downloads_cumulative[all_projects_incl_obsoletes_sorted].plot.area()
    plt.title("Overall Cumulative nb downloads over time")
    val = 0
    for proj in all_projects_incl_obsoletes_sorted:
        val += downloads_totals2[proj]
        plt.text(last_date, val, proj)

    plt.show()


if __name__ == '__main__':
    plot_stats()
