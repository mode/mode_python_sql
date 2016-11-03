# mode_python_sql
This script allows users to download a CSV of raw SQL from queries in a report.


# Steps to use this script:

1.  In Mode, generate API token (under Settings -> Your Name -> API Tokens).
2.  Add the token and password values to the python.properties file.
3.  Run this script using: 
    `python demo.py -org={{organization_username}} -reporttoken={{report_token}}`

For example, for this report https://modeanalytics.com/modeanalytics/reports/eb7e7c23e72f I would run:

`python demo.py -org=modeanalytics -reporttoken=eb7e7c23e72f`


