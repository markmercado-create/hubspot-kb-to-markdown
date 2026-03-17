---
title: "ICT Readiness Check"
subtitle: "Check readiness before sending request for ICT"
knowledge_base: "Globalization Help Center"
category: "Globalization Pipeline"
subcategory: "ict doc"
language: "en"
status: "PUBLISHED"
archived: "false"
last_modified: "1749606949553"
source_url: "https://help.straker.ai/en/g11n/ict-readiness-check"
exported_at: "2026-03-17T11:33:20Z"
---

# ICT Readiness Check

### ICT Readiness Check

Before you can submit a translation request for ICT, it is required to perform the **ICT Readiness Check** until a **Ready** status is reached. This is to protect you from sending an ICT request without all the necessary information provided.

You can download the ICT readiness check report from [dashboard](https://g11n-pipeline-console.straker.global/login.wss) or via the [command line interface tool](https://github.ibm.com/1t1p/gpv2-java-tools/tree/master/gp-java-tools/gp-cli) of Globalization Pipeline. We suggest you to import the CSV file into a spreadsheet software to help you better organize the issues.

For readiness check, it is required that all the errors ⛔︎ are resolved before you can get a Ready status and can submit the translation request. For the messages of the level "Warn" (warning) ⚠️, they serve as a reminder for some potential issues, but they may not be real issues depending on context of your project, and you are not required to fix them before submitting the translation request.

▸ Refer to [Process: ICT](https://kb.strakertranslations.com/en/knowledge/in-context-testing-ict) for the overall ICT (in-context testing) workflow.

### Message List

In this page, we have listed all the possible messages you may see in a readiness check report. We explain the situation why the message is reported, and suggest some possible ways to fix them. You can search the messages via "Message Code" in the list below.

ⓘ Click on the message code to expand the full content.

**STR0001** ⚠️

**Level:**

Warning

**Message:**

The resource entry has not been reviewed. It is not associated with any attachments.

**Explanation:**

This message is reported when a bundle in your translation request contains a string with status of "unreviewed". And, this string is not associated with any attachments. It is a warning message for you to check if this string is to be covered in this ICT.

**Suggestions:**

ℹ️ This is a "Warning" level message, no mandatory actions needed.

In an ICT translation request, we expect all resource entries included should have been reviewed or translated by human. Therefore, a warning is reported for you to confirm if the "unreviewed" string is as expected.

This string is also not associated with any attachments. The string may be out of scope and might have been automatically added by some DevOps automation process. If you confirm that this string is not within the scope of this ICT, you can safely ignore this warning. The string will be excluded from the ICT scope.

On the contrary, if you intend to include this string in the ICT scope, please send a regular translation request to get the string translated or reviewed by human in advance, and provide corresponding screenshot after the translation is returned, before you start the ICT process.

**STR0002** ⚠️

**Level:**

Warning

**Message:**

The resource entry in ICT scope has no associated attachments.

**Explanation:**

This message is to inform you that a string, which is in ICT scope (shown as R (reviewed) on GP Dashboard) in your translation request, is not associated with any attachments. As a result, this string does not have associated attachments to hold ICT screenshots and will be excluded from the ICT scope.

**Suggestions:**

ℹ️ This is a "Warning" level message, no mandatory actions needed.

As this string is marked as "reviewed," we assume it is within the ICT scope to be verified by the tester. However, you have not associated it with any attachment. Possible reasons may include:

1. 1. You forgot to perform attachment association for this string.
   2. The association process was not correctly completed. For example, it was not correctly detected by OCR during the auto-association process and need some manual correction.

If this string is intended to be verified during the ICT, please associate it with the corresponding attachment and upload screenshots of source and target languages.

▻ For information on how to associate attachment with resource entry, please refer to [Process: Translation with context - Step 4: Associate attachment](https://kb.strakertranslations.com/en/knowledge/translation-with-context)

We understand that sometimes it is difficult to provide screenshot for certain strings, such as an error message that only appears under rare conditions. Therefore, this message is only a warning. If you are certain that this string will be excluded from this ICT due to no screenshots, you can safely ignore this warning message. You can mark this string as "verified" to prevent such warning in the future.

**STR0003** ⛔︎

**Level:**

Error

**Message:**

There are no resource entries in ICT scope. All resource entries are verified, or unreviewed, or included in another in-progress TR.

**Explanation:**

There are no resource entries being considered as "in scope" for this ICT translation request (marked as "reviewed"). It means that these messages either

- - have already been verified in the past (marked as "verified"), or
  - have not yet been translated or reviewed by human (marked as "unreviewed"), or
  - they are marked as "reviewed", but they have been included in some other translation requests which are still in progress.

**Suggestions:**

An effective ICT translation request should include at least one resource entry marked as "reviewed" so that the tester has something to test. Please double check that you have selected all the bundles and all the target languages you wish to include in the translation request.

If your bundle and language selections are correct, there could be on-going translation requests not yet merged to GP. After all impacting translation requests are returned and merged, you can re-run the readiness check and submit the ICT translation request when there is no more error. (Note: if you believe all your previous translation requests have been merged, please seek technical assistance on [#g11n-pipeline](https://ibm-cloudplatform.slack.com/archives/C0EP2MFR7) slack channel.)

**STR0004** ⛔︎

**Level:**

Error

**Message:**

All resource entries in ICT scope have no associated attachments.

**Explanation:**

In the bundles included in your translation request, all the resource entries in the ICT scope (shown as R (reviewed) on GP Dashboard) do not have any associated attachments. As a result, this ICT cannot proceed because there are no screenshots to be checked by testers.

**Suggestions:**

Please ensure that you have correctly associated attachments with the resource strings in the ICT scope.

▻ For information on how to associate attachment with resource entry, please refer to [Process: Translation with context - Step 4: Associate attachment](https://kb.strakertranslations.com/en/knowledge/translation-with-context)

If you are using auto-association, please review the association results again to ensure they are correct. Please note that due to the use of OCR to recognize text in image during the auto-association process, there might be omissions that require manual review and correction.

**STR0005** ⚠️

**Level:**

Warning

**Message:**

The resource entry in ICT scope has no associated attachments with a tag included in TR's attachmentTags.

**Explanation:**

This scenario is similar to STR0002, with the difference that your translation request has the "attachment tags" provided to identify which attachments are within the scope of this ICT.

A string which is in ICT scope (shown as R (reviewed) on GP Dashboard) in your translation request is not associated with any attachment that has a tag included in the "attachment tags" of this ICT translation request. The ICT tester requires the attached screenshots to perform translation testing for the string. As a result, this string will be excluded from the ICT scope.

**Suggestions:**

ℹ️ This is a "Warning" level message, no mandatory actions needed.

As this string is marked as "reviewed," we assume it is within the ICT scope to be verified by the tester. However, you have not associated it with any attachment that has a tag included in the "attachment tags" of this ICT translation request. Possible reasons may include:

1. 1. You forgot to perform attachment association for this string.
   2. The association process was not correctly completed. For example, it was not correctly detected by OCR during the auto-association process and need some manual correction.
   3. You have correctly completed attachment association, but the attachment tag is not consistent with the translation request. For example:
      - You did not add the correct tag to the attachment.
      - You did not add the tag into the "attachment tags" of the translation request.

For case 1 and 2, this string is the one you intended to verify during the ICT, but the association was not done correctly. Please associate the resource entry with the corresponding attachment and upload screenshots of source and target languages for it.

▻ For information on how to associate attachment with resource entry, please refer to [Process: Translation with context - Step 4: Associate attachment](https://kb.strakertranslations.com/en/knowledge/translation-with-context)

For case 3, the attachment association has been correctly established, but the tag of attachment and translation request is not consistent. Please ensure that you have tagged the attachment with a correct tag which is included in the "attachment tags" of the translation request.

▻ For information on how to add tags to an attachment, please refer to [Process: ICT - Step 5: Tag attachment](https://kb.strakertranslations.com/en/knowledge/in-context-testing-ict)

We understand that sometimes it is difficult to provide screenshot for certain strings, such as an error message that only appears under rare conditions. Therefore, this message is only a warning. If you are certain that this string will be excluded from this ICT due to no screenshots, you can safely ignore this warning message. You can mark this string as "verified" to prevent such warning in the future.

**STR0006** ⛔︎

**Level:**

Error

**Message:**

All resource entries in ICT scope have no associated attachments with a tag included in TR's attachmentTags.

**Explanation:**

This scenario is similar to STR0004, with the difference that your translation request has the "attachment tags" provided to identify which attachments are within the scope of this ICT.

In the bundles included in your translation request, all the resource entries in the ICT scope (shown as R (reviewed) on GP Dashboard) do not have any associated attachment that has a tag included in the "attachment tags" of this ICT translation request. As a result, this ICT cannot proceed because there are no screenshots to be checked by testers.

**Suggestions:**

Please ensure that you have tagged the attachment with a correct tag which is included in the "attachment tags" field of the translation request.

▻ For information on how to add tags to an attachment, please refer to [Process: ICT - Step 5: Tag attachment](https://kb.strakertranslations.com/en/knowledge/in-context-testing-ict)

If you confirmed the tag is correct, please ensure that you have correctly associated attachments with the resource strings included in this ICT.

▻ For information on how to associate attachment with resource entry, please refer to [Process: Translation with context - Step 4: Associate attachment](https://kb.strakertranslations.com/en/knowledge/translation-with-context)

If you are using auto-association, please review the association results again to ensure they are correct. Please note that due to the use of OCR to recognize text in image during the auto-association process, there might be omissions that require manual review and correction.

**STR0007** ⛔︎

**Level:**

Error

**Message:**

The resource entry has not been reviewed, and is associated with one or more attachments.

**Explanation:**

This message is reported when a bundle in your translation request contains a string that is still in the status of "unreviewed". And, this string is associated with one or more attachment. It is an error level message, you need to check and fix some settings before you can proceed with the ICT.

**Suggestions:**

In an ICT translation request, we expect all resource entries included should have been translated or reviewed by human. And, the "unreviewed" string is associated with one or more attachments, meaning that there could be an intention to provide screenshots for it. As you did not provide "attachment tags" in your translation request, all the attachments are to be considered as in scope for the ICT. You need to confirm what is the real intention and update the corresponding settings to resolve the issue.

1. 1. If you intend to include this string in the ICT, please send a regular translation request to get the string translated or reviewed by human in advance. This will mark the string as "reviewed". You will also need to prepare and upload corresponding screenshots of the source and target languages after the translation is returned, before you start the ICT process.
   2. If you do not intend to include this string in the ICT:
      1. Remove the attachment association if it was done by mistake.
      2. If you do want to keep the attachment association, for example, for a future regular translation request you are preparing. You can create or update attachment tags for both attachments and ICT translation request to define the ICT attachments.. For example, you can add a tag like "ICT-2023-Q1" for the attachments you'd like to include, and to the "attachment tags" of the translation request. Do not add the tag to this attachment (or change to other tag) as it is not intended for this ICT.

**STR0008** ⛔︎

**Level:**

Error

**Message:**

The resource entry has not been reviewed, and is associated with one or more attachments with a tag included in TR's attachmentTags.

**Explanation:**

This scenario is similar to STR0007, with the difference that your translation request has the "attachment tags" provided to identify which attachments are within the scope of this ICT.

This message is reported when a bundle in your TR contains a string that is still in the status of "unreviewed". And, this string is associated with one or more attachments that has a tag included in the "attachment tags" of this ICT translation request. It is an error level message, you need to check and fix some settings before you can proceed with the ICT.

**Suggestions:**

In an ICT translation request, we expect all resource entries included should have been translated or reviewed by human.  And, the "unreviewed" string is associated with one or more attachments that has a tag included in the "attachment tags" of this ICT translation request, meaning that you have the intention to provide screenshots for it. You need to confirm what is the real intention, and update the corresponding settings to resolve the issue.

1. 1. If you intend to include this string in the ICT, please send a regular translation request to get the string translated or reviewed by human in advance. This will mark the string as "reviewed". You will also need to prepare and upload corresponding screenshots after the translation is returned before you start the ICT process.
   2. If you do not intend to include this string in the ICT, you should not associate it with an attachment that is marked as in scope by a tag included in the translation request's "attachment tags". There are some possibilities:
      1. You made a wrong association of the resource entry with the attachment: please remove the association.
      2. You wrongly added the tag to the attachment (you are not intended to include the attachment in the ICT scope):  please remove the tag from the attachment.
      3. You wrongly add the tag to the "attachment tags" of the translation request (you are not intended to include attachments with this tag in the ICT scope): please remove the tag from the "attachment tags" list of the translation request.

**STR0009** ⚠️

**Level:**

Warning

**Message:**

The resource entry has not been reviewed. It is not associated with any attachments with a tag included in TR's attachmentTags.

**Explanation:**

This scenario is similar to STR0001, with the difference that your translation request has the "attachment tags" provided to identify which attachments are within the scope of this ICT.

This message is reported when a bundle in your translation request contains a string that is in the status of "unreviewed". And, this string is not associated with any attachment that has a tag included in the "attachment tags" of this ICT translation request. It is a warning message for you to check if this string is to be covered in this ICT.

**Suggestions:**

ℹ️ This is a "Warning" level message, no mandatory actions needed.

In an ICT translation request, we expect all resource entries included should have been translated or reviewed by human. Therefore, a warning is reported for you to confirm if the "unreviewed" string is as expected.

This string is not associated with any attachment that has a tag included in the "attachment tags" of this ICT translation request. The string may be out of scope and might have been automatically added by some DevOps automation process. If you confirm that this string is not within the scope of this ICT, you can safely ignore this warning. The string will be excluded from the ICT scope.

On the contrary, if you intend to include this string in the ICT, please send a regular translation request to get the string translated or reviewed by human in advance, and prepare corresponding screenshots after the translation is returned. Also, tag the attachment with a tag in the "attachment tags" of the ICT translation request, before you start the ICT process.

**SCR0001** ⛔︎

**Level:**

Error

**Message:**

There are no screenshots uploaded for both source and target languages for this attachment.

**Explanation:**

The attachment in the ICT scope must have screenshot uploaded for both source and target languages. This is a pre-requisite for the ICT tester to perform translation testing. But both screenshots are missing for your attachment.

**Suggestions:**

This attachment is detected to be "in ICT scope", which means either:

1. When your ICT translation request has non-empty "attachment tags":

It is an attachment with a tag included in the "attachment tags" of  the translation request, and is referenced from at least one resource entry marked as "reviewed".

2. When your ICT translation request has empty "attachment tags":

It is an attachment referenced from at least one resource entry marked as "reviewed".

As this attachment is in the ICT scope and will be utilized by the tester to verify the translation, please prepare and upload the screenshot images for this attachment. You need to provide screenshots of both source and target languages.

▻ For information on how to upload attachment content for a certain language, please refer to[Process: Translation with context - Step 3: Upload attachment](https://kb.strakertranslations.com/en/knowledge/translation-with-context)

**SCR0002** ⛔︎

**Level:**

Error

**Message:**

There is no screenshot uploaded for the source language for this attachment.

**Explanation:**

The attachment in the ICT scope must have screenshot uploaded for both source and target languages. This is a pre-requisite for the ICT tester to perform translation testing. It is detected that the source language content is missing for the attachment.

**Suggestions:**

This attachment is detected to be "in ICT scope", which means either:

1. When your ICT translation request has non-empty "attachment tags":

It is an attachment with a tag included in the "attachment tags" of  the translation request, and is referenced from at least one resource entry marked as "reviewed".

2. When your ICT translation request has empty "attachment tags":

It is an attachment referenced from at least one resource entry marked as "reviewed".

It is detected that the source language content is missing for this attachment, and the attachment is in the ICT scope. Please prepare and upload the source language (English) screenshot for the attachment.

▻ For information on how to upload attachment content for a certain language, please refer to[Process: Translation with context - Step 3: Upload attachment](https://kb.strakertranslations.com/en/knowledge/translation-with-context)

**SCR0003** ⛔︎

**Level:**

Error

**Message:**

There is no screenshot uploaded for the target language for this attachment.

**Explanation:**

The attachment in the ICT scope must have screenshot uploaded for both source and target languages. This is a pre-requisite for the ICT tester to perform translation testing. It is detected that the target language content is missing for the attachment.

**Suggestions:**

This attachment is detected to be "in ICT scope", which means either:

1. When your ICT translation request has non-empty "attachment tags":

It is an attachment with a tag included in the "attachment tags" of  the translation request, and is referenced from at least one resource entry marked as "reviewed".

2. When your ICT translation request has empty "attachment tags":

It is an attachment referenced from at least one resource entry marked as "reviewed".

It is detected that the target language content is missing for this attachment, and the attachment is in the ICT scope. Please prepare and upload the target language screenshot to the attachment. (The target language can be found in the "language" field of this log entry.)

▻ For information on how to upload attachment content for a certain language, please refer to[Process: Translation with context - Step 3: Upload attachment](https://kb.strakertranslations.com/en/knowledge/translation-with-context)

**SCR0004** ⛔︎

**Level:**

Error

**Message:**

The source string timestamp is later than source screenshot timestamp.

**Explanation:**

The system detects that your source string has its value changed later than the source language screenshot is uploaded. This means that your source language screenshot could be using the old string value and could have been outdated. In such case, you need to provide a new screenshot for this attachment with the latest source string value.

**Suggestions:**

It is detected that your source string has its value changed after the source language screenshot is uploaded. In most cases, this indicates that your source language screenshot is outdated and you should provide a new screenshot with the latest source string value. Please upload the latest screenshot to the attachment.

If you confirmed the original screenshot has been the latest one, you need to perform the following steps to fix the issue:

1. 1. Delete the source language content (usually English) of this attachment.
   2. Upload the screenshot again for the source language.

⚠️ You need to delete the source language content first instead of directly uploading the same image again, as the system won't change the updated time if the content is exactly the same as the previous one.

▻ For information on how to upload attachment content for a certain language, please refer to[Process: Translation with context - Step 3: Upload attachment](https://kb.strakertranslations.com/en/knowledge/translation-with-context)

**SCR0005** ⛔︎

**Level:**

Error

**Message:**

The target string timestamp is later than target screenshot timestamp.

**Explanation:**

The system detects that the target language translation value of the string is changed later than the target language screenshot is uploaded. This means that your target language screenshot could be using the old translation value and could have been outdated. In such case, you need to provide a new screenshot for this attachment with the latest translation value.

**Suggestions:**

It is detected that your resource string has the target language translation value changed after the corresponding screenshot is uploaded. In most cases, this indicates that your target language screenshot is outdated and you should provide a new screenshot with the latest translation value. Please upload the latest screenshot to the attachment.

If you confirmed the original screenshot has been the latest one, you need to perform the following steps to fix the issue:

1. 1. Delete the target language content of this attachment. (The target language can be found in the "language" field of this log entry.)
   2. Upload the screenshot again for this target language.

⚠️ You need to delete the target language content first instead of directly uploading the same image again, as the system won't change the updated time if the content is exactly the same as the previous one.

▻ For information on how to upload attachment content for a certain language, please refer to[Process: Translation with context - Step 3: Upload attachment](https://kb.strakertranslations.com/en/knowledge/translation-with-context)

**SCR0006** ⚠️

**Level:**

Warning

**Message:**

Possible hardcoded strings detected: %s.

*(Note: %s will be replaced by the detected hard-coded strings.)*

**Explanation:**

If you have ever uploaded screenshot to the pseudo language "English (XP)" (locale code: "en-XP") for attachment auto-association, the system will also perform the hard-coded string detection. This warning message is to provide you the information of possible hard-coded strings detected on this screenshot for your reference and further actions. You don't have to fix it before submitting the ICT translation request.

**Suggestions:**

ℹ️ This is a "Warning" level message, no mandatory actions needed.

The message lists the possible hard-coded strings detected in your attachment, based on the screenshot you uploaded for the pseudo language "English (XP)".

It is a reminder for you to check if these strings are missing during the globalization effort. You may consider to extract them from the source code for translation.

Note that the hard-coded string detection result may include some false alarms. It just serves as a reminder for your awareness of some possible hard-coded string issues before ICT. It is not required to fix the issue before submitting the ICT translation request.

**SCR0007** ⚠️

**Level:**

Warning

**Message:**

The attachment with a tag included in TR's attachmentTags has no reference from any resource entry in ICT scope.

**Explanation:**

This attachment has a tag included in the "attachment tags" of the ICT translation request, which indicates the attachment is to be included in the ICT scope. However, no strings in the ICT scope (shown as R (reviewed) on GP Dashboard) are associated with it. It is a warning message for you to check if some association is missing for this attachment.

**Suggestions:**

ℹ️ This is a "Warning" level message, no mandatory actions needed.

The message serves as a reminder for you to check the association for this attachment. As you added a tag to it which is included in the "attachment tags" of the ICT translation request, you show the intention to include this attachment in the ICT scope for tester to verify.

However, the system does not find any association from the resource entry that is in the ICT scope (marked as "reviewed") with this attachment, and this might be a signal that you have missed the association for this attachment from some strings to be verified in this ICT.

There are some possibilities:

1. You would like to include this attachment in the ICT scope, which includes some strings to be verified: please associate these strings with the attachment.

▻ For information on how to associate attachment with resource entry, please refer to [Process: Translation with context - Step 4: Associate attachment](https://kb.strakertranslations.com/en/knowledge/translation-with-context)

2. You do not intend to include this attachment in the ICT scope, which is the reason why there is no association from strings to be verified: in this case, you should remove the tag from the attachment so that it won't be treated as in scope.

**SCR0008** ⛔︎

**Level:**

Error

**Message:**

The analysis of the pseudo translated (en-XP) screenshot is not yet completed. The current status is [%s].

(Note: %s will be replaced by the current status of the analysis, followed by a timestamp of when the status was updated.)

**Explanation:**

The system detects that you have uploaded a screenshot to the pseudo language "English (XP)" (locale code: "en-XP") for attachment auto-association. However, the process is not yet completed, indicating that it may still on-going, or may encounter some internal error.

**Suggestions:**

As the auto-association process has not been completed yet, some associations could be missing. Depending on the status reported in the message, below actions are suggested:

- - The current status is Pending or InProgress:

Please wait for a period of time and run the Readiness Check again.

If the error still presents and the status is not changing for a long time, please seek technical assistance on [#g11n-pipeline](https://ibm-gssc.slack.com/archives/C0EP2MFR7) slack channel.

- - The current status is Error:

Some internal error occurs, probably due to some transient environmental issues. Please upload the en-XP screenshot again to trigger a new run of the auto-association process.

If the problem persists, please seek technical assistance on [#g11n-pipeline](https://ibm-gssc.slack.com/archives/C0EP2MFR7) slack channel.

**SCR0009** ⛔︎

**Level:**

Error

**Message:**

There are no attachments with a tag [%s] available in this instance.

(Note: %s will be replaced by a tag name, which is included in the TR's "attachment tags" field.)

**Explanation:**

The system detects that there is one tag specified in the "attachment tags" of the translation request, but no attachments actually have the tag. The tag name might have been entered incorrectly.

**Suggestions:**

In the "attachment tags", you can enter the tag(s) of the attachments to be included in this ICT translation request. However, the system detected that you entered a tag name that no attachments actually have been tagged with. In most cases, this could be due to some typos on the tag names, or  some misunderstanding on the usage.

Please check the following:

- - You have added the correct tag for the attachments you want to include in this ICT.

▻ For information on how to add tags to an attachment, please refer to [Process: ICT - Step 5: Tag attachment](https://kb.strakertranslations.com/en/knowledge/in-context-testing-ict)

- - You have entered the correct tag into the "attachment tags" field of the translation request.

Please note that in the "attachment tags" field of your translation request, you should enter the tag name that you added to the attachments, instead of the attachment ID.

**SCR0010** ⚠️

**Level:**

Warning

**Message:**

Identical screenshots detected: %s

(Note: %s will be replaced by a list of duplicated attachments and their languages. For example, a1: en, de; a2: fr means the English and German screenshots of attachment a1, and the French screenshot of attachment a2, all three have identical content.​ )

**Explanation:**

The system detects that several attachment content (screenshots) are identical (by checking their MD5 hash values). As we generally expect the screenshots of different languages of the same attachment, or the screenshots of different attachments, should not have identical content, a warning is provided for your further check.

We added this test because of some real cases were reported due to the engineer wrongly uploaded the same screenshots to 2 different languages.

**Suggestions:**

ℹ️ This is a "Warning" level message, no mandatory actions needed.

Please check if the detected identical screenshots were uploaded in error. If you have checked and are certain the screenshot content is correct, you may ignore this warning.

**NOR0001** ⛔︎

**Level:**

Error

**Message:**

No bundles in this TR.

**Explanation:**

There is no bundles included in the translation request (yet).

**Suggestions:**

For an ICT translation request, it is required to have at least one bundle included. Please select the bundles for the translation request before you start the readiness check.

**NOR0002** ⛔︎

**Level:**

Error

**Message:**

The bundle does not exist.

**Explanation:**

The bundle to be included in the translation request does not exist in Globalization Pipeline.

**Suggestions:**

The system cannot find the bundle you specified in the translation request. For example, you might specify an incorrect bundle ID, or your bundle might have been deleted by someone else during the process of readiness check, etc. Please confirm again and specify the correct bundles in the translation request.

**NOR0003** ⛔︎

**Level:**

Error

**Message:**

The bundle does not have all specified target languages.

**Explanation:**

The translation request specifies some target languages which the bundle does not really have.

**Suggestions:**

This is a general issue of a translation request, not specific to ICT. Please confirm you specify the correct target languages that the bundle has. (If you are using dashboard, the system will only show the target languages the bundle has for your selection, so this error should never happen.)

**NOR0004** ⛔︎

**Level:**

Error

**Message:**

The source language is not supported.

**Explanation:**

You specified a source language that is not supported in Globalization Pipeline for this translation request.

**Suggestions:**

Currently, English is the default and the only supported source language in Globalization Pipeline, so you should never hit this issue. However, we keep the flexibility for future extension and this error may occur when we relax the source language limitation to accept other languages.

**NOR0005** ⛔︎

**Level:**

Error

**Message:**

The target language(s) %s are not supported.

(Note: %s will be replaced by the unsupported target language(s).)

**Explanation:**

You specified some target language code that is not supported in Globalization Pipeline for this translation request.

**Suggestions:**

Please confirm the language code you specified for the target language is correct and supported in Globalization Pipeline. (If you are using dashboard and select the languages from the list, you should never hit this error.)

**NOR0006** ⚠️

**Level:**

Warning

**Message:**

The resource entry is included in another TR [%s], which is still in progress. So it won't be included in this TR.

(Note: %s will be replaced by the translation request ID.)

**Explanation:**

This is a warning message to remind you the resource entry will be excluded in this translation request, as it has been included in a previous translation request which is still on-going. (The TR id is provided.)

**Suggestions:**

ℹ️ This is a "Warning" level message, no mandatory actions needed.

You have some translation requests that are still on-going. In Globalization Pipeline, the resource entry that has been included in a previous translation request will be automatically excluded from a later translation request.

If this has no impact to your planed scope, you can safely ignore this warning message. If this is not expected (e.g., you believe all previous translation requests should have been merged), please seek technical assistance on [#g11n-pipeline](https://ibm-gssc.slack.com/archives/C0EP2MFR7) slack channel.

**NOR0007** ⛔︎

**Level:**

Error

**Message:**

Failed to process readiness check [%s], please try again.

(Note: %s will be replaced by the error details.)

**Explanation:**

Readiness check cannot proceed due to some internal error, for example, a temporary outage of the underlying services or platform.

**Suggestions:**

Please try to run readiness check again. If the problem persists, please seek technical assistance on [#g11n-pipeline](https://ibm-gssc.slack.com/archives/C0EP2MFR7) slack channel.

**NOR0008** ⛔︎

**Level:**

Error

**Message:**

All bundles included in an ICT TR must use a same source language.

**Explanation:**

The source languages of the bundles included in your ICT translation request are different. It is required that the source language to be the same for all the bundles included in an ICT translation request.

**Suggestions:**

Please ensure all the bundles to be included in an ICT translation request to have the same source language.

Currently, English is the default and the only supported source language in Globalization Pipeline, so you should never hit this issue. However, we keep the flexibility for future extension and this error may occur when we relax the source language limitation to accept other languages.
