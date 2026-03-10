from io import BytesIO
import streamlit as st
import pytest
import pandas as pd
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import app  # your Streamlit app filename (app.py)

# Use the offline agent in app.py

T1_FILE = "portfolio_t1.xlsx"
T2_FILE = "portfolio_t2.xlsx"


def create_filelike_from_excel(path):
    """Helper: read Excel and return BytesIO object for Streamlit upload simulation"""
    df = pd.read_excel(path)
    buffer = BytesIO()
    df.to_excel(buffer, index=False)
    buffer.seek(0)
    return buffer


@pytest.mark.parametrize("formula", ["SUM(weight * return)"])
def test_streamlit_ui_runs(formula, monkeypatch):
    # Simulate file upload
    t1_buffer = create_filelike_from_excel(T1_FILE)
    t2_buffer = create_filelike_from_excel(T2_FILE)

    # Monkeypatch st.file_uploader to return our buffers
    monkeypatch.setattr(st, "file_uploader", lambda label, type=None: t1_buffer if "T1" in label else t2_buffer)
    monkeypatch.setattr(st, "text_input", lambda label, value=None: formula)
    monkeypatch.setattr(st, "button", lambda label: True)  # simulate clicking "Run Attribution"

    # Monkeypatch st.write to capture outputs
    outputs = []
    monkeypatch.setattr(st, "write", lambda *args, **kwargs: outputs.append(args))
    monkeypatch.setattr(st, "code", lambda *args, **kwargs: outputs.append(args))

    # Run the app script
    app  # import triggers execution

    # Check that outputs contain KPI values
    flat_outputs = [str(o) for arg in outputs for o in arg]
    assert any("KPI" in s for s in flat_outputs)
    assert any("change" in s.lower() for s in flat_outputs)
    assert any("drivers" in s.lower() for s in flat_outputs)
