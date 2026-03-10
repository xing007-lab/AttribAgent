import pytest
from agent_offline import SelfBuildingKPIOfflineAgent

T1_FILE = "portfolio_t1.xlsx"
T2_FILE = "portfolio_t2.xlsx"

def test_shapley_sum_equals_change():
    agent = SelfBuildingKPIOfflineAgent()
    formula = "SUM(weight * return)"
    result = agent.run(T1_FILE, T2_FILE, formula)

    total_contrib = sum(result["drivers"].values())
    # Shapley contributions should sum to total KPI change
    assert abs(total_contrib - result["change"]) < 1e-6