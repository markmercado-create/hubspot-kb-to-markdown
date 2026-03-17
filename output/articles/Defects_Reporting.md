---
title: "Defects Reporting"
subtitle: "Download and view the ICT defects information"
knowledge_base: "Globalization Help Center"
category: "Globalization Pipeline"
subcategory: "ict doc"
language: "en"
status: "PUBLISHED"
archived: "false"
last_modified: "1749606949728"
source_url: "https://help.straker.ai/en/g11n/defects-reporting"
exported_at: "2026-03-17T10:52:04Z"
---

# Defects Reporting

During ICT, testers can submit defects to the product development team through their internal Straker workbench. The product development team can download ICT defect reports on Globalization Pipeline dashboard or use Globalization Pipeline command line interface tool (gp-cli). Product development team can view details of ICT defect reports and attachments uploaded by testers directly in Globalization Pipeline, and the reports can be exported.

### How to download ICT defect reports

Users can download one CSV file as a quick summary of defects, and download one ZIP package for more comprehensive information.

- With Globalization Pipeline dashboard:

1. On the **Translation Requests** tab, click on the translation request name, or click on overflow menu to select **View the translation request detail**.

   2. To view a summary of the defects identified in the translation request, scroll to the bottom of the translation request detail page. Here, you will find a table that summarizes the number of defects presenting in language and severity levels.

![](https://20462040.fs1.hubspotusercontent-na1.net/hubfs/20462040/undefined-Jul-22-2024-07-16-02-7334-AM.png)

   3. Users can click on "**Export CSV**" link to download one CSV file named as "*ICT-defect-report-[issueTrackingId].csv*".

   4. Users can click on "**Export ZIP**" link to download one ZIP package named as "*[InstanceId]\_[issueTrackingId]\_[timestamp].zip*".

- With Globalization pipeline command line interface tool (gp-cli):

1. Utilize the "export-defects" command to export all defects reported by testers as an attachment, using a specified tracking ID.

                   a. The parameters:

- - - - \* **-t**: Issue Tracking ID
      - **-j**: JSON file containing Globalization Pipeline service credentials
      - \* **-o**: File name where the exported data will be written.
      - **-r**: Report type to be generated, *HTML* or *CSV* are valid types. Default if not provided is *CSV.*

        - Default: *CSV*
        - Possible Values: [*HTML*, *CSV*]

b. To download one CSV file:

`java -jar gp-cli.jar export-defects -r CSV -o ./Report-CSV.csv -j credential.json`

                c. To download one ZIP package:

`java -jar gp-cli.jar export-defects -r HTML -o ./Report-HTML.zip -j credential.json`

### Sample information obtained from CSV file and ZIP package

a. Open downloaded CSV file, users can find a quick summary of defects like the following:![](https://20462040.fs1.hubspotusercontent-na1.net/hubfs/20462040/undefined-Jul-22-2024-07-16-03-6610-AM.png)

- - Defect ID - The ID of ICT defect.
  - Languages - The native language that has defects.
  - Severity - The severity of ICT defect, include critical, major, moderate and minor.
  - Category - The type of ICT defect, include untranslated, truncation, corruption, layout, concatenation, cultural-format, text-rendering, bidi and other.
  - Title - The summary of ICT defect.
  - Author - The creator of ICT defect.
  - Date - The time of ICT defect is submitted on.

b. Users can extract downloaded ZIP package for more comprehensive information.

- - Users can open the ***index.html*** file to see the detail defect list with hyper links directing users to detail page of each individual defect.

![Index page](https://20462040.fs1.hubspotusercontent-na1.net/hubfs/20462040/undefined-Jul-22-2024-07-16-03-1268-AM.png)

- - Users can click on ID link, such as "23000130", to obtain details of this defect as below:[![](https://20462040.fs1.hubspotusercontent-na1.net/hubfs/20462040/undefined-Jul-22-2024-07-16-04-0533-AM.png)](https://w3.ibm.com/w3publisher/ict/)

- - Then users can click on Attachments link to open screenshots or other attachments that were added by the testers.

    - Supported types of attachment as GIF, JPEG, PNG, BMP, SVG, TXT, HTML, CSV, Markdown, XML, ZIP and PDF.
