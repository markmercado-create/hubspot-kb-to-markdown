---
title: "Why translations got `!!PE` character appended?"
knowledge_base: "Globalization Help Center"
category: "Globalization Pipeline"
subcategory: "translation"
language: "en"
status: "DRAFT"
archived: "false"
last_modified: "1742760082324"
source_url: "https://help.straker.ai/en/g11n/why-translations-got-pe-character-appended"
exported_at: "2026-03-17T11:33:30Z"
---

# Why translations got `!!PE` character appended?

The `!!PE` gets added when you submit a TR where the `Human translation provider` specified in your GP ‘default’ profile is the dummy `TEST` provider which does not send the translation to Straker for review and so it does not incur any cost; however, it doesn’t provide any REAL review of the Machine Translated string.  The Test provider is just for use when setting up your processes or testing out the features of GP where you want to try something out.

If you are needing to send the translation off for actual review by the Straker team and incur the associated cost of translation review, then you will need to change the Human translation provider value to `Straker` by going to the “Profiles” tab in the GP dashboard, click the “3 dot” Action button for the `default` profile and updating the value for Human translation provider.
