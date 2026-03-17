---
title: "Edit Translation"
knowledge_base: "Globalization Help Center"
category: "Globalization Pipeline"
subcategory: "gp doc"
language: "en"
status: "PUBLISHED"
archived: "false"
last_modified: "1762998382352"
source_url: "https://help.straker.ai/en/g11n/edit-translation"
exported_at: "2026-03-17T11:35:52Z"
---

# Edit Translation

The **Edit Translation** feature allows users to modify translations directly from Globalization Pipeline.

### Steps to Edit a Translation

1. Login Globalization Pipeline
2. Navigate to **Bundles** tab
3. Select the bundle you want to modify.
4. Open the target language.
5. Search for the specific **resource key** you wish to edit.
6. On the right side of the entry, click the overfly menu(**⋯ )** and choose Edit translation.  
     
   ![1](media_files/1_1.png)
7. In the **New Translation** text box, enter your desired translation.

![2](media_files/2_1.png)

### Important Notes

- The modified translation will **not** be saved to the **Translation Memory (TM)**.
- Only translations returned from **Human Translation** are automatically registered in TM**.**
- Therefore, if the same source string appears in a new bundle, your manual edits will **not** be automatically applied.
- However, you can use the **copy-bundle** command of GP CLI to copy your edited translations to a new bundle when needed.
- The edited resource strings with **Unreviewed** status will be included in the new TR.
- The edited resource strings with **Reviewed** or **Verified** status will **not** be included in the TR.
