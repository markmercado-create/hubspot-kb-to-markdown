---
title: "What is CAITS?"
knowledge_base: "Globalization Help Center"
category: "CAITS"
language: "en"
status: "PUBLISHED"
archived: "false"
last_modified: "1742760067093"
source_url: "https://help.straker.ai/en/g11n/what-is-caits"
exported_at: "2026-03-17T11:33:30Z"
---

# What is CAITS?

### CAITS overview

CAITS is an IBM Cloud service that provides underlying machine translation and human translation supports for Globalization Pipeline, IDHub orchestration and other CAITS applications.

### CAITS Job and Task

In CAITS, a job is a unit of translation request. A job typically has a single input object in a single language (e.g., source language is English), and may have multiple target languages (e.g., target languages are French, German, and Japanese). CAITS creates one or more tasks for executing translation operations and each task may produce one or more output objects in a single target language.

  

For example, when a CAITS application wants to translate a document in English to French and German, the application creates a job. CAITS job controller creates two tasks, one for German translation and another for French. Each task has its own lifecycle and a CAITS application can get translation result for German independently from CAITS. The job has collective status of tasks and will be completed when all tasks are completed.

### CAITS Workflow Type

A workflow type defines a series of translation operations to be done in a single job. CAITS supports multiple translation workflow types.

Following two workflow types are commonly used.

- **AUTO\_TRANSLATION**: Automated translation workflow. This workflow is designed for fast turnaround (in a few seconds), with source text analysis, translation memory lookup and machine translation.
- **FLUENT\_TRANSLATION**: Fluent translation workflow. This workflow is designed for high quality translation, but slower turnaround. This workflow usually goes through translation post-editing by professional translator (from *Straker Translations*) after automated translation.

### Phase and Operation in CAITS

CAITS consists from multiple microservices, and each microservice implements one or more granular translation operations, such as XLIFF transformation, term analysis, machine translation, and so on. A translation phase is a stage in a workflow which has well defined input objects and output objects and consists from one or more operations.

Below is the list of translation phase and semantics in CAITS.

- **INITIAL**: Special phase indicating a translation task is not yet started.
- **PREP**: Preparation phase. In this phase, translation input object will be parsed and transformed or normalized into format for consumption in later phase. For example, input HTML file for translation is segmented and transformed into XLIFF in this phase.
- **AT**: Automated translation phase. In this phase, a translation of each input segment is supplied by translation memory or machine translation engine.
- **PE**: Post-editing phase, i.e., human translation. CAITS notifies arrival of new translation task assigned to IBM translation service provider (i.e., *Straker*), and waits for completion of post-editing task.
- **MERGE**: Merge phase. In this phase, final translation output will be produced from the original input object and translation result object. At the end of this phase, the translation output object is readily available for CAITS consumer.
- **FINAL**: Special phase indicating a translation task completion.

### **Job Status and Task Status in CAITS**

A status indicates current state of each translation task, independent from phase. For now, following status keywords are available.

- **NOT\_STARTED**: Not started yet. It might require someone to trigger the process.
- **IN\_PROGRESS**: Being processed.
- **COMPLETED**: Successfully completed.
- **CANCELLED**: Cancelled.
- **FAILED**: Failed. It might require someone to fix the issue, or creates a brand new job.

A Job has collective statues of tasks which belong to the job, with precedence below.

- One of tasks turns to `FAILED`, then the job status becomes `FAILED`.  
- All of tasks turn to `COMPLETED`, then the job status becomes `COMPLETED`.  
- One of tasks turns to `IN\_PROGRESS`, then the job status becomes `IN\_PROGRESS`.
