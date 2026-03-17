---
title: "What file types of attachments are supported by GP ICT?"
knowledge_base: "Globalization Help Center"
category: "Globalization Pipeline"
subcategory: "ict"
language: "en"
status: "DRAFT"
archived: "false"
last_modified: "1749606950144"
source_url: "https://help.straker.ai/en/g11n/what-file-types-of-attachments-are-supported-by-gp-ict"
exported_at: "2026-03-17T11:28:22Z"
---

# What file types of attachments are supported by GP ICT?

1. The types of attachments allowed by GP are:  
                  image/gif (.gif)  
                  image/jpeg (.jpg)  
                  image/png (.png)  
                  image/svg+xml (.svg)  
                  text/html (.txt, .html)  
                  application/pdf (.pdf)

2. The GSSC script `ict.py` (used to semi-automate some steps in ICT preparation) **does not support**uploading with some formats (e.g., `text/html`, `application/pdf`). Workaround: the attachments were uploaded via the GP dashboard.

3. Straker Workbench **supports all attachment types**. Some formats do not show a preview (such as txt, html, pdf), but this is expected. It is recommended to download the attachment or open it in a new browser window.

4. **ONLY FOR .TXT:** The  `text/html` type treats txt files and html files all the same. Straker Workbench previews (and opens) the .txt file via the browser. That causes the loss of line breaks, since the browser renders the file as html. **To view the original .txt file, the tester must right-click "Save link contents as..." and save the file with a .txt extension.**

As a reference, find attached the .xliff that was generated for the ICT test.
