---
title: "How the delta is calculated for bundles?"
knowledge_base: "Globalization Help Center"
category: "Globalization Pipeline"
subcategory: "bundle"
language: "en"
status: "DRAFT"
archived: "false"
last_modified: "1742760078296"
source_url: "https://help.straker.ai/en/g11n/how-the-delta-is-calculated-for-bundles"
exported_at: "2026-03-17T10:52:04Z"
---

# How the delta is calculated for bundles?

Let's suppose this use case: *An existing bundle in GP is deleted, and then it is uploaded into GP freshly. Does GP consider the whole bundle as delta?*

It will search memory when uploading bundle to GP. The entry will be marked as **reviewed** if memory match. Please note: if memory match is a short phrase (less than 5 words in source), entry will not be marked as **reviewed**. The **unreviewed** entires will be taken as delta.  
So deleting existing bundle and re-uploading, most of entries will be marked as **reviewed** if source string is equal or greater than 5 words.
