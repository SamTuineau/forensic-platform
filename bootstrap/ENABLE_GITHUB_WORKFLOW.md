GITHUB WORKFLOW INITIALIZATION

Extend the forensic-platform repository with commit governance.

--------------------------------------------------
STEP 1 - CREATE GITHUB DIRECTORY
--------------------------------------------------

Create directory:

.github/workflows

--------------------------------------------------
STEP 2 - ADD BASIC CI VALIDATION
--------------------------------------------------

Create file:

.github/workflows/ci.yml

Content:

name: Platform Validation

on:
  push:
    branches: [ main ]
  pull_request:

jobs:
  validate:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - name: Validate docker compose
        run: docker compose config

--------------------------------------------------
STEP 3 - COMMIT MESSAGE STANDARD
--------------------------------------------------

Create file:

docs/COMMIT_STANDARD.md

Content:

Commit Format:

<phase>: <short description>

Examples:

phase1: add ingestion scanner
phase3: implement sql extractor
infra: docker compose improvements

Rules:
- Must reference PROJECT_TODO item
- Keep under 72 characters
- One logical change per commit

--------------------------------------------------
STEP 4 - TODO LINKING RULE
--------------------------------------------------

Append to PROJECT_TODO.md:

When completing a task:

1. Implement feature
2. Commit code
3. Update checkbox with date and commit id

Example:

- [x] Implement directory scanner (2026-02-25 commit 4f2c1a)

--------------------------------------------------
STEP 5 - SUCCESS CONDITION
--------------------------------------------------

Repository now enforces:

- commits tracked
- docker config validated in CI
- TODO linked to commits
