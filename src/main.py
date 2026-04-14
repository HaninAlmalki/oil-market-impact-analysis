from src.data_loader import load_oil_data
from src.analysis import run_analysis

events_list = [
     # --- War with Supply Impact ---
    {"date": "2019-09-14", "name": "Abqaiq Attack", "type": "war_supply_impact", "supply_impact": True, "surprise": True},
    {"date": "2022-02-24", "name": "Russia-Ukraine War", "type": "war_supply_impact", "supply_impact": True, "surprise": True},
    {"date": "2018-05-08", "name": "US Exit Iran Deal", "type": "war_supply_impact", "supply_impact": True, "surprise": False},
    {"date": "2024-01-12", "name": "Red Sea Strikes", "type": "war_supply_impact", "supply_impact": True, "surprise": True},
    
    # --- War without direct Supply Impact ---
    {"date": "2016-01-03", "name": "SA-IR Tension", "type": "war_no_supply_impact", "supply_impact": False, "surprise": True},
    {"date": "2019-06-20", "name": "US Drone Down", "type": "war_no_supply_impact", "supply_impact": False, "surprise": True},
    {"date": "2020-01-03", "name": "Soleimani Assassination", "type": "war_no_supply_impact", "supply_impact": False, "surprise": True},
    {"date": "2023-10-07", "name": "Gaza Conflict", "type": "war_no_supply_impact", "supply_impact": False, "surprise": True},
    
    # --- OPEC+ Decisions ---
    {"date": "2016-11-30", "name": "OPEC Cut", "type": "opec", "supply_impact": True, "surprise": False},
    {"date": "2018-06-22", "name": "OPEC+ Increase", "type": "opec", "supply_impact": True, "surprise": False},
    {"date": "2020-03-06", "name": "OPEC+ Failure", "type": "opec", "supply_impact": True, "surprise": True},
    {"date": "2020-04-12", "name": "Historic OPEC+ Cut", "type": "opec", "supply_impact": True, "surprise": False},
    {"date": "2021-07-18", "name": "OPEC+ Gradual Inc", "type": "opec", "supply_impact": True, "surprise": False},
    {"date": "2022-10-05", "name": "OPEC+ 2M Cut", "type": "opec", "supply_impact": True, "surprise": False},
    {"date": "2023-04-02", "name": "OPEC+ Surprise Cut", "type": "opec", "supply_impact": True, "surprise": True},
    {"date": "2023-06-04", "name": "Saudi Solo Cut", "type": "opec", "supply_impact": True, "surprise": True},

    # --- Economic & Market Crises ---
    {"date": "2016-06-23", "name": "Brexit Vote", "type": "economic", "supply_impact": False, "surprise": True},
    {"date": "2018-09-17", "name": "Trade War Escalation", "type": "economic", "supply_impact": False, "surprise": False},
    {"date": "2020-03-11", "name": "COVID Pandemic", "type": "economic", "supply_impact": False, "surprise": True},
    {"date": "2020-04-20", "name": "Negative Oil Price", "type": "economic", "supply_impact": False, "surprise": True},
    {"date": "2022-06-15", "name": "Fed 75bps Hike", "type": "economic", "supply_impact": False, "surprise": False},
    {"date": "2022-09-21", "name": "Global Recession Fears", "type": "economic", "supply_impact": False, "surprise": False},
    {"date": "2023-03-10", "name": "SVB Bank Collapse", "type": "economic", "supply_impact": False, "surprise": True},
    {"date": "2023-05-01", "name": "First Republic Bank", "type": "economic", "supply_impact": False, "surprise": True},

    # --- Infrastructure & Disruption ---
    {"date": "2016-05-04", "name": "Canada Wildfires", "type": "disruption", "supply_impact": True, "surprise": True},
    {"date": "2021-03-23", "name": "Suez Canal Block", "type": "disruption", "supply_impact": True, "surprise": True},
    {"date": "2021-05-07", "name": "Colonial Pipeline", "type": "disruption", "supply_impact": True, "surprise": True},
    {"date": "2022-09-26", "name": "Nord Stream Sabotage", "type": "disruption", "supply_impact": True, "surprise": True},
    {"date": "2023-02-06", "name": "Turkey Earthquake", "type": "disruption", "supply_impact": True, "surprise": True}
]

def main():
    print("Loading oil data...")
    oil = load_oil_data()

    print("Running analysis...")
    run_analysis(oil, events_list)

if __name__ == "__main__":
    main()
