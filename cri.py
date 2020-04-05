import pandas as pd
import numpy as np

def ReadExcel(FileName):
    e_data = pd.read_excel(FileName)
    df = pd.DataFrame(e_data)
    print(df)
    return df

def FindByTeam(em, key):
    Team = em[em.Team == key]
    print(Team)
if _name_ == "_main_":
 main()
 main._doc_
