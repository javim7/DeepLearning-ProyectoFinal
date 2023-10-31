import pandas as pd

#lista de archivos a unir
files = ['13-14.csv', '14-15.csv', '15-16.csv', '16-17.csv', '17-18.csv', '18-19.csv', '19-20.csv', '20-21.csv', '21-22.csv', '22-23.csv']

# crear lista para guardar los datasets
dfs = []

#recorrer la lista de archivos
for file in files:
    df = pd.read_csv('temporadas/' + file)
    dfs.append(df)

# unir los datasets
df = pd.concat(dfs, ignore_index=True)
df.to_csv('temporadas.csv', index=False)
