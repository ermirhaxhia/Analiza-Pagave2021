import pandas as pd

def lexo_te_dhenat(path):
    return pd.read_csv(path, encoding='latin1')



def pastrim_te_dhenave(df):

    df = df.rename(columns={
        "Numri Personal": "NP",
        "EMRI I PLOTE" : "Emri i plote",
        " Paga Bruto ": "P_Bruto", 
        "type" : "Lloji biznesit"
    })

    df['P_Bruto'] = df['P_Bruto'].str.replace(",", "", regex=False)
    df['P_Bruto'] = pd.to_numeric(df['P_Bruto'], errors='coerce')

    df = df.drop(columns="Subjekti")

    df.dropna()

    return df
