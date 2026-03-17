---
title: "How to handle FAILED (chkpii: Unknown single quote handling for this file. Special NLS_MESSAGEFORMAT comment must be added.)?"
knowledge_base: "Globalization Help Center"
category: "Globalization Pipeline"
subcategory: "resource filter"
language: "en"
status: "DRAFT"
archived: "false"
last_modified: "1742760086211"
source_url: "https://help.straker.ai/en/g11n/how-to-handle-failed-chkpii-unknown-single-quote-handling-for-this-file.-special-nls_messageformat-comment-must-be-added"
exported_at: "2026-03-17T11:33:20Z"
---

# How to handle FAILED (chkpii: Unknown single quote handling for this file. Special NLS_MESSAGEFORMAT comment must be added.)?

NLS\_MESSAGEFORMAT comment was proprietary comment used by legacy translation tools. chkpii can be still used, but it's out of date. Stock GP properties filter is equivalent to old NLS\_MESSAGEFORMAT\_VAR by default. With an extra option, it can also support NLS\_MESSAGEFORMAT\_ALL. This was a markup table feature. In the new process, it's GP resource filter's behavior. Because there are no more developers who can work on markup table/resource filter in IBM, IBM teams are responsible to extract translatable strings from PII resource properly on going forward. We have no plan to release new version of chkpii. It's simply deprecated at this point.

chkpii is not mandatory in current process. You can check `Include ChkPII Failed Files in Package` option on WebFM - Dispatcher page, if you want to ignore chkpii error.
