---
title: "Migration Checklist"
subtitle: "WebFM migration checklist"
knowledge_base: "Globalization Help Center"
category: "WebFM"
subcategory: "Overview"
language: "en"
keywords: "webfm"
status: "PUBLISHED"
archived: "false"
last_modified: "1749606206466"
source_url: "https://help.straker.ai/en/g11n/webfm/migration-checklist"
exported_at: "2026-03-17T10:52:04Z"
---

# Migration Checklist

### Checklist

#### 1. User login

- Go to <https://webfm.straker.global/webapp/webfmx/jsp/welcome.jsp> then redirect to AppID login page
- Click 'Forgot password' link

  ![appid-login](https://20462040.fs1.hubspotusercontent-na1.net/hubfs/20462040/knowledge-base-files/webfm/appid-login.png)
- Input user's IBM Email which is used in WebFM and click 'Reset password'

  ![appid-resetpw](https://20462040.fs1.hubspotusercontent-na1.net/hubfs/20462040/knowledge-base-files/webfm/appid-resetpw.png)
- Follow the instruction in email to reset user password
- Login WebFM

#### 2. Very project access

- Click drop down list and check project list the new environment

  ![proj-selection](https://20462040.fs1.hubspotusercontent-na1.net/hubfs/20462040/knowledge-base-files/webfm/proj-selection.png)
- Verify project list is the same project list in original environment

#### 3. Verify GitHub repository access

- Select one project- Click Application Configuration
- Click one application in application list
- Click 'Test Connection' in Source Repository configuration, and verify the connection

  ![git-test-source](https://20462040.fs1.hubspotusercontent-na1.net/hubfs/20462040/knowledge-base-files/webfm/git-test-source.png)
- Click 'Test Connection' in Target Repository configuration, and verify the connection

  ![git-test-target](https://20462040.fs1.hubspotusercontent-na1.net/hubfs/20462040/knowledge-base-files/webfm/git-test-target.png)
- If test connection fails, please refer setup GitHub repository connection manually

### Setup GitHub repository connection

Go to <https://file-access.g11n.ibm.com/webfm> by clicking ‘Add/Edit‘ link in WebFM repository configuration panel or opening it directly in web browser.

Check GitHub credentials list or add a new credential.

![git-cred-mg](https://20462040.fs1.hubspotusercontent-na1.net/hubfs/20462040/knowledge-base-files/webfm/git-cred-mg.png)

Go to or `refresh` WebFM application configuration page, check Git Credential option in repository connection setup.

![git-cred-sel](https://20462040.fs1.hubspotusercontent-na1.net/hubfs/20462040/knowledge-base-files/webfm/git-cred-sel.png)

Click Test Connection to verify the credential access.

![git-test-source](https://20462040.fs1.hubspotusercontent-na1.net/hubfs/20462040/knowledge-base-files/webfm/git-test-source.png)

![git-test-target](https://20462040.fs1.hubspotusercontent-na1.net/hubfs/20462040/knowledge-base-files/webfm/git-test-target.png)
