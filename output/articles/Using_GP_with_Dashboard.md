---
title: "Using GP with Dashboard"
knowledge_base: "Globalization Help Center"
category: "Globalization Pipeline"
subcategory: "gp doc"
language: "en"
status: "PUBLISHED"
archived: "false"
last_modified: "1749606922595"
source_url: "https://help.straker.ai/en/g11n/using-gp-with-dashboard"
exported_at: "2026-03-17T10:52:05Z"
---

# Using GP with Dashboard

If you choose to use Globalization Pipeline as a stand-alone service, you will perform all Globalization Pipeline tasks using the service's dashboard. Once you have a service instance of **Globalization Pipeline**, you use the service dashboard to create Globalization Pipeline bundles. A bundle is a container for a group of application strings. A Globalization Pipeline bundle consists of key-value pairs in the source language of your strings, and one or more sets of key-value pairs in your translation target languages. Working in a particular bundle, you can upload resource files containing your application content, select languages for machine translation, make minor edits to individual translated key values, download translations, and submit human translation requests - See [Sending Content for Human Translation](https://kb.strakertranslations.com/en/knowledge/sending-content-for-human-translation) for the details. Note that there are many additional features available through our DevOps tools that are not exposed in the UI dashboard.

![](https://20462040.fs1.hubspotusercontent-na1.net/hubfs/20462040/image-png-Jul-16-2024-02-17-07-2401-AM.png)

Create Bundle: you can upload your resource file in three file formats in UI - Java properties, AMD I18N, JSON. Note: we provide support for additional formats if you upload your files using our DevOps tools  (See DevOps Integration below).

![](https://20462040.fs1.hubspotusercontent-na1.net/hubfs/20462040/image-png-Jul-16-2024-02-25-22-8659-AM.png)You can view/edit/delete bundles once created.

![](https://20462040.fs1.hubspotusercontent-na1.net/hubfs/20462040/image-png-Jul-16-2024-02-27-34-5240-AM.png)You can view all the translated target resources, add/remove languages, upload source files again using the Bundles tab.

![](https://20462040.fs1.hubspotusercontent-na1.net/hubfs/20462040/undefined-4.png)

![](https://20462040.fs1.hubspotusercontent-na1.net/hubfs/20462040/image-png-Jul-16-2024-02-30-59-6877-AM.png)

Each target resource file can be viewed/edited. You can modify the translation of individual source key values, set its state to reviewed **(R)** or unreviewed **(U)** and download the target resource file. If you choose to request human translation (See Human Translation), then each time a human translation request is completed, the strings reviewed by translators will be merged and the state will be changed to reviewed**(R)**.

**Note**:In addition to Bundles, you can also upload files supported by GP via the **Files** tab for whole file translation.
