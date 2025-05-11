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
 
         if "issues" in data and data["issues"]:
             all_issues.extend(data["issues"])
 
             if len(data["issues"]) < max_results:
                 break
             start_at += max_results
         else:
             print("✅ No more issues found.")
             break
     else:
         print(f"❌ Failed with status code: {response.status_code}")
         print(response.text)
         break
 
 if all_issues:
     issues_df = pd.json_normalize(all_issues)
 
     if 'fields.project.key' in issues_df.columns:
         project_keys = issues_df['fields.project.key'].unique().tolist()
         print("\n✅ Found Project Keys:", project_keys)
 
         project_data = []
 
         for key in project_keys:
             project_url = f"{base_url}/rest/api/3/project/{key}"
             project_response = requests.get(
                 project_url,
                 headers={"Accept": "application/json"},
                 auth=HTTPBasicAuth(email, api_token)
             )
 
             if project_response.status_code == 200:
                 project_details = project_response.json()
                 project_data.append(project_details)
             else:
                 print(f"❌ Failed to fetch details for project: {key}")
 
         if project_data:
             project_df = pd.json_normalize(project_data)
 
             print("\n✅ Project Details:")
             pd.set_option("display.max_rows", None)
             pd.set_option("display.max_columns", None)
             pd.set_option("display.width", 1000)
             pd.set_option("display.max_colwidth", None)
 
             display(project_df)
 
         else:
             print("\n❌ No project details found.")
     else:
         print("\n❌ 'fields.project.key' column not found in the data.")
 else:
     print("\n❌ No issues found.")