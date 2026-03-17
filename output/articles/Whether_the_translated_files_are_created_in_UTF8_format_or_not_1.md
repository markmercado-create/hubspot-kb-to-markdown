---
title: "Whether the translated files are created in UTF8 format or not?"
knowledge_base: "Globalization Help Center"
category: "Globalization Pipeline"
subcategory: "resource filter"
language: "en"
status: "DRAFT"
archived: "false"
last_modified: "1742760080048"
source_url: "https://help.straker.ai/en/g11n/whether-the-translated-files-are-created-in-utf8-format-or-not"
exported_at: "2026-03-17T11:27:52Z"
---

# Whether the translated files are created in UTF8 format or not?

It really depends on the behavior of resource filter. Some resource file formats defines charset encoding to be used - for example, JSON must be encoded by UTF-8, Java properties is encoded by ISO-8859-1 by default. Charset encoding conversion should be done by resource filter, which should be under your management.
