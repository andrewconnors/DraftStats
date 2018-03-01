import pandas as pd
import os, os.path

DIR = "./hockeyreference/hockeyreference/DraftData/"
draft_files = [draft_file for draft_file in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, draft_file))]

columns = ['Year', 'Name', 'Overall Pick', 'GP', 'Amateur Team']
allplayers = pd.DataFrame(columns=columns);

for f in draft_files:
    allplayers = allplayers.append(pd.read_csv(DIR + f))

print(allplayers[allplayers['Name'] == 'Dante Fabbro'])
