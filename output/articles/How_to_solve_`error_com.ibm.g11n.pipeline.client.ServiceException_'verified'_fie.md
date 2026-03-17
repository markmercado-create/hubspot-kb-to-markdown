---
title: "How to solve `error: com.ibm.g11n.pipeline.client.ServiceException: 'verified' field cannot be set to true because reviewed field is not true.`?"
knowledge_base: "Globalization Help Center"
category: "Globalization Pipeline"
subcategory: "java sdk"
language: "en"
status: "DRAFT"
archived: "false"
last_modified: "1742760072746"
source_url: "https://help.straker.ai/en/g11n/what"
exported_at: "2026-03-17T10:52:05Z"
---

# How to solve `error: com.ibm.g11n.pipeline.client.ServiceException: 'verified' field cannot be set to true because reviewed field is not true.`?

When using CLI to import existing translation files, using the -v option to mark them as verified gave the following error: *com.ibm.g11n.pipeline.client.ServiceException: 'verified' field cannot be set to true because reviewed field is not true.*

Verified and Reviewed are implemented as independent boolean fields. But when verified=true, reviewed should be true as well. The short term workaround would be to specify `-r` at the same time.
