---
title: "Preparing UI Screenshots"
subtitle: "Prepare screenshots for translation and testing in context"
knowledge_base: "Globalization Help Center"
category: "Globalization Pipeline"
subcategory: "ict doc"
language: "en"
status: "PUBLISHED"
archived: "false"
last_modified: "1749607050857"
source_url: "https://help.straker.ai/en/g11n/preparing-ui-screenshots"
exported_at: "2026-03-17T10:52:05Z"
---

# Preparing UI Screenshots

In this article, we will explain how the screenshots are kept on globalization pipeline, and how to capture a suitable screenshots for translation reference.

### Attachments versus Screenshots

In globalization pipeline, all reference documents provided to translators could be stored as attachments. There are several attachment types supported by Globalization Pipeline, that includes:

- **Image formats** like PNG, JPEG, GIF, and SVG
- **Document formats** like HTML and PDF
- **URL link** that points to some public web sites like IBM Knowledge Center.

The most useful translation reference could be the UI screenshots that contain the strings to be translated or to be reviewed by a human translator.

For each screenshot, we would create an attachment container to hold it, and then the attachment content can be uploaded for specific language after the attachment container is created. During ICT, we can also leverage this feature to provide screenshots for all languages in the testing scope for ICT tester to verify.

For example, if we have 10 screenshots for ICT test in 5 languages , we would create 10 attachments, and upload 5 language screenshot into each attachments.

- Attachment is visible in instance level, it could be associated to any bundle/bundle entry/ file in the instance.
- To use Globalization Pipeline for translation with context, English screenshots and/or documents are required.
- In order to utilize Globalization Pipeline for ICT, it is necessary to have NL screenshots prepared for each language to be validated, along with English screenshots.
- Pseudo screenshots are necessary if users desire an automated linkage between PII entries and screenshots.

### Requirement for screenshots

- When capturing screenshots of the product UI, ensure that the full window is captured and that any unrelated background is excluded.
- The minimum resolution for the screenshots should be 1024x768.
- Name the screenshots meaningfully and maintain consistency across different languages.
- The supported screenshot file formats are gif, jpeg and png files.
- For screenshots used in auto association

  - If the screenshots will be used for auto association, it's worth noting that the recognition of pseudo strings is dependent on OCR technology. If the UI font size is smaller than 12 or the UI background is dark, it may impact the recognition rate.
  - It's important to avoid capturing screenshots with overlapping elements, as this can also affect the recognition and segmentation of UI strings.

    - For instance, take a look at the screenshot below where the text present in various overlapping user interface components will be identified as a singular resource entry.

      ![](https://20462040.fs1.hubspotusercontent-na1.net/hubfs/20462040/undefined-Aug-12-2024-07-29-10-4214-AM.png)

![](https://w3.ibm.com/w3publisher/)
