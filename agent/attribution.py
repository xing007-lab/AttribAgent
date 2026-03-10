import itertools
import math


def shapley_attribution(kpi_fn, df1, df2, variables):

    contributions = {v: 0 for v in variables}
    n = len(variables)

    for var in variables:

        others = [v for v in variables if v != var]

        for r in range(len(others) + 1):

            for subset in itertools.combinations(others, r):

                base = df1.copy()

                for s in subset:
                    base[s] = df2[s]

                kpi_before = kpi_fn(base)

                with_var = base.copy()
                with_var[var] = df2[var]

                kpi_after = kpi_fn(with_var)

                weight = (
                    math.factorial(len(subset))
                    * math.factorial(n - len(subset) - 1)
                    / math.factorial(n)
                )

                contributions[var] += weight * (kpi_after - kpi_before)

    return contributions
