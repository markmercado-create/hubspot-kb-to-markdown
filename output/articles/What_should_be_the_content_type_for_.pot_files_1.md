---
title: "What should be the content type for .pot files?"
knowledge_base: "Globalization Help Center"
category: "Globalization Pipeline"
subcategory: "resource filter"
language: "en"
status: "DRAFT"
archived: "false"
last_modified: "1742760077926"
source_url: "https://help.straker.ai/en/g11n/what-should-be-the-content-type-for-.pot-files"
exported_at: "2026-03-17T11:33:30Z"
---

# What should be the content type for .pot files?

POT is a template only containing English. "Translated POT" does not exist. There is no official MIME content type assigned for GNU gettext PO/POT files. It's not supported by GP "File" translation. There is a stock GP filter supporting GNU gettext POT, and please refer to the following two links:

- GP CLI user guide - <https://github.ibm.com/1t1p/gpv2-java-tools/tree/master/gp-java-tools/gp-cli>
- Filter type - <https://github.ibm.com/1t1p/gpv2-java-tools/tree/master/gp-java-tools/gp-cli#import>
