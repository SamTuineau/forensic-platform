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