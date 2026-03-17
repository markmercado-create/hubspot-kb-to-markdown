---
title: "Large File Check Mechanism"
knowledge_base: "Globalization Help Center"
category: "IdHub"
language: "en"
keywords: "IdHub"
status: "PUBLISHED"
archived: "false"
last_modified: "1758866618151"
source_url: "https://help.straker.ai/en/g11n/large-file-check-mechanism"
exported_at: "2026-03-17T11:35:24Z"
---

# Large File Check Mechanism

### Background:

Based on past observations, there have occasionally been cases where large files that do not require translation were mistakenly submitted for translation. To help reduce unnecessary machine translation costs, IDhub Orchestration has introduced a large-file validation mechanism. Whenever a file in a request exceeds 1 MB, we will first contact the user by email to confirm whether the file truly requires translation or was submitted in error, and then proceed accordingly.

##### Operation:

1. If the request was submitted by mistake, it will be deleted.
2. If the request is valid, blocked large-file requests will be released for processing.
3. In addition, we have exception rules in place, such as bypassing size checks for certain file types or for specific PIDs.
