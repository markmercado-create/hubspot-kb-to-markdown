---
title: "Create Source Bundle"
knowledge_base: "Globalization Help Center"
category: "WebFM"
subcategory: "GP Integration"
language: "en"
keywords: "webfm"
status: "PUBLISHED"
archived: "false"
last_modified: "1749606167968"
source_url: "https://help.straker.ai/en/g11n/webfm/create-source-bundle"
exported_at: "2026-03-17T11:30:02Z"
---

# Create Source Bundle

### Prepare needed Data

1. Create your Project in WebFM if you haven't created it, and configure your application.
2. GP instance credential JSON file.
3. Source English files
4. Translated files of the **same file level** for creating translation baseline

### Setup

1. Go to WebFM application
2. Select your project and click **Select**
3. Go to **Project Config > GP Settings** through the left menu
4. Browse to your GP instance credential JSON file and then click **Update** button   
   ![gp-cred-upload](media_files/gp-cred-upload.png)

### Create English Source Bundle/File

1. Create a zip file of all your English source files.

   - If you are using general WebFM project, all your files should be under a folder with the name of a WebFM application. For example, if your WebFM application name is "ITM", you zip may look like:  
      ![zip-package-folder](media_files/zip-package-folder_1.png)
   - If you are using 'Singe application' WebFM project, just upload your zip and WebFM will put them in to webfampp application. No additional folder required.
2. Go to **Upload File Manager**, select your zip file, Language "en\_US" and click **Upload**
3. Click the **checkbox** of your uploaded zip in the Package Manager below, and click **UNZIP!**
4. Go to **Work with English Files** through the left menu
5. Select the source files you want to upload to GP and click **Run GP Import/Export**   
   ![work-eng-files](media_files/work-eng-files.png)
6. Input the **Resource Filter ID** for each source file and **Uncheck Download Translations to WebFM**

   - If you want to send the file through GP File-based Translation, please input `FILE-BASED` as ID. (ref. [GP Files supported types](https://w3.ibm.com/w3publisher/globalization-pipeline/files-supported-types))
   - WebFM may suggest some resource filter ID based on file extension, but you can change it based on your files.  
     ![upload-gp-source](media_files/upload-gp-source.png)

 7. Click **Run GP  
![gp-import-output](media_files/gp-import-output.png)**   
 8. Done, the English bundle is created. Next Step: Create GP Translation Baseline.
