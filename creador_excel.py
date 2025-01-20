import pandas as pd

# Dataframe

data = {
    "Piezas: ": ["Pata", "Tablero", "Puerta", "Estante", "Panel Lateral"],
    "Centimetros": [20, 60, 180, 30, 200],
}

df = pd.DataFrame(data)

# Guardar el Dataframe en Excel

df.to_excel("muebles_medidas.xlsx", index=False)
