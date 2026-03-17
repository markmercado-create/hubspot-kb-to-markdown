---
title: "Introduction"
subtitle: "WebFM"
knowledge_base: "Globalization Help Center"
category: "WebFM"
subcategory: "Overview"
language: "en"
keywords: "webfm"
status: "PUBLISHED"
archived: "false"
last_modified: "1749606206314"
source_url: "https://help.straker.ai/en/g11n/webfm/introduction"
exported_at: "2026-03-17T11:30:13Z"
---

# Introduction

The Web-based File Management Tool is a localization engineering tool used in the development and translation of localized files. The basic work flow is as follows:

- **Input into WebFM:** *Base product source files* which have been coded in such a way that they can be easily translated and localized to support any local market. The files which are translated are called Product Integrated Information (PII) files. These are any files that display information to the user while the program is running that need to be translated or localized, whether as text in dialog boxes, on buttons, as help, task wizards, cli text, etc.
- **Process by WebFM Application:** *Application* is the basic unit in WebFM. Every file will be categorized into a single application and put into the application folder during file operation. WebFM will use the application folder as identifier. The application name should not be changed between releases.
- **Output from WebFM:** *Localized versions of the source files* which can be easily built as part of the base product build, for instance if they are needed during the installation of the base product or deployed with product.

### Users of WebFM

When a project is configured, users are added to the project so that they have access to only specific projects. They are also given access to specific languages in a project so that users will not accidentally delete or over write files of another user.

Users are usually created and given access to project by the person who has been assigned the authority of Globalization Project Manager (GPM) for the project. The GPM create projects and add users to that project.

There are different authorization levels for TVT testers and Translators as well. These levels are set when the GPM adds users to their project.

- **GPM:** Typically the GPM is responsible for creating the project, adding the languages to be translated, adding the proper users, and assigning languages to the users of the project, and configuring the applications for the project.
- **File-handler:** In most cases the File-handler will use the dispatcher tool to extract files from the source components to create a zip package that will be used for the shipments to the translation centers. They will also unzip, Easycheck and check into source controls the shipments of translated PII received from the translation centers. They are also responsible for running dispatcher daily, or as required, during TVT to monitor changes to the English PII files.
- **Translator:** The translator receives the files from the translation center and then imports the files into the IBM Translation Manager (TM) tool. The files are then translated, exported from TM, and packaged into zip files for uploading to WebFM. Once the files are uploaded to WebFM they are unzipped, error-checked, and then checked into source controls. This process is normally repeated several times during the translation phase of a product development cycle.
- **TVT Tester:** During Translation Verification Testing (TVT) the File-handler will run WebFM's Dispatcher function daily to get the latest changes to the source PII. The "new" PII will be given to the tester for translation. If the tester has files that have changed they will zip those files up and upload them to WebFM for error-checking (Easycheck) and checking into source controls.

### Components of WebFM

- **User Manager:** This view allows for creation and removal of users.
- **Project Manager:** This view allows GPMs to create, delete, and add users and languages to projects.
- **Work with NLV files and Work with English files:** The Work with NLV files tool allows a user to validate (Easycheck) translated files and check files into source controls.

  - **Easycheck(CHKPII):** The easycheck (CHKPII) tool checks translated PII files for errors and processes and converts the PII files according to file type. Easycheck will also change, if needed, the encoding of the translated files from the native code page to the proper code page before checking the files into source controls.
  - **Filecheckin/Download:** This tool takes translated files and checks them into the configured components and releases in source controls. Filecheckin also performs certain conversions on specified file types during the filecheckin process. For example: For JAVA files the tool will change the name of foo.java to foo\_.java.
  - **View:** The Work with English files view allows the user to view set of English files that translated files are error-checked against.
- **Dispatcher:** The Dispatcher tool allows the user to monitor a source repository and release to determine if there are any new or changed files since a specified date or since the last run of Dispatcher (depending on the option that you select), download those files using the "Dispatcher Packages" tool, check a copy of those files into the specified destination repository and release when desired, and create mock translated files when desired.
- **Dispatcher Packages:** Used to download zip packages created by the Dispatcher program.
- **Compare Package Files:** This tool allows users to compare the contents of package files (.zip files) to determine if any files have been accidentally removed or discarded during the process of translation or testing.
- **Applications Configuration:** From here the GPM sets up the source repository data for a specific application so that the WEBFM tool will interface properly with source repository.
