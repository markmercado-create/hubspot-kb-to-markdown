---
title: "How to update bundles in some languages that were reverted back to English?"
knowledge_base: "Globalization Help Center"
category: "Globalization Pipeline"
subcategory: "bundle"
language: "en"
status: "DRAFT"
archived: "false"
last_modified: "1742760069527"
source_url: "https://help.straker.ai/en/g11n/how-to-update-bundles-in-some-languages-that-were-reverted-back-to-english"
exported_at: "2026-03-17T11:33:30Z"
---

# How to update bundles in some languages that were reverted back to English?

Sometimes there are many translated terms in your bundles that are processed by translation requests (TR) are still English, which might be caused by unexpected translation memory match. Please try the following process for fixing those terms:

1. For the safety purpose, it's better to import "good" revision including translation to a separate GP instance. You can ask the support team (e.g., [yoshito\_umaoka@us.ibm.com](mailto:yoshito_umaoka@us.ibm.com))  
   to create a **temporary** GP instance for you. Then, you can import the previous translated files at the previous revision (from your source repository). Refer to [Import existing bundle translations](https://github.ibm.com/1t1p/gpv2-java-tools/tree/master/gp-java-tools/gp-cli#import-existing-bundle-translations).
2. When the new instance is ready, you can take the previous changes.
3. Finally, the support team can programmatically merge the lost translation back to production instance.
