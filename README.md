🕵️ OSINT-Scraper

A powerful, modular Python tool for collecting Open Source Intelligence (OSINT) from public web sources including GitHub, LinkedIn (public info only), and Whois records.

> ⚠️ For ethical research and educational purposes only. This tool does not bypass authentication or collect any private or unauthorized data.

---

## 💡 Features

- 🔍 LinkedIn: Extracts public information (headline, location, experiences)
- 🧑‍💻 GitHub: Gathers repos, languages, contribution history
- 🌐 Whois: Fetches domain registration details
- ✅ JSON output & CLI-based operation
- 🧩 Modular scrapers for easy extension

---
## The Scrapers

![image](https://github.com/user-attachments/assets/af002d7d-9637-47d6-ad94-c7f313d92127)

- LinkedIn: linkedin.py
- GitHub: github.py
- WhoIs: whois.py

---

## OSNIT Scraper FlowChart

![image](https://github.com/user-attachments/assets/d76cbb6d-0b8d-4a47-b1b4-10863545cb36)

- Step 1: User runs the tool using a command containing a target & a sources to collect data from.
- Step 2: The tool checks which sources you requested.
- Step 3: Each scraper runs separately.
- Step 4: Results are collected in a Python dictionary.
- Step 5: If you gave an output file name, it saves the result as a JSON file.
- Step 6: Done! You now have structured OSINT data that can be used for reports, visualization, or further analysis.

---
