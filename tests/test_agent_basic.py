import pytest
from agent import KPIAttributionAgent

T1_FILE = "portfolio_t1.xlsx"
T2_FILE = "portfolio_t2.xlsx"


@pytest.mark.parametrize("formula", [
    "SUM(weight * return)",
])
def test_kpi_computation(formula):
    agent = KPIAttributionAgent()
    result = agent.run(T1_FILE, T2_FILE, formula)

    # KPI values are numeric
    assert isinstance(result["kpi_t1"], (int, float))
    assert isinstance(result["kpi_t2"], (int, float))

    # Change equals T2 - T1
    assert abs(result["change"] - (result["kpi_t2"] - result["kpi_t1"])) < 1e-8

    # Drivers are numeric
    for v in result["drivers"].values():
        assert isinstance(v, (int, float))

    # Explanation contains "drivers"
    assert "drivers" in result["explanation"].lower()
    