---
title: "Platform Glossary"
knowledge_base: "Globalization Help Center"
category: "GTech Platform"
language: "en"
status: "DRAFT"
archived: "false"
last_modified: "1762831436947"
source_url: "https://help.straker.ai/en/g11n/platform-glossary"
exported_at: "2026-03-17T11:35:47Z"
---

# Platform Glossary

This Platform glosary will detail the Core Modules (Platform Glossary), illustrate the System Workflow and Inter-Module Integration model, specify the Supported Processing Languages for each component, list the acceptable Data File Formats, enumerate the Key API Endpoints, and identify the designated Supported User Personas (Lab Users).

|  |  |
| --- | --- |
| MODULES | DESCRIPTIONS |
| CAITS | **Brief Overview:**  CAITS (Cloud-based AI Translation Service) is an IBM Cloud offering that provides both machine and human translation services. It supports IBM's Globalization Pipeline, IDHub orchestration, and other translation-driven applications. CAITS streamlines multilingual content delivery by automating translation tasks and integrating human post-editing for enhanced accuracy and naturalness.  **Key Features:**   - Scalable, cloud-native translation service. - Supports both automated and human-assisted translation. - Seamless integration with IBM's globalization tools.   **How It Works:**  CAITS operates through jobs and tasks, leveraging various microservices to manage and execute translation requests.  **Job & Task Structure**   - *Job*: A single translation request with one source language and potentially multiple target languages. - *Task*: A unit of work within a job, responsible for translating into one target language.   **Translation Workflow**  1. *Job Creation*: A translation job is initiated with a source file and selected target languages.  2. *Task Execution*: Tasks are created for each target language, progressing through predefined phases.  3. *Phase Progression*: Each task follows a workflow with multiple phases:   - INITIAL: Task created but not started. - PREP: Input files parsed, segmented, and transformed into translatable formats (e.g., XLIFF). - AT (Auto-Translation): Automated translation using translation memory or machine learning models. - PE (Post-Editing): Human translators review and refine the automated output for quality. - MERGE: Final output is compiled into the original format. - FINAL: Task completion status is recorded.   Status Tracking  - NOT\_STARTED: Awaiting initiation.  - IN\_PROGRESS: Translation tasks are actively being processed.  - COMPLETED: All tasks successfully finished.  - FAILED: Errors occurred requiring intervention.  - CANCELLED: Job manually terminated.    **Language Supported:**  CAITS supports a broad range of languages, including regional variants, to cater to diverse global audiences. Below are some of the supported languages:   - European: German, French, Spanish (including Latin American variants), Italian, Dutch, Swedish, Greek, etc. - Asian: Simplified/Traditional Chinese, Japanese, Korean, Vietnamese, Thai, etc. - Middle Eastern & African: Arabic, Hebrew, Persian, Swahili, Amharic, etc. - American: English (US, UK, CA), Spanish (Mexico, Colombia, LATAM), Haitian Creole, etc.   This comprehensive language support ensures efficient communication across global markets.    **File Formats Supported:**  CAITS supports a variety of file types across documents, web content, and media formats:   - Documents: DOC, DOCX, ODT, PPT, PPTX, ODP, XLS, XLSX, ODS, RTF, TXT, Markdown. - Web & Markup: HTML, XML, XLIFF, DITA, JSON, YAML. - PDF: Portable Document Format. - Images: PSD, GIF, JPG, JPEG, PNG, SVG. - Specialized: OTM\_ZIP, LNK (CAITS External Reference).   With its robust file type compatibility, CAITS simplifies multilingual content delivery across diverse content formats.    **List of endpoints:**  Refer to CAITS Swagger UI (<https://caits.straker.global/combined/>)    **Supported Lab Users:**  IBM CloudDocs Team |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
