---
title: "Do spaces and/or tabs count as characters in the 1 million characters?"
knowledge_base: "Globalization Help Center"
category: "CAITS"
subcategory: "mt api"
language: "en"
status: "DRAFT"
archived: "false"
last_modified: "1742760081770"
source_url: "https://help.straker.ai/en/g11n/do-spaces-and/or-tabs-count-as-characters-in-the-1-million-characters"
exported_at: "2026-03-17T10:52:05Z"
---

# Do spaces and/or tabs count as characters in the 1 million characters?

Yes. 1 char = 1 unicode code point. So you send 50 white spaces, then it is counted as 50 characters. It also counts HTML tags - e.g. `<b>` is counted as 3 characters.
