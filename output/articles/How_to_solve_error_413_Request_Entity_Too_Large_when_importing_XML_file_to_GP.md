---
title: "How to solve error \"413 Request Entity Too Large\" when importing XML file to GP?"
knowledge_base: "Globalization Help Center"
category: "Globalization Pipeline"
subcategory: "java sdk"
language: "en"
status: "DRAFT"
archived: "false"
last_modified: "1742760084717"
source_url: "https://help.straker.ai/en/g11n/how-to-solve-error-413-request-entity-too-large-when-importing-xml-file-to-gp"
exported_at: "2026-03-17T10:52:04Z"
---

# How to solve error "413 Request Entity Too Large" when importing XML file to GP?

When using GSSC filter  `XML-IBMXUXML10` to import a XML file to GP (e.g., using GP CLI), the GSSC filter  `XML-IBMXUXML10` maybe generate a lot of metadata and try to save all data in a Cloudant DB document. When importing such a XML file, the document size can be over 1M including metadata which causes `413 Request Entity Too Large` error.

The technique used in the resource filter is to support "write" method to restore original file structure. When resource filter was designed, there was originally "write" method. Later "merge" method was added. But, majority of users are not really using the code path that requires RF's "write" method. To implement "write" method with preserving all lines, markups and comments not relevant to translation, you have to keep them aside from key-value pairs. This data is stored in bundle metadata, and exceeding the 1MB limit. Such "side" data is not required only "merge" path is used, because these data not related to translation are all available in the original English file.

If one xml file has a lot of content, it will soon reach the 1M Cloudant DB document size limitation.

- For short term, you may divide the xml file into small ones. If you want to split these bundles, please don't forget to inherit previous translation status. Simply splitting English file and importing them into GP - you will loose translation and status from previous version.
- For long term, updates for `XML-IBMXUXML10` will be required. Updating the custom resource filter and give up "write" would make the data causing max document size limit unnecessary. You should never use generic XML filter like this.
