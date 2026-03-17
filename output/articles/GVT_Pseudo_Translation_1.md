---
title: "GVT Pseudo Translation"
subtitle: "Tutorial and guide to Pseudo Translation"
knowledge_base: "Globalization Help Center"
category: "Globalization Pipeline"
subcategory: "gp doc"
language: "en"
status: "PUBLISHED"
archived: "false"
last_modified: "1749606937928"
source_url: "https://help.straker.ai/en/g11n/gvt-pseudo-translation"
exported_at: "2026-03-17T11:33:20Z"
---

# GVT Pseudo Translation

Globalization Pipeline supports GVT pseudo translation. GVT pseudo translation will be automatically generated under pseudo locale and GP users can leverage GP CLI to export the GVT pseudo translation with desired locale and file naming. The use of GP CLI is similar to other languages except GVT pseudo translation is always saved under "en-XA" pseudo locale. For bundles that require pseudo translation, one must add the "en-XA" as one of the supported languages.

Users could follow the following steps to create pseudo translations:

1. Create/Update bundle with 'en-XA' language using [GP CLI tool](https://github.ibm.com/1t1p/gpv2-java-tools/tree/master/gp-java-tools/gp-cli).
   - If the bundle has not been created: Create a bundle and add 'en-XA' to the target language list (along with other supported languages of your product).
   - If the bundle has been created: Update the bundle by adding 'en-XA' to the target language list.
2. Once the 'en-XA' target language is added, GP will initiate the GVT pseudo translation AT job automatically.
3. When the GVT pseudo translation is completed, you will be able to see the result on GP dashboard, where a new language of ' English(Pseudo-Accents)' will be displayed.  Note: 'en-XA' is displayed as "English (Pseudo-Accents)" on GP dashboard.![null](media_files/undefined-Jul-15-2024-07-03-31-4100-AM.png)
4. Export PII from GP. For different UI framework, users might need to put the pseudo translation to the desired language folder that can be supported.

   - Export PII using GP CLI: We can use GP CLI to export PII directly. Rename the exported bundles to PII files with desired target language code and put the files to the related folder. After incorporating this GVT Pseudo Translated PII files into product build or testing environment, user can see the pseudo string in the UI under correct language locale.
   - Export PII using Jenkins: If product team uses Jenkins to generate builds, developer also can use GP Jenkins plugin to export the PII files and add scripts to rename the PII files to the desired target language and put the file to the related folder.
   - Others: If you are using WebFM and have it configured, you could also export export GVT Pseudo Translation PII files using WebFM with additional configuration.

### The pseudo translation format:

- The "Full width" pseudo translation methodology is adopted by GP GVT Pseudo Translator AT service based on GVT guide.
- Example of a "Full width" pseudo translation for an English source string "You have been logged out." will look like following:
  - [('ฏูİı｜)Ｙｏｕ ｈａｖｅ ｂｅen logged out.]
- Elements in pseudo translation:
  - The bracket bookends [ ] identify the string boundary to detect concatenation issue
  - The (') detects the apostrophe issue.
  - The full-width characters ensure the the non-ASCII characters can correctly display.
  - ฏูİı｜are some problematic characters.
  - The text length expansion rule can be found here: [Rule A3: Providing for MRI Expansion](https://w3.ibm.com/globalization/page/4619#LinkTarget_5620)
