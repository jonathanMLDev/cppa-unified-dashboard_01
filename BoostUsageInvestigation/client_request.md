# Request: Google Cloud Account Setup for Boost Library Investigation

## Overview
We need to investigate all GitHub projects using the C++ Boost library. This requires access to Google BigQuery, which hosts the public GitHub dataset.

## Action Required
Please create a new Google Cloud account and enable billing for this project.

## Steps to Complete

### 1. Create Google Cloud Account
- Go to [cloud.google.com](https://cloud.google.com)
- Sign up for a free Google Cloud Platform (GCP) account
- No credit card required for account creation

### 2. Enable BigQuery
- Navigate to [BigQuery Console](https://console.cloud.google.com/bigquery)
- Enable the BigQuery API if prompted

### 3. Set Up Billing
- Link a payment method (credit card) to your billing account
- **Budget Recommendation**: $5 is sufficient for this one-time investigation
- The first 1 TiB of query processing per month is **free**
- Expected cost for this work: **$0-2.50** (well within the $5 budget)

## Why This Is Needed
- Google BigQuery provides access to the complete GitHub public dataset
- This allows us to efficiently search millions of repositories for Boost library usage
- The analysis will identify all C++ projects using Boost across GitHub

## Cost Breakdown
- **Free Tier**: First 1 TiB/month of query processing is free per billing account
- **Estimated Scan Size**: ~1-1.4 TiB (C++ files in GitHub dataset)
- **Overage**: ~0-0.4 TiB (if scan exceeds 1 TiB free tier)
- **Expected Cost**: $0-2.50
  - If scan is ≤ 1 TiB: $0 (covered by free tier)
  - If scan is 1.4 TiB: 0.4 TiB × $6.25/TiB = $2.50
- **Maximum Cost**: $2.50
- **Budget Set**: $5 (provides safety margin)

## Timeline
Once the account is set up and billing is enabled, we can proceed immediately with the investigation.


---

**Note**: This is a one-time analysis. No ongoing subscription or commitment required.

