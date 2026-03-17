---
title: "What is the new string that was added to the file not present in the translations?"
knowledge_base: "Globalization Help Center"
category: "WebFM"
language: "en"
status: "DRAFT"
archived: "false"
last_modified: "1742760067649"
source_url: "https://help.straker.ai/en/g11n/what-is-the-new-string-that-was-added-to-the-file-not-present-in-the-translations"
exported_at: "2026-03-17T11:30:13Z"
---

# What is the new string that was added to the file not present in the translations?

There are two duplicated keys `provisioning.vsi.volumes` at line 156 and line 204.  
Then WebFM exported only one `provisioning.vsi.volumes` at line 156 in the translated json file. Those two duplicate keys in the English file would mess things up.
