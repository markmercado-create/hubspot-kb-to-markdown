---
title: "Code Pattern"
knowledge_base: "Globalization Help Center"
category: "Globalization Pipeline"
subcategory: "GP Functionality 0verview"
language: "en"
status: "PUBLISHED"
archived: "false"
last_modified: "1770972696850"
source_url: "https://help.straker.ai/en/g11n/code-pattern"
exported_at: "2026-03-17T10:52:05Z"
---

# Code Pattern

**Introduction:**

GP supports a feature called “Code Pattern”. One code pattern is actually a (java) regular expression. For example, a regular expression that matches any numeral is `[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?`. GP allows users to configure one or more code patterns at *bundle* or *profile* level for a GP instance. Multiple code patterns are separated by the OR operator (i.e. “**|**”).

For an example resource string `User "{name}" was added.` , GP users can configure a code pattern ( `\{[A-Za-z0-9]+\}`) at bundle level. Then, the sub-string “*{name}*” in the resource string will not be included in a translatable segment, so “*{name}*” will never be translated by machine translation engines or human translators.   
  
From the perspective of the parsed XLIFF, the corresponding segment for this resource string is shown below, wherein "*{name}*" is not included in the sentence segment (i.e. `<source>…</source>`).

```
<unit id="1">  
<originalData>  
<data id="d1">{name}</data>  
</originalData>  
<segment id="s1">  
<source xml:space="preserve">User "<ph id="1" canCopy="no" canDelete="no" disp="{name}" dataRef="d1"/>" was added.</source>  
</segment>  
</unit>
```

When a code (e.g. “*{name}*”) is embedded with in a sentence segment, the code is replaced with a place holder tag (XLIFF <ph/>), e.g. “<ph id="1" canCopy="no" canDelete="no" disp="{name}" dataRef=“d1”/>” in the example above, this may lead to the following effects:

- Low quality translation with machine translation
- Straker Workbench (used by Straker human translators) handles all inline tags in a same way and does not provide information about what code is replaced with the place holder tag, therefore human translation result might be still low quality.

---

**Configure code patterns at bundle level in GP dashboard:**  
![](https://20462040.fs1.hubspotusercontent-na1.net/hubfs/20462040/image-png-Feb-13-2026-06-39-47-1621-AM.png)

![](https://20462040.fs1.hubspotusercontent-na1.net/hubfs/20462040/image-png-Feb-13-2026-06-40-09-0221-AM.png)

---

**Configure code patterns at profile level in GP dashboard:**

![](https://20462040.fs1.hubspotusercontent-na1.net/hubfs/20462040/image-png-Feb-13-2026-06-40-25-2541-AM.png)

![](https://20462040.fs1.hubspotusercontent-na1.net/hubfs/20462040/image-png-Feb-13-2026-06-41-48-1905-AM.png)

![](https://20462040.fs1.hubspotusercontent-na1.net/hubfs/20462040/image-png-Feb-13-2026-06-41-55-0700-AM.png)
