This project can be used to crawl issues and PRs from GitHub warehouses, store them in data, extract closed issues information and store them in the detail folder, and randomly select issues and store them in the issues table.

At first, prepare data.xlsx and a folder named 'detail'.
Then, use githubIssue.py to crawl data.
After this, you can run issueDetail.py to filter closed issues data and store it in the detail folder, with an excel sheet for each issue.

We can also use randomExtract.py to select a specified number of issues and save them in an excel table, checkRepeat.py is used to check whether there are duplicates in the table.
