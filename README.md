<div align="center">

# ⚡ LEAKSCHECK-CLI 
**Advanced OSINT & Dark Web Credential Reconnaissance**

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![API Version](https://img.shields.io/badge/api-v1-fcc139.svg)](https://leakscheck.com/api/docs)
[![License: MIT](https://img.shields.io/badge/License-MIT-10b981.svg)](https://opensource.org/licenses/MIT)

*The official Python terminal interface for the [LeaksCheck Global Situation Room](https://leakscheck.com).*

</div>

---

## 👁️ Overview
Manual OSINT is dead. **LeaksCheck-CLI** allows penetration testers, red teamers, and security analysts to programmatically query over 13+ Million breached records and live Telegram intelligence nodes directly from the command line. 

Submit a target domain or identity, and the engine will automatically aggregate, filter, and return structured credential intelligence in real-time.

## 🚀 Features
- **Dual-Engine Recon:** Instantly queries the high-speed Smack DB while simultaneously allocating asynchronous Celery workers to scrape live Global Telegram nodes.
- **Asynchronous Polling:** Non-blocking architecture. The CLI retrieves partial intelligence instantly and streams the remaining payload as background nodes finish their sweeps.
- **JSON Output:** Ready to be piped into `jq` or integrated into larger automated Red Team pipelines.

---

## ⚙️ Installation

**1. Clone the repository:**
```bash
git clone [https://github.com/yourusername/leakscheck-cli.git](https://github.com/yourusername/leakscheck-cli.git)
cd leakscheck-cli
