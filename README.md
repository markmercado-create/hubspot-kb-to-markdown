# HubSpot Knowledge Base → Markdown Converter

A lightweight Python CLI tool that converts a **HubSpot Knowledge Base CSV export** into individual, clean **Markdown files** — one `.md` file per article — with full YAML front matter.

## What it does

| Input | Output |
|---|---|
| HubSpot KB CSV export (`*.csv`) | One `.md` file per article |
| Raw HTML article body | Clean Markdown (headings, bold, lists, code blocks, links) |
| All 12 HubSpot export columns | YAML front matter (title, category, language, status, URL, etc.) |

### Example output

```markdown
---
title: "How to Reset Your Password"
knowledge_base: "Help Center"
category: "Account & Security"
subcategory: "Passwords"
language: "en"
status: "published"
source_url: "https://help.example.com/reset-password"
exported_at: "2026-03-17T10:48:26Z"
---

# How to Reset Your Password

1. Click **Forgot Password** on the login page.
2. Enter your email address.
3. Check your inbox for the reset link.
```

---

## Requirements

- Python 3.10 or higher
- pip

---

## Setup

### 1. Clone or download this folder

```bash
git clone https://github.com/YOUR_USERNAME/hubspot-kb-converter.git
cd hubspot-kb-converter
```

Or download and unzip the folder, then open a terminal inside it.

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure (optional)

Copy the example environment file and edit if needed:

```bash
# Windows
copy .env.example .env

# macOS / Linux
cp .env.example .env
```

The defaults (`input/` and `output/` folders) work out of the box — no changes needed unless you want custom paths.

---

## How to export your Knowledge Base from HubSpot

1. Log in to HubSpot
2. Click the **Gear icon** (Settings) in the top navigation
3. In the left sidebar go to **Content → Knowledge Base**
4. Click **Options** (top right)
5. Select **Export Knowledge Base Articles**
6. Choose **CSV** format and click **Export**
7. HubSpot will email you a download link — save the `.csv` file

---

## Usage

### Convert all CSVs in the `input/` folder

```bash
# 1. Drop your exported CSV into the input/ folder
# 2. Run:
python main.py
```

### Convert a specific CSV file

```bash
python main.py --file path/to/your-export.csv
```

### Save output to a custom folder

```bash
python main.py --file path/to/your-export.csv --output path/to/output-folder
```

### See all options

```bash
python main.py --help
```

---

## Project structure

```
hubspot_kb_converter/
├── src/
│   ├── config.py       # All settings (paths, column mappings) — from .env
│   ├── parser.py       # Reads CSV, auto-detects HubSpot column names
│   └── converter.py    # Converts HTML → Markdown, writes .md files
├── input/
│   └── sample_export.csv   # Example CSV to test with
├── output/             # Converted .md files appear here
├── main.py             # CLI entry point
├── requirements.txt    # Python dependencies
├── .env.example        # Environment variable template
└── README.md
```

---

## Supported HubSpot export columns

The tool automatically detects these columns regardless of order:

| HubSpot Column | Front Matter Key |
|---|---|
| Article title | `title` |
| Article body | *(converted to Markdown body)* |
| Knowledge base name | `knowledge_base` |
| Category | `category` |
| Subcategory | `subcategory` |
| Article language | `language` |
| Article subtitle | `subtitle` |
| Keywords | `keywords` |
| Article URL | `source_url` |
| Status | `status` |
| Last modified date | `last_modified` |
| Archived | `archived` |

---

## Configuration (`.env`)

| Variable | Default | Description |
|---|---|---|
| `INPUT_DIR` | `input` | Folder where CSV files are placed |
| `OUTPUT_DIR` | `output` | Folder where `.md` files are written |
| `USE_DATED_SUBFOLDER` | `false` | If `true`, creates a `output/YYYY-MM-DD/` subfolder per run |
| `LOG_LEVEL` | `INFO` | Logging verbosity: `DEBUG`, `INFO`, `WARNING`, `ERROR` |

---

## Troubleshooting

**"No .csv files found in input/"**
→ Make sure you placed your HubSpot export CSV inside the `input/` folder.

**"Could not detect a title or body column"**
→ The CSV may not be a HubSpot KB export. Open it and verify it has `Article title` and `Article body` columns.

**Articles have empty body**
→ Only *published* articles have body content in the HubSpot export. Draft articles export with an empty body — this is a HubSpot limitation.

---

## Dependencies

| Package | Purpose |
|---|---|
| `markdownify` | Converts HTML to Markdown |
| `pandas` | CSV reading and parsing |
| `python-dotenv` | Loads `.env` configuration |
