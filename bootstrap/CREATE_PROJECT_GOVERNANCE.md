PROJECT GOVERNANCE INITIALIZATION

You are extending the existing forensic-platform repository.

GOAL
Create a persistent planning and task tracking system inside the repo.
All future development must reference these files.

Do NOT modify existing architecture.

--------------------------------------------------
STEP 1 - CREATE DOCUMENT STRUCTURE
--------------------------------------------------

Create directory:

docs/ADR

Create files:

docs/PROJECT_PLAN.md
docs/PROJECT_TODO.md

--------------------------------------------------
STEP 2 - CREATE MASTER PROJECT PLAN
--------------------------------------------------

Create docs/PROJECT_PLAN.md with the following content.

TITLE: Forensic Platform Execution Plan

MISSION
Build a forensic environment modelling platform capable of reconstructing
how a server operates using directory evidence.

PHASES

Phase 0 - Platform Foundation
Environment setup
Container runtime validation
Architecture governance

Phase 1 - Ingestion Engine
Directory scanning
File hashing
Manifest generation
Evidence storage

Phase 2 - Evidence Model
Fact schema
Provenance tracking
Confidence scoring

Phase 3 - Extractor Framework
Plugin architecture
Config extractor
Scheduler extractor
SQL extractor

Phase 4 - Graph Construction
Entity normalization
Relationship modelling
External system stubs

Phase 5 - Visual Explorer
Graph visualization
Evidence panel
Search and filtering

Phase 6 - Sensitivity and Safety
Secret detection
Redaction engine
Sensitive mode

Phase 7 - Inference Engine
Rule-based inference
Optional local LLM enrichment

Phase 8 - Runtime Overlay
Log ingestion
Runtime vs config comparison

Phase 9 - Case Bundles
Portable investigation snapshots
Diff and timeline analysis

RULES

Every feature must:
- map to a phase
- align with SYSTEM_SPEC.md
- update PROJECT_TODO.md

--------------------------------------------------
STEP 3 - CREATE TODO LIST
--------------------------------------------------

Create docs/PROJECT_TODO.md

Content:

# Project TODO

## Phase 0 - Platform Foundation

- [ ] Validate docker runtime stability
- [ ] Add environment validator script
- [ ] Add Makefile commands
- [ ] Confirm cross-platform startup
- [ ] Document developer onboarding

## Phase 1 - Ingestion Engine

- [ ] Create ingestion service module
- [ ] Implement directory scanner
- [ ] Implement SHA256 hashing
- [ ] Create manifest.json output
- [ ] Add ingestion API endpoint
- [ ] Display ingestion status in UI

## Phase 2 - Evidence Model

- [ ] Define Fact schema
- [ ] Add provenance tracking
- [ ] Create evidence database tables
- [ ] Evidence search endpoint

## Phase 3 - Extractor Framework

- [ ] Create extractor base class
- [ ] Plugin loader
- [ ] Config extractor
- [ ] Scheduler extractor
- [ ] SQL extractor

## Phase 4 - Graph Construction

- [ ] Graph schema
- [ ] Node normalization
- [ ] Relationship builder
- [ ] External stub generation

## Phase 5 - Visual Explorer

- [ ] Graph canvas
- [ ] Node expansion
- [ ] Evidence panel
- [ ] Path tracing

## Platform Investigation Items

- [ ] Implement environment validator instead of Docker bootstrap
- [ ] Decide SQLite vs Postgres transition
- [ ] Define graph storage strategy

--------------------------------------------------
STEP 4 - TASK TRACKING MECHANISM
--------------------------------------------------

Add instructions at top of PROJECT_TODO.md:

Tasks are tracked using markdown checkboxes.

When a task is completed:
- change [ ] to [x]
- add date completed
- reference related commit id

Example:
- [x] Implement directory scanner (2026-02-25 commit abc123)

--------------------------------------------------
STEP 5 - AI GOVERNANCE RULE
--------------------------------------------------

Append to SYSTEM_SPEC.md:

DEVELOPMENT GOVERNANCE

All coding agents must:

1. Read SYSTEM_SPEC.md
2. Read PROJECT_PLAN.md
3. Read PROJECT_TODO.md

before implementing changes.

Agents must implement ONLY tasks listed in PROJECT_TODO.md
unless explicitly instructed otherwise.

--------------------------------------------------
STEP 6 - SUCCESS CONDITION
--------------------------------------------------

After creation:

Repository contains:
SYSTEM_SPEC.md
PROJECT_PLAN.md
PROJECT_TODO.md

These documents reference each other and guide development.
