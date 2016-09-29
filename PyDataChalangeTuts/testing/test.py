import numpy as np
import pandas as pd
import matplotlib as matp

mortalidad = pd.read_csv("mortalidad_materna_2002-2013.csv")
mortalidad.head()
madresNoMujeres = mortalidad.ix[mortalidad.Genero != 2]
mortalidad2 = mortalidad.copy()
mortalidad2.drop("Genero", axis=1, inplace=True)
columnas = mortalidad2.columns
valores = [nombres for nombres in columnas if nombres.startswith('Descr')]
for i, nombre in enumerate(columnas):
    llaves = [columnas[i - 1] for i in range(len(columnas)) if columnas[i].startswith('Descr')]
    traduccion = dict(zip(llaves, valores))
    prohibidas = ['ñ', ' ', 'á', 'é', 'í', 'ó', 'ú']
    alternativas = ['ni', '_', 'a', 'e', 'i', 'o', 'u']
    traductor = dict(zip(prohibidas, alternativas))
    for p in prohibidas:
        mortalidad2.rename(columns=lambda x: x.replace(p, traductor[p]), inplace=True)
columnasQueMeImportan = [c for c in columnas if not c in valores]
mortalidadImportante = mortalidad2[columnasQueMeImportan]
mortalidadImportante.dropna(inplace=True)
mortalidadImportante2 = mortalidad2[columnasQueMeImportan]
mortalidadImportante2.Ano_de_registro.replace('NaN', mortalidadImportante2.columns[0])
mortalidadImportante2.corr()
