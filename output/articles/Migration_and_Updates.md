---
title: "Migration and Updates"
subtitle: "WebFM migration and updates"
knowledge_base: "Globalization Help Center"
category: "WebFM"
subcategory: "Overview"
language: "en"
keywords: "webfm"
status: "PUBLISHED"
archived: "false"
last_modified: "1749606167789"
source_url: "https://help.straker.ai/en/g11n/webfm/migration-and-updates"
exported_at: "2026-03-17T10:52:05Z"
---

# Migration and Updates

### Migration

- Migration date: 2025-02-07
- Production new URL: <https://webfm.straker.global/webapp/webfmx/jsp/welcome.jsp>
- GitHub credentials are migrated to File Access service
- WebFM data is migrated from DB2 database to IBM Cloud MySQL database

### Major Updates

- WebFM uses IBM Cloud AppID service for user authentication.
- WebFM accesses GitHub repository through File Access service.
  - File Access service is managed and maintained by IBM or other service provider. It provides features such as GitHub credential management, COS file access and GitHub repository access.
- RTC repository is not accessible from WebFM or File Access service.

### Features introduction

#### Reset AppID user password (Not W3ID password)

1. When user opens WebFM main page in browser and redirects to login page, click 'Forgot password' link.

   ![appid-login](https://20462040.fs1.hubspotusercontent-na1.net/hubfs/20462040/knowledge-base-files/webfm/appid-login.png)
2. Input user's Email which is used in WebFM and click 'Reset password'.

   ![appid-resetpw](https://20462040.fs1.hubspotusercontent-na1.net/hubfs/20462040/knowledge-base-files/webfm/appid-resetpw.png)
3. Follow the instruction in email to reset user password.

### 

#### Setup GitHub repository connection

1. Go to <https://file-access.g11n.ibm.com/webfm> by clicking a link in WebFM or opening it directly in web browser.
2. Check GitHub credentials list or add a new credential.

   ![git-cred-mg](https://20462040.fs1.hubspotusercontent-na1.net/hubfs/20462040/knowledge-base-files/webfm/git-cred-mg.png)
3. Go to or refresh WebFM application configuration page, check Git Credential option in repository connection setup.

   ![git-cred-sel](https://20462040.fs1.hubspotusercontent-na1.net/hubfs/20462040/knowledge-base-files/webfm/git-cred-sel.png)
4. Click Test Connection to verify the credential access.

   ![git-repo-test](https://20462040.fs1.hubspotusercontent-na1.net/hubfs/20462040/knowledge-base-files/webfm/git-repo-test.png)
