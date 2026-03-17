---
title: "Initial Setup"
knowledge_base: "Globalization Help Center"
category: "Globalization Pipeline"
subcategory: "tutorial"
language: "en"
status: "PUBLISHED"
archived: "false"
last_modified: "1749606167249"
source_url: "https://help.straker.ai/en/g11n/initial-setup"
exported_at: "2026-03-17T11:32:12Z"
---

# Initial Setup

Let's start by initiating our GP instance and preparing it to fit into our build automation.

### GP Instance

Usually you need to create two GP instances, and the main difference between these two GP instances is the use of different human translation providers (i.e., **Test** or **Straker** provider).

- **Test instance**: One for testing/playground purpose.
- **Production instance**: One for your actual production.

When practicing this tutorial, you need to create a *test instance* first. Please download **[GP instance creation - template.xlsx](media_files/GP_20instance_20creation_2.xlsx)** and fill in this file with the information needed to create a new GP instance. Then, file a support ticket in [Straker HubSpot ticketing tool](http://support.strakertranslations.com) and upload the file as attachment, so that Straker GTech support team can help you create a test or product instance. After the GP instance is created for you, instance credentials will be sent to you via email. With the instance credentials, you can log into GP dashboard.

GP credentials should look something like:

```
{  
    "url" : "https://g11n-pipeline-api.straker.global/translate/rest",  
    "instanceId": "gp-demo-test",  
    "userId": "****",  
    "password": "****"  
}
```

**NOTE**:  `"https://g11n-pipeline-api.straker.global/translate/rest"` is a REST endpoint. To access the server, please browse with `https://g11n-pipeline-api.straker.global` (removing `/translate/rest`) at which users can access and process requests in [swagger UI](https://g11n-pipeline-api.straker.global/translate/swagger/)

While filling the file *GP instance creation - template.xlsx*, please consider:

- Keep unique name for **Instance ID** for your product, e.g. *cloud-gtech-test* and *cloud-gtech*.
- If you are not sure about the **searchDomainCodes** and **registerDomainCode**, ask the support team for help via the Slack channel [#g11n-pipeline](https://ibm.enterprise.slack.com/archives/C0EP2MFR7).
- Please store the instance credentials generated after you receive it.

### Default profile

While a GP instance is created for you, a default profile will also be created at the same time. For this tutorial, you should create a *test instance*for you, so that **Human translation provider** can be set to **Test** in the related default profile.



### Maven and Artifactory settings

Please make sure that Maven is installed in your test OS. Run `mvn --version` in your shell/bash to check if it returns a version number. This requires maven, java and their paths (JAVA\_HOME) to setup properly. See Maven official [download](https://maven.apache.org/download.cgi) and [installation](https://maven.apache.org/install.html) reference.

**NOTE**: The minimum required Java version for GP is JDK 1.8.0\_261. The tools may work with earlier versions (of Java 1.8) if necessary, but it is recommended to run at least 1.8.0\_261.

Regarding to **Access Token** and **Maven Settings**, please read [Straker Maven Repository](https://ibm.box.com/s/tekmv57vc19gq1z0q2k9a5ynqvruz0jw) for the details.

### Tutorial data

For this tutorial, let's set a translation resource folder. Let's have our resource path to be at `src/main/resources` for this tutorial.

```
src  
├── main  
│   ├── java  
│   │   └── com  
│   │       └── ibm  
│   │           └── tutorial  
│   │               └── App.java  
│   └── resources  
│       ├── csv  
│       │   ├── fr  
│       │   │   └── test_demo.csv  
│       │   ├── ja  
│       │   │   └── test_demo.csv  
│       │   └── test_demo.csv  
│       ├── json  
│       │   ├── en  
│       │   │   └── test_demo.json  
│       │   ├── fr  
│       │   │   └── test_demo.json  
│       │   └── ja  
│       │       └── test_demo.json  
│       └── properties  
│           ├── test_demo-fr.properties  
│           ├── test_demo-ja.properties  
│           └── test_demo.properties  
└── test  
    └── java  
        └── com  
            └── ibm  
                └── tutorial  
                    └── AppTest.java
```

[Download the resources (Right click -> Save link as)](media_files/resources_1.zip). Unzip it and we will place this later under `src/main` for our tutorial projects.

**NOTE**: We will consider `src/main` as our base directory for this tutorial. The context of this is to refer all the sub-files/folders based on this base directory.

In this tutorial, we have setup a source (json for example) with 4 key value pairs

```
{  
    "greetings" : "Hello there!",  
    "day" : "Monday",  
    "new_greetings" : "Goodbye!",  
    "new_id" : "User code is @@45 today"  
}
```

And we have the existing translation for `French` and `Japanese` for two of those key value pairs already.

`fr`

```
{  
    "greetings" : "Bonjour!",  
    "day" : "Lundi"  
}
```

`ja`

```
{  
    "greetings" : "こんにちは！",  
    "day" : "月曜"  
}
```

Similarly, we have properties files and csv files setup.

### Custom filter jar

Before we import our translations into GP, we need to see what filters are already provided out of the box by the service and what filters need to be customized. [Here](https://github.ibm.com/1t1p/gpv2-java-tools/tree/master/resource-filter/gp-res-filter-impl/src/main/java/com/ibm/g11n/pipeline/resfilter/impl) are all the stock filters. For this tutorial, we can handle `JSON` and `JAVAUTF8` filters. However, we need to build custom filter for processing CSV files. [Here](https://github.ibm.com/1t1p/gp-ibmer-examples) is a tutorial reference on how to develop a custom filter.

**NOTE**: We may want to check if there are any file formats filters already developed for/by some other teams [here](https://github.ibm.com/1t1p/gp-ibmer-examples) to avoid re-creating a custom filter. For filter developers : You need the [impl](https://github.ibm.com/1t1p/gpv2-java-tools/tree/master/resource-filter/gp-res-filter-impl/src/main/java/com/ibm/g11n/pipeline/resfilter/impl) if you need to use any of the default filter functionality but only the [api](https://github.ibm.com/1t1p/gpv2-java-tools/tree/master/resource-filter/gp-res-filter) when developing a custom filter.

For our case, let's assume that we have developed a custom filter already. So, now we have [Download the CSV Resource Filter jar file (Right click -> Save link as)](https://kb.strakertranslations.com/hubfs/knowledge-base-files/csv-res-filter-2.0.0-SNAPSHOT-jar-with-dependencies.jar), and make sure to install it.

```
mvn install:install-file \  
  -Dfile=PATH_TO_csv-filter.jar \  
  -DcreateChecksum=true \  
  -DgroupId=com.ibm.g11n.pipeline \  
  -DartifactId=csv-res-filter \  
  -Dversion=2.0.0-SNAPSHOT \  
  -Dpackaging=jar \  
  -DgeneratePom=true
```

**NOTE**: The custom filter CSV version `2.0.0-SNAPSHOT` is provided by this tutorial, so we put `-Dversion=2.0.0-SNAPSHOT` but please put your custom filter's version when you use your own custom filter.

### Bundle naming convention

GP plugins and tools use base directory and path of source file to determine the bundle name and uses that as reference to where the files are located. It is important to maintain the path since it is related to the bundle identity.

- For any formats other than `JAVA`, `JAVAUTF8`, `JAVAMSG` and `JAVAMSGUTF8`, the path of a source file is mapped to bundle name by replacing the `\` from path to `.` but the latest parent path `\` to `-` . For example:

  - `com/ibm/g11n/example/MyStrings.json` will correspond to bundle name `com.ibm.g11n.example-MyStrings.json`
  - **NOTE**: This is handled a bit differently if you are using Jenkins plugin. For Jenkins plugin, `com/ibm/g11n/example/MyStrings.json` will correspond to bundle name `com-ibm-g11n-example-MyStrings.json`
- For these java formats - `JAVA`, `JAVAUTF8`, `JAVAMSG` and `JAVAMSGUTF8`, the path of a source file is mapped to bundle name by replacing `\` from path to `.` and removing the extension of file name. For example:

  - `com/ibm/g11n/example/MyStrings.properties` will correspond to bundle name `com.ibm.g11n.example.MyStrings` . This is same for Jenkins and Maven plugin.

### Finally - The import run for our tutorial

You can get the latest jar with dependency from Straker Maven Repository. Please refer to [Straker Maven Repository](https://ibm.box.com/s/tekmv57vc19gq1z0q2k9a5ynqvruz0jw) for the details and  [GP SDK-Tool Release](https://ibm.box.com/s/btwe6nzsmvrl87kutetuilhkovgxeo8g) which includes the latest release version and download links.

But, we will build it locally for ourselves:

1. Clone GP Tools repository for access to tools.  
   `git clone https://github.ibm.com/1t1p/gpv2-java-tools.git`
2. Make sure the *pom.xml* has `<revision>`, `<gp.res.filter.version>` and `<gp.java.client.version>` to some `-SNAPSHOT` version because this would be the development version to test stuff with. It is a development version that precedes the final release version.
3. Build GP client by navigating to `gp-java-client` and run `mvn clean install -DskipTests`.
4. Build the res-filter by navigating to `resource-filter/gp-res-filter` and run `mvn clean install -DskipTests`.
5. Run all the tools now by navigating to the root of `gpv2-java-tools` and run `mvn clean install -DskipTests`.
6. Get gp-cli jar file (`gp-java-tools/gp-cli/target/gp-cli-xxx-with-dependencies.jar`) in desired location - let's say Desktop. Let's copy `csv-filter.jar` there too. Let's add our GP credential into `mycreds.json`.
7. Based on all the information above, Let's import the translations from these [instructions](https://github.ibm.com/1t1p/gpv2-java-tools/blob/master/gp-java-tools/gp-cli/README.md#TOC-Import-Existing-Translations).  
   **NOTE**: Please create the bundle name based on the tool you are using. Jenkins and maven plugins handle path a tiny bit differently (as explained above).

#### If you are using MAVEN PLUGIN:

`resources/json/en/test_demo.json`

```
# Note that we will use `src/main` as our base directory.  
  
  
# Create empty en bundle for resources/json/en/test_demo.json  
java -jar gp-cli-xxx-with-dependencies.jar create -b resources.json.en-test_demo.json -l en -j mycreds.json  
  
# Import English source for resources/json/en/test_demo.json  
java -jar gp-cli-xxx-with-dependencies.jar import -b resources.json.en-test_demo.json -l en -t JSON -f PATH_TO_resources/json/en/test_demo.json -j mycreds.json  
  
# Import French translation for resources/json/fr/test_demo.json and mark them reviewed  
java -jar gp-cli-xxx-with-dependencies.jar import -b resources.json.en-test_demo.json -l fr -t JSON -f PATH_TO_resources/json/fr/test_demo.json -j mycreds.json -r  
  
# Import Japanese translation for resources/json/ja/test_demo.json and mark them reviewed  
java -jar gp-cli-xxx-with-dependencies.jar import -b resources.json.en-test_demo.json -l ja -t JSON -f PATH_TO_resources/json/ja/test_demo.json -j mycreds.json -r
```

`resources/properties/test_demo.properties`

```
# Note that we will use `src/main` as our base directory.  
  
  
# Create empty en bundle for resources/properties/test_demo.properties  
java -jar gp-cli-xxx-with-dependencies.jar create -b resources.properties.test_demo -l en -j mycreds.json  
  
# Import English source for resources/properties/test_demo.properties  
java -jar gp-cli-xxx-with-dependencies.jar import -b resources.properties.test_demo -l en -t JAVAUTF8 -f PATH_TO_resources/properties/test_demo.properties -j mycreds.json  
  
# Import French translation for resources/properties/test_demo-fr.properties and mark them reviewed  
java -jar gp-cli-xxx-with-dependencies.jar import -b resources.properties.test_demo -l fr -t JAVAUTF8 -f PATH_TO_resources/properties/test_demo-fr.properties -j mycreds.json -r  
  
# Import Japanese translation for esources/properties/test_demo-ja.properties and mark them reviewed  
java -jar gp-cli-xxx-with-dependencies.jar import -b resources.properties.test_demo -l ja -t JAVAUTF8 -f PATH_TO_resources/properties/test_demo-ja.properties -j mycreds.json -r
```

`resources/csv/test_demo.csv`

```
# Note that we will use `src/main` as our base directory.  
  
  
# Create empty en bundle for resources/csv/test_demo.csv  
java -classpath gp-cli-xxx-with-dependencies.jar:csv-filter.jar com/ibm/g11n/pipeline/tools/cli/GPCmd create -b resources.csv-test_demo.csv -l en -j mycreds.json  
  
# Import English source for resources/csv/test_demo.csv  
java -classpath gp-cli-xxx-with-dependencies.jar:csv-filter.jar com/ibm/g11n/pipeline/tools/cli/GPCmd import -b resources.csv-test_demo.csv -l en -t CSV -f PATH_TO_resources/csv/test_demo.csv -j mycreds.json  
  
# Import French translation for resources/csv/fr/test_demo.csv and mark them reviewed  
java -classpath gp-cli-xxx-with-dependencies.jar:csv-filter.jar com/ibm/g11n/pipeline/tools/cli/GPCmd import -b resources.csv-test_demo.csv -l fr -t CSV -f PATH_TO_resources/csv/fr/test_demo.csv -j mycreds.json -r  
  
# Import Japanese translation for resources/csv/ja/test_demo.json and mark them reviewed  
java -classpath gp-cli-xxx-with-dependencies.jar:csv-filter.jar com/ibm/g11n/pipeline/tools/cli/GPCmd import -b resources.csv-test_demo.csv -l ja -t CSV -f PATH_TO_resources/csv/ja/test_demo.csv -j mycreds.json -r
```

#### ---

#### If you are using JENKINS PLUGIN:

`resources/json/en/test_demo.json`

```
# Note that we will use `src/main` as our base directory.  
  
  
# Create empty en bundle for resources/json/en/test_demo.json  
java -jar gp-cli-xxx-with-dependencies.jar create -b resources-json-en-test_demo.json -l en -j mycreds.json  
  
# Import English source for resources/json/en/test_demo.json  
java -jar gp-cli-xxx-with-dependencies.jar import -b resources-json-en-test_demo.json -l en -t JSON -f PATH_TO_resources/json/en/test_demo.json -j mycreds.json  
  
# Import French translation for resources/json/fr/test_demo.json and mark them reviewed  
java -jar gp-cli-xxx-with-dependencies.jar import -b resources-json-en-test_demo.json -l fr -t JSON -f PATH_TO_resources/json/fr/test_demo.json -j mycreds.json -r  
  
# Import Japanese translation for resources/json/ja/test_demo.json and mark them reviewed  
java -jar gp-cli-xxx-with-dependencies.jar import -b resources-json-en-test_demo.json -l ja -t JSON -f PATH_TO_resources/json/ja/test_demo.json -j mycreds.json -r
```

---

`resources/properties/test_demo.properties`

```
# Note that we will use `src/main` as our base directory.  
  
  
# Create empty en bundle for resources/properties/test_demo.properties  
java -jar gp-cli-xxx-with-dependencies.jar create -b resources.properties.test_demo -l en -j mycreds.json  
  
# Import English source for resources/properties/test_demo.properties  
java -jar gp-cli-xxx-with-dependencies.jar import -b resources.properties.test_demo -l en -t JAVAUTF8 -f PATH_TO_resources/properties/test_demo.properties -j mycreds.json  
  
# Import French translation for resources/properties/test_demo-fr.properties and mark them reviewed  
java -jar gp-cli-xxx-with-dependencies.jar import -b resources.properties.test_demo -l fr -t JAVAUTF8 -f PATH_TO_resources/properties/test_demo-fr.properties -j mycreds.json -r  
  
# Import Japanese translation for esources/properties/test_demo-ja.properties and mark them reviewed  
java -jar gp-cli-xxx-with-dependencies.jar import -b resources.properties.test_demo -l ja -t JAVAUTF8 -f PATH_TO_resources/properties/test_demo-ja.properties -j mycreds.json -r
```

---

`resources/csv/test_demo.csv`

```
# Note that we will use `src/main` as our base directory.  
  
  
# Create empty en bundle for resources/csv/test_demo.csv  
java -classpath gp-cli-xxx-with-dependencies.jar:csv-filter.jar com/ibm/g11n/pipeline/tools/cli/GPCmd create -b resources-csv-test_demo.csv -l en -j mycreds.json  
  
# Import English source for resources/csv/test_demo.csv  
java -classpath gp-cli-xxx-with-dependencies.jar:csv-filter.jar com/ibm/g11n/pipeline/tools/cli/GPCmd import -b resources-csv-test_demo.csv -l en -t CSV -f PATH_TO_resources/csv/test_demo.csv -j mycreds.json  
  
# Import French translation for resources/csv/fr/test_demo.csv and mark them reviewed  
java -classpath gp-cli-xxx-with-dependencies.jar:csv-filter.jar com/ibm/g11n/pipeline/tools/cli/GPCmd import -b resources-csv-test_demo.csv -l fr -t CSV -f PATH_TO_resources/csv/fr/test_demo.csv -j mycreds.json -r  
  
# Import Japanese translation for resources/csv/ja/test_demo.json and mark them reviewed  
java -classpath gp-cli-xxx-with-dependencies.jar:csv-filter.jar com/ibm/g11n/pipeline/tools/cli/GPCmd import -b resources-csv-test_demo.csv -l ja -t CSV -f PATH_TO_resources/csv/ja/test_demo.csv -j mycreds.json -r
```

---

**NOTE**: For new users, do not forget to "import your existing translation" in production GP instance before filing the first TR (Translation Request).  

### 

### **Supplement**

For this tutorial, we focus on bundles for demonstration and practice. However, it would be helpful to know about some features that are outside the scope of this tutorial.

#### 1. File support for PII content:

Globalization Pipeline supports PII documents (Files). Bundles are used for the formats that can be parsed into strings of key:value pairs, while other document formats are considered as "Files" in GP norms. See supported file types [here](https://help.straker.ai/en/g11n/supported-file-types).

- Maven plugin - Maven supports `<fileSet>` similar to `<bundleSet>`. See an [example](https://github.ibm.com/1t1p/gpv2-java-tools/tree/master/gp-java-tools/gp-maven-plugin#filesets). Note to use `<resourceType>file</resourceType>`.
- Jenkins plugin - Jenkins supports an option to choose either bundle or file.
- CLI - GP CLI supports file commands similar to bundle commands. Run `help` with cli to see the list.

#### 2. Additional filter options:

GP allows filter developers to set **FilterOptions** so as to additionally set configurations.

- To use this feature with gp-cli, you'll need to pass the Java environment arg `-DGP_RES_FILTER_OPTIONS`. This arg must be a path to a Java *.properties* file that contains the filter options as follows:

```
JavaUTF8.colmax=100  
IOS.maxLineLength=100  
XLIFF12.fillInTargetWithSource=true
```

- Maven supports **FilterOptions** from environment variable or explicitly adding option in pom.xml. Explicitly allowing options on configuration will override `GP_RES_FILTER_OPTIONS` environment variable, like:

```
<configuration>  
    ...  
    <credentials>  
        ...  
    </credentials>  
    <bundleSets>  
        ...  
    </bundleSets>  
    <filterOptions>  
        <JavaUTF8.colmax>50</JavaUTF8.colmax>  
    </filterOptions>  
    ...  
</configuraion>
```

- Jenkins has a field for custom filter option like a JSON representation of key:value pairs where each key is in the form: " . " and each value is the corresponding filter option property value. If no value is found, the key will be ignored. If the JSON is invalid, no options will applied. For example:

`{ "JavaUTF8.colmax": "100", "Javamsg.colmax": "75" }`

- Ant supports filter options as well. In your target `<gp:upload>` or `<gp:download>` you can put any filter option. For example:

```
<target name="upload-java">  
    <gp:upload credentialsJson="${gp.credentials.json}">  
        <targetLanguage lang="es"/>  
        <targetLanguage lang="fr"/>  
        <targetLanguage lang="zh-Hans"/>  
        <bundleSet type="JAVAUTF8">  
            ...  
        </bundleSet>  
        <filterOption key="JavaUTF8.colmax" value="50"/>  
    </gp:upload>  
</target>
```

**NOTE**: To find out what filter options are supported for particular file format, see the implementation for that filter. For example: `JAVA`, `JAVAUTF8`, `JAVAMSG` and `JAVAMSGUTF8` provides `excludeescapecharacters` and `colmax` filter options [here](https://github.ibm.com/1t1p/gpv2-java-tools/blob/master/resource-filter/gp-res-filter-impl/src/main/java/com/ibm/g11n/pipeline/resfilter/impl/JavaPropertiesResource.java#L48). For a complete list of all custom filter options and what they do, you can look [here](https://github.ibm.com/1t1p/gpv2-java-tools/blob/master/resource-filter/docs/customFilterOptions.md).

#### 3. Filter developers can assign Do-Not-Translate:

Filter developers can decide on marking a whole string untranslatable while parsing/merging content. See an example in csv filter [here](https://github.ibm.com/1t1p/gpv2-java-tools/blob/master/resource-filter/csv-res-filter/src/main/java/com/ibm/g11n/pipeline/resfilter/csv/CSVFilter.java#L56).
