---
title: "Why source English source having can not be translated by MT?"
knowledge_base: "Globalization Help Center"
category: "Globalization Pipeline"
subcategory: "translation"
language: "en"
status: "DRAFT"
archived: "false"
last_modified: "1749607049987"
source_url: "https://help.straker.ai/en/g11n/why-source-english-source-having-br-can-not-be-translated-by-mt"
exported_at: "2026-03-17T10:52:04Z"
---

# Why source English source having can not be translated by MT?

For example -

```
Click OK after you<br>have verified the settings, or click Cancel to go back and change the settings.
```

This is one English sentence segment to be translated by MT. You placed `<br>` between `you` and `have`. It is not possible to translate this in other languages by MT as you want.

Of course, MT can handle input segment

```
Click OK after you have verified the settings, or click Cancel to go back and change the settings.
```

But, you don't knows where `<br>` is inserted.

What you need is to avoid such "preformatted" text input for translation process. Translation process is not able to place appropriate number of new lines at expected position. If translated sentence is very short, number of desired `<br>` s might be decreased,

The best practice for translation is not to include such controls for visual formatting.
