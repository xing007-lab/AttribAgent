import pandas as pd

def align_datasets(df1, df2, key="security"):

    merged = pd.merge(
        df1,
        df2,
        on=key,
        how="outer",
        suffixes=("_t1", "_t2")
    )

    merged = merged.fillna(0)

    df1_aligned = merged.filter(regex="_t1$")
    df2_aligned = merged.filter(regex="_t2$")

    df1_aligned.columns = [c.replace("_t1", "") for c in df1_aligned.columns]
    df2_aligned.columns = [c.replace("_t2", "") for c in df2_aligned.columns]

    return df1_aligned, df2_aligned
