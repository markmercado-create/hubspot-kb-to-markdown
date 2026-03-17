---
title: "Resource Filters"
knowledge_base: "Globalization Help Center"
category: "Globalization Pipeline"
subcategory: "gp doc"
language: "en"
status: "PUBLISHED"
archived: "false"
last_modified: "1749606923461"
source_url: "https://help.straker.ai/en/g11n/resource-filters"
exported_at: "2026-03-17T10:52:05Z"
---

# Resource Filters

Core Globalization Pipeline service does not recognize resource file formats. Resource format is handled by Globalization Pipeline tools, such as CLI, Jenkins plugin and maven plugin.

All of Globalization Pipeline tools share a common component gp-res-filter written in Java.  
The source code is available at: <https://github.ibm.com/1t1p/gpv2-java-tools/tree/master/resource-filter/gp-res-filter-impl/src/main/java/com/ibm/g11n/pipeline/resfilter/impl>.

This component supports SPI (service provider interface) to allow you to register new filter type. When behavior of the default filter does not support your requirement, or resource file format is not supported, you can develop your own filter and use it with Globalization Pipeline tools.   
Note: You need the [impl](https://github.ibm.com/1t1p/gpv2-java-tools/tree/master/resource-filter/gp-res-filter-impl/src/main/java/com/ibm/g11n/pipeline/resfilter/impl) if you need to use any of the default filter functionality but only the [api](https://github.ibm.com/1t1p/gpv2-java-tools/tree/master/resource-filter/gp-res-filter) when developing a custom filter.

To develop a new custom filter, please view the following video for details:

{% video\_player "embed\_player" overrideable=False, type='hsvideo2', hide\_playlist=True, viral\_sharing=False, embed\_button=False, autoplay=False, hidden\_controls=False, loop=False, muted=False, full\_width=False, width='688', height='387', player\_id='173071302787', style='' %}

Also refer to a sample csv-res-filter: <https://github.ibm.com/1t1p/gpv2-java-tools/tree/master/resource-filter/csv-res-filter>.

There are some custom filters  created for IBM teams: <https://github.ibm.com/1t1p/gp-ibmer-examples/blob/master/README.md#filters>. If you have implemented any additional filters or custom scripts, then please add your contribution to the repository. Please fork this repository and file a [pull request](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).
