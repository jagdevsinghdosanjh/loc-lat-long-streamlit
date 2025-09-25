# 📍 Location Lookup Dashboard

A modular Streamlit app for batch geocoding, export history, and classroom overlays. Built for educators, coordinators, and hackathon contributors.

## 🔧 Features

- Single & batch location lookup
- Role-based access (Coordinator / Student)
- Export to CSV and Excel
- Map overlays and contributor diagnostics
- Honor-driven login system

## 🚀 Setup

```bash
git clone https://github.com/jagdevsinghdosanjh/loc-lat-long-streamlit.git
cd loc-lat-long-streamlit
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
streamlit run app.py

🧠 Roles
coordinator → full access

student → limited export and diagnostics

📁 File Structure
Code
├── app.py
├── auth/
│   ├── login.py
│   └── roles.py
├── pages/
│   ├── 1_Single_Lookup.py
│   ├── 2_Batch_Lookup.py
│   └── 3_Export_History.py
├── utils/
│   ├── geocode.py
│   └── export.py
💡 Inspired by
Hack at Honor · Punjab Green Hackathon · Modular classroom tools

## ⚙️ 3. GitHub Actions (Optional)

Create `.github/workflows/deploy.yml` for auto-linting or deployment:

```yaml
name: Streamlit Deploy

on:
  push:
    branches: [ main ]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
      - name: Run Streamlit app (optional)
        run: streamlit run app.py