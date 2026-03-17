---
title: "How to onboard to Globalization Pipeline"
knowledge_base: "Globalization Help Center"
category: "Globalization Pipeline"
subcategory: "gp doc"
language: "en"
status: "PUBLISHED"
archived: "false"
last_modified: "1749606949229"
source_url: "https://help.straker.ai/en/g11n/onboarding"
exported_at: "2026-03-17T10:52:04Z"
---

# How to onboard to Globalization Pipeline

IBM Globalization Pipeline provides IBM development teams with the ability to integrate application translation (machine and human) into their DevOps infrastructure and their continuous delivery schedules.

When you are ready to onboard to Globalization Pipeline, here are the getting started steps.

#### Step 1: Understand Translation Process with Globalization Pipeline

- Check [Process](https://kb.strakertranslations.com/en/knowledge/process-overview) page
- Create plan for build integration - see [SDKs and Tools](https://kb.strakertranslations.com/en/knowledge/sdks-and-tools) page

#### Step 2: Request New Globalization Pipeline Accounts

To request new Globalization Pipeline accounts, download **[GP instance creation - template.xlsx](https://kb.strakertranslations.com/hubfs/knowledge-base-files/GP%20instance%20creation.xlsx)** and fill in this file with the information needed to create new GP instances. Then, write a post to **[Jordi Serratosa](mailto:jordi.serratosa@partner.ibm.com)** (from Globalization onboarding team) in Slack channel [**#g11n-pipeline**](https://ibm.enterprise.slack.com/archives/C0EP2MFR7) and provide the filled file, so that Globalization onboarding team will create two Globalization Pipeline services accounts for your team - one for test integration and another for production. These accounts are designed for IBM internal use and separately maintained from the Globalization Pipeline service on the public IBM Cloud.

#### Step 3: Test Integration

At this point, you can start test integration with Globalization Pipeline. The test integration should evaluate:

- All resource files are imported correctly to Globalization Pipeline *bundles*.
- Translated Globalization Pipeline *bundles* are exported to desired file paths.
- Exported translation contents are not corrupted.

#### Step 4: Production Integration

After checking everything working well on test environment, switch to production instance of Globalization Pipeline.

If your team has previously translated contents, please follow the instruction explained below.

1. Collect English resource files used for the latest translation.
2. Import all of these English resource files into GP.
3. Import the latest translated resource files into GP. In this case, set these translations as "reviewed"
4. Update English bundle with the latest version.

You can use GP Java CLI for importing English and existing translations as described [here](https://github.ibm.com/1t1p/gpv2-java-tools/tree/master/gp-java-tools/gp-cli).

#### Step 5: Submit A New Translation Request

You can use Globalization Pipeline dashboard to submit a new human translation request at this point. Please check a page [Sending Content for Human Translation](https://kb.strakertranslations.com/en/knowledge/sending-content-for-human-translation) for more details.

**NOTE:** [Globalization Pipeline Tutorial](https://kb.strakertranslations.com/en/knowledge/gp-tutorial) is published to help you onboard and setup your DevOps integration with Globalization Pipeline step by step. It is highly recommended to have a DevOps Engineer from your product team practice on the published tutorial to ease the integration process.
