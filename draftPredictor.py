import pandas as pd

scoring = pd.read_csv('./professional-hockey-database/Scoring.csv')
scoring.set_index("playerID")

master = pd.read_csv('./professional-hockey-database/Master.csv')
master.set_index("playerID")


print scoring.loc[: , "pos"]
