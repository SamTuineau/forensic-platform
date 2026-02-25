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

Tasks are tracked using markdown checkboxes.

When a task is completed:
- change [ ] to [x]
- add date completed
- reference related commit id

Example:
- [x] Implement directory scanner (2026-02-25 commit abc123)

When completing a task:

1. Implement feature
2. Commit code
3. Update checkbox with date and commit id

Example:

- [x] Implement directory scanner (2026-02-25 commit 4f2c1a)