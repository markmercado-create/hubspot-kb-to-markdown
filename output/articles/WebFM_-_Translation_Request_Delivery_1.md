---
title: "WebFM - Translation Request Delivery"
knowledge_base: "Globalization Help Center"
category: "WebFM"
subcategory: "How to guide"
language: "en"
keywords: "webfm"
status: "PUBLISHED"
archived: "false"
last_modified: "1772244298503"
source_url: "https://help.straker.ai/en/g11n/webfm/translation-request-delivery"
exported_at: "2026-03-17T11:35:44Z"
---

# WebFM - Translation Request Delivery

When the Translation Request (TR) is in “Merged” status (as per automated mail + post in the #alerts-ibm-gp Slack channel), the following steps should be followed:

Go to the Translation Requests page in the Globalization Pipeline (GP) and verify that your request is in Merged state (Note that Partially Merged means it’s not yet completed):

![Picture11](media_files/Picture11_1.png)

After that, go to WebFM, select the application, and go to Work with English Files. Sort or filter by date and find the files you sent for translation:  
  
![Picture12](media_files/Picture12_1.png)

Select the files with the checkbox (they may be already selected if you worked with them previously) and click on the green Run GP Import Export button to reach this panel:  
  
![Picture13](media_files/Picture13_1.png)

Uncheck the Upload to GP Source checkbox (since you actually want to download the translations), verify the languages, and click “Run GP”.

The process will output a report; check that everything is OK (i.e. no error messages), and then go to the Upload File Manager (from the menu bar at the left, or directly from the link you will find at the end of the output):  
  
![Picture14](media_files/Picture14.png)

Select the checkboxes corresponding to the zip files you just imported (again, you can sort/filter by date) and click UNZIP!

You will get an output report again, and a click here link at the end. Click it to continue.

You will be taken to the Work with NLV files section of WebFM, and there you will see your freshly imported files (again, sort/filter by date if necessary). It is always good to check the last line, where it says the total number of files, and ensure that it matches the expected number (for example, 5 files x 9 languages = 45 files):  
  
![Picture15](media_files/Picture15.png)

[…]  
  
![Picture16](media_files/Picture16.png)

Select their checkboxes and click Run EzChecks. A pop-up window will show the results of CHKPII and other controls. If any errors appear, review them to see if they are actual errors or just false positives. If they are errors, fix them before continuing; if they are false positives, click the button Process Options, then in the first field (CHKPII settings) select Skip CHKPII, and click Save & Close:  
  
![Picture17](media_files/Picture17.png)

Then click Run EzChecks again, and the process should run without errors.

After that, click the green Check-in button, watch the process as it uploads the files to GitHub, and when it finishes you will receive one or more e-mails (depending on how the files are organized) in your IBM account. These e-mails contain the link to the Pull Request (PR) in IBM’s GitHub, so you will need to copy the links and send them to the lab via the corresponding Slack channel.

So, the last step is to notify the lab via Slack and send them the links, as mentioned above. After that, you are done!
