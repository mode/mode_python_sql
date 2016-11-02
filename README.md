# mode_results_python
This script allows users to download PDF's from email shared reports that include PDF


# Steps to use this script:

1.  Make sure your report has run successfully at least once.
2.  In Mode, generate API token (under Settings -> Your Name -> API Tokens).
3.  Add the token and password values to the python.properties file.
4.  Modify lines 77 - 80 in demo.py to reflect the column names in your dataset.
4.  Run this script the first time using 
    `python demo.py -org={{organization_username}} -reporttoken={{report_token}}`
    You will receive an error stating no querytoken was provide but querytokens will be printed above the error with it's SQL to help you choose the correct token.  
4.  Once you've selected a querytoken, run the script using 

    `python demo.py -org={{organization_username}} -reporttoken={{report_token}} -querytoken={{query_token}}`

For example, for this report https://modeanalytics.com/modeanalytics/reports/eb7e7c23e72f I would run:

`python demo.py -org=modeanalytics -reporttoken=eb7e7c23e72f -querytoken=d832cd041c7a`


