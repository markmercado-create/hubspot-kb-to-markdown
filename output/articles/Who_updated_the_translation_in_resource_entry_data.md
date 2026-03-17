---
title: "Who updated the translation in resource entry data?"
knowledge_base: "Globalization Help Center"
category: "Globalization Pipeline"
subcategory: "translation"
language: "en"
status: "DRAFT"
archived: "false"
last_modified: "1742760069331"
source_url: "https://help.straker.ai/en/g11n/how-to-check-who-updated-the-translation-in-the-resource-entry-data"
exported_at: "2026-03-17T10:52:04Z"
---

# Who updated the translation in resource entry data?

GP records who updated the translation in the resource entry data, and you can check it on your own.

Access the GP API <https://g11n-pipeline-api.straker.global/translate/swagger/#/bundle/getResourceEntryInfo> with your GP instance ID and bundle ID. For example:

![](https://20462040.fs1.hubspotusercontent-na1.net/hubfs/20462040/image-png-3.png)

In the API response, you can identify who updated the translation accoridng to the filed called `translatedBy`. For example,  `"translatedBy": "(CAITS-AT_XLIFF)-ws-core_20240312T180918-13"` indicates that CAITS (GP backend service) updated the translation, and **subState=\"caits:grts-exact-same-domain\"** indicates the translation is caused by exact translation memory match in GRTS.
