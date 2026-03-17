---
title: "In-context testing (ICT)"
subtitle: "from Globalization Pipeline dashboard"
knowledge_base: "Globalization Help Center"
category: "Globalization Pipeline"
subcategory: "ict doc"
language: "en"
status: "PUBLISHED"
archived: "false"
last_modified: "1749607123973"
source_url: "https://help.straker.ai/en/g11n/in-context-testing-ict"
exported_at: "2026-03-17T10:52:05Z"
---

# In-context testing (ICT)

### Definition

In-context testing (ICT) is a post-translation process to ensure translation quality by comparing product UI English screenshots with the translated UI screenshots.

### Scope

During ICT, the tester will check for:

- **Correctness:** Verify the correctness of translation in context
- **Completeness:** Verify that there is no translatable data left in English (hardcoded strings)
- **Appearance:** Verify that the expansion of PII  does not exceeds the space (truncation), Other issues like concatenation, overlap, inappropriate wrapping, alignment, Bidi, etc.
- **Consistency:** Verify the consistency of translation of titles/labels on different panels.
- **Mis-translation:** Omissions or mistranslations of keywords or sentences leading to incorrect or incomprehensive translation
- **Mismatch:** translated version does not match English reference version (back level or wrong version translation)

### Workflow

With Globalization Pipeline, product development team can create in-context testing (ICT) translation requests for purpose of translation testing. With ICT translation request, translation testers can perform the testing with attached screenshots in shipment and do the update for resource entries.

![](https://20462040.fs1.hubspotusercontent-na1.net/hubfs/20462040/undefined-Jul-22-2024-07-22-20-4245-AM.png)

![](https://w3.ibm.com/w3publisher/)

### Differences from Legacy ICT

The In-context testing (ICT) approach differs from Legacy ICT translation requests in several ways:  

- **No pre-booking step:** There is no need for a Straker TJ number or iteration ID to be submitted with files.
- **Single iteration only:** The testing process is limited to a single iteration.
- **No dependencies on WEP:** Screenshots for testing needs to be uploaded to Globalization Pipeline attachments.
- **Defect reporting:** Translation testers report defects using Globalization pipeline's defect API, with a unique issue tracking ID assigned to each ICT Translation Request.

### Steps

The four steps for **attachment preparation** are:

    Step1: Prepare ICT screenshots

    Step2: Create attachment

    Step3: Upload attachment

    Step4: Associate attachment

    Step5: Tag attachment

After all the attachment are ready, you can proceed to do **translation request creation**

    Step6: Create a draft translation request

    Step7: Run readiness check and Fix issues

    Step8: Send ICT translation request

Then tester could perform their test with the resource strings in the TR and report issues they found. When the test is done,

    Step9: export the issues translator report to take follow up actions

### Step1: Prepare ICT screenshots

First, you need to prepare the screenshots for translation testing. For in-context testing, you need to prepare the screenshots for source and target languages.

You need to take UI screenshots in one of the following supported image formats, including:

- JPEG
- GIF
- PNG

***▸** For more information on preparing screenshots images, refer to " [How-to / Prepare UI screenshots](https://kb.strakertranslations.com/en/knowledge/preparing-ui-screenshots)".*

***▸**  If you have a huge amount of screenshots and would like to leverage the **auto-association** feature, you need to prepare the screenshots of pseudo language "English (XP)" as well. Refer to "[How-to / Perform auto-association](https://kb.strakertranslations.com/en/knowledge/auto-association)**"** for more information.*

### Step2: Create attachment

In order to create screenshot ICT attachments , you can utilize the identical UI or CLI operation as in the ICX flow. For detail information, refer to [Process - Translation with context Step2 Create attachment](https://kb.strakertranslations.com/en/knowledge/translation-with-context).

### Step3: Upload attachment

To upload the screenshots as attachment content, you could follow the same UI or CLI operation as in ICX flow. For detail information, refer to [Process - Translation with context Step3 Upload attachment](https://kb.strakertranslations.com/en/knowledge/translation-with-context)

### Step4: Associate attachment

There are two ways to associate the screenshots to specific resource string: by following the UI or CLI operation within the ICX flow. For a more detailed explanation, please refer to [Process - Translation with context Step4 Associate attachment](https://kb.strakertranslations.com/en/knowledge/translation-with-context) and its guidelines on how to associate attachments.

### Step5: Tag attachment

In the In-Context Testing (ICT) flow, you have the flexibility to assign multiple tags to each attachment, allowing you to easily group them into different sets for better organization and management. When generating an ICT translation request, you have the option to define a group of tags that determine the scope of attachments to be included in it With the ability to customize and organize your attachments through tagging, ICT makes it easy to keep track of all your testing materials and minimizing the risk of something being forgotten or overlooked.

**Tagging with GP Dashboard**

If you would like to assign the "**ICT\_2023April**" tag to identify the ICT shipment to which an attachment belongs, and also specify the UI component for the screenshot, you can easily do so with this workflow.

1. On the **Attachments** tab, click on the attachment name "**quickTranslation-01**" .

![](https://20462040.fs1.hubspotusercontent-na1.net/hubfs/20462040/undefined-Jul-22-2024-07-22-28-1406-AM.png)

2. Click on the overflow menu in the header of attachment, and then click on **Update attachment**

**![](https://20462040.fs1.hubspotusercontent-na1.net/hubfs/20462040/undefined-Jul-22-2024-07-22-21-4992-AM.png)**

3. Input "**ICT\_2023April,QuickTrans-UI**"in In **Attachment tags** field, and then click on **Update** button.

![](https://20462040.fs1.hubspotusercontent-na1.net/hubfs/20462040/undefined-Aug-13-2024-07-07-47-0326-AM.png)

4. You will see the newly created attachment tags in attachment detail.

![](https://20462040.fs1.hubspotusercontent-na1.net/hubfs/20462040/undefined-Aug-13-2024-07-07-56-1784-AM.png)

5. It is also possible to add tags to attachment when you create a new attachment. You could see the attachment tags in creation process. Refer to link for more info in [Process - Translation with context Step2 Create attachment section](https://kb.strakertranslations.com/en/knowledge/translation-with-context)

**Tagging with command line interface tool (gp-cli)**

To create an attachment with specific tags, you can use the "**create-attachment**" command. For example, by using this command, you can quickly and easily create an image/jpg attachment with the ID "**attachment01**" and assign it the tag "**ICT\_2023April**".

The parameters you can specify:

- **-a** to provide an attachment name that you want to create.
- **-t** to provide a content type for the screenshot you want to use.
- **-g** to provide a list of tags separated by comma.
- **-j** point to a credential file.

```
java -jar gp-cli.jar create-attachment -a attachment01 -t image/jpg -g "ICT_2023April,QuickTrans-UI" -j creds.json
```

2. Use "**update-atachment**" command to update an attachment with a certain tag. For example, below command update attachment "**attachment01**" and tag "**ICT\_2023April**":

The parameters you can specify:

- **-a** to provide an attachment name that you want to create.
- **-g** to provide a list of tags separated by comma.
- **-j** point to a credential file.

```
java -jar gp-cli.jar update-attachment -a attachment01 -g "ICT_2023April,QuickTrans-UI" -j creds.json
```

3. In addition to creating attachments one at a time, you can also use the bulk "**create-attachment**" and "**update-attachment**" commands to manage multiple attachments at once. By listing multiple attachments in a file such as "**attachmentlist.txt**", you can easily update the tags for all of them with just a few simple commands. For example, you can update multiple attachments and assign them both the "**ICT\_2023April**" and "**QuickTrans-UI**" tags using the following command.

The parameters you can specify:

- **-al** to provide an attachment list name that contains a list of attachment ids you want to create.
- **-t** to provide a content type for the screenshot you want to use.
- **-g** to provide a list of tags separated by comma.
- **-j** point to a credential file.

```
java -jar gp-cli.jar create-attachment -al ./attachmentlist.txt -t image/jpg -g "ICT_2023April,QuickTrans-UI" -j creds.json  
java -jar gp-cli.jar update-attachment -al ./attachmentlist.txt -g "ICT_2023April,QuickTrans-UI" -j creds.json
```

```
#attachmentlist.txt  
attachment1  
attachment2  
attachment3
```

- *For the latest information,* 
  - *refer to the* [***create-attachment** command*](https://github.ibm.com/1t1p/gpv2-java-tools/tree/master/gp-java-tools/gp-cli#create-attachment) *and* [***update-attachment** command*](https://github.ibm.com/1t1p/gpv2-java-tools/tree/master/gp-java-tools/gp-cli#update-attachmen) *in gp-cli README page.*

### 

### Step6: Create a draft translation request

To request an In-Context Testing, you just need to create a draft translation request, which is similar to how you would create a translation request for regular translation or legacy ICT. You are recommended to create the draft translation request for the In-Context Testing in advance because this helps you plan out what you need to do for your testing and make sure that everything is included.

**With Dashboard**

If you are planning to send an In-Context Testing translation request, for example, in May 2023, it is helpful to create the draft translation request in advance, for example, in April or even earlier.

1.   On the **Translation Requests** tab, click on the **New Request** button.

2.   Pick the bundles you want to include in the translation on step1 and click **Next** button

![](https://20462040.fs1.hubspotusercontent-na1.net/hubfs/20462040/undefined-Jul-22-2024-07-22-23-4464-AM.png)

![](https://w3.ibm.com/w3publisher/)3.   Select **ICT** Request type and input the fields on step3 (see examples below), and then click **Next** button.

- **Expected return time**: Normal

  - There are two choices: "**Normal**" and "**Urgent**." These options help the translation project manager know how urgent a job is.
- **Translation request name**: ICT2023April
- **Profile ID**: default
- **Issue Tracking ID**: **2023Q1TRdefect**

  - Default value for issue tracking id is TR id. It is possible to assign a unique ID to group defects across different translation requests. Assume you want to group all defects in 2023 first quarter into same defect list, you could specify **2023Q1TRdefect** as Issue Tracking ID for all the translation requests created in 2023 first quarter.
- **Attachment tags**: ICT\_2023April

  - You can choose to use tags or not. They help to define the scope of the testing attachments.
- **Contact email**: test@ibm.com
- **Special Instructions**: ICT\_2023April TR instruction

![](https://20462040.fs1.hubspotusercontent-na1.net/hubfs/20462040/undefined-Jul-22-2024-07-22-24-4442-AM.png)

![](https://20462040.fs1.hubspotusercontent-na1.net/hubfs/20462040/undefined-Jul-22-2024-07-22-27-0032-AM.png)

4.  The final step in the process entails reviewing the saved information for your translation request to ensure that all necessary details have been included and that the request is ready for in-context testing. We recommend taking a moment to thoroughly review the information to ensure its accuracy before proceeding.

![](https://20462040.fs1.hubspotusercontent-na1.net/hubfs/20462040/undefined-Aug-13-2024-06-53-14-4071-AM.png)

**With command line interface tool (gp-cli)**

1. To create draft ICT translation request, you can use **"****submit-ict-tr**" command to create a draft translation request.

The parameters you can specify:

- **-j** point to a credential file.
- **-g** to provide a comma separated list of attachment tags to be associated with this TR.
- **-t** to provide translation note that you want to add.
- **-l** to provide a comma separated target language list.
- **-e** to provide additional e-mail addresses for status notification
- **-b** to provide a comma separated bundle list.
- **-n** to provide a translation request name.

```
java -jar gp-cli.jar create-ict-tr -n "ICT shipment for 2023April" -b trasnlation.json -e tester@ibm.com -l fr -t "this is test TR" -g "ICT_2023April" -j credential.json
```

### Step7: Run readiness check and Fix issues

After completing the preparation of the screenshot and creating the draft TR, the next step is to perform a readiness check to confirm that the translation request is ready for submission.

**With Dashboard**

1. By clicking on "**Check readiness**" during the final step of creating a translation request, you can initiate the readiness check process right away.

![](https://20462040.fs1.hubspotusercontent-na1.net/hubfs/20462040/undefined-Aug-13-2024-06-53-10-9317-AM.png)

2. Click **OK** button to start the readiness check.

![](https://20462040.fs1.hubspotusercontent-na1.net/hubfs/20462040/undefined-Aug-13-2024-06-53-12-2182-AM.png)3. The readiness check process may take some time to complete. Once you receive a notification email, you can return to the dashboard to view the results. If the Readiness check status displays as "**Ready**", it indicates that there are no critical issues with the request and that the translation request is now suitable for submission.

![](https://20462040.fs1.hubspotusercontent-na1.net/hubfs/20462040/undefined-Jul-22-2024-07-22-25-5736-AM.png)

4. To ensure that you have not missed any test items by mistake, it is advisable to review the readiness check details. You can view the readiness check results by clicking on the name of the translation request. Additionally, you can download the readiness check report in CSV format, which can be useful for filtering, sorting, or keeping it as a log.

![](https://20462040.fs1.hubspotusercontent-na1.net/hubfs/20462040/undefined-Aug-13-2024-06-53-15-5930-AM.png)

5. To obtain more information regarding the validation items and how to resolve any errors identified during the readiness check process, please refer to the ***"[How to - Readiness Check](https://kb.strakertranslations.com/en/knowledge/ict-readiness-check)"*** guide.

6. Once you have followed the instructions provided to address the errors identified in the report, you can proceed to run the readiness check once again.

![](https://20462040.fs1.hubspotusercontent-na1.net/hubfs/20462040/undefined-Jul-22-2024-07-22-22-5921-AM.png)7. Continue to repeat the previous two steps until the translation is completely error-free. At this point, the translation request will be ready for submission.

**With command line interface tool (gp-cli)**

1. If you wish to review the content of a draft ICT translation request, you can utilize the "**check-ict-tr**" command to perform a readiness check on the request.

The parameters you can specify:

- **-t** to provide the translation request id that you want to submit.
- **--items** to specify the type of check you wish to perform, for ICT shipment checks, you can use "ict-content"
- **-j** point to a credential file.

```
java -jar gp-cli.jar check-ict-tr -t "ee5889f828429ad6a88821e4f1b636db" --items ict-contents -j credential.json
```

2. To export the readiness check report, you can run the command "**export-ict-readiness-report****"** to get it.

The parameters you can specify:

- **-t** to provide the translation request id that you want to get.
- **-o** to specify exported file name
- **-j** point to a credential file.

```
java -jar gp-cli.jar export-ict-readiness-report -t "f77f55ee40e9969b82457574091f10a7" -o 0316.csv -j credential.json
```

### Step8: Send ICT translation request

Once the readiness check is completed without any errors, the readiness status of the translation request will be updated to "**READY**", indicating that it is now suitable for submission. You may proceed to send the translation request at this point. If you change the ICT scope or updated the resource entries, updated translation values, attachments or attachment contents and tags for this ICT translation request, you will need to re-run the readiness check before submission.

**With Dashboard**

1.   On the **Translation Requests** tab, click on the overflow menu and click on **Submit**.

![](https://20462040.fs1.hubspotusercontent-na1.net/hubfs/20462040/undefined-Jul-22-2024-07-22-26-2413-AM.png)

**With command line interface tool (gp-cli)**

1.   To submit a translation request that is in the "Ready" status, utilize the "**submit-ict-tr**" command.

The parameters you can specify:

- **-t** to provide the translation request id that you want to submit.
- **-j** point to a credential file.

```
java -jar gp-cli.jar submit-ict-tr -t "dc52e631283e5f49dfe0b73cc6cf135f" -j credential.json
```

### Step9: Review issues report

When the testing is done, you could export the defect list from dashboard or cli to review them and take follow up actions.

**With Dashboard**

1. On the **Translation Requests** tab, click on the translation request name, or click on overflow menu to select **View the translation request detail**.

2. To view a summary of the defects identified in the translation request, scroll to the bottom of the translation request detail page. Here, you will find a table that summarizes the number of defects present in each language and their respective severity levels.

![](https://20462040.fs1.hubspotusercontent-na1.net/hubfs/20462040/undefined-Aug-13-2024-06-53-13-4300-AM.png)

3. To obtain further details regarding the defects identified during the In-Context testing , you can download the zip file for more comprehensive information or the CSV file for a quick summary.

![](https://20462040.fs1.hubspotusercontent-na1.net/hubfs/20462040/undefined-Jul-22-2024-07-22-18-7566-AM.png)

####

**With command line interface tool (gp-cli)**

1. Utilize the "**export-defects**" command to export all defects reported by translation testers as an attachment, using a specified tracking ID.

  

The parameters you can specify:

- **-t** to provide Issue Tracking ID
- **-r** to specify the report type. Currently HTML or CSV report type could be generated
- **-o** to specify the file name where the exported data will be written.
- **-j** point to a credential file.

```
java -jar gp-cli.jar export-defects -t 2023Q1TRdefect -r html -o ./2023Q1TRdefect -j credential.json
```
