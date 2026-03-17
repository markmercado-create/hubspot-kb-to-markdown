---
title: "Automation Configuration and Settings"
knowledge_base: "Globalization Help Center"
category: "WebFM"
subcategory: "Automation(Beta)"
language: "en"
keywords: "webfm"
status: "DRAFT"
archived: "false"
last_modified: "1749606923748"
source_url: "https://help.straker.ai/en/g11n/webfm/automation-configuration"
exported_at: "2026-03-17T11:29:32Z"
---

# Automation Configuration and Settings

### Assumption

1. IBM Github server as source repository
2. All PII files are supported by built-in GP resource filters or GSSC developed resource filters

### Preparation

1. Configure Project and Application on WebFM
2. Defined source PII files list, resource filters and renaming rules
3. Create GP bundles and translation baseline

### WebFM Automation App

1. Go to WebFM Automation  
2. Enable the Automation Tasks needed for your Automation workflow  

- Dispatcher
  - Extract delta PII by calculate the word count changes by CHKPII
  - Run pre-translation process
  - Update the extracted result to “Work with Eng Files” table in WebFM
- Import Eng To GP
  - Import all files from “Work with Eng Files” to GP
- Export translation to WebFM
  - List all English files in “Work with Eng Files”, and export their translation files from GP
  - Fallback to English value if translation is unreviewed
  - Run post-translation checks
- Check In to Repo
  - Run post-translation process (encoding change, rename, text-replace)

3. Use/setup one or more your Automation trigger(s)  

- Run now
- Webhook Trigger – call by Github or Jenkins
  - Go to Github settings
  - Add webhook to Github push and pull request
- TR Monitor – check TR status every 4 hours by WebFM
  - Trigger when any merge event detected
  - Wait to trigger until all languages of the file is merged
