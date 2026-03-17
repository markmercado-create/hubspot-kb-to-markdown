---
title: "How to handle CERT_HAS_EXPIRED error?"
knowledge_base: "Globalization Help Center"
category: "Globalization Pipeline"
subcategory: "java sdk"
language: "en"
status: "DRAFT"
archived: "false"
last_modified: "1742760075894"
source_url: "https://help.straker.ai/en/g11n/how-to-handle-cert_has_expired-error"
exported_at: "2026-03-17T11:33:17Z"
---

# How to handle CERT_HAS_EXPIRED error?

When using [NodeJS client SDK](https://github.ibm.com/1t1p/gp-js-client) to access https://g11n-pipeline-api.straker.global/translate/rest, `CERT_EXPIRED` error is probably caused by CA cert installed on client was already expired. Previously, it needs IBM internal CA cert installed on client side as trusted CA. The new Straker host uses server cert signed by GoDaddy CA, and this CA should be already available on your client system as trusted CA.
