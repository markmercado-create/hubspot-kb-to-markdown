---
title: "GB18030 Certification Training Guide (Straker Internal Use)"
knowledge_base: "Globalization Help Center"
category: "GB18030 Certification"
subcategory: "Certification Training Guide"
language: "en"
status: "PUBLISHED"
archived: "false"
last_modified: "1756861639191"
source_url: "https://help.straker.ai/en/g11n/gb18030-certification-training-guide-straker-internal-use"
exported_at: "2026-03-17T10:52:05Z"
---

# GB18030 Certification Training Guide (Straker Internal Use)

### **1. Overview of GB18030 Certification**

**What is GB18030?**

GB18030 is a mandatory Chinese government character encoding standard required for any software sold or distributed in China that handles text. It ensures correct display, storage, processing, and input of a wide range of characters:

- Simplified and Traditional Chinese
- Minority languages (e.g., Tibetan, Uyghur)
- Unicode characters (beyond Basic Multilingual Plane)
- Emoji and symbols

**Why is it Mandatory?**

Compliance ensures legal distribution in China and avoids regulatory risks such as product bans, fines, or legal actions. GB18030 certification also ensures that software meets localization standards for diverse Chinese users.

**Example of GB18030 testing data**   
![Picture1](https://20462040.fs1.hubspotusercontent-na1.net/hubfs/20462040/knowledge-base-files/GB18030%20Certification/Picture1.png)

### **1.1 GB18030: The Chinese Standard**

**Last Updated:** 2024-10-07

GB18030-2000 is a Chinese standard that specifies an extended code page for use in the Chinese market.

A brief history of major GB code pages:

- **GB 2312-1980**: Encodes 6000+ frequently used ideographs.
- **GBK**: Extends GB2312 to cover all 20,902 unified ideographs from Unicode 2.1.
- **Unicode 3.0–3.1**: Adds 48,000+ ideographs.
- **GB18030**: Extends GBK for Unicode 3.0 and adds mapping to all Unicode code points. It's functionally similar to a UTF encoding, while maintaining compatibility with GB2312 and GBK.

GB18030 character assignments:

- Compatible with GB2312-1980 and GBK
- Maintains Unicode mapping tables
- Required for legal compliance in China

### **2. Certification Process**

#### **Step-by-Step Certification Flow**

1. **Preparation Phase**
   1. Identify target IBM software products
   2. Confirm GB18030 requirement applicability
   3. Review existing product encoding and UI language support

The product team provides information to the GB18030 engineer to help identify GB18030 certification testing coverage. Typically focusing on new or changed product features—in the form of either existing test cases or the ‘What’s New’ documentation for the release.

![Picture2](https://20462040.fs1.hubspotusercontent-na1.net/hubfs/20462040/knowledge-base-files/GB18030%20Certification/Picture2.png)

![Picture3](https://20462040.fs1.hubspotusercontent-na1.net/hubfs/20462040/knowledge-base-files/GB18030%20Certification/Picture3.png)

The GB18030 Engineer will investigate the product following the above information to develop GB18030 Test cases.  
  
![Picture4](https://20462040.fs1.hubspotusercontent-na1.net/hubfs/20462040/knowledge-base-files/GB18030%20Certification/Picture4.png)

2. **Documentation Collection**  
  
  

1. 1. Product manuals
   2. Technical specifications
   3. Language support and encoding charts
   4. UI samples

3. **Testing**  

1. 1. Conducted by a certified government lab in China
   2. Tests cover:
      1. Character encoding coverage
      2. Input/output rendering
      3. Data storage compliance

GB18030 lab testing interface/tool in use on Chinese OS environment.

![Picture5](https://20462040.fs1.hubspotusercontent-na1.net/hubfs/20462040/knowledge-base-files/GB18030%20Certification/Picture5.png)

![Picture6](https://20462040.fs1.hubspotusercontent-na1.net/hubfs/20462040/knowledge-base-files/GB18030%20Certification/Picture6.png)

![Picture7](https://20462040.fs1.hubspotusercontent-na1.net/hubfs/20462040/knowledge-base-files/GB18030%20Certification/Picture7.png)

4. **Validation**  

1. 1. Collect test results and screenshots
   2. Compile certification package

Once testing is successfully completed, we will archive all related compliance documents in the repository as required by the client and send a closing email notification

![Picture8](https://20462040.fs1.hubspotusercontent-na1.net/hubfs/20462040/knowledge-base-files/GB18030%20Certification/Picture8.png)

5. **Approval**  

1. 1. Receive certification approval from lab
   2. Update product compliance records

### **3. Requirements for Certification Submission**

#### **A. Product Manuals**

Each manual must:

- Be translated into Simplified Chinese
- Include character support documentation
- Highlight or show how character input/output is supported across features

#### **B. Technical Specifications**

Specs must include:

- Encoding libraries used (Unicode/GB18030)
- Input/output frameworks and font support
- Character fallback/error handling strategies

#### **C. Language Support Lists**

Software must demonstrate support for:

- Simplified Chinese
- Traditional Chinese
- Minority scripts
- Unicode supplementary characters
- Emoji and special symbols

#### **D. UI & Character Rendering Samples**

Provide screenshots of:

- Input fields showing correct Chinese character input
- Menus and labels with Simplified and Traditional Chinese
- Font rendering for ethnic languages (e.g., Uyghur, Tibetan)
- Emoji and symbol rendering in context

### **4. Technical Testing Requirements**

#### **Lab Testing Includes:**

- GB18030 character encoding coverage
- Correct character display in UI
- Input method compatibility
- Data storage integrity with GB18030

#### **Test Tools**

- Tools used by labs are government-approved and simulate:
  - Chinese OS environments
  - GB18030-specific text inputs
  - Rendering consistency across platforms

Test tool screen showing GB18030 encoding test results  
  
![Picture9](https://20462040.fs1.hubspotusercontent-na1.net/hubfs/20462040/Picture9.png)

### ***GB18030 Code Page Support***

**Last Updated:** 2025-04-07

- Multi-byte encoding
- Direct mapping to Unicode
- 64K+ characters

Character Representation:

- UTF-8 for narrow characters & string literals
- UTF-32 for wide characters & string literals
- Compiler internally processes UTF-8

### **5. Responsibilities and Stakeholders**

|  |  |
| --- | --- |
| **Party** | **Responsibility** |
| Straker China Team | Manages process execution and coordination |
| IBM Product Team | Provides product details and approvals |
| Training Department | Prepares training and documentation |
| Testing Lab | Conducts validation and issues certification |

### **6. Common Issues to Avoid**

- **Political sensitivity**: Ensure maps or country names (e.g., Taiwan) follow Chinese regulations
- **Incorrect rendering**: Validate display of all required character sets, not just Simplified Chinese
- **Input limitations**: Ensure input methods allow minority scripts and special symbols

Examples of **incorrect rendering**:

- Square boxes / question marks replacing missing characters.

![Picture10](https://20462040.fs1.hubspotusercontent-na1.net/hubfs/20462040/Picture10.png)

- Map with politically sensitive labeling vs. compliant labeling.

![Picture11](https://20462040.fs1.hubspotusercontent-na1.net/hubfs/20462040/Picture11.png)

  

### **7. Appendices**

#### **Appendix A: Screenshot Samples**

- Actual certified examples from past successful GB18030 tests.
- Before-and-after UI for products that had rendering issues fixed.

![Picture12](https://20462040.fs1.hubspotusercontent-na1.net/hubfs/20462040/Picture12.png)

#### **Appendix B: Language Support Table**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Language** | **Encoding** | **UI Support** | **Input Method** | **Test Passed** |
| Simplified Chinese | GB18030 | Yes | Yes | Yes |
| Traditional Chinese | GB18030 | Yes | Yes | Yes |
| Tibetan | GB18030 | Partial | Yes | In progress |
| Uyghur | GB18030 | Partial | Yes | In progress |

Language selection menu in the product with GB18030 languages visible  
  
![Picture13](https://20462040.fs1.hubspotusercontent-na1.net/hubfs/20462040/Picture13.png)

#### **Additional Technical Notes**

### **Handling Data in Globalized Applications**

**Last Updated:** 2024-10-07

Topics include:

- Unicode and character processing
- GB18030 integration and CCSIDs (e.g., CCSID 1392)
- Bidirectional and DBCS data handling
- Use of locales for regional behavior

### **Unicode Support for Wide-Character Literals**

**Last Updated:** 2025-04-07

- Unicode character storage enables global character support
- Wide-character literals stored as UCS-2 (Unicode CCSID 13488)
- Reduces need for code page conversions in C/C++ development
- Internal support in compiler through UTF-based processing

### **Exemption Document – Definition:**

In the context of GB18030 certification (China’s national character encoding standard), the "Exemption Document" is a formal document submitted to or approved by Chinese regulatory authorities (such as the Ministry of Industry and Information Technology – MIIT). It is used to request exemption from specific technical requirements in the GB18030 standard that a product cannot comply with due to:

- Technical limitations
- Legacy system constraints
- Justified reasons why compliance is infeasible

**Key Points About the Exemption Document:**

- It is only applicable when a product cannot fully comply with GB18030-2022 requirements.
- It must provide detailed rationale and supporting technical evidence.
- Approval is not guaranteed; it depends on the review and decision of the regulatory body.
- It is often submitted for legacy products or software components where updates would cause significant disruption or are technically impractical.

**Example Usage:**

If a legacy IBM software product cannot support all Unicode characters required by GB18030, the team may submit an Exemption Document explaining:

"This version of the software uses a fixed-width encoding structure that cannot be modified without breaking core functions. Therefore, full GB18030-2022 support is not feasible."
