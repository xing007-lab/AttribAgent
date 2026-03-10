import pytest
import pandas as pd
from agent import KPIAttributionAgent


def test_empty_dataset(tmp_path):
    # Create empty datasets
    df_empty = pd.DataFrame(columns=["weight", "return"])
    t1 = tmp_path / "t1.xlsx"
    t2 = tmp_path / "t2.xlsx"
    df_empty.to_excel(t1, index=False)
    df_empty.to_excel(t2, index=False)

    agent = KPIAttributionAgent()
    formula = "SUM(weight * return)"

    result = agent.run(t1, t2, formula)
    assert result["kpi_t1"] == 0
    assert result["kpi_t2"] == 0
    assert result["change"] == 0
    assert result["drivers"] == {}


def test_missing_columns(tmp_path):
    # Dataset missing 'return' column
    df_t1 = pd.DataFrame({"weight": [0.2, 0.3]})
    df_t2 = pd.DataFrame({"weight": [0.25, 0.35]})
    t1 = tmp_path / "t1.xlsx"
    t2 = tmp_path / "t2.xlsx"
    df_t1.to_excel(t1, index=False)
    df_t2.to_excel(t2, index=False)

    agent = KPIAttributionAgent()
    formula = "SUM(weight * return)"

    with pytest.raises(KeyError):
        agent.run(t1, t2, formula)
