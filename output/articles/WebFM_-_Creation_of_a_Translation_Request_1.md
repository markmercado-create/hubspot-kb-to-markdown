---
title: "WebFM - Creation of a Translation Request"
knowledge_base: "Globalization Help Center"
category: "WebFM"
subcategory: "How to guide"
language: "en"
keywords: "webfm"
status: "PUBLISHED"
archived: "false"
last_modified: "1772244481067"
source_url: "https://help.straker.ai/en/g11n/webfm/creation-of-a-translation-request"
exported_at: "2026-03-17T11:35:24Z"
---

# WebFM - Creation of a Translation Request

Start session in WebFM and select the project; then go to Dispatcher and check which files have changed since the last run. To do this, you have two options:

1. Simply click the Submit button next to Hit this to get files newer than last run of each app.

1. Alternatively, if you have run this check before (for example, for testing purposes), you can enter the date of that last run (or a reasonably suitable one) in the Get files newer than field and hit the Submit button next to it.

Then go to the Dispatcher Packages section. You will see a list of packages, and the latest one(s) you just generated should be at the top of the list; check the date and time and select the corresponding checkbox(es). Then click the Unzip to English button at the top:   
  
![Picture1](media_files/Picture1_1.png)

After that, go to Work with English Files. Sort or filter by date (if they are not) and find the files you sent for translation. Select them (checkboxes) and click Run EzChecks:  
  
![Picture2](media_files/Picture2_1.png)

A pop-up window will show up so you can see the outcome of the preliminary checks. Should there be any errors, check them and take appropriate action. If you know what you’re doing, you can try disabling the preliminary checks by using the Process Options button.

After the EzChk Pass button appears next to the file(s), click the Run GP Import/Export button to send the files to the Globalization Pipeline. You will see this screen:  
  
![Picture3](media_files/Picture3_1.png)

Here you need to state whether you need to upload the sources or download the translations. In this case, what we need is to upload, so you will mark the first checkbox and unmark the second (Note: When delivering the completed translations, it will be the other way around).

Click the Run GP button and you will see the output of the process. Note that the message suggests you a console command. This can be useful if you need to process many files, but you would need to have Java installed in your computer and the environment properly set up, so let’s leave it alone for now and continue with the web interface.  
  
![Picture4](media_files/Picture4_1.png)

Next step is to go to the Globalization Pipeline and select the Translation Requests tab to create a new one (using the New request button) you will find in that page).  
  
![Picture5](media_files/Picture5_1.png)

You will see a list of the bundles (translation packages) for the product. Select the same ones you selected for the Run GP Import/Export step before, check the languages which should be translated (usually all of them except Russian, if present) and click Next:  
  
![Picture6](media_files/Picture6_1.png)

In the next step, you will see a status of the MT process for each language. It’s necessary to ensure that all the MTs have finished (i.e. the MT PENDING column shows “No”. If there is any “Yes”, then go back and wait for a while before trying again:  
  
![Picture7](media_files/Picture7_1.png)

When all the “MT Pending” are in “No” status, click Next. You will see the next step:  
  
![Picture8](media_files/Picture8_1.png)

Here you only need to change two things: add a name to the translation request (anything you want but that helps you to identify the TR in the future), and the profile ID, which should be “default” unless you know what you are doing. Then click Next once more.

Last step is a double-check of everything. Take a final look and, if everything is OK, click the Confirm and submit button:  
  
![Picture9](media_files/Picture9_1.png)

A pop-up will ask for confirmation; click OK, and the job is done! Don’t forget to tell the lab (via Slack) that their translation is underway.
