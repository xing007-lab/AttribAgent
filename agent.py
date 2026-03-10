import numpy as np
import pandas as pd

from attribution import shapley_attribution
from explanation import generate_explanation
from formula_parser import parse_formula
from utils import align_datasets


class KPIAttributionAgent:

    def run(self, file_t1, file_t2, formula, online_mode=True):

        df1 = pd.read_excel(file_t1)
        df2 = pd.read_excel(file_t2)

        df1, df2 = align_datasets(df1, df2)

        numeric_cols = df1.select_dtypes(include=np.number).columns.tolist()

        kpi_fn, code = parse_formula(formula, numeric_cols)

        kpi_t1 = kpi_fn(df1)
        kpi_t2 = kpi_fn(df2)

        change = kpi_t2 - kpi_t1

        drivers = shapley_attribution(kpi_fn, df1, df2, numeric_cols)

        if online_mode:
            explanation = generate_explanation(change, drivers)
        else:
            explanation = None

        return {
            "kpi_t1": kpi_t1,
            "kpi_t2": kpi_t2,
            "change": change,
            "drivers": drivers,
            "explanation": explanation,
            "generated_code": code,
        }
