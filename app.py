import streamlit as st
from agent import KPIAttributionAgent

st.title("Universal KPI Attribution Agent")

file1 = st.file_uploader("Upload T1 dataset")
file2 = st.file_uploader("Upload T2 dataset")

formula = st.text_input(
    "KPI Formula",
    "SUM(weight * return)"
)

if st.button("Run Attribution"):

    agent = KPIAttributionAgent()

    result = agent.run(file1, file2, formula)

    st.subheader("KPI Results")

    st.write("T1:", result["kpi_t1"])
    st.write("T2:", result["kpi_t2"])
    st.write("Change:", result["change"])

    st.subheader("Drivers")

    st.write(result["drivers"])

    st.subheader("Explanation")

    st.write(result["explanation"])

    st.subheader("Generated KPI Code")

    st.code(result["generated_code"])