---
title: "Setup File Repository (Git)"
knowledge_base: "Globalization Help Center"
category: "WebFM"
subcategory: "Project Setup"
language: "en"
keywords: "webfm"
status: "PUBLISHED"
archived: "false"
last_modified: "1749606206752"
source_url: "https://help.straker.ai/en/g11n/webfm/setup-file-repository-git"
exported_at: "2026-03-17T10:52:05Z"
---

# Setup File Repository (Git)

- Step 1: select the project and click **Select**
- Step 2: go to **Application Config** and click **Add new Application**
- Step 3: input **Application Name**, which should start with a letter and subsequent with letters, digits, dashes or underscores
- Step 4: select **Git** for **Application Type  
  ![new-app-type-git](https://20462040.fs1.hubspotusercontent-na1.net/hubfs/20462040/knowledge-base-files/webfm/new-app-type-git.png)**
- Step 5: click **+Add Source Repository (Pre-Translation)** to input English PII files repository information  
  ![app-source-repo](https://20462040.fs1.hubspotusercontent-na1.net/hubfs/20462040/knowledge-base-files/webfm/app-source-repo.png)

**Example:** here is an example of where you can get the required information from Git

1. Source Git Repo: `https://github.ibm.com/APM/AMUI_Resource_Pages`
2. Git Branch Name: `develop`
3. Git Credential: Select Git Credential and click **Test Connection** to ensure the access
4. If there is no option for Git Credential selection, click **Add/Edit** to create Git Credential with user email account. Then refresh the application creation page and select Git Credential
5. Select **PII File List** for "Files to be Extracted". Then setup "PII File List" later.

- Step 6: click **+Add Target Repository (Post-Translation)** to input translation files repository information
- Step 7: input the required information, or click **Copy from SrcRepo** if the repository information is identical to the English files repository information
- Step 8: **Create Pull Request?**, if yes, input your Git repository in **Git Repo for Commit Branch**. WebFM will create a temporary branch in your Git repository automatically.
- Step 9: select if you'd like to create a merged PR during one check-in or create different PR for each language
- Step 10: if your pull request requires reviewer, you can set the reviewer at **Advanced Options** field  
  ![app-target-repo](https://20462040.fs1.hubspotusercontent-na1.net/hubfs/20462040/knowledge-base-files/webfm/app-target-repo.png)
- Step 11: click **Save** to save the application settings
