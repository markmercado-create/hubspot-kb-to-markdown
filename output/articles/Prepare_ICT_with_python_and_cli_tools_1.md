---
title: "Prepare ICT with python and cli tools"
subtitle: "The showcase for semi-automation approach to prepare ICT"
knowledge_base: "Globalization Help Center"
category: "Globalization Pipeline"
subcategory: "ict doc"
language: "en"
status: "PUBLISHED"
archived: "false"
last_modified: "1749606949872"
source_url: "https://help.straker.ai/en/g11n/prepare-ict-with-python-and-cli-tools"
exported_at: "2026-03-17T11:29:01Z"
---

# Prepare ICT with python and cli tools

### Introduction

Welcome to this tutorial on how to prepare attachments using the globalization pipeline tools when auto association approaches may not be suitable. As you are likely aware, in the world of ICT workflow, the proper preparation of matching attachments for resource strings is crucial to ensure success.

### Preparation steps

As describe in the flowchart below, we start from export the resource strings in specified bundles/languages. You can filter out the unreviewed resources strings to identify ICT scope. And then you need to locate the strings in product user interface, capture/save the screenshots in local directory and record the screenshots name in csv file. When the screenshots are ready, we could run the scripts to create/upload/tag attachments, and associate the resource string with attachment based on the record in csv file. The number indicated on the flow chart corresponds to the option number that can be utilized in the script tool.

### Steps to perform preparation

In this tutorial, we will demonstrate how to utilize existing gp-cli tools to complete this important task using Python scripts. This process involves the following steps:

    Step 0: Download and Configure tools

    Step 1: Export resource strings as a CSV file.

    Step 2: Create and upload the attachments with/without tags.

    Step 3: Update attachment tags.

    Step 4: Associate the attachments.

These steps will be thoroughly explained and demonstrated in the following sections. Additionally, all the scripts required for this tutorial can be downloaded from ict-tutorial [release page.](https://github.ibm.com/1t1p/ict-tutorial/releases) We hope that you will find this tutorial useful and that it will help you overcome any challenges you may encounter while preparing your attachments. So, let's get started!

### 

### Step 0: Download and Configure tools

For the first step, you need to install the pre-requisites, download the scripts and configure the environment variables. Follow these steps to get started:

1. Install the Python execution environment. The installation steps might be different for different system and version, you would need to refer to python site or operating system user guide for more information.

- - [Download Windows installer (64-bit)](https://www.python.org/ftp/python/3.11.2/python-3.11.2-amd64.exe)
  - [Download MacOS 64-bit installer (for macOS 10.9 and later)](https://www.python.org/ftp/python/3.11.2/python-3.11.2-macos11.pkg)

2. Install Python depended module "urllib3", "requests" based on environment need.

`py -m pip install requests   
py -m pip install urllib3`

3. You can get the latest version of scripts in <https://github.ibm.com/1t1p/ict-tutorial/releases>, download **semiauto\_showcase.zip** that contains the python script you need to run the operation below. And then unzip it.

4. Get the latest version of Globalization Pipeline Command line interface tool (gp-cli) from [Artifactory](https://na.artifactory.swg-devops.com/ui/native/txo-gp-maven-local/com/ibm/g11n/pipeline/gp-cli/)

5. Copy the ./**config\_template.ini** file to ./**config.ini** and replace the variables to match your environment.

```
[settings]  
# Absolute path of GP credentials  
gpJsonCredential = /Users/username/GPDemo/translation-ibm-demo.json  
# When using GP CLI, we need to configure the following three parameters  
# For GP CLI's certificates, please refer to: [6. Certificates] https://pages.github.ibm.com/1t1p/gp-tutorial/initial-setup.html  
# Trust store password  
trustStorePassword = password  
# Absolute path  to the keystore file  
keystorePath = /Users/username/GPDemo/.keystore  
# Absolute path to the gp-cli jar file  
# Latest GP CLI Jar can be downloaded from: https://na.artifactory.swg-devops.com/ui/native/txo-gp-maven-local/com/ibm/g11n/pipeline/gp-cli  
cliJarRealPath = /Users/username/GPDemo/gp-cli-20230323.jar  
  
[bundle]  
# Comma-separated list of bundle names to be exported  
bundleArray = bundle1,bundle2  
# Comma-separated list of language codes to be exported  
# language code can refer here: https://github.ibm.com/1t1p/caits/blob/master/data/language-ids.json  
languageArray = en-XP,en,fr,ja  
# Name of the exported csv file  
exportedcsvFile = ResourceStatusAndAttachmentMapping.csv  
  
[attachment]  
# Path to the folder where screenshots are stored, it should be a absolute path  
originalScreenshotPath = /Users/username/GPDemo/OrignalScreenshots  
screenshotsPath = /Users/username/GPDemo/Screenshots/   
# Comma-separated list of tags for attachments, used for grouping attachments,  
# Only a-z, A-Z, 0-9, hyphen (-), underscore (_), and period (.) are allowed for attachment tag.   
# Empty value or skip this setting means the tags will be kept empty  
tags = tag1,tag2  
# Optional. Description for all the attachments  
description = Attachments created for ICT  
# Path to the file containing a list of attachment IDs  
UpdAttachmentIDList = ./UpdAttachmentIDList.txt  
# File types for attachments (image/jpeg, image/png or image/gif)  
attachmentContentType = image/jpeg
```

Once your environment is configured, you can use the tool to prepare ICT. To use the script tool, simply enter the following command:

```
> python ict.py
```

This will launch the tool and present you with a selection list of four options as below.

```
***********************************************************  
Tool for preparing ICT process  
Please select the option you would like to run:  
    1: Export resource entry status  
    2: Upload screenshot tree structure as shipment attachment  
       If screenshots are not sorted by attachment id, please run 5 firstly  
    3: Update tags to attachment  
    4: Associate resource string and attachment  
       Prerequisite: Run 1 firstly, then make the association between entry and attachment in ResourceStatusAndAttachmentMapping.csv  
    5: Reorganize screenshot folders (Sort by language to sort by attachment id)  
    For detailed usage, refer to publisher: https://w3.ibm.com/w3publisher/ict/how-to/prepare-ict-with-python-and-cli-tools  
***********************************************************  
Please select(1,2,3,4,5)
```

Choose an option by entering the corresponding number and pressing enter. This will take you to the corresponding tool function and allow you to perform the desired task.

### Step 1: Export resource strings as a CSV file.

**Export the csv**

The first step in preparing ICT is to identify the strings that need to be tested. To do this, you can use the script tool to export the status of resource strings for the bundles and languages you specify.

To generate a CSV file that contains the bundle and language specified in the **config.ini** file, enter "**1**" in terminal.

```
Please select(1,2,3,4,5) 1  
File already exists. Do you want to delete it and continue? (Y/N): Y  
ResourceStatusAndAttachmentMapping.csv has been deleted.  
Start to export language entries for bundle [translation.json]......  
Language [en] for bundle [translation.json] is exported completely!  
Language [fr] for bundle [translation.json] is exported completely!  
Language [ja] for bundle [translation.json] is exported completely!  
Export job is completed and csv file is located at: /Users/peiyilin/Downloads/ict-tutorial/semiauto_showcase/ResourceStatusAndAttachmentMapping.csv  
To view the details of the execution, please refer to the log file in: log/ict_2023-04-12_16-10-02.log
```

Once you have the CSV file, you can import it into Excel using the following steps:

The detail steps might be changed for different version of Excel, you could refer to user document to import **UTF-8** content.

1. Open a new or existing Excel workbook.
2. Click on "File" in the top left corner of the screen.
3. Click on "Import" at the drop-down menu that appears.
4. In the "Import" dialog box, select "CSV file" from the list of options and then click on "Import" button
5. Browse and select the CSV file that contains the resource strings you want to import and click on "Get Data" button.
6. In the "Import Wizard - Step 1 of 3" dialog box, select "Unicode (UTF-8)" as the "File origin" to ensure that double-byte characters can be correctly displayed.
7. Click on "Next" to proceed to the next step of the wizard.
8. In the "Import Wizard - Step 2 of 3" dialog box, ensure that "Comma" is selected as the delimiter.
9. You can preview the imported data in the "Data Preview" section of this dialog box.
10. Click on "Next" to proceed to the next step of the wizard.
11. In the "Import Wizard - Step 3 of 3" dialog box, choose the destination for the imported data, such as a new worksheet or an existing one.   ![](media_files/undefined-Jul-22-2024-07-17-01-0774-AM.png)

12. Click on "**Finish**" to complete the import process.

It's worth noting that if garbled codes are displayed for double-byte characters, this is not a script issue. The default encoding of Excel is not UTF-8, which is why it's important to select UTF-8 as the file origin in step 6 of the import wizard.

**Sort out the testing scope**

When it comes to ICT, our focus is on strings that have been translated or reviewed by humans but haven't been verified on the UI. These strings are labeled as "reviewed" in the system.

To sort the reviewed strings by language, you can leverage Excel functions.

1. Select the imported sheet, click **Data** on menu, and then select **Sort** option.

2. You could sort entries order by selecting columns you want. Here we change **Sort by** column to Column A (Bundle ID), and then click on the **+** button to add column B (String ID) , and then click **OK** button.

![](media_files/undefined-Jul-22-2024-07-16-59-3945-AM.png)

3. Select the imported sheet, click **Data** on menu, and then select **Filter** option.

4. Click on column header with down arrow icon. Filter out the "reviewed" in column F.

![](media_files/undefined-Jul-22-2024-07-16-59-9025-AM.png)

5.  Then you would get a list of strings with "reviewed" status.

![](media_files/undefined-Jul-22-2024-07-16-59-1432-AM.png)

6.  Then you would need to locate the strings in user interface of your product, and capture the screenshots needed for in context testing. In the meantime, you need to assign an attachment id for the screenshot and update it in column H.

When updating the attachments name, you should notice:

- Reviewed strings appearing on the same UI should have the same attachment id. So there might be several resource strings with the same attachment id.
- For each String ID, we only need to fill the attachments in one language. For example, if you have *attachment A* for *key A* in French, we don't need to add the association in Japanese also.

  - Because the association is not language dependent. It establishes the connection between a resource entry and an attachment, which will have language specific attachment content.
- The attachments id recorded in csv file should be consistent with the attachment id you use to group the screenshots in screenshot storage directory.

![](media_files/undefined-Jul-22-2024-07-16-58-6608-AM.png)

**Group Screenshots**

It is recommended to group the screenshots by attachment ID, and then organize the language screenshots by their language ID within the corresponding attachment folder.

![](media_files/image-png-Aug-13-2024-02-44-32-8719-AM.png)

### Step 2: Create and upload the attachments.

Once you have captured the screenshots and arranged them in the specified tree structure, you are ready to create and upload the corresponding attachments.

To accomplish this, choose option 2 from the list of ICT tool options. This will based on the content of screenshot directory to generate an attachment list to create and then upload all of the screenshots located in the designated folder as attachments.

If you want to set attachment tags in the same time, you could specified the **tags** value in **config.ini**.

### Step 3: Tag the attachments.

When no tags are used, globalization pipeline will treat all the reviewed string as potential ICT scope. However, you can also leverage tags to define your own the ICT scope. With this scripting tool, you can assign or overwrite tags to attachments from a predetermined list. You need to create and place this attachment list file under the folder you specified in config.ini file.

To assign a tag to the attachments in the list, you need to follow the steps below:

1. Configure the variable listed below in config.ini. Replace the tags, description and your attachment id file location based on your preference.

```
[attachment]  
# Comma-separated list of tags for attachments  
tags = tag1,tag2  
# Description for all the attachments  
description = Attachments created for ICT  
# Path to the file containing a list of attachment IDs, one attachment per line  
UpdAttachmentIDList = ./UpdAttachmentIDList.txt
```

2. Run ict.py then choose option 3 from the list of ICT tool options.

It will overwrite the existingtags and descriptions as what is configured in **config.ini** for all the attachments listed in **AttachmentIDList.txt****.**

### Step 4: Associate the attachments

To establish a linkage between the resource string and attachment, it is necessary to record the attachment ID during the string locating and screenshot capturing process.

If you have saved the mapping attachment ID in the Excel file generated during Step 1, it is only necessary to record the association in English language. Updating it for each language is not required.

![](media_files/undefined-Jul-22-2024-07-17-00-2695-AM.png)

Then you could follow the steps:

1. Configure `exportedcsvFile` variable in config.ini. Replace the file name with the one you use to record the attachment id. Here we assume you used tool option 1 to export the csv file and use it to record attachment id.

```
[bundle]  
# Name of the exported csv file  
exportedcsvFile = ResourceStatusAndAttachmentMapping.csv
```

2. Run ict.py then choose option 4 from the list of ICT tool options.

```
Tool for preparing ICT process  
Please select the option you would like to run  
    1: Export resource entry status  
    2: Upload screenshot tree structure as shipment attachment  
    3: Add tags to attachment  
    4: Associate resource string and attachment  
Please select(1,2,3,4) 4  
Sucessfully generated the batch update shell scrip to udpate the entry-attachment association in ./temp/associateScript.sh  
Start to update the association, it might takes a while to complete this step....  
Complete the association updating, check the log file to see the detail: ./log/associateResult.txt  
To view the details of the execution, please refer to the log file in: log/ict_2023-04-07_14-34-46.log
```

It might take a while to complete the association update, which depends on the amount of association that need to be updated. The association result  would be kept in ./log/associationResult.txt, for you to check the errors during execution.  Once the association process is complete, the whole ICT preparation is done.  You are ready for ICT TR creation. Please go to [ICT process](https://kb.strakertranslations.com/en/knowledge/in-context-testing-ict) to complete the TR creation.
