---
title: "What's the difference between Code Pattern and DNT"
knowledge_base: "Globalization Help Center"
category: "Globalization Pipeline"
subcategory: "dnt"
language: "en"
status: "DRAFT"
archived: "false"
last_modified: "1742760073126"
source_url: "https://help.straker.ai/en/g11n/whats-the"
exported_at: "2026-03-17T10:52:04Z"
---

# What's the difference between Code Pattern and DNT

**Code Pattern** and **DNT** (*Do Not Translate*) are two mechanisms for protecting a fragment of text from translation.

### Code pattern

Code pattern makes matching text as external reference. The matching texts are excluded from translation and a translator cannot change it.

For example:

A date in a source segment can be protected by Code Pattern from translation. See how a date is excluded from an English source segment "*The file was created on %date%*" in XLIFF <source>:

```
<originalData><data id="d1">%date%</data></originalData>  
…  
<source>The file was created on <ph id="1" dataRef="d1"/></source>
```

### DNT

DNT mechanism still includes a matching text fragment in XLIFF <source>, and adds annotation to the matching text fragment. Thus, even some texts are detected as DNT, a translator can override it.

For example:  
Below shows how the terms "WebSphere Application Server" and "log4j" are annotated as DNT in XLIFF <source>:

```
<source><mrk id="1" type="caits:regex-no-translate" translate="no">WebSphere Application Server</mrk> supports <mrk id="2" type="caits:regex-no-translate" translate="no">log4j</mrk> logging interface.</source>
```
