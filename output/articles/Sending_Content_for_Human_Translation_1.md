---
title: "Sending Content for Human Translation"
knowledge_base: "Globalization Help Center"
category: "Globalization Pipeline"
subcategory: "gp doc"
language: "en"
status: "PUBLISHED"
archived: "false"
last_modified: "1749607123277"
source_url: "https://help.straker.ai/en/g11n/sending-content-for-human-translation"
exported_at: "2026-03-17T11:28:09Z"
---

# Sending Content for Human Translation

In addition to providing near real-time machine translation, IBM Globalization Pipeline enables you to submit your application content for human translation through either the dashboard or using our DevOps tools. See [Machine Translation and Human Translation](https://kb.strakertranslations.com/en/knowledge/mt-and-human-translation) for information that you should consider regarding when and how to best to use machine translation and request human translation.

### Create Human Translation Request on Dashboard

![](media_files/image-png-Jul-16-2024-03-11-23-6611-AM.png)You can create a **New Request** from **Translation Requests** tab in your instance of Globalization Pipeline.

![](media_files/image-png-Jul-16-2024-03-11-49-3541-AM.png)Step 1 - Choose bundle(s) you want to send for human translation and the target language(s). Note that you can also choose file(s) to send for human translation.

![](media_files/image-png-Jul-16-2024-03-19-15-4190-AM.png)Step 2 - Confirm the word count ( of unreviewed**(U)** strings  ) for your translation.

![](media_files/image-png-Jul-16-2024-03-19-44-2797-AM.png)Step 3 - Fill in translation request information.



![](media_files/image-png-Jul-16-2024-03-52-50-0718-AM.png)Final step 4 - Confirm your request and submit it.

![](media_files/image-png-Jul-16-2024-05-06-12-9405-AM.png)

You can view information about your human translation requests on **Translation Requests** tab. In this tab, you can view the status of your human translation request in flow as:

- **Draft** - until you submit a human translation request, it stays in Draft state. You can only cancel a translation request at this stage.
- **Pending** - if there is bundle/file in the request still under automatic translation phase, the request is changed to pending, and it would be sent out once automatic translation is completed.
- **Submitted**- once you submit the human translation request and the request is waiting to be picked up for translation.
- **Editing** **started** - once translators start working on your request.
- **Partially Merged** - one or more human translators have submitted your request back to Globalization Pipeline and those changes have been merged back to your bundles. (turning translations to reviewed**(R)**). However, there are some languages in the translation request which have not yet been received from the translators.
- **Merged** - once all translators submit your request back to Globalization Pipeline and it merges translation back to your bundles. (turning translations to reviewed**(R)**).

Your translation request might show a state **Cancelled** automatically if the parameters are wrong. Note: You can only cancel a translation request personally in **Draft** state.
