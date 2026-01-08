# Secure Intelligence Synthesis Agent (Ollama-Native)

## Overview
This is a prototype "hands-on builder" project designed to bridge the gap between high-velocity AI synthesis and the strict data-privacy requirements of the intelligence and venture capital sectors. 

By leveraging a local Llama3 instance and a deterministic security layer, this tool enables analytical, executive-style briefings without transmitting sensitive data to the cloud.

## Features
- **Local LLM Execution:** Powered by Ollama (Llama3) for 100% data sovereignty.
- **Deterministic Security Wrapper:** Automated redaction of PII (emails) and restricted internal keywords using Regex.
- **Strategic Briefing Format:** Outputs structured reports optimized for senior executives (Bottom Line Up Front, Capital at Risk, Security Implications).

## Use Cases
- **High-Stakes Geopolitics:** Analyzing sensitive field reports where cloud exposure is a non-starter.
- **Pre-Deal Diligence:** Summarizing internal VC notes on "stealth-mode" startups.
- **Government/Public Service:** Processing data within air-gapped or restricted networks.

## When NOT to use this
- **High-Volume Real-Time Feeds:** Local execution may be slower than scaled cloud clusters.
- **Creative/Nuanced Content:** The model is tuned for analytical output, not creative writing.

## Potential Future Extensions (Roadmap)
1. **RAG Integration:** Connecting the agent to a local database of historical reports.
2. **Hybrid-Cloud Gateway:** Implementing "Differential Privacy" to leverage cloud models for complex tasks while keeping raw data local.
3. **Automated PDF Export:** Adding a library to generate ready-to-send PDF briefings.

## Setup
1. Install [Ollama](https://ollama.com/) and run `ollama pull llama3`.
2. `pip install -r requirements.txt`
3. `python intel_agent.py`