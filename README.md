📊 Self-Building KPI Attribution Agent

Automatically computes KPI changes, performs Shapley attribution, and generates explanations. Works entirely offline — no OpenAI API required.

🚀 Features

Load two Excel portfolio or KPI datasets (T1 and T2)

Parse any KPI formula dynamically

Compute KPI change between T1 and T2

Attribute change using Shapley values

Generate automatic explanations locally

Works for finance, business, operations, or marketing KPIs

Fully offline — no API keys needed

📦 Installation

Clone the repository:

git clone https://github.com/yourusername/self-building-kpi-agent.git
cd self-building-kpi-agent

Create a virtual environment (recommended):

python3 -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows

Install dependencies:

pip install pandas numpy openpyxl

Optional for Streamlit UI: pip install streamlit

📂 Project Structure
self-building-kpi-agent/
│
├─ agent_offline.py       # Main offline agent script
├─ portfolio_t1.xlsx      # Sample T1 dataset
├─ portfolio_t2.xlsx      # Sample T2 dataset
├─ requirements.txt       # Python dependencies
└─ README.md              # Project documentation
📝 Usage (Offline Mode)
python agent_offline.py

Example KPI formula:

SUM(weight * return)

Output:

KPI T1: 0.041
KPI T2: 0.056
Change: 0.015

Driver Contributions:
weight: 0.0082
return: 0.0068

Explanation:
KPI change mainly driven by weight and return contributions.