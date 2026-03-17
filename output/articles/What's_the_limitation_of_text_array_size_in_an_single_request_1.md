---
title: "What's the limitation of text array size in an single request?"
knowledge_base: "Globalization Help Center"
category: "CAITS"
subcategory: "mt api"
language: "en"
status: "DRAFT"
archived: "false"
last_modified: "1742760079655"
source_url: "https://help.straker.ai/en/g11n/whats-the-limitation-of-text-array-size-in-an-single-request"
exported_at: "2026-03-17T11:31:43Z"
---

# What's the limitation of text array size in an single request?

WLT does not have any limitation of text array size in an single request (but max 5kb payload restriction). With Google cloud translation engine, number of text array entries is restricted up to 128. So if a single API call contains String array with more than 128 elements, the API call will be failed.
