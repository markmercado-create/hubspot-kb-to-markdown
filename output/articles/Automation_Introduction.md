---
title: "Automation Introduction"
subtitle: "What is WebFM Automation"
knowledge_base: "Globalization Help Center"
category: "WebFM"
subcategory: "Automation(Beta)"
language: "en"
keywords: "webfm"
status: "DRAFT"
archived: "false"
last_modified: "1749606938674"
source_url: "https://help.straker.ai/en/g11n/webfm/automation-introduction"
exported_at: "2026-03-17T10:52:05Z"
---

# Automation Introduction

WebFM Automation is a new extension of WebFM, to help development team to achieve automatic globalization and translation process.

With a simple yaml file, you can trigger WebFM Automation through webhook and perform the tasks in DevOps workflow:

- extract new and changed PII files
- perform checks (chkpii, eslint, gencat)
- import/export translation bundle
- modify text content
- rename files
- change file encoding
- create pseudo translation
- commit translated file to Github
- create PullRequest(Github), MergeRequest(Gitlab)

The settings are configured mostly through the build configuration which is stored in the file `i18n.yaml` in your repository. That allows your configuration to be version controlled and flexible. Detailed information about the config format can be found in i18n.yaml ConfigReference.
