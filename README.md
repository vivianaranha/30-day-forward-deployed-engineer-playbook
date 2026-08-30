# 30-Day Forward Deployed Engineer Playbook

A hands-on, customer-facing engineering repository for learning how to operate like a **Forward Deployed Engineer (FDE)**.

> Discover → Define → Design → Build → Integrate → Deploy → Observe → Measure → Improve → Enable

The emphasis is not only on code. It is on solving ambiguous customer problems, building the simplest useful solution, integrating with real systems, measuring business impact, and helping the customer own what you build.

## 30-Day Learning Path

### Week 1 — Discover and Define
1. What Is Forward Deployed Engineering?
2. Customer Discovery
3. Business Problem Framing
4. Users and Workflow Mapping
5. Requirements Engineering
6. Constraints, Risks, and Assumptions
7. Success Metrics and Engagement Brief

### Week 2 — Design and Prototype
8. Architecture Thinking
9. Simplest Architecture That Can Prove Value
10. Data Discovery and Data Contracts
11. Build the FastAPI Backend
12. Build Business Logic
13. Add AI Intelligence
14. Build the Customer-Facing Prototype

### Week 3 — Integrate and Deliver
15. API Integration
16. Enterprise Systems and Tool Abstraction
17. Authentication and Authorization Concepts
18. Failure Handling
19. Testing and Edge Cases
20. Deployment Readiness
21. End-to-End Customer Demo

### Week 4 — Operate, Measure, and Scale
22. Observability
23. Reliability and Production Hardening
24. User Acceptance Testing
25. Business Value and ROI
26. Customer Feedback and Iteration
27. Executive Communication
28. Handoff and Customer Enablement
29. Scale and Reuse
30. Capstone: Complete FDE Engagement

## Capstone Scenario

You are the FDE for **Northstar Support Services**. The VP of Support says:

> “Our support team spends too much time manually reading, classifying, prioritizing, and routing incoming tickets.”

Your job is to discover the real problem, define success, design the simplest useful solution, build it, integrate it, deploy it, measure it, and leave the customer able to own it.

## Quick Start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python scripts/seed_data.py
uvicorn backend.app.main:app --reload
```

In another terminal:

```bash
streamlit run frontend/app.py
```

Run tests:

```bash
pytest -q
```

## Repository Structure

```text
30-day-forward-deployed-engineer-playbook/
├── days/
├── discovery/
├── architecture/
├── backend/
├── frontend/
├── integrations/
├── data/
├── docs/
├── engagement/
├── metrics/
├── scripts/
├── tests/
└── templates/
```

## FDE Principle

The goal isn't to build impressive technology. The goal is to use technology to create a measurable customer outcome.

## License
MIT
