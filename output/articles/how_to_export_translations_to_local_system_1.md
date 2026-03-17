---
title: "how to export translations to local system?"
knowledge_base: "Globalization Help Center"
category: "Globalization Pipeline"
subcategory: "java sdk"
language: "en"
status: "DRAFT"
archived: "false"
last_modified: "1742760086581"
source_url: "https://help.straker.ai/en/g11n/how-we-can-export-all-the-bundles-to-local-system-how-to-export-whole-tr-to-local-system-with-all-the-format-cover-and-with-all-the-comments-availab-1718087310960"
exported_at: "2026-03-17T11:32:10Z"
---

# how to export translations to local system?

There are two paths: self-serve (free) or having our translation partner, Straker, manage the process for you (paid).

To pursue the `Straker option`. Contact [@Anna Mondragon](https://ibm-cloudplatform.slack.com/team/U0607NR68P5) for details. The place to start your `self-serve` journey is [Globalization Central](https://w3.ibm.com/globalization/).  In this site you will find an overview of the entire globalization/translation process and specific docs on [Globalization Pipeline](https://w3.ibm.com/globalization/develop/globalizationpipeline) under the Develop topic.

As an outline of the process, Dev Teams generally follow:

1. Use CLI to import strings into GP.
2. Use GP Console (or CLI) to send your strings to the translators.
3. When translations come back, use CLI to export the strings and place them back in your code repository.

Helpful topics in Globalization Central:

- [GP Topic](https://w3.ibm.com/globalization/develop/globalizationpipeline)
- [GP Tutorial](https://pages.github.ibm.com/1t1p/gp-tutorial/)
- [GP CLI docs](https://github.ibm.com/1t1p/gpv2-java-tools/tree/master/gp-java-tools/gp-cli)
