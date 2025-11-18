# BigQuery One-Time Analysis: Finding GitHub Projects Using Boost

## Overview
This guide explains how to use Google BigQuery for a one-time analysis to find all GitHub projects using the C++ Boost library.

---

## 1. BigQuery GitHub Dataset and Scanned Data

### What is the GitHub Dataset?
Google BigQuery hosts a **public dataset** containing snapshots of GitHub repositories.

### Key Table: `bigquery-public-data.github_repos.contents`
- Stores file contents from GitHub repositories
- **Total size**: ~3.5-4 TiB (all languages)
- **C++ files**: ~1-1.4 TiB

### Important Columns
- `repo_name`: Repository name (e.g., `owner/repo-name`)
- `path`: File path (e.g., `src/main.cpp`)
- `content`: File content (base64-encoded)
- `mime_type`: File type (e.g., `text/x-c++`)

### Storage vs. Scanned Data

**Storage (What's Stored)**
- **Total dataset**: ~4 TiB

**Scanned Data (What You Process)**
- **What BigQuery reads** when running your query
- **Cost**: Based on bytes scanned, not stored
- **Free tier**: First 1 TiB/month is free

### Why It Matters
BigQuery charges for **data scanned**, not data returned. Even if your query returns 10 results, you pay for all data processed.

---

## 2. One-Time Analysis Process

### Step 1: Set Up Google Cloud Account
1. Go to [cloud.google.com](https://cloud.google.com)
2. Create account and enable billing
3. Navigate to [BigQuery Console](https://console.cloud.google.com/bigquery)

### Step 2: Run Full Query
Use this query to find all GitHub repos using C++ Boost library:

```sql
-- Find all GitHub repos using C++ Boost library
WITH cpp_files AS (
  SELECT repo_name, content
  FROM `bigquery-public-data.github_repos.contents`
  WHERE mime_type IN (
    'text/x-c++', 'text/x-c++src', 'text/x-c++hdr',
    'text/x-c', 'text/x-csrc', 'text/x-chdr'
  )
  AND REGEXP_CONTAINS(path, r'\.(cpp|cxx|cc|hpp|hxx|hh|c|h)$')
)
SELECT DISTINCT repo_name
FROM cpp_files
WHERE REGEXP_CONTAINS(
  FROM_BASE64(content),
  r'(?i)#include\s*<boost/'
)
ORDER BY repo_name;
```

**How to run**:
1. Click "Compose New Query" in BigQuery Console
2. Paste the query above
3. Check "Bytes processed" estimate (will show ~1-1.4 TiB for C++ files)
4. Click "Run"
5. Wait 5-15 minutes for results

### Step 3: Export Results
1. Click "Save results"
2. Choose **CSV** format
3. Download the complete list

---

## 3. Cost for One-Time Analysis

| Item | Amount | Cost |
|------|--------|------|
| Free tier | 1 TiB | $0 |
| Data scanned (C++ files) | ~1-1.4 TiB | - |
| Overage (if > 1 TiB) | ~0-0.4 TiB | $0-2.50 |
| Storage | 0 | $0 (public dataset) |
| **Total** | | **$0-2.50** |

**Note**: 
- First 1 TiB/month is free per billing account
- C++ files total ~1-1.4 TiB, so you may need to pay for ~0.4 TiB overage
- Cost: 0.4 TiB × $6.25/TiB = **$2.50 maximum**
- **$5 budget is sufficient** for this one-time analysis
