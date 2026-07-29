import pandas as pd
import os

# Get the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "NBA_team_salarycap_2026.csv")
 
df = pd.read_csv(csv_path)
print(df)