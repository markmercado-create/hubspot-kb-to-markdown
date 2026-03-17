---
title: "Dispatcher"
knowledge_base: "Globalization Help Center"
category: "WebFM"
subcategory: "Handle English Files"
language: "en"
keywords: "webfm"
status: "PUBLISHED"
archived: "false"
last_modified: "1749606207467"
source_url: "https://help.straker.ai/en/g11n/webfm/dispatcher"
exported_at: "2026-03-17T10:52:05Z"
---

# Dispatcher

1. Go to **Dispatcher** to dispatch new&changed files from repository  

**![dispatcher](https://20462040.fs1.hubspotusercontent-na1.net/hubfs/20462040/knowledge-base-files/webfm/dispatcher.png)  
Options:**

- ☑️ **Test Run (Do NOT Open Defect for ChkPII Errors)**  
  If unchecked, WebFM will create defects (RTC/CMVC) or send emails to developer (Github/FTP) when there's any CHKPII errors
- ☐ **Run Mock Process on Applications**  
  If checked, WebFM will create pseudo translation and commit the translations back to source control
- ☐ **Include ChkPII Failed Files in Package**  
  The CHKPII-failed files will be excluded from dispatcher package if not checked
- ☐ **Run Wordcount**  
  Calculate workdcount against the files to "Work with English Files" or the selected package
- ☐ **Perform TextContentReplace on Eng files**  
  Check when you need to perform Text content replacement on English files

2. Click one of the blue buttons on page to run the dispatcher

1. 1. **Hit this to base on last run ...**  
      Extract English PII Files which were changed only **from "The time when last Dispatcher run" to "Now"** from File Repository files
   2. **Get all files newer than [year/month/day hr:min:sec]**  
      Extract English PII Files which were changed only **from "Input time" to "Now"** from File Repository files  
      ✴️ *Tips: If you want to collect **all files**, you should use this button with a old time (e.g `2001/01/01 00:00:00`).*
   3. **Upload an archive as the source of Dispatcher**  
      Upload Existing New-and-Changed English PII files
   4. **Get files of specific time (Retrieve historical version)**  
      Git only. Extract English PII Files **of the input time** from File Repository

3. Go to **Dispatcher Packages** to check the dispatched .zip package, and click **Unzip to English**

![dispatcher-packages](https://20462040.fs1.hubspotusercontent-na1.net/hubfs/20462040/knowledge-base-files/webfm/dispatcher-packages.png)  
4. Go to **Work with English Files** to find the English PII Files

![work-eng-files-2](https://20462040.fs1.hubspotusercontent-na1.net/hubfs/20462040/knowledge-base-files/webfm/work-eng-files-2.png)
