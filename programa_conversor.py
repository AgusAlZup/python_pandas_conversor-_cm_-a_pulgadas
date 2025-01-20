import pandas as pd


def cm_a_pulgadas(cm):
    return cm / 2.54


# Leer el archivo excel
df = pd.read_excel("muebles_medidas.xlsx")

# Añadir una columna al DF de pulgadas

df["Pulgadas"] = df["Centimetros"].apply(cm_a_pulgadas)

df.to_csv("mueble_medidas_convertidas.csv", index=False)


print("Conversión completa y guardada en archivo : mueble_medidas_convertidas")
