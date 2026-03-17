---
title: "How to solve error \"413 Request Entity Too Large\" when using sync-res-entries?"
knowledge_base: "Globalization Help Center"
category: "Globalization Pipeline"
subcategory: "bundle"
language: "en"
status: "DRAFT"
archived: "false"
last_modified: "1742760075720"
source_url: "https://help.straker.ai/en/g11n/how-to-solve-error-413-request-entity-too-large-when-using"
exported_at: "2026-03-17T10:52:05Z"
---

# How to solve error "413 Request Entity Too Large" when using sync-res-entries?

When synchronizing your bundles using `sync-res-entries` and you get an error as below:

```
ERROR: com.ibm.g11n.pipeline.client.ServiceException: com.ibm.g11n.pipeline.client.ServiceException: Received HTTP status: 413 from POST safer-payments/v2/xliff/bundles, body: <html> <head><title>413 Request Entity Too Large</title></head> <body> <center><h1>413 Request Entity Too Large</h1></center> <hr><center>nginx</center> </body> </html>
```

It's because you uploaded a very large bundle. There are too many entries in the bundle. When running AT task, the entry key will be saved to GP job. In this case, so many keys try to be all saved to GP prep job. But Cloudant DB has document limitation (maximum size is 1MB).

In general, if you want to create new bundle inheriting the existing bundle is to use "copy bundle" command. Once you copied a bundle, upload the new English content. This will only update translation for modified/new strings, which should be much smaller set.
