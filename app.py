# app.py
import os

import pandas as pd
import streamlit as st

from agent.agentclient import KPIAttributionAgent

# ----------------------------
# OpenAI key handling
# ----------------------------
api_key = os.environ.get("OPENAI_API_KEY")

if api_key:
    import openai

    openai.api_key = api_key
    ONLINE_MODE = True
else:
    ONLINE_MODE = False
    st.info("⚠️ OpenAI key not found. Running in offline mode.")

# ----------------------------
# Streamlit UI
# ----------------------------
st.title("Self-Building KPI Attribution Agent")

# Upload Excel files
t1_file = st.file_uploader("Upload T1 Excel file", type=["xlsx"])
t2_file = st.file_uploader("Upload T2 Excel file", type=["xlsx"])

formula = st.text_input("Enter KPI formula (e.g., SUM(weight * return))", "")

if st.button("Run Attribution"):
    if not t1_file or not t2_file or not formula:
        st.error("Please upload both Excel files and enter a formula.")
    else:
        # Read Excel files
        df_t1 = pd.read_excel(t1_file)
        df_t2 = pd.read_excel(t2_file)

        # Run agent
        try:
            result = KPIAttributionAgent().run(
                df_t1, df_t2, formula, online_mode=ONLINE_MODE
            )
        except Exception as e:
            st.error(f"Error: {e}")
        else:
            st.subheader("KPI Results")
            st.write(f"KPI T1: {result['kpi_t1']}")
            st.write(f"KPI T2: {result['kpi_t2']}")
            st.write(f"Change: {result['change']}")

            st.subheader("Driver Contributions")
            st.write(result["drivers"])

            st.subheader("Explanation")
            st.code(result["explanation"])
