---
title: "GP source warning & error"
knowledge_base: "Globalization Help Center"
category: "Globalization Pipeline"
subcategory: "gp doc"
language: "en"
status: "PUBLISHED"
archived: "false"
last_modified: "1755656970841"
source_url: "https://help.straker.ai/en/g11n/gp-source-warning-error"
exported_at: "2026-03-17T10:52:05Z"
---

# GP source warning & error

#### **Overview**

GP checks whether resource strings in a bundle are ready for translation in a source language immediately after those strings are uploaded into GP. When input string contains corrupted HTML/XML, escaped HTML or other source issues, GP sets source warning (or error) for these strings. Machine translation might be still generated, but GP users cannot submit human translation requests including these strings. Otherwise, these strings are too difficult or even impossible for Straker translators to do human translation. GP users need to review and fix these warnings or errors before proceeding.

#### **There are two options for users to** **fix source warnings**

1. Fix a source string flagged with a source warning (or error).
2. Ignore a source warning (or error) if a user thinks it’s false warning.

#### **Fix through GP dashboard**

On bundle page, a **source-issue count** displayed in the “Translation Status“ column (e.g. “2 source issues” highlighted in the following screenshot) indicates some resource strings in your bundle contain source issues, which need you to review and fix the related warnings or errors.![]()

![1](https://20462040.fs1.hubspotusercontent-na1.net/hubfs/20462040/knowledge-base-files/GP%20Source%20Warning/1.png)![]()

Or on the new TR page, an **unselectable** bundle(e.g. the bundle “test“ depicted in the following screenshot) also indicates some resource strings in this bundle contain source issues, which need you to review and fix the related warnings or errors before proceeding.

![2](https://20462040.fs1.hubspotusercontent-na1.net/hubfs/20462040/knowledge-base-files/GP%20Source%20Warning/2.png)

In the source language view on GP dashboard, you can check the status of source warnings (or errors) and the source-issue details (i.e. *type* and *message*). You can also filter resource strings flagged with source warning or error.

![3](https://20462040.fs1.hubspotusercontent-na1.net/hubfs/20462040/knowledge-base-files/GP%20Source%20Warning/3.png)

If you are sure a source warning (or error) is actually false warning, you can just ignore this warning by using “**Ignore warning/error**“ option (refer to the screenshot below).

![4](https://20462040.fs1.hubspotusercontent-na1.net/hubfs/20462040/knowledge-base-files/GP%20Source%20Warning/4.png)

Or you can ignore a set of selected resource strings that are actually false warnings (or errors) in one shot. Refer to the screenshot below.

![5](https://20462040.fs1.hubspotusercontent-na1.net/hubfs/20462040/knowledge-base-files/GP%20Source%20Warning/5.png)

#### **Fix through GP API**

GP API (<https://g11n-pipeline-api.straker.global/translate/swagger/#/bundle/getBundleInfo>) allows GP users to check **source-issue count** for a specific bundle. Specify the newly-added query parameter called “**sourceIssueCount**“ when calling this API (refer to the screenshot below).

![6](https://20462040.fs1.hubspotusercontent-na1.net/hubfs/20462040/knowledge-base-files/GP%20Source%20Warning/6.png)

GP API (<https://g11n-pipeline-api.straker.global/translate/swagger/#/bundle/getResourceStrings>) allows GP users to query all resource entries with source issues. Specify the newly-added query parameter called “**resourceEntriesWithSourceIssue**“ when calling this API (refer to the screenshot below).

![7](https://20462040.fs1.hubspotusercontent-na1.net/hubfs/20462040/knowledge-base-files/GP%20Source%20Warning/7.png)

The response of GP API (<https://g11n-pipeline-api.straker.global/translate/swagger/#/bundle/getResourceEntryInfo>) returns the newly-added field called “**sourceIssues**“ if there is any source issues in a bundle. GP users can check the field “**sourceIssues**“ for source-issue details.

To ignore source issues (or errors) for a source resource entry, GP users can use GP API (<https://g11n-pipeline-api.straker.global/translate/swagger/#/bundle/updateResourceEntryData>). When calling this API, set the field “**sourceIssueIgnored**“ to true in the body (refer to the screenshot below).

![8](https://20462040.fs1.hubspotusercontent-na1.net/hubfs/20462040/knowledge-base-files/GP%20Source%20Warning/8.png)

To ignore source issues (or errors) for a set of source resource entries, GP users can use GP API (<https://g11n-pipeline-api.straker.global/translate/swagger/#/bundle/updateResourceStrings>). When calling this API, set field “**sourceIssueIgnored**“ for each resource key in the body (refer to the screenshot below).

![9](https://20462040.fs1.hubspotusercontent-na1.net/hubfs/20462040/knowledge-base-files/GP%20Source%20Warning/9.png)

#### **Fix through GP CLI**

To check **source-issue count** (i.e. the field “*sourceIssueCount*“), please use show command with parameter **-m**. Below is the example show command:

java -jar gp-cli.jar show -b MyBundle -m -j mycreds.json

To exportproblematic source resource entries in a bundle or a list of bundles to a json file, use the newly-added command called “**export-problematic-res-entries**“.

- For example, export problematic source resource entries in a bundle:

- - - java -jar gp-cli.jar export-problematic-res-entries -b MyBundle -o entires.json -j mycreds.json
- For example, export problematic source resource entries in a list of bundles:
  - - java -jar gp-cli.jar export-problematic-res-entries -bl MyBundle.lst -o entires.json -j mycreds.json

- Below is an example output (json):

  `{`  
    
  `"MyBundle": {`  
    
  `"key2": {`  
    
  `"sourceValue": "Syntax error: Missing or mismatch element <% or %> at line <Variable formatSpec=\"{line}\">line</Variable>",`  
    
  `"unit": "<unit id=\"key2\"><mda:metadata xmlns:mda=\"urn:oasis:names:tc:xliff:metadata:2.0\"><mda:metaGroup category=\"caits-prep\"><mda:meta type=\"process-format\">text/plain</mda:meta><mda:meta type=\"WARN_UNSUPPORTED_HTML\">Unable to process the content containing one or more document parts</mda:meta></mda:metaGroup></mda:metadata><segment id=\"s1\"><source xml:space=\"preserve\">Syntax error: Missing or mismatch element &lt;% or %&gt; at line &lt;Variable <mrk id=\"1\" type=\"caits:regex-no-translate\" translate=\"no\">formatSpec=\"{line</mrk>}\"&gt;line&lt;/Variable&gt;</source></segment></unit>",`  
    
  `"sourceIssues": [`  
    
  `{`  
    
  `"type": "WARN_UNSUPPORTED_HTML",`  
    
  `"message": "Unable to process the content containing one or more document parts"`  
    
  `}`  
    
  `]`  
    
  `},`  
    
  `"key6": {`  
    
  `"sourceValue": "Bad <span class-123>HTML",`  
    
  `"unit": "<unit id=\"key6\"><mda:metadata xmlns:mda=\"urn:oasis:names:tc:xliff:metadata:2.0\"><mda:metaGroup category=\"caits-prep\"><mda:meta type=\"process-format\">text/plain</mda:meta><mda:meta type=\"ERROR_INVALID_HTML\">Invalid HTML fragment: ERROR: StartTag at (r1,c5,p4) missing required end tag\n</mda:meta></mda:metaGroup></mda:metadata><notes><note>this is a test</note></notes><segment id=\"s1\"><source xml:space=\"preserve\">Bad &lt;span <mrk id=\"1\" type=\"caits:regex-no-translate\" translate=\"no\">class-123&gt;HTML</mrk></source></segment></unit>",`  
    
  `"sourceIssues": [`  
    
  `{`  
    
  `"type": "ERROR_INVALID_HTML",`  
    
  `"message": "Invalid HTML fragment: ERROR: StartTag at (r1,c5,p4) missing required end tag\n"`  
    
  `}`  
    
  `]`  
    
  `}`  
    
  `}`  
    
  `}`
