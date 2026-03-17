---
title: "Full Step-by-Step Process for Setting up File-Access Service"
knowledge_base: "Globalization Help Center"
category: "WebFM"
subcategory: "How to guide"
language: "en"
status: "PUBLISHED"
archived: "false"
last_modified: "1759718439584"
source_url: "https://help.straker.ai/en/g11n/full-step-by-step-process-for-setting-up-file-access-service"
exported_at: "2026-03-17T10:52:05Z"
---

# Full Step-by-Step Process for Setting up File-Access Service

### PART 1: Understand What You’re Working With

##### 1. What is WebFM?

WebFM is Straker’s platform that manages:

- - - Projects
    - Users
    - GitHub repositories
    - File workflows (import/export)
    - Translation processing via GP (Globalization Pipeline)

##### 2. What is File-Access?

File-Access is a service that securely:

- - Connects WebFM to GitHub
  - Fetches files
  - Sends files to GP
  - Pushes translated files back to GitHub

### 

### PART 2: Required Accounts and Tools

Before you begin, ensure you have:

- - A GitHub account with a personal access token
  - AppID credentials (provided by the GTech team)
  - IBM Cloud COS access (credentials: key, secret, endpoint, bucket name)
  - Docker installed (for local use)
  - Access to WebFM Admin and Secret Manager
  - A Bitbucket login (to view deployment scripts)

### PART 3: Deploy File-Access in a Cloud Environment

*Used in production and staging.*

##### Step 1: Prepare Secret Manager

In the Secret Manager, define the following keys:

- - - objectivec
    - CopyEdit
    - CLOUDANT\_URL
    - CLOUDANT\_APIKEY
    - cos\_accessKey
    - cos\_secretKey
    - cos\_endpoint
    - cos\_region
    - cos\_bucketName
    - api\_clientId
    - api\_oauthServerUrl
    - web\_openidConnectClientId
    - web\_clientId
    - web\_clientSecret
    - web\_discoveryEndpointUrl
    - webfm\_aes\_key

##### Step 2: Configure the Deployment

Update the following in your Jenkins job and config files:

- - Jenkinsfile:
    - Secret naming rules
    - configmap/webfm-file-access.yaml:
    - openssl\_certs\_uri for GitHub domain trust
  - Set environment values:
    - SM\_URL, SM\_GP, NAMESPACE, K8S\_CLUSTER\_NAME, APP\_URL\_NAME

##### Step 3: Deploy to Kubernetes

- - Trigger the Jenkins job to deploy File-Access
  - Wait for deployment success message

##### Step 4: Validate Deployment

- - Open Swagger UI: [https://<your-url>/openapi/ui/](https://<your-url>/openapi/ui)
  - Confirm you can authorize using client ID and secret
  - Confirm endpoints are working (test a GET request)

### PART 4: Run File-Access Locally (No CloudantDB)

*Used for testing and development environments.*

##### Step 1: Prepare Credentials

Create git-credentials.json:

json  
CopyEdit  
`{`  
`"gitCredentials": [`  
`{`  
`"gitCredential": {`  
`"email": "your@email.com",`  
`"gitId": "yourgithubid",`  
`"gitToken": "youraccesstoken"`  
`}`  
`}`  
`]`

`}`

##### Step 2: Set Environment Variables

In your terminal or .env file:

`ini`  
`CopyEdit`  
`cos_accessKey=...`  
`cos_secretKey=...`  
`cos_endpoint=...`  
`cos_region=...`  
`cos_bucketName=...`  
  
Get AppID credentials from GTech:  
  
`json`  
`CopyEdit`  
`{`  
`"clientId": "...",`  
`"secret": "...",`  
`"oAuthServerUrl": "..."`  
`}`

##### Step 3: Run the Docker Image

`bash`  
`CopyEdit`  
`docker pull strakerglobal/webfm-file-access`  
`docker run --rm --platform linux/amd64 \`  
`--name webfm-file-access \`  
`-v $(pwd)/git-credentials.json:/usr/src/app/git-credentials.json \`  
`-e cos_accessKey=... \`  
`-e cos_secretKey=... \`  
`-e cos_endpoint=... \`  
`-e cos_region=... \`  
`-e cos_bucketName=... \`  
`-p 9080:9080 \`  
`strakerglobal/webfm-file-access`

##### Step 4: Access Swagger UI

- - Go to: <http://localhost:9080/openapi/ui/>
  - Click "Authorize", enter client ID and secret

### PART 5: Configure WebFM for New Projects

##### **Step 1: Add File-Access Credentials**

- - Login to WebFM Admin
  - Under File-Access Configurations, input:

`json`  
`CopyEdit`  
`{`  
`"email": "your@email.com",`  
`"gitId": "yourgithubid",`  
`"gitToken": "youraccesstoken"`  
`}`

##### Step 2: Create a New Project

- - In WebFM, click **Create Project**
  - Select **LC** as File Provider
    - Note: You can’t change file provider later
  - Add users to the project

##### Step 3: Add Application Configuration

- - Go to **Application Config**
  - Add source and target GitHub repositories
  - Input:
    - GitHub URLs
    - Branches
    - Git credentials
  - Save the application

### PART 6: File Workflow (What Happens After Setup)

Once the project and application are ready, the system performs:

##### 1. Dispatcher Pulls Files

- - WebFM fetches files from the **source GitHub repository**

##### 2. Files Imported to GP

- - Files are sent to IBM’s GP translation platform

##### 3. Translations Are Completed

##### 4. Files Exported from GP

##### 5. Files Pushed to GitHub

- - Exported (translated) files are checked into the **target repository**

### Final Notes and Reminders

- Redeploy File-Access to update tokens if using secret manager
- Local testing disables login but uses mounted credentials
- Coordinate AppID configuration with GTech team
- Test locally before deploying to production
