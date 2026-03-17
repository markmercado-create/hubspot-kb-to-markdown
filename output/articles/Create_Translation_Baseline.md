---
title: "Create Translation Baseline"
knowledge_base: "Globalization Help Center"
category: "WebFM"
subcategory: "GP Integration"
language: "en"
keywords: "webfm"
status: "PUBLISHED"
archived: "false"
last_modified: "1749606206975"
source_url: "https://help.straker.ai/en/g11n/webfm/create-translation-baseline"
exported_at: "2026-03-17T10:52:04Z"
---

# Create Translation Baseline

### Prerequisite

The GP English source bundle is created.

### Check your translation file level

1. Create a zip file of all your translated files.

*The file paths of translated files must be the same as the English file.*

For example, if your application name is "ITM", you zip may look like:

![zip-package-folder](https://20462040.fs1.hubspotusercontent-na1.net/hubfs/20462040/knowledge-base-files/webfm/zip-package-folder.png)

\*\*If you are using 'Singe application' WebFM project, just upload your zip and WebFM will put them in to *webfampp* application. No additional folder required.

2. Go to **Upload File Manager**, select your zip file, Language and click **Upload**  
3. Click the **checkbox** of your uploaded zip in the Package Manager below, and click **UNZIP!**  
4. Go to **Work with NLV Files** through the left menu  
5. Select the files and **Run ChkPII**. WebFM will perform chkpii on your translated files against English source files, and ensure the file level of your translation is the same as English source files.   
![work-nlv-files](https://20462040.fs1.hubspotusercontent-na1.net/hubfs/20462040/knowledge-base-files/webfm/work-nlv-files.png)  

### Create Translation Baseline

1. Select the translation files you want to upload to GP and click **Upload to GP as Reviewed/Verified**
2. Input the resource filter ID for each translated file

   - If you are sending the file through GP File-based Translation, please input `FILE-BASED` as ID.
   - WebFM may suggest some resource filter ID based on file extension, but you can change it based on your files.   
     ![gp-upload-nlv](https://20462040.fs1.hubspotusercontent-na1.net/hubfs/20462040/knowledge-base-files/webfm/gp-upload-nlv.png)
3. Click **Upload to GP as Reviewed Translation** button
4. Done, the translation baseline is created. Next Step: Export Translations from GP
