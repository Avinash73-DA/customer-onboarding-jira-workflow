import requests
 import pandas as pd
 from requests.auth import HTTPBasicAuth
 from IPython.display import display, JSON
 
 email = ""
 api_token = ""
 base_url = ""
 
 jql = (
     'type IN (standardIssueTypes(), subTaskIssueTypes())'
     'AND (assignee IN membersOf("Customer Success and KAM") OR assignee = EMPTY)'
     'AND reporter IN membersOf("Customer Success and KAM") ORDER BY assignee DESC'
 )
 
 max_results = 100
 start_at = 0
 all_issues = []
 
 while True:
     url = f"{base_url}/rest/api/3/search"
 
     params = {
         "jql": jql,
         "maxResults": max_results,
         "startAt": start_at
     }
 
     response = requests.get(
         url,
         headers={"Accept": "application/json"},
         params=params,
         auth=HTTPBasicAuth(email, api_token)
     )
 
     if response.status_code == 200:
         data = response.json()
 
 
         display(JSON(data))
 
         if "issues" in data and data["issues"]:
             all_issues.extend(data["issues"])
 
             # Pagination handling
             if len(data["issues"]) < max_results:
                 break
             start_at += max_results
         else:
             print("No more issues found.")
             break
     else:
         print(f"Failed with status code: {response.status_code}")
         print(response.text)
         break
 
 if all_issues:
 
     issues_df = pd.json_normalize(all_issues)
 
     print("\nAll Issues Fetched and Formatted:")
     pd.set_option("display.max_rows", None)
     pd.set_option("display.max_columns", None)
     pd.set_option("display.width", 1000)
     pd.set_option("display.max_colwidth", None)
     display(issues_df)
 else:
     print("\nNo issues found.")