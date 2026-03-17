---
title: "Integrating GP into DevOps"
knowledge_base: "Globalization Help Center"
category: "Globalization Pipeline"
subcategory: "gp doc"
language: "en"
status: "PUBLISHED"
archived: "false"
last_modified: "1749606922752"
source_url: "https://help.straker.ai/en/g11n/integrating-gp-into-devops"
exported_at: "2026-03-17T11:27:52Z"
---

# Integrating GP into DevOps

While you can use Globalization Pipeline through its service dashboard, we recommend integrating Globalization Pipeline into your DevOps environment to automate Globalization Pipeline operations and make translation part of your continuous delivery infrastructure. Based on your preference, there are three scenarios for integrating Globalization Pipeline into DevOps.

### Static build time integration

Globalization Pipeline provides tools that can help you perform Globalization Pipeline operations during the build phase of your app. Please explore our build tools in these topics - Maven plugin, IBM UrbanCodeDeploy plugin, Jenkins plugin, Command-line and Ant tool.

![](media_files/undefined-Jul-15-2024-06-34-45-3184-AM.png)Note: These tools provide you more flexibility in terms of supported file formats and controls than the Stand-alone use of Globalization Pipeline.

### Dynamic run time integration

Globalization Pipeline provides SDKs and clients that you can use to perform Globalization Pipeline operations at application runtime. Please explore our SDKs/clients in [SDKs and Tools](https://kb.strakertranslations.com/en/knowledge/sdks-and-tools) . You can also perform Globalization Pipeline operations using our [swagger UI](https://g11n-pipeline-api.straker.global/translate/swagger/). You can perform REST calls to this swagger's endpoints from your app as an alternative to taking a  SDK/client approach.

![](media_files/undefined-Jul-15-2024-06-34-45-6284-AM.png)

![](media_files/undefined-Jul-15-2024-06-34-45-8122-AM.png)

Note that your swagger doc instances will be different based on our configuration of Globalization Pipeline for your team. Please contact us for swagger doc access upon onboarding.

### Hybrid integration

Your team can also choose a hybrid approach to DevOps integration where you opt for Static Build Time integration for your production app instance and Dynamic Run Time integration for your test/development environment, or in any other configuration you wish.
