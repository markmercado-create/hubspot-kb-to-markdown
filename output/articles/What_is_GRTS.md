---
title: "What is GRTS?"
knowledge_base: "Globalization Help Center"
category: "GRTS"
language: "en"
status: "PUBLISHED"
archived: "false"
last_modified: "1742760067841"
source_url: "https://help.straker.ai/en/g11n/what-is-grts"
exported_at: "2026-03-17T10:52:04Z"
---

# What is GRTS?

### GRTS Overview

GRTS is a cloud-based, elastic memory search service, which supports both term memory search as well as segment-level memory search (including fuzzy and exact memory match).

### GRTS Architecture

![](https://20462040.fs1.hubspotusercontent-na1.net/hubfs/20462040/image-png-2.png)

GRTS includes three components: Java SDK, Restful service and Dashboard.  
  
[Java SDK](https://github.ibm.com/1t1p/grts-java-sdk)  is used by:  
  
   - CAITS AT phase to search the memory result.  
  
   - CAITS MEM-REG phase to register updated memory records.   
  
   - Java agent to register the memory in batch.  
  
   - Java class to export memories by project/product ID and language.

Dashboard is deployed within rest service:  
  
   - Dashboard is a web UI. For example: https://grts.straker.global/grts/  
  
   - Dashboard is used by L1/L3 support team to search memory and investigate memory issues.  
  
  
Restful service:  
  
   - The storage layer is Elastic Search Cluster.  
  
   - The index name of ES is construct of source language, target language and domain.  
  
   - The shard number of each index is different depending on memory size in this index.

Restful API (Java):  
   - Admin APIs - manage accounts and permissions to access GRTS service.  
  
   - Auth APIs - OAuth 2.0 service side to authorize the request from clients.  
  
   - Memory APIs - memory search and registration.  
  
   - Term APIs - term search.
