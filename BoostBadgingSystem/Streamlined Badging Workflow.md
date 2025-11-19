# Boost Badging System – Streamlined Workflow Plan

## Overview

Refined Solana-based badging flow that supports two badge classes:

- **Blockchain-backed badges** – minted to wallets or stored inside the token contract until claimed.
- **Database-only badges** – managed purely inside the application database with no blockchain touchpoints or wallet requirement.

Both classes share the same metadata and notification pipeline. The implementation window is estimated at three weeks.

---

## Workflow Diagram

```mermaid
sequenceDiagram
    autonumber
    participant FE as Frontend
    participant IPFS as IPFS Service
    participant DB as Database
    participant Admin as Admin Wallet
    participant Sol as Token Contract<br/>(with vault functionality)
    participant Mail as Mailing Service
    participant Hook as Admin Webhook
    participant User as User (with email)
    participant Claim as Claim Service
    participant Wallet as User Wallet

    FE->>IPFS: Submit user + badge payload
    IPFS-->>FE: Return URI + CID metadata
    FE->>DB: Persist issuance record (user data, URI, flags)
    alt Blockchain-backed badge
        Admin->>FE: Initiate mint (via frontend with admin wallet)
        FE->>Admin: Request transaction signing (token IDs, URI, wallet)
        Admin->>FE: Sign mint or batch mint transaction
        FE->>Sol: Send mint transaction
        Sol-->>Wallet: Mint badge to user wallet (if provided)
        Sol-->>Sol: Store badge in contract (no wallet address)
        Sol-->>DB: Emit confirmation event (tx signatures)

        Sol-->>Mail: Trigger notification payload (wallet vs stored in contract)
        Mail-->>User: Send email (direct badge info or claim instructions)

        Note over Claim,DB: Claim service queries DB for contract-stored badges<br/>and associated recipient metadata

        User->>FE: Login & view claim notifications
        FE->>Claim: Request pending contract-stored badges
        Claim->>DB: Query pending badge notifications
        Claim-->>FE: Return selectable notifications
        User->>FE: Select badges
        FE->>Claim: Submit claim selection (URI, token ID, wallet) with newly registered wallet address
        Claim->>DB: Update claim intent, log timestamp
        Claim->>Hook: Send claim request payload (URI, token ID, wallet)
        Hook-->>Admin: Notify admin via webhook
        Admin->>FE: Initiate transfer (via frontend with admin wallet)
        FE->>Admin: Request transaction signing (from contract to wallet)
        Admin->>FE: Sign transfer transaction
        FE->>Sol: Send transfer transaction
        Sol-->>Wallet: Deliver claimed badge to user wallet
        Sol-->>DB: Record claim completion (tx signature, wallet)
        Mail-->>User: Send claim confirmation email
    else Database-only badge
        DB->>Mail: Generate database-only badge notification
        Mail-->>User: Send badge email (no wallet required)
        User->>FE: View badge notification history
        Note over DB: Database tracks issuance, views, and acknowledgements<br/>without blockchain transactions
    end

    Note over DB: Maintain full lifecycle history<br/>(metadata hash, issuance, claim selections, completion)
```

---

## End-to-End Workflow

1. **Preparation**  
   - Frontend retrieves token catalogue and recipient roster.  
   - Admin selects badge set (single or batch) and recipients.

2. **Metadata & Persistence**  
   - Frontend submits badge issuance payload to the IPFS service. 
   - IPFS returns content URI plus derived metadata (hash, gateway URL).  
   - Application persists issuance record in the database, including user data, claim eligibility flags, and URI references.

3. **Minting / Issuance**  
   - **Blockchain-backed badges**  
     - Admin initiates mint via frontend with admin wallet. Frontend requests transaction signing from admin.  
     - Admin signs mint or batch mint transaction (supplying recipient wallet if available, token IDs, and metadata URI).  
     - Frontend sends the signed transaction to the token contract.  
     - Token contract (with built-in vault functionality) validates call and mints tokens:
       - **If wallet provided**: Routes tokens directly to user wallets.
       - **If no wallet provided**: Stores tokens in the contract's internal storage (vault functionality).
     - Token contract emits confirmation event with transaction signatures to the database.
     - Post-confirmation hook triggers notification payload to mailing service (indicating whether badge was sent to wallet or stored in contract).
     - Mailing service sends email to user:
       - **Direct wallet recipients** – badge details and blockchain links.
       - **Contract-stored recipients** – claim instructions, emphasizing security posture.
   - **Database-only badges**  
     - Application marks the issuance as "database-only" and stores the badge entirely in the database (no wallet required).  
     - Database generates database-only badge notification and triggers mailing service.
     - Mailing service sends badge email to user (no wallet required).
     - User can view badge notification history in the frontend.
     - Database tracks issuance, views, and acknowledgements without blockchain transactions.

4. **Claim (Blockchain-backed / Contract-Stored Only)**  
   - Claim service queries the database for contract-stored badges and associated recipient metadata.
   - User logs into the frontend and views pending claim notifications.
   - Frontend requests pending contract-stored badges from the claim service.
   - Claim service queries the database for pending badge notifications and returns selectable notifications to the frontend.
   - User selects one or more badges and provides a newly registered wallet address, then submits the claim request.
   - Frontend sends the claim selection (URI, token ID, wallet) to the claim service.
   - Claim service updates the database with claim intent details (URI, token ID, wallet, timestamp).
   - Claim service sends claim request payload (URI, token ID, wallet) to admin webhook.
   - Admin receives webhook notification and logs into the admin frontend.
   - Admin initiates transfer via frontend with admin wallet. Frontend requests transaction signing (from contract to wallet).
   - Admin signs transfer transaction.
   - Frontend sends the signed transfer transaction to the token contract.
   - Token contract delivers the claimed badge to the user wallet.
   - System records claim completion in the database (transaction signature, wallet, timestamp).
   - Mailing service sends claim confirmation email to the claimant.
   - **Database-only badges skip this section entirely** – users already "own" the badge in the portal and can view/download without wallet submission or admin transfer.

5. **Auditing & Reporting**  
   - Database maintains full lifecycle history (metadata hash, issuance, claim selections, completion).
   - Dashboard surfaces mint/claim status, IPFS hashes, and notification delivery logs.  
   - Scheduled jobs reconcile on-chain state with database records.

---


