---
title: "What is \"en-XA\" or \"en-XP\" for?"
knowledge_base: "Globalization Help Center"
category: "Globalization Pipeline"
subcategory: "translation"
language: "en"
status: "DRAFT"
archived: "false"
last_modified: "1749606937549"
source_url: "https://help.straker.ai/en/g11n/what-is-1"
exported_at: "2026-03-17T10:52:04Z"
---

# What is "en-XA" or "en-XP" for?

**en-XA** is for GVT. A pseudo translation (e.g., a pseudo translated string below) is designed for Globalization Verification Test (GVT). With this, you can check if UI strings are externalized, no Moji-bake on UI, no unexpected string concatenation and other basic testing check points - which can be verified by English native speakers.

```
[('ฏูİı｜)Ｄｕｐｌｉｃａｔe(s): ${duplicateList}]
```

**en-XP** is for automatic string association. It assigns unique string number for each string, e.g., an en-XP string below. When you take screenshots for ICT with `en-XP` pseudo translation, OCR can scan these string numbers and automatically associate screenshot image with strings.

```
$ad34b2ee#{[Duplicate(s): ${duplicateList}]}
```
