---
title: "Is there a way for GP to provide plugins that allow translation at runtime?"
knowledge_base: "Globalization Help Center"
category: "Globalization Pipeline"
language: "en"
status: "DRAFT"
archived: "false"
last_modified: "1742760079483"
source_url: "https://help.straker.ai/en/g11n/is-there-a-way-for-gp-instance-to-provide-plugins-that-allow-translation-at-runtime"
exported_at: "2026-03-17T11:27:52Z"
---

# Is there a way for GP to provide plugins that allow translation at runtime?

Actually, this was the original scope - providing translation on cloud and download it at application runtime. Technically, it should still work, but no one takes this approach. For example, GP Java client SDK provides integration with java ResourceBundle class. With this implementation, even you don't have .properties/ListResourceBundle .class file locally, it can fetch translation through GP instance on cloud (with code changes).
