---
title: "Translation process config(Checks, Rename, Encoding, Text-replacement)"
subtitle: "What are Pre/Post-Translation processes"
knowledge_base: "Globalization Help Center"
category: "WebFM"
subcategory: "Handle Translation Files"
language: "en"
keywords: "webfm"
status: "PUBLISHED"
archived: "false"
last_modified: "1749606207615"
source_url: "https://help.straker.ai/en/g11n/webfm/translation-process-config"
exported_at: "2026-03-17T11:34:19Z"
---

# Translation process config(Checks, Rename, Encoding, Text-replacement)

Translation processes are used to handle with requirements when process ENG and NLV files. The areas you can configure including Checks, Encoding Change, Rename and Text Content Replacement.

- **Pre-translation Process**

  The pre-translation process is used to handle with English files. Usually, we don't suggest any operation on English files unless developer asks. So you can skip configure this process if there is no special request on your English PII files
- **Post-translation Process**

  The post-translation process is used to handle with requirements when process NLV files. The areas you can configure including Post-Translation Checks, Post-Translation Encoding Change, Post-Translation Rename and Post-Translation Text Content Replacement.

### Checks (Pre and Post-Translation)

- **Config for different languages:** You can choose whether to apply the settings to all language or set individual setting for each language here
- **CHKPII Settings:** You can enable or disable CHKPII checks here
  - **File Content:** Whether to conpare language content with English source or not
  - **File Type:** Keep as Auto-detect or manually select the wanted type
  - **Encoding:** Keep as Auto-detect or manually select the wanted option
  - **Exclude specific messages IDs:** Select the specific message ID you don't want to check
- **File existence check:** Run English source file existence check or not
- **Syntax check:** Default is all disabled, enable the ones as you prefer

### Encoding Change (Pre and Post-Translation)

- **Change encoding to:** This is for translation file encoding change when downloading them, select the encoding type as you prefer

### Rename (Post-Translation Only)

Ths part is about rename rule settings when you want to download the language PII files. You can design the file full path based on your needs. Here is the steps:

1. Confirm the Regular Expression for the PII files list you want to rename, please refer details about how to design a regular expression on ([Reg101](https://regex101.com/?regex=(%5B%5E%2F%5D%2B)%2F(.%2B).(properties%7Chs%7Cnlsprops%7Cplmres%7Cjava%7Cprop%7Chs)%24&flags=gmi&delimiter=%60&flavor=java&testString=%3Cfilepath%3E/%3Cfilename%3E.%3Cextension%3E&subst=%241.nl1%2F%242_de.%243))
2. Input the regular expression in the field of **Appname and Full File Path**
3. Input the desired renamed value of each language with groups and parameters predefined in webfm. More predefined variables during processing could be found [here](https://github.ibm.com/gssc/webfm/wiki/i18n.yaml-Reference#Variables-during-processing)
4. Click on **Test** button to test the rule, modify them if the output value is not same as desired   
   ![post-trans-rename](media_files/post-trans-rename.png)
5. If you have defined multiple rename rules, you can also verify them all in the Replacement Rules page

   1. Choose Post-translation Process Config from sidebar in Project Settings section
   2. Click on Save to save all the rules you have created
   3. Click on Evaluate Renaming
   4. Select a language from the dropdown per your need
   5. Input all the source paths(App folder/filepath) you want to verify in the left box
   6. Click on **Evaluate path** button to view the output in Target path box
   7. Verify all the paths are output as desired and correct the rule which has wrong output
   8. Click **Save** after correction and duplicate **step3 ~ step7** again   
      ![post-replacerule-test](media_files/post-replacerule-test.png)

### Text Content Replacement (Pre and Post-Translation)

This part is for text replacement in translation file. If some texts in English PII files need to be changed after they are translated to other language, you can apply these in this section.
