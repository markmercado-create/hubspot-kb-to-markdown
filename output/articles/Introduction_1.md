---
title: "Introduction"
knowledge_base: "Globalization Help Center"
category: "Globalization Pipeline"
subcategory: "tutorial"
language: "en"
status: "PUBLISHED"
archived: "false"
last_modified: "1749607131959"
source_url: "https://help.straker.ai/en/g11n/introduction"
exported_at: "2026-03-17T10:52:05Z"
---

# Introduction

The Globalization Pipeline tutorial is designed to cover all the major steps and flow of DevOps process integration for IBM Globalization pipeline service.

There are few basic components that go hand in hand with all the operations performed in IBM Globalization Pipeline (abbreviated as **GP**):

1. [**REST server**](https://g11n-pipeline-api.straker.global/translate/): This is the core component that handles all the GP requests.
2. **[GP Dashboard](https://g11n-pipeline-console.straker.global/login.wss)**: This is the UI component that communicates with REST server.
3. **Tools**/**Plugins**: These are the DevOps or supplementary tools that handle the requests/response with REST server. These are made specifically to fit in your DevOps CI/CD builds.

**NOTE**: Please assign a DevOps engineer to follow through this tutorial. This tutorial provides overall end-to-end understanding of GP integration. It is highly recommended to go through this once and apply the similar changes to your product.
