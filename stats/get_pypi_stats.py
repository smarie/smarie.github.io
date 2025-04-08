""" from https://langui.sh/2016/12/09/data-driven-decisions/
and bigquery doc https://googleapis.dev/python/bigquery/latest/usage/pandas.html"""
from pathlib import Path

# IMPORTANT PATH TO CREDENTIALS FILE SHOULD BE IN ENV VARIABLE GOOGLE_APPLICATION_CREDENTIALS
import pandas as pd

from os.path import exists
from google.cloud import bigquery

from plot_available_stats import ALL_PROJECTS_INCL_OBSOLETES


STATS_DATA_DIR = Path(__file__).parent / "data"
ALL_YEARS = tuple(range(2025, 2015, -1))

# Construct a BigQuery client object.
client = bigquery.Client()

ref_projects = [
    # 'scikit-learn',
    # 'scipy',
    # 'numpy',
    # 'pandas',
    # 'attrs',
    'click',
    'tabulate',
    # 'fastapi',
    # 'pydantic',
    # 'tox',
    'nox',
]

# combine all for the query
all_proj_string = "(%s)" % ", ".join(("%r" % p for p in ALL_PROJECTS_INCL_OBSOLETES + ref_projects))  # indeed we need the quotes
print(all_proj_string)


NEW_QUERY = """
    #standardSQL
    SELECT
      FORMAT_DATE("%Y-%m", timestamp) AS yyyymm,
      file.project AS project,
      ROUND(100 * SUM(CASE WHEN REGEXP_EXTRACT(details.python, r"^([^\.]+)") = "3" THEN 1 ELSE 0 END) / COUNT(*), 1) AS percent_3,
      COUNT(*) as download_count
    FROM
      `bigquery-public-data.pypi.file_downloads`
    WHERE
      file.project IN {p}
      AND DATE(timestamp)
        BETWEEN DATE('{y}-{m}-01 00:00:00+00')
            AND DATE('{y2}-{m2}-01 00:00:00+00')
    group by
      project,
      yyyymm
    ORDER BY
      yyyymm DESC
    # LIMIT 100
"""

OLD_QUERY = """
#legacySQL
    SELECT
      STRFTIME_UTC_USEC(timestamp, "%Y-%m") AS yyyymm,
      file.project AS project,
      ROUND(100 * SUM(CASE WHEN REGEXP_EXTRACT(details.python, r"^([^\.]+)") = "3" THEN 1 ELSE 0 END) / COUNT(*), 1) AS percent_3,
      COUNT(*) as download_count
    FROM
      TABLE_DATE_RANGE(
        [the-psf:pypi.downloads],
        # DATE_ADD(CURRENT_TIMESTAMP(), -5, "year"),
        TIMESTAMP('{y}-01-01 00:00:00+00'),
        TIMESTAMP('{y2}-01-01 00:00:00+00')
        # CURRENT_TIMESTAMP()
      )
    WHERE
      file.project IN {p}
    group by
      project,
      yyyymm
    ORDER BY
      yyyymm DESC
    # LIMIT 100
"""

debug_mode_explicit_query = False
if debug_mode_explicit_query:
    from_year = 2023
    from_month_included = 4
    to_year = 2023
    to_month_excluded = 5
    res = input("DEBUG MODE EXPLICIT QUERY. CONTINUE ?(y)")
    if res == "" or res.lower() == "y":
        query = NEW_QUERY.format(
            y=str(from_year), m=str(from_month_included), y2=str(to_year), m2=str(to_month_excluded), p=all_proj_string
        )
        # Set use_legacy_sql to True to use legacy SQL syntax.
        job_config = bigquery.QueryJobConfig(use_legacy_sql=False)  # set to True to use OLD_QUERY

        print("Querying for (custom) and projects %r" % all_proj_string)
        print(query)
        df = client.query(query, job_config=job_config).to_dataframe()
        print("Success. Saving to tmp.csv")

        # drop downloads for the next year 01-01 00:00:00
        df = df.drop(df.query(f"yyyymm=='{to_year:04d}-{to_month_excluded:02d}'").index)
        df.to_csv("tmp.csv")
        raise ValueError("SUCCESS!")

for year in sorted(ALL_YEARS):
    # for project in ALL_PROJECTS:
    csv_path = STATS_DATA_DIR / "all_%s.csv" % (year,)  # "%s_%s.csv" % (project, year)
    if exists(csv_path):
        # already downloaded stats, only complete what is missing (last month might be wrong)
        existing_df = pd.read_csv("all_%s.csv" % (year,), index_col=[0])
        date_col = pd.to_datetime(existing_df['yyyymm'], format="%Y-%m")  # + pd.offsets.MonthEnd(0)
        last_month = date_col.max().month
        remove_last_month = False
        if last_month == 12:
            if year > 2016 and len(date_col.dt.month.unique()) < 12:
                raise ValueError("not 12 months ?")
            res = input(f"Year {year} file seems complete, do you confirm (y)?")
            if res == "" or res.lower() == "y":
                # Move to another year
                continue
            else:
                # re-Query the last month
                remove_last_month = True
        else:
            # remove last month since it is incomplete
            res = input(f"Last Month {year}-{last_month} is assumed complete, do you confirm (y)?")
            if res == "" or res.lower() == "y":
                remove_last_month = False
            else:
                remove_last_month = True

        if remove_last_month:
            # Rewrite the last month
            not_last_month = date_col < date_col.max()
            existing_df = existing_df.loc[not_last_month]
            start_at_month = last_month
        else:
            start_at_month = last_month + 1
    else:
        existing_df = None
        start_at_month = 1

    # Create query
    if start_at_month < 12:
        next_year = year
        next_month = start_at_month + 1
    else:
        next_year = year+1
        next_month = 1

    query = NEW_QUERY.format(
        y=str(year), m=str(start_at_month), y2=str(next_year), m2=str(next_month), p=all_proj_string
    )

    # Set use_legacy_sql to True to use legacy SQL syntax.
    job_config = bigquery.QueryJobConfig(use_legacy_sql=False) # set to True to use OLD_QUERY

    # Start the query, passing in the extra configuration.
    # query_job = client.query(query, job_config=job_config)  # Make an API request.
    #
    # print("The query data:")
    # for row in query_job:
    #     print(row)

    print("Querying for year %s and projects %r" % (year, all_proj_string))
    print(query)
    df = client.query(query, job_config=job_config).to_dataframe()
    print("Success. Saving the results table")

    # drop downloads for the next year 01-01 00:00:00
    df = df.drop(df.query("yyyymm=='%04d-%02d'" % (next_year, next_month)).index)
    if existing_df is not None:
        df = pd.concat([df, existing_df], axis=0)
        assert not df.duplicated().any()

    df.to_csv(csv_path)


# other sources
# from https://github.com/ofek/pypinfo/blob/master/README.rst
# pypinfo --auth "C:\_dev\python_ws\_ProjectsToFocus\pypi_stats\pypinfo-a799dc4f0bbf.json"
#
# import pypistats
#
#
# if __name__ == '__main__':
#     # Show overall downloads over time, excluding mirrors
#     data = pypistats.overall("makefun", total=True, format="pandas")
#     data = data.groupby("category").get_group("without_mirrors").sort_values("date")
#
#     chart = data.plot(x="date", y="downloads", figsize=(10, 2))
#     chart.figure.show()
#     chart.figure.savefig("overall.png")  # alternatively
