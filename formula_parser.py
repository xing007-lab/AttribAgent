import sympy as sp

def parse_formula(formula, columns):

    expr = formula

    for col in columns:
        expr = expr.replace(col, f'df["{col}"]')

    expr = expr.replace("SUM(", "(")
    expr = expr.replace(")", ").sum()")

    code = f"""
def KPI(df):
    return {expr}
"""

    local_vars = {}
    exec(code, {}, local_vars)

    return local_vars["KPI"], code