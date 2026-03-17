---
title: "Create Pseudo Build"
knowledge_base: "Globalization Help Center"
category: "Globalization Pipeline"
subcategory: "ict doc"
language: "en"
status: "PUBLISHED"
archived: "false"
last_modified: "1749607132450"
source_url: "https://help.straker.ai/en/g11n/create-pseudo-build"
exported_at: "2026-03-17T10:52:04Z"
---

# Create Pseudo Build

### Manual Association - Link attachments to the PII entries by manual way

For cases that auto association can't be done, users would need to associate the screenshot attachment to testing strings.

The manual association is also supported by GP dashboard and CLI tools.

1. Globalization pipeline dashboard

1. 1. In the first step, we need to create the attachments. For UI operation, we could follow the section "**Upload the screenshots as Attachment**" to create the attachment
   2. When you want to upload a screenshot to cover all the testing strings in a bundle, you could specify the bundle versus attachment linkage.

         Switch to Bundles tab, find the bundle name related to the screenshots, click on the bundle name to open the bundle details page

![](https://20462040.fs1.hubspotusercontent-na1.net/hubfs/20462040/undefined-Aug-13-2024-05-53-12-1577-AM.png)

                     Select "Update attachment" option under the flowover menu

![](https://20462040.fs1.hubspotusercontent-na1.net/hubfs/20462040/undefined-Aug-13-2024-05-53-12-6334-AM.png)

                    Pick the related attachment

![](https://20462040.fs1.hubspotusercontent-na1.net/hubfs/20462040/undefined-Aug-13-2024-05-53-12-3789-AM.png)

         c. If you want to upload a screenshot only related to one of the testing strings in a bundle, you could specify the bundle entry versus attachment linkage.

  

                    First, user could locate the bundle as previous step and then click **English** locale

![](https://20462040.fs1.hubspotusercontent-na1.net/hubfs/20462040/undefined-Aug-13-2024-05-53-13-0054-AM.png)

  

                     Use filter to find the string

![](https://20462040.fs1.hubspotusercontent-na1.net/hubfs/20462040/undefined-Aug-13-2024-05-53-13-6372-AM.png)

                     Click on "**Update & Display the attachments**"

![](https://20462040.fs1.hubspotusercontent-na1.net/hubfs/20462040/undefined-Aug-13-2024-05-53-13-3316-AM.png)

                    Check related attachments

![](https://20462040.fs1.hubspotusercontent-na1.net/hubfs/20462040/undefined-Aug-13-2024-05-53-12-8219-AM.png)

  
  

2. Command line tool (Note: obtain the latest version in <https://github.ibm.com/1t1p/gpv2-java-tools/releases>)

          a. Bulk create and import attachments （refer to [bulk create and import command](https://github.ibm.com/1t1p/gpv2-java-tools/tree/master/gp-java-tools/gp-cli#bulk-operations) in CLI document)  
  

b. For bundle vs attachment association, the [update-attachment](https://github.ibm.com/1t1p/gpv2-java-tools/tree/master/gp-java-tools/gp-cli#update-update-bundle) command with -a parameter could be used to link screenshots with bundle.

c. For bundle entry versus attachment association, please use CLI [update-res-entry](https://github.ibm.com/1t1p/gpv2-java-tools/tree/master/gp-java-tools/gp-cli#update-res-entry-previously-mark) command with -a parameter.
