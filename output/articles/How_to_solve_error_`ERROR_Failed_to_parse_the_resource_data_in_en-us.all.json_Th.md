---
title: "How to solve error `ERROR: Failed to parse the resource data in en-us.all.json: The root JSON element is not an JSON object`?"
knowledge_base: "Globalization Help Center"
category: "Globalization Pipeline"
subcategory: "resource filter"
language: "en"
status: "DRAFT"
archived: "false"
last_modified: "1742760075375"
source_url: "https://help.straker.ai/en/g11n/how-to-solve-error-error-failed-to-parse-the-resource-data-in-en-us.all.json-the-root-json-element-is-not-an-json-object"
exported_at: "2026-03-17T10:52:05Z"
---

# How to solve error `ERROR: Failed to parse the resource data in en-us.all.json: The root JSON element is not an JSON object`?

While importing a JSON Array file to GP, instead of JSON object file,  an error with `ERROR: Failed to parse the resource data in en-us.all.json: The root JSON element is not an JSON object`  will be thrown.

This is GP stock filter's behavior. You can create your own resource filter if necessary. Example filter - <https://github.ibm.com/1t1p/gpv2-java-tools/tree/master/resource-filter/csv-res-filter>
