import pandas as pd

payroll = pd.read_csv("NBA_team_payroll_2026.csv")
salarycap = pd.read_csv("NBA_team_salarycap_2026.csv")
stats = pd.read_csv("NBA_team_stats.csv")
advanced = pd.read_csv("NBA_team_stats2.csv")

stats["Team"] = stats["Team"].str.replace("*", "", regex=False)
advanced["Team"] = advanced["Team"].str.replace("*", "", regex=False)

team_map = {
    "Atlanta Hawks": "ATL",
    "Boston Celtics": "BOS",
    "Brooklyn Nets": "BKN",
    "Charlotte Hornets": "CHA",
    "Chicago Bulls": "CHI",
    "Cleveland Cavaliers": "CLE",
    "Dallas Mavericks": "DAL",
    "Denver Nuggets": "DEN",
    "Detroit Pistons": "DET",
    "Golden State Warriors": "GSW",
    "Houston Rockets": "HOU",
    "Indiana Pacers": "IND",
    "Los Angeles Clippers": "LAC",
    "Los Angeles Lakers": "LAL",
    "Memphis Grizzlies": "MEM",
    "Miami Heat": "MIA",
    "Milwaukee Bucks": "MIL",
    "Minnesota Timberwolves": "MIN",
    "New Orleans Pelicans": "NOP",
    "New York Knicks": "NYK",
    "Oklahoma City Thunder": "OKC",
    "Orlando Magic": "ORL",
    "Philadelphia 76ers": "PHI",
    "Phoenix Suns": "PHX",
    "Portland Trail Blazers": "POR",
    "Sacramento Kings": "SAC",
    "San Antonio Spurs": "SAS",
    "Toronto Raptors": "TOR",
    "Utah Jazz": "UTA",
    "Washington Wizards": "WAS"
}

stats["Team"] = stats["Team"].map(team_map)
advanced["Team"] = advanced["Team"].map(team_map)

# Remove any rows that aren't actual NBA teams
stats = stats[stats["Team"].notna()]
advanced = advanced[advanced["Team"].notna()]

payroll = payroll[
    [
        "Team",
        "Avg Age",
        "Total Cash",
        "Dead"
    ]
].rename(
    columns={
        "Avg Age": "AvgAge",
        "Total Cash": "Payroll",
        "Dead": "DeadCash"
    }
)

salarycap = salarycap[
    [
        "Team",
        "Team Total Cap Allocations",
        "Cap Space",
        "Dead Cap"
    ]
].rename(
    columns={
        "Team Total Cap Allocations": "CapAllocations",
        "Dead Cap": "DeadCap"
    }
)

stats = stats[
    [
        "Team",
        "PTS",
        "FG%",
        "3P%",
        "FT%",
        "TRB",
        "AST",
        "STL",
        "BLK",
        "TOV"
    ]
]

advanced = advanced[
    [
        "Team",
        "Age",
        "W",
        "L",
        "MOV",
        "SRS",
        "ORtg",
        "DRtg",
        "NRtg",
        "Pace",
        "TS%"
    ]
].rename(
    columns={
        "Age": "RosterAge"
    }
)

df = payroll.merge(salarycap, on="Team", how="inner")

df = df.merge(stats, on="Team", how="inner")

df = df.merge(advanced, on="Team", how="inner")


df["WinPct"] = df["W"] / (df["W"] + df["L"])

df["CostPerWin"] = df["Payroll"] / df["W"]

df["PayrollRank"] = df["Payroll"].rank(
    ascending=False,
    method="min"
)

df["CapAllocationRank"] = df["CapAllocations"].rank(
    ascending=False,
    method="min"
)

df["PointDiffPerDollar"] = (
    df["MOV"] / (df["Payroll"] / 1_000_000)
)

df["NetRatingPerMillion"] = (
    df["NRtg"] / (df["Payroll"] / 1_000_000)
)


df = df.sort_values(
    by="W",
    ascending=False
)

round_cols = [
    "WinPct",
    "CostPerWin",
    "PointDiffPerDollar",
    "NetRatingPerMillion"
]

df[round_cols] = df[round_cols].round(3)


output_file = "NBA_Master_Dataset_2026.csv"
backup_file = "NBA_Master_Dataset_2025_26.csv"

df.to_csv(output_file, index=False)
df.to_csv(backup_file, index=False)

print(f"Dataset created successfully: {output_file}")
print(df.head())

print("\nRows:", len(df))
print("Columns:", len(df.columns))