---
title: "How to handle error \"Failed to build resource bundle. Duplicate keys detected\"?"
knowledge_base: "Globalization Help Center"
category: "Globalization Pipeline"
subcategory: "java sdk"
language: "en"
status: "DRAFT"
archived: "false"
last_modified: "1742760080389"
source_url: "https://help.straker.ai/en/g11n/how-to-handle-error-failed-to-build-resource-bundle.-duplicate-keys-detected"
exported_at: "2026-03-17T10:52:04Z"
---

# How to handle error "Failed to build resource bundle. Duplicate keys detected"?

When using GP Java tools, you might get this error:

```
ERROR: Failed to parse the resource data in /root/art_i18n_LKSAgent.js: Failed to build resource bundle. Duplicate keys detected: [databaseIsUnreachable, reportNotSaved, scheduleHasExpired, password, archived, active]
```

Resource filter parses the file (e.g., art\_i18n\_LKSAgent.js) and converts strings in file to key value pairs. It gets error when find duplicated keys. Please update/fix the js file on your own.
