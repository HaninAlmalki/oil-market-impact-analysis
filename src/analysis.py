import pandas as pd
import matplotlib.pyplot as plt
from src.impact_calculator import calculate_impact


def run_analysis(oil, events_list):
    results = []

    for ev in events_list:
        imp = calculate_impact(oil, ev["date"])
        if imp is not None:
            results.append({
                "name": ev["name"],
                "type": ev["type"],
                "supply_impact": ev["supply_impact"],
                "surprise": ev["surprise"],
                "abs_impact": imp
            })

    df = pd.DataFrame(results)

    print("\n" + "="*45)
    print("   OIL MARKET ANALYSIS: SURPRISE & SUPPLY")
    print("="*45)

    if not df.empty:
        print("\n[1] MEAN ABS IMPACT BY SURPRISE")
        print(df.groupby("surprise")["abs_impact"].mean())

        print("\n[2] MEAN ABS IMPACT BY SUPPLY")
        print(df.groupby("supply_impact")["abs_impact"].mean())

        print("\n--- BY TYPE ---")
        print(df.groupby("type")["abs_impact"].mean().sort_values(ascending=False))

        plot_results(df)
    else:
        print("No data processed.")


def plot_results(df):
    fig, ax = plt.subplots(1, 2, figsize=(14, 6))

    df.groupby("surprise")["abs_impact"].mean().plot(
        kind='bar', ax=ax[0], color=['grey', 'darkred']
    )
    ax[0].set_title("Surprise vs. Anticipated")
    ax[0].set_ylabel("Mean Absolute Impact (%)")
    ax[0].set_xticklabels(["Anticipated", "Surprise"], rotation=0)

    df.groupby("supply_impact")["abs_impact"].mean().plot(
        kind='bar', ax=ax[1], color=['lightblue', 'orange']
    )
    ax[1].set_title("Supply vs Sentiment")
    ax[1].set_xticklabels(["Sentiment", "Supply"], rotation=0)

    plt.tight_layout()
    plt.show()
