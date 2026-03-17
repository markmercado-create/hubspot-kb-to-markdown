---
title: "How to set up the file translation and supplying \"filter option\" to handle HTML embedded in CDATA properly parsed as HTML?"
knowledge_base: "Globalization Help Center"
category: "Globalization Pipeline"
subcategory: "java sdk"
language: "en"
status: "DRAFT"
archived: "false"
last_modified: "1742760082549"
source_url: "https://help.straker.ai/en/g11n/how-to-set-up-the-file-translation-and-supplying-filter-option-to-handle-html-embedded-in-cdata-properly-parsed-as-html"
exported_at: "2026-03-17T10:52:05Z"
---

# How to set up the file translation and supplying "filter option" to handle HTML embedded in CDATA properly parsed as HTML?

The GP CLI is here - <https://github.ibm.com/1t1p/gpv2-java-tools/releases/tag/gp-java-tools-v2.4.6>

To translate these XML file, you should create "GP File" first. This is similar to create a GP bundle.

```
java -jar gp-cli.jar create-file -f myXmlFileId -t application/xml -l en,de,fr --filter-option global_cdata_subfilter=okf_html -j myGpCreds.json
```

This command creates a GP file configuration - `-f` to specify file ID, `-t` to specify media type of the file, `-l` to list source language code and target language codes, then `--filter-option global_cdata_subfilter=okf_html` to tell the file parser to process `CDATA` in this XML file as HTML.

Once you create the configuration (for each file), use `java -jar gp-cli.jar import-file -f myXmlFileId -F foo/bar/abc.xml -l en -j myGpCreds.json` to upload English file content.

`-f` to specify the GP file ID created in the previous step, `-F` to specify the local file path to be translated, `-l` to specify the language of the local file.

`create-file` option `--filter-option` is new in CLI v2.4.6.
