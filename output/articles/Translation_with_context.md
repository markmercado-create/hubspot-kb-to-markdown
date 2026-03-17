---
title: "Translation with context"
subtitle: "for better translation quality"
knowledge_base: "Globalization Help Center"
category: "Globalization Pipeline"
subcategory: "ict doc"
language: "en"
status: "PUBLISHED"
archived: "false"
last_modified: "1749607123816"
source_url: "https://help.straker.ai/en/g11n/translation-with-context"
exported_at: "2026-03-17T10:52:05Z"
---

# Translation with context

### Translation with context

With Globalization Pipeline, product development team can now provide **attachments** and associate them with bundles and resource entries. When a translation request (TR) is submitted for human translation, translators can refer to the associated attachments and get the context information of the resource entries.

### Workflow

Below diagram shows a typical workflow of translation with context using Globalization Pipeline. The block **Attachment Preparation** is the newly introduced step for achieving translation with context.

![](https://20462040.fs1.hubspotusercontent-na1.net/hubfs/20462040/undefined-Jul-22-2024-07-20-18-7782-AM.png)

### Step 1: Prepare reference material

First, you need to prepare the attachment used for translation reference. One of the most useful translation reference could be the English UI screenshots that contain the strings to be translated or to be reviewed by a human translator. Besides UI screenshots, you can also provide related documents such as HTML or PDF files, or a URL link that points to some public web sites like IBM Knowledge Center.

Three types of attachments are supported in Globalization Pipeline:

- Image files, including:

  - JPEG
  - GIF
  - PNG
  - SVG

**▸** *For more information on preparing screenshots images, refer to "[How-to / Prepare UI screenshots](https://kb.strakertranslations.com/en/knowledge/preparing-ui-screenshots)".*

**▸**  *If you have a huge amount of screenshots and would like to leverage the **auto-association** feature, you need to prepare the screenshots of pseudo language "English (XP)" as well. R**efer to "[How-to / Perform auto-association](https://kb.strakertranslations.com/en/knowledge/auto-association)**"** for more information.*

- Document files, including:

  - PDF
  - HTML
- External reference links:

  - URL links that point to public web resources

### Step 2: Create attachment

Now, let's create the attachments on GP.

The attachment we are going to create is like a container that holds the attachment content for different languages. Attachment content can be uploaded only for a specific language after the attachment container is created.

**With Dashboard**

Assuming you would like to create an attachment of a JPEG image for a specific panel.

1. On the **Attachments** tab, click the **New Attachment** button.

![](https://20462040.fs1.hubspotusercontent-na1.net/hubfs/20462040/undefined-Jul-22-2024-07-20-17-1514-AM.png)

2. Enter an **Attachment ID****.**

**⚠** *Attachment ID needs to be unique within the instance.*

![](https://20462040.fs1.hubspotusercontent-na1.net/hubfs/20462040/undefined-Jul-22-2024-07-20-25-1756-AM.png)

3. Select the **Content Type** of attachmentfrom the drop-down menu.

![](https://20462040.fs1.hubspotusercontent-na1.net/hubfs/20462040/undefined-Jul-22-2024-07-20-26-8814-AM.png)

ⓘ If the attachment is an external reference link, select the "**Is external reference**" checkbox.

![](https://20462040.fs1.hubspotusercontent-na1.net/hubfs/20462040/undefined-Jul-22-2024-07-20-17-8219-AM.png)

4. Optionally, you can enter a **Description** for the attachment.

![](https://20462040.fs1.hubspotusercontent-na1.net/hubfs/20462040/undefined-Aug-13-2024-06-17-21-3651-AM.png)

5. Click **Save** to complete the attachment creation. You will see the newly created attachment in the table.

![](https://20462040.fs1.hubspotusercontent-na1.net/hubfs/20462040/undefined-Aug-13-2024-06-17-25-7718-AM.png)

**With command line interface tool (gp-cli)**

1. Use **create-atachment** command to create an attachment with a certain content type. For example, below command creates an image/jpg attachment with id attachment01:

```
java -jar gp-cli.jar create-attachment -a attachment01 -t image/jpg -d "description of the attachment (optional)" -j creds.json
```

2. Use **create-atachment** command with **-e** option to create an external reference attachment:

```
java -jar gp-cli.jar create-attachment -a attachment02 -e -j creds.json
```

**▸**    *For the latest information, refer to the **create-attachment** command in gp-cli README page:* [*https://github.ibm.com/1t1p/gpv2-java-tools/tree/master/gp-java-tools/gp-cli#create-attachment*](https://github.ibm.com/1t1p/gpv2-java-tools/tree/master/gp-java-tools/gp-cli#create-attachment)

### 

### Step 3: Upload attachment

After the attachment is created, you can upload the content for a certain language.

**With Dashboard**

Assuming you would like to upload a English screenshot JPEG image to the attachment.

1. On the **Attachment** tab, select the attachment you created.

![](https://20462040.fs1.hubspotusercontent-na1.net/hubfs/20462040/undefined-Aug-13-2024-06-17-20-7817-AM.png)

2. Click the **Upload Content** button at the right-hand side.

![](https://20462040.fs1.hubspotusercontent-na1.net/hubfs/20462040/undefined-Aug-13-2024-06-17-24-9568-AM.png)

3. For the **Target language** field, select the language you want to upload. (In this example, we select *English*.)

![](https://20462040.fs1.hubspotusercontent-na1.net/hubfs/20462040/undefined-Jul-22-2024-07-20-21-0041-AM.png)

4. For the **File** field, click **Browse** to select the file you want to upload. (In this example, we select the JPEG screenshot file we prepared in advance.)

![](https://20462040.fs1.hubspotusercontent-na1.net/hubfs/20462040/undefined-Jul-22-2024-07-20-19-6216-AM.png)

5. Click **Upload** to complete the uploading.

![](https://20462040.fs1.hubspotusercontent-na1.net/hubfs/20462040/undefined-Jul-22-2024-07-20-24-2266-AM.png)

Now, you can see the **English** row appears on the table. From the overflow menu, you can choose to download the uploaded content for English, or delete the content if it is no longer needed.

![](https://20462040.fs1.hubspotusercontent-na1.net/hubfs/20462040/undefined-Aug-13-2024-06-17-22-2505-AM.png)

**With command line interface tool (gp-cli)**

1. Use **import-atachment** command to import a file to an attachment for a specific language:

```
java -jar gp-cli.jar import-attachment -a attachment01 -F path/to/source/image.jpg -l en -j creds.json
```

2. If the attachment is an external reference, use **-ln** option to provide a link for a specific language:

```
java -jar gp-cli.jar import-attachment -a attachment01 -ln https://it.docs.ibm.com/myreference.html -l en -j creds.json
```

**▸**    *For the latest information, refer to the****import-attachment*** *command in gp-cli README page:* <https://github.ibm.com/1t1p/gpv2-java-tools/tree/master/gp-java-tools/gp-cli#import-attachment>

### 

### Step 4: Associate attachment

You need to establish the association between a resource entry and an attachment by updating the resource entry data for translators to reference the attachment content when translating an entry. (Note: it will become handy for the upcoming ICT, if ICT is planned)

![](https://20462040.fs1.hubspotusercontent-na1.net/hubfs/20462040/image-png-Aug-13-2024-06-46-47-3449-AM.png)

**▸**  *If you have a huge amount of screenshots and would like to leverage the **auto-association** feature, r**efer to "[How to / Perform auto-association](https://kb.strakertranslations.com/en/knowledge/auto-association)**"** for more information.*

**With Dashboard**

Assuming you would like to associate the attachment previously established to one resource string with the resource key of "*qualityoptions.mt*".

1. On the **Bundles** tab, select the bundle that contains the resource string to be associated.

![](https://20462040.fs1.hubspotusercontent-na1.net/hubfs/20462040/undefined-Aug-13-2024-06-17-20-0469-AM.png)

2. Click **English** in the **LANGUAGE** column to view the source entries.

![](https://20462040.fs1.hubspotusercontent-na1.net/hubfs/20462040/undefined-Aug-13-2024-06-17-23-0283-AM.png)

3. Find the resource entry to be associated. You can search it with the resource key using the search bar at top of the table.

![](https://20462040.fs1.hubspotusercontent-na1.net/hubfs/20462040/undefined-Aug-13-2024-06-17-24-0809-AM.png)

4. From the overflow menu, select **Update attachments**.

![](https://20462040.fs1.hubspotusercontent-na1.net/hubfs/20462040/undefined-Jul-22-2024-07-20-26-1527-AM.png)

5. In the **Attachments** list, select the attachment(s) you want to associate with. Click **Update** to save the change.

![](https://20462040.fs1.hubspotusercontent-na1.net/hubfs/20462040/undefined-Jul-22-2024-07-20-22-1727-AM.png)

To check the association result, you can select **Display associated attachments**from the overflow menu.

![](https://20462040.fs1.hubspotusercontent-na1.net/hubfs/20462040/undefined-Jul-22-2024-07-20-27-8048-AM.png)

You can see the list of associated attachments on the pop-up window.

![](https://20462040.fs1.hubspotusercontent-na1.net/hubfs/20462040/undefined-Jul-22-2024-07-20-23-1224-AM.png)

**With command line interface tool (gp-cli)**

1. Use the command **update-res-entry** to update the attachment association of the resource entry. For example, below command add association of "attachment01" to the resource key "key01" under bundle "bundle01":

```
java -jar gp-cli.jar update-res-entry -b bundle01 -l en -k "key01" -a attachment01 -j mycreds.json
```

**▸**    *For the latest information, refer to the **update-res-entry** command in gp-cli README page:* <https://github.ibm.com/1t1p/gpv2-java-tools/tree/master/gp-java-tools/gp-cli#update-res-entry-previously-mark>

### Optional step: Tag attachment

As the feature introduced with the ICT (in-context testing) support, you can have the flexibility to assign multiple tags to each attachment, allowing you to easily group them into different sets for better organization and management. By tagging attachments with a tag to indicate their usage (e.g., "TR\_2023May"), it will be handy for you to delete, to locate, or to include attachments into the scope of future ICT.

We recommend you to add the attachment tags when attachments are being created. Please refer to [Process ICT (In-context testing) / Step5: Tag attachment](https://kb.strakertranslations.com/en/knowledge/in-context-testing-ict) for how to tag attachments.

### Step 5: Send translation request

After you completed the above steps for all the attachments you have prepared, you can now proceed to send a translation request. As you have created the attachments, uploaded the attachment content, and associated them with the resource strings, the information will be included in the translation request, and the translators will be able to refer to the attached context information, e.g., the English screenshots, when performing translation on their workbench.

▸  *The steps to send a translation request (TR) is the same as before. If you are new to Globalization Pipeline, please refer to [Sending Content for Human Translation](https://kb.strakertranslations.com/en/knowledge/sending-content-for-human-translation) for more details.*
