---
title: "Export Translations from GP"
knowledge_base: "Globalization Help Center"
category: "WebFM"
subcategory: "GP Integration"
language: "en"
keywords: "webfm"
status: "PUBLISHED"
archived: "false"
last_modified: "1749606207131"
source_url: "https://help.straker.ai/en/g11n/webfm/export-translations-from-gp"
exported_at: "2026-03-17T10:52:05Z"
---

# Export Translations from GP

### Prerequisite

1. WebFM project, application, and GP credential settings are configured.
2. English files are unzipped in WebFM 'Work with English files'

### Export Translation from GP

1. Go to WebFM server https://webfm.straker.global/webapp/webfmx/jsp/welcome.jsp
2. Select Project and click **Select**
3. Go to **Work with English Files** through the left menu
4. Select the source files you want to export translation from GP and click **Run GP Import/Export**   
   ![work-eng-files](https://20462040.fs1.hubspotusercontent-na1.net/hubfs/20462040/knowledge-base-files/webfm/work-eng-files.png)
5. Input the resource filter ID for each source file
   - If you were sending the file through GP File-based Translation, please input `FILE-BASED` as ID. (ref. [GP Files supported types](https://w3.ibm.com/w3publisher/globalization-pipeline/files-supported-types))
   - WebFM may suggest some resource filter ID based on file extension, but you can change it based on your files.   
     ![gp-export-translation](https://20462040.fs1.hubspotusercontent-na1.net/hubfs/20462040/knowledge-base-files/webfm/gp-export-translation.png)
6. Ensure **Download Translations to WebFM** is checked and click **Run GP**   
   ![gp-export-output](https://20462040.fs1.hubspotusercontent-na1.net/hubfs/20462040/knowledge-base-files/webfm/gp-export-output.png)
7. Go to **Upload File Manager** and you can download the exported translation zips.   
   ![download-nlv-zip](https://20462040.fs1.hubspotusercontent-na1.net/hubfs/20462040/knowledge-base-files/webfm/download-nlv-zip.png)

### Export English from GP

- If you want to export English from GP, you can add `en_AU` language in WebFM. And just perform the export translation operation of `en_AU` as above.
