---
title: "WebFM(Web UI) – Functions & Screens Detailed Guide"
knowledge_base: "Globalization Help Center"
category: "WebFM"
subcategory: "How to guide"
language: "en"
keywords: "webfm"
status: "PUBLISHED"
archived: "false"
last_modified: "1772243792756"
source_url: "https://help.straker.ai/en/g11n/webfm/web-ui-functions-screens-detailed-guide"
exported_at: "2026-03-17T10:52:05Z"
---

# WebFM(Web UI) – Functions & Screens Detailed Guide

- **Login Screen  
    
  ![Picture1](https://20462040.fs1.hubspotusercontent-na1.net/hubfs/20462040/knowledge-base-files/webfm/How%20to%20guides/WebUI/Picture1.png)**
  - **Username / Email Field**
    - Function: Accepts registered WebFM login ID.
    - Redirects: Validates when paired with password.
    - Info: Username/email string.
    - Use Case: Identify user account.
  - **Password Field**
    - Function: Accepts account password.
    - Redirects: Works with login button.
    - Info: Password (masked input).
    - Use Case: Secure access.
  - **Login Button**
    - Function: Authenticates credentials.
    - Redirects: **Dashboard Home** if successful; **Error Message Popup** if invalid.
    - Info: Submits login data.
    - Use Case: Access WebFM environment.
  - **Forgot Password Link**
    - Function: Initiates password reset workflow.
    - Redirects: Password Recovery Screen.
    - Info: Registered email address.
    - Use Case: Recover access.
- **Dashboard Home Screen  
    
  ![Picture2](https://20462040.fs1.hubspotusercontent-na1.net/hubfs/20462040/knowledge-base-files/webfm/How%20to%20guides/WebUI/Picture2.png)**

- - **Top Navigation Bar**
    - Tabs: Projects | Files | Users | Settings | Reports | Help.
    - Function: Provides quick navigation.
    - Redirects: Each tab’s dedicated module.
    - Use Case: Central hub.
  - **Quick Actions Panel**
    - Buttons:
      - **+ New Project** → Project Setup Screen
      - **Upload File** → File Upload Modal
      - **Invite User** → User Registration Screen
    - Use Case: Fast access to common tasks.
  - **Recent Activity Feed**
    - Displays: Recently updated projects/files.
    - Redirects: Clicking opens related details screen.
    - Use Case: Monitor ongoing activity.
  - **Elements**
    1. **Left Navigation Panel**
    2. **Select Project (Dropdown + Select Button)**
    3. **Function:** Allows the user to choose an active project workspace.
    4. **Redirects To:** The **Project Dashboard**, where project files, tasks, and settings are displayed.
    5. **Use Case:** Users switch between multiple client or lab projects (e.g., different translation/localization projects).
  - **Admin Tools**
    1. **User Manager**
    2. **Function:** Opens the user management screen.
    3. **Redirects To:** User Manager screen where administrators can add, remove, or edit user accounts.
    4. **Use Case:** Used by team leads or admins to control system access.
  - **Projects Manager**
    1. **Function:** Opens project settings and configurations.
    2. **Redirects To:** Project Manager screen.
    3. **Use Case:** Manage project metadata, assign resources, or update configurations.
  - **Maintenance \ Troubleshooting**
    1. **Report Problem**
       1. **Function:** Opens a form to report technical/system issues.
       2. **Redirects To:** Problem Report screen.
       3. **Use Case:** Users log bugs, errors, or access issues.
    2. **Stop all File Processing**
       1. **Function:** Halts all ongoing file-processing jobs.
       2. **Redirects To:** Confirmation prompt.
       3. **Use Case:** Emergency stop if jobs are corrupted or system load needs to be reduced.
    3. **System Log**
       1. **Function:** Displays logs of WebFM processes.
       2. **Redirects To:** Log viewer screen.
       3. **Use Case:** For troubleshooting, monitoring activity, or reviewing errors.
    4. **Help → WebFM Help**
       1. **Function:** Provides documentation or knowledge base.
       2. **Redirects To:** WebFM Help page.
       3. **Use Case:** Quick reference for users to learn system operations or troubleshoot.

- - **Main Content Area**
    - **Migration & Major Updates Section**
      - Provides system version changes, migration details, and update notes.
      - Useful for admins to know about environment changes (e.g., IBM Cloud AppID authentication, GitHub repository integration).
    - **Footer Links**
    - **Terms of Use & Privacy Policy** → Redirects to IBM policy documents.
    - **Screen: User Manager**

![Picture3](https://20462040.fs1.hubspotusercontent-na1.net/hubfs/20462040/knowledge-base-files/webfm/How%20to%20guides/WebUI/Picture3.png)

- - - **Purpose:**  
      The User Manager screen provides an overview of all users registered in WebFM. It allows admins to **search, review, and export** user account information.

- - - **Elements** 
      - **Table Columns:**
      - **Email Address (Column)**
      - **Function:** Lists the email addresses of all registered users.
      - **Use Case:** Primary identifier for each user.
    - **Display Name (Column)**
      - **Function:** Shows the full name or preferred display name.
      - **Use Case:** Helps recognize users without relying only on email.
    - **Created By (Column)**
      - **Function:** Indicates the entity/system that created the user. In this case, most are created by *WebFM*.
      - **Use Case:** Tracks origin of account creation.
    - **Search Bar:**
      - **Location:** Top right of the User Manager box.
      - **Function:** Allows filtering of the user list by email or display name.
      - **Redirects To:** Filtered view of the table (dynamic, instant).
      - **Use Case:** Quickly find a user among hundreds of records.

- - - **Export to Excel (Button):**
      - **Location:** Bottom left, beside “Showing 1 to 10 of 330 entries.”
      - **Function:** Exports the entire user list (all pages) into an Excel file.
      - **Use Case:**
      - Backup user information.
      - Share with other admins or external stakeholders.
      - Perform offline analysis.

- - - **Pagination Controls:**
      - **Location:** Bottom right (Previous / 1 / 2 / 3 … Next).
      - **Function:** Navigate through user records.
      - **Use Case:** View all registered users across multiple pages (in this screenshot, 330 entries spread across 33 pages).

- - - **Example Use Case Flow:**

1. 1. 1. 1. Admin needs to find **“Michael Darden.”**
            1. Enters *“Darden”* in the **Search Bar**.
            2. User entry appears immediately.
         2. Admin needs a full report of users.
            1. Clicks **Excel Export**.
            2. Downloads an .xlsx file with all users.
            3. Admin reviews users by paging through using **Next/Previous** buttons.

- #### **Projects Tab**

  ![Picture4](https://20462040.fs1.hubspotusercontent-na1.net/hubfs/20462040/knowledge-base-files/webfm/How%20to%20guides/WebUI/Picture4.png)

- - **Create New Project Button**
    - Function: Start new project setup.
    - Redirects: Project Setup Screen.
    - Info: Project name, due date, language pair.
    - Use Case: Initialize client jobs.
  - **Project List Table**
    - Columns: Project ID, Name, Status, Owner, Due Date.
    - Function: Display/manage active projects.
    - Redirects: Clicking row → Project Details Screen.
    - Use Case: Track project lifecycle.
  - **Search/Filter Bar**
    - Function: Search by project name, status, or owner.
    - Redirects: Inline filter.
    - Info: Keyword text input.
    - Use Case: Narrow view to relevant jobs.
  - **Project Actions (per row)**
    - **Edit** → Project Setup Screen (edit mode).
    - **Archive** → Confirmation popup, moves to archived list.
    - **Delete** → Permanent removal confirmation popup.
    - Use Case: Manage individual projects.
  - **Screen: Project Manager**
    - **Purpose:**  
      The Project Manager screen is used to create, view, update, and delete projects within WebFM. It serves as the central hub for managing project metadata and ownership.

- - **Elements** 
    - **Top Menu:**
    - **Add New Project (Button)**
    - **Function:** Opens a form to create a new project.
    - **Redirects To:** *New Project Creation Screen*.
    - **Information Required:**
      - Project Name
      - Project Description
      - Contact Person
      - (Optional) Associated project configurations
      - **Use Case:** Create new project environments for labs or clients.
    - **Show Entries Dropdown**
      - **Function:** Sets the number of projects displayed in the table at once (e.g., 10, 25, 50).
      - **Redirects To:** Refreshes the current Project Manager table.
      - **Use Case:** Useful when managing a large number of projects.
    - **Search Bar**
      - **Function:** Filters the project list by project name, description, or contact person.
    - **Redirects To:** Dynamic filter applied on the table below.
    - **Use Case:** Quickly locate a project when many exist.

- - **Project Table Columns:**
  - **Project Name (Clickable Link)**
    - **Function:** Opens the selected project dashboard.
    - **Redirects To:** *Project Overview screen*.
    - **Use Case:** Access detailed project management tools.
  - **Project Desc**
    - **Function:** Displays the project description (user-defined at creation).
    - **Use Case:** Quick identification of project scope/purpose.
  - **Contact Person**
    - **Function:** Displays the project’s assigned owner or responsible user.
    - **Use Case:** Helps in escalation or reaching the right project focal.
  - **Action Buttons (per row):**
  - **Edit (Button)**
    - **Function:** Opens the edit project form.
    - **Redirects To:** *Edit Project screen*.
    - **Information Editable:**
      - Project name
      - Description
      - Contact details
    - **Use Case:** Update project details if scope, ownership, or naming changes.
  - **Delete (Button)**
    - **Function:** Deletes the project entry after confirmation.
    - **Redirects To:** *Confirmation dialog*.
    - **Use Case:** Remove inactive, obsolete, or test projects.
    - ⚠️ **Caution:** This action is irreversible.

- - **Pagination Controls:**
  - **Previous / Next Buttons + Page Number**
    - **Function:** Navigate between pages of projects if there are more entries than can be shown.
    - **Use Case:** Required when managing multiple labs/projects.

- - **Example Use Case Flow:**

1. 1. 1. A new lab requires onboarding. Admin clicks **“Add New Project”**.
      2. Enters project details → saves.
      3. Project appears in the table → assigned to contact person (e.g., Yzsa Soriano).
      4. If changes are needed, admin clicks **Edit**.
      5. If project is deprecated, admin clicks **Delete** to remove.

- #### **Files Tab**

  - **Upload File Button**

- - - Function: Add new source file.
    - Redirects: Upload Modal.
    - Info: File path, target languages.
    - Use Case: Provide content for translation.
  - **File List Table**
    - Columns: File Name, Size, Version, Project Link, Status.
    - Function: Repository of uploaded files.
    - Redirects: Clicking file → File Details Screen.
    - Use Case: File management.
  - **Per-file Actions**
    - **Download** → Starts local download.
    - **Preview** → Opens inline preview.
    - **Delete** → Removes file after confirmation.
    - **Replace/Version Upload** → Opens file replace modal.
    - Use Case: Lifecycle management of translation files.

![Picture5](https://20462040.fs1.hubspotusercontent-na1.net/hubfs/20462040/knowledge-base-files/webfm/How%20to%20guides/WebUI/Picture5.png)

- - **Screen: Stop File Processing**
    - **Purpose:**  
      This screen allows administrators to **terminate all background file processing activities** for a specific user. It acts as a safeguard to prevent system overload, unintended uploads, or incorrect job executions.

- - **Elements**

- - **Warning Message**
    - **Text:** *“You are about to stop all background file processing for this user.”*
    - **Function:** Alerts the admin about the impact of the action.
    - **Use Case:** Ensures the admin is aware before stopping potentially critical file operations.

- - **Buttons**
    - **Continue (Button)**
      - **Location:** Center, below the warning message (left side).
      - **Function:** Confirms the action. Immediately halts **all active and pending background file processing tasks** for the selected user.
      - **Redirects To:** A confirmation page or system log update showing that processing has been stopped.
      - **Use Case:**
        - Stop incorrect or corrupted file processes.
        - Free up system resources.
        - Prevent duplicate or erroneous processing.
    - **Cancel (Button)**
      - **Location:** Next to the Continue button (right side).
      - **Function:** Aborts the stop request. No background processes are affected.
      - **Redirects To:** Returns the admin to the **previous page** (usually the main Maintenance menu or dashboard).
      - **Use Case:**
        - When the admin clicks by mistake.
        - When further verification is needed before stopping processes.

- - **Example Use Case Flow:**

1. 1. 1. Admin notices a user’s files are stuck in a **processing loop.**
      2. Admin navigates to **Stop File Processing.**
      3. Admin clicks **Continue** to halt all pending file tasks.
      4. System logs the stop action, and the admin can re-trigger or reassign the processing later.

- **Users Tab**
  - **Add User Button**

- - - Function: Register new user.
    - Redirects: User Registration Screen.
    - Info: Name, Email, Role, Permissions.
    - Use Case: Onboard staff or partners.
  - **User List Table**
    - Columns: Name, Email, Role, Status, Last Login.
    - Function: Overview of all users.
    - Redirects: Clicking row → User Profile Screen.
    - Use Case: Track and manage accounts.
  - **Actions (per user)**
    - **Edit Profile** → User Profile Screen.
    - **Assign Role Dropdown** → Admin, Project Manager, Translator, Viewer.
    - **Deactivate User** → Confirmation modal.
    - Use Case: Access control and administration.

- **Settings Tab**

- - **API Keys Section**
    - Buttons:
      - **Generate New Key** → Creates new API key.
      - **Revoke Key** → Removes API key.
    - Redirects: Key Management Screen.
    - Use Case: For Jenkins, GitHub, COS integrations.
  - **Integrations Section**
    - Options: GitHub | Jenkins | CloudantDB | COS.
    - Function: Manage third-party integrations.
    - Redirects: Integration Setup Screens.
    - Info: API tokens, credentials.
    - Use Case: Automation pipelines.
  - **Preferences Section**
    - Buttons/fields: Timezone Dropdown, Language Dropdown, Notification Toggles.
    - Redirects: Saves to user profile.
    - Use Case: Personalize WebFM experience.

- - **Reports Tab**
  - **Generate Report Button**
    - Function: Build custom report.
    - Redirects: Report Setup Modal.
    - Info: Date range, filters (user/project).
    - Use Case: Analytics, billing, performance.
  - **Report History Table**
    - Function: Shows past reports.
    - Redirects: Clicking → Report Detail View.
    - Use Case: Reuse or review historical data.
  - **Export Options**
    - Buttons: CSV | XLSX | PDF.
    - Function: Download reports in multiple formats.
    - Use Case: Share with stakeholders.

- **Help Tab**
  - **Knowledge Base Link**

- - - Function: Opens KB in new tab.
    - Use Case: Access training docs.
  - **Contact Support Button**
    - Function: Submit a support request.
    - Redirects: Support Form Screen.
    - Info: Subject, description, file attachments.
    - Use Case: Raise issues or bugs.
  - **System Status Link**
    - Function: View system uptime/maintenance.
    - Redirects: Status page.
    - Use Case: Troubleshoot outages.
