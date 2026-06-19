# Autonomous Directory Canary Trap & Ransomware Mitigation SOAR Architecture

## 🎯 Architectural Integrity Target
Developed as prior-work domain evidence for the IIT Kanpur Bachelor of Cybersecurity (B.Cyber) Selection Panel. This project provides a production-grade blueprint for capturing cryptographic malware activity at execution runtime, bypassing traditional host signature limitations.

## ⚙️ Engineering Execution Map
1. **Canary Trap Daemon (`canary_trap.py`):** Establishes high-value system directories containing simulated infrastructure keys, tracing metadata flags asynchronously to detect modifications.
2. **Analysis Node (`ransom_analyzer.py`):** Operates on low-latency 100ms file-cursor tracking loops, extracting cryptographic signatures (`ENCRYPT_AES_256`) and streaming JSON payloads to automation end-points.
3. **SOAR Logic Hub (n8n Node Javascript):** Executes string manipulation passes to extract target profiles, automatically generating immediate process termination scripts (`pkill`) to stop encryption chains.
