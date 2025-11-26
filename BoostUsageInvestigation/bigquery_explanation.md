# BigQuery Analysis: Finding GitHub Projects Using Boost

## Overview
This guide explains how to use Google BigQuery to find all GitHub projects using the C++ Boost library. The analysis returns file information, full source code content, and latest commit metadata.

---

## 1. Dataset Overview

Google BigQuery hosts a public dataset containing snapshots of GitHub repositories.

### Key Tables
- **`contents`**: File contents
- **`files`**: File metadata (paths, refs, modes) - links to `contents` via `id`
- **`commits`**: Commit history - `repo_name` is an array
- **Sample tables**: `sample_contents`, `sample_files`, `sample_commits` for testing

### Scripts
- **`find_boost_repos.sql`**: Production query - scans 2.95 TiB, returns all matching files with content and commit info
- **`list_github_repos_schema.sql`**: Schema explorer - lists all tables and columns

---

## 2. How to Use

### Step 1: Set Up
1. Create Google Cloud account at [cloud.google.com](https://cloud.google.com)
2. Enable billing
3. Open [BigQuery Console](https://console.cloud.google.com/bigquery)

### Step 2: Run Query
1. Open `find_boost_repos.sql`
2. Copy and paste into BigQuery Console
3. Check "Bytes processed" estimate (2.95 TiB)
4. Click "Run"
5. Wait 1-2 minutes for results

### Step 3: Export Results
**For large results (millions of rows)**:
1. Export table to Cloud Storage for download
2. Click "Save results" → "BigQuery table"

**For small results**:
1. Click "Save results" → "CSV"
---

## 3. What the Query Does

The query has two main parts:

1. **Finds C++ files with Boost includes**:
   - Joins `contents` and `files` tables
   - Filters to C/C++ text files (`.cpp`, `.cxx`, `.cc`, `.hpp`, `.hxx`, `.hh`, `.c`, `.h`)
   - Decodes base64 content if needed
   - Searches for `#include <boost/` patterns

2. **Retrieves latest commit info**:
   - Scans `commits` table
   - Unnests `repo_name` array and groups by repository
   - Returns latest commit metadata per repo

### Returns
- **File info**: `repo_name`, `ref`, `path`, `mode`, `id`, `symlink_target`, `file_size_bytes`
- **File content**: Full source code (`file_content`)
- **Commit info**: `last_commit_ts`, `commit_sha`, `tree_sha`, `parent_commits`, `author_info`, `committer_info`, `subject`, `message`

---

## 4. Additional Resources

- **Schema**: Run `list_github_repos_schema.sql` to see all columns

---
