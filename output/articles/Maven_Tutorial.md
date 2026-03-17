---
title: "Maven Tutorial"
knowledge_base: "Globalization Help Center"
category: "Globalization Pipeline"
subcategory: "tutorial"
language: "en"
status: "PUBLISHED"
archived: "false"
last_modified: "1749606167488"
source_url: "https://help.straker.ai/en/g11n/maven-case"
exported_at: "2026-03-17T10:52:05Z"
---

# Maven Tutorial

Please go through [Initial Setup](https://kb.strakertranslations.com/en/knowledge/initial-setup) if you haven't already.

### Create a project

Let's start by creating a project at your desired location.

Run the following command in your shell to generate the tutorial project.

`mvn archetype:generate -DgroupId=com.ibm.tutorial
-DartifactId=demo-gp -DarchetypeArtifactId=maven-archetype-quickstart
-DarchetypeVersion=1.4 -DinteractiveMode=false`

### Add resources

Now let's add our resources we discussed in Initial Setup - [Resources (Right click -> Save link as)](https://kb.strakertranslations.com/hubfs/knowledge-base-files/resources.zip)

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

### Add custom filter

Let's add our custom CSV filter to runtime build path - Simply add [CSV Resource Filter jar file (Right click -> Save link as)](https://kb.strakertranslations.com/hubfs/knowledge-base-files/csv-res-filter-2.0.0-SNAPSHOT-jar-with-dependencies.jar)  to `src/lib` folder. You may need to create `lib` folder under `src` if it is not already generated. And make sure to install it:

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

**NOTE**: The custom filter CSV version `2.0.0-SNAPSHOT` is provided by this tutorial, so we put `-Dversion=2.0.0-SNAPSHOT`. But please put your custom filter's version when you use your own custom filter.

### Update the pom.xml

Here is the complete pom.xml for my project:

```
<?xml version="1.0" encoding="UTF-8"?>  
  
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"  
  xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">  
  <modelVersion>4.0.0</modelVersion>  
  
  <groupId>com.ibm.tutorial</groupId>  
  <artifactId>demo-gp</artifactId>  
  <version>1.0-SNAPSHOT</version>  
  
  <name>demo-gp</name>  
  <!-- FIXME change it to the project's website -->  
  <url>http://www.example.com</url>  
  
  <properties>  
    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>  
    <maven.compiler.source>1.7</maven.compiler.source>  
    <maven.compiler.target>1.7</maven.compiler.target>  
  </properties>  
  
  <dependencies>  
    <dependency>  
      <groupId>junit</groupId>  
      <artifactId>junit</artifactId>  
      <version>4.11</version>  
      <scope>test</scope>  
    </dependency>  
  </dependencies>  
  
  <pluginRepositories>  
    <pluginRepository>  
      <id>gp-central</id>  
        <name>GP TaaS Artifactory Repo</name>  
        <url>https://na.artifactory.swg-devops.com:443/artifactory/txo-gp-maven-local</url>  
    </pluginRepository>  
  </pluginRepositories>  
  <repositories>  
        <repository>  
            <id>gp-central</id>  
            <name>GP TaaS Artifactory Repo</name>  
            <url>https://na.artifactory.swg-devops.com:443/artifactory/txo-gp-maven-local</url>  
        </repository>  
    </repositories>  
  
  <build>  
    <pluginManagement><!-- lock down plugins versions to avoid using Maven defaults (may be moved to parent pom) -->  
      <plugins>  
        <!-- clean lifecycle, see https://maven.apache.org/ref/current/maven-core/lifecycles.html#clean_Lifecycle -->  
        <plugin>  
          <artifactId>maven-clean-plugin</artifactId>  
          <version>3.1.0</version>  
        </plugin>  
        <!-- default lifecycle, jar packaging: see https://maven.apache.org/ref/current/maven-core/default-bindings.html#Plugin_bindings_for_jar_packaging -->  
        <plugin>  
          <artifactId>maven-resources-plugin</artifactId>  
          <version>3.0.2</version>  
        </plugin>  
        <plugin>  
          <artifactId>maven-compiler-plugin</artifactId>  
          <version>3.8.0</version>  
        </plugin>  
        <plugin>  
          <artifactId>maven-surefire-plugin</artifactId>  
          <version>2.22.1</version>  
        </plugin>  
        <plugin>  
          <artifactId>maven-jar-plugin</artifactId>  
          <version>3.0.2</version>  
        </plugin>  
        <plugin>  
          <artifactId>maven-install-plugin</artifactId>  
          <version>2.5.2</version>  
        </plugin>  
        <plugin>  
          <artifactId>maven-deploy-plugin</artifactId>  
          <version>2.8.2</version>  
        </plugin>  
        <!-- site lifecycle, see https://maven.apache.org/ref/current/maven-core/lifecycles.html#site_Lifecycle -->  
        <plugin>  
          <artifactId>maven-site-plugin</artifactId>  
          <version>3.7.1</version>  
        </plugin>  
        <plugin>  
          <artifactId>maven-project-info-reports-plugin</artifactId>  
          <version>3.0.0</version>  
        </plugin>  
      </plugins>  
    </pluginManagement>  
    <plugins>  
            <plugin>  
                <groupId>com.ibm.g11n.pipeline</groupId>  
                <artifactId>gp-maven-plugin</artifactId>  
                <version>2.0.0-M20210607</version>  
                <dependencies>  
                    <dependency>  
                        <groupId>com.ibm.g11n.pipeline</groupId>  
                        <artifactId>gp-res-filter</artifactId>  
                        <version><USE THE SUITABLE VERSION></version>  
                    </dependency>  
                    <dependency>  
                        <groupId>com.ibm.g11n.pipeline</groupId>  
                        <artifactId>csv-res-filter</artifactId>  
                        <version>2.0.0-SNAPSHOT</version>  
                    </dependency>  
                </dependencies>  
                <configuration>  
                    <credentials>  
                        <url>https://g11n-pipeline-api.straker.global/translate/rest</url>  
                        <userId>****</userId>  
                        <password>****</password>  
                        <instanceId>parth-demo-test</instanceId>  
                    </credentials>  
                    <bundleSets>  
                        <bundleSet>  
                            <type>JAVAUTF8</type>  
                            <sourceFiles>  
                                <directory>src/main</directory>  
                                    <includes>  
                                        <include>**/*.properties</include>  
                                    </includes>  
                                    <excludes>  
                                        <exclude>**/*-*.properties</exclude>  
                                    </excludes>  
                            </sourceFiles>  
                            <outputDir>target/nls</outputDir>  
                            <targetLanguages>  
                                <param>fr</param>  
                                <param>ja</param>  
                            </targetLanguages>  
                        </bundleSet>  
                        <bundleSet>  
                            <type>JSON</type>  
                            <sourceFiles>  
                                <directory>src/main</directory>  
                                    <includes>  
                                        <include>**/en/*.json</include>  
                                    </includes>  
                            </sourceFiles>  
                            <outputDir>target/nls</outputDir>  
                            <targetLanguages>  
                                <param>fr</param>  
                                <param>ja</param>  
                            </targetLanguages>  
                        </bundleSet>  
                        <bundleSet>  
                            <type>CSV</type>  
                            <sourceFiles>  
                                <directory>src/main</directory>  
                                    <includes>  
                                        <include>**/csv/*.csv</include>  
                                    </includes>  
                            </sourceFiles>  
                            <outputDir>target/nls</outputDir>  
                            <targetLanguages>  
                                <param>fr</param>  
                                <param>ja</param>  
                            </targetLanguages>  
                        </bundleSet>  
                    </bundleSets>  
                </configuration>  
            </plugin>  
        </plugins>  
  </build>  
</project>
```

### Points to note

- Here we add `pluginRepository` and `repository` to point to our Artifactory.
- We add GP plugin in `<plugins>..</plugins>` outside of `pluginManagement` but inside `build`.
- Maven plugin has dependency for gp-res-filter, and you can feel free to use the latest version from the Straker Maven respository. Please read [Straker Maven Repository](https://ibm.box.com/s/tekmv57vc19gq1z0q2k9a5ynqvruz0jw) and [GP SDK-Tool Release](https://ibm.box.com/s/btwe6nzsmvrl87kutetuilhkovgxeo8g).
- The GP plugin version `2.0.0-M20210607` comes from latest released version.
- The custom filter CSV version `2.0.0-SNAPSHOT` is provided by this tutorial, but please put your custom filter's version when you use your own custom filter.
- All the configurations are self explanatory (especially after going through Initial Setup). Further configuration details can be understood by [Maven plugin readme](https://github.ibm.com/1t1p/gpv2-java-tools/blob/master/gp-java-tools/gp-maven-plugin/README.md).

### Run

Now you can simply run `mvn gp:upload` and `mvn gp:download` as many times from build as you'd like.

### TR submission

With your test GP instance, let's create a mock TR (Translation Request) on GP dashboard.

![](https://20462040.fs1.hubspotusercontent-na1.net/hubfs/20462040/image-png-Jul-05-2024-04-58-32-3245-AM.png)

Your TR should be merged in some time since it is a mock TR. Feel free to run `mvn gp:download` after that with any configuration of your choice from [Maven readme](https://github.ibm.com/1t1p/gpv2-java-tools/blob/master/gp-java-tools/gp-maven-plugin/README.md).
