---
title: "How does the GP work with the desktop-based product?"
knowledge_base: "Globalization Help Center"
category: "Globalization Pipeline"
subcategory: "translation"
language: "en"
status: "DRAFT"
archived: "false"
last_modified: "1749607064516"
source_url: "https://help.straker.ai/en/g11n/how-does-the-gpinstance-work-with-the-desktop-based-product"
exported_at: "2026-03-17T10:52:04Z"
---

# How does the GP work with the desktop-based product?

GP was designed for integrating translation process as a part of DevOps. When English UI string is updated in the source code repository, it may trigger a build process to upload the resource to GP, then fetch translation from GP. It does not matter if this is a desktop-based product or cloud service. Your product build system is suggested to integrate with GP tooling - a certain event triggers translatable resource files uploaded to GP. You don't really need to wait for translation is completed (MT for seconds / HT for a few days). As soon as GP receives the latest English version, you can export matching translated version immediately (at this point, new/modified string might not be translated yet - and use the English string value as fallback).
