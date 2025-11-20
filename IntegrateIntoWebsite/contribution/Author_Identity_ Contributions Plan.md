## Author Identity & Contributions Plan

Part 1 – Author grouping errors and email verification plan

1. Current state: the admin action `merge_authors` (libraries/admin.py ~131-140) calls `CommitAuthor.merge_author` (libraries/models.py ~80-96). That method rewrites `Commit`, `CommitAuthorEmail`, and `EmailData` records and deletes the secondary author. There is no verification gate, so a single mistake permanently merges unrelated contributors.

2. Why email verification is not the final answer:

    - Requiring legacy contributors to prove email ownership is unrealistic. People lose access to old mailboxes or switch providers, so their data would remain fragmented forever.
    - Many commits arrive through GitHub no-reply addresses such as `*@users.noreply.github.com`. Those aliases cannot be verified, yet they represent real work. Blocking them would split history for entire projects.
    - Merges are irreversible. Even with verification, an error would still rewrite commit history and there is no undo path.
      Given these constraints, the safer approach is to leave commit authors untouched and use a reversible grouping layer.

3. Plan:
    - Create an `Identity` table that represents the human contributor (display name, description, `needs_review`, timestamps). `CommitAuthor` rows will point to an identity instead of another author.
    - Create an `EmailIdentityRelation` table with (`email`, `identity`, `created_at`). This keeps a reversible history of which addresses belong to which person. Adding or removing rows never touches commit history.
    - Add a dedicated `Email` table so each address is stored once and linked to multiple identities. Admins regroup authors by moving the identity pointer, which keeps merges reversible and eliminates the need for strict email verification.
    - Implement AI-driven identity suggestions, but require human approval through the admin UI to ensure accuracy before groups affect reporting.

Part 2 – Contribution coverage gap

1. The current project stores only top-level `Issue` and `PullRequest` metadata (title, number, state, timestamps, GitHub ID, JSON blob). It never imports PR review events or issue comments, so we cannot credit reviewers or discussants.

2. We will build a contribution log (single table) that records every GitHub contribution type in one place. Each record will include:

    - Email FK to the claimed contributor (once the grouping layer links authors to real accounts).
    - `type` field capturing every GitHub activity we care about: `commit`, `pr-create`, `pr-review`, `pr-approve`, `pr-merge`, `pr-close`, `issue-create`, `issue-comment`, `issue-close`.
    - `date`, `repo`, `info` (PR or issue number or commit hash), and a `comment` with title and body text.
    - Indexes on email, date, type, and repo so reports and admin filters stay fast.

3. Import tasks will read GitHub review/comment feeds and upsert these contribution rows. Because commits remain untouched under the new grouping approach, staff can reassign an identity group without rewriting historical contribution data.
