import pandas as pd

# Lista de archivos a unir
files = ['13-14.csv', '14-15.csv', '15-16.csv', '16-17.csv', '17-18.csv', '18-19.csv', '19-20.csv', '20-21.csv', '21-22.csv', '22-23.csv']

# Crear lista para guardar los DataFrames
dfs = []

# Recorrer la lista de archivos
for file in files:
    df = pd.read_csv('temporadas/' + file)
    dfs.append(df)

# Unir los DataFrames
df = pd.concat(dfs, ignore_index=True)

# Eliminar columnas que no se van a utilizar
columns_to_drop = [
    'Div', 'B365H', 'B365D', 'B365A', 'BWH', 'BWD', 'BWA', 'IWH', 'IWD', 'IWA',
    'LBH', 'LBD', 'LBA', 'PSH', 'PSD', 'PSA', 'WHH', 'WHD', 'WHA', 'SJH', 'SJD',
    'SJA', 'VCH', 'VCD', 'VCA', 'Bb1X2', 'BbMxH', 'BbAvH', 'BbMxD', 'BbAvD', 'BbMxA', 
    'BbAvA', 'BbOU', 'BbMx>2.5', 'BbAv>2.5', 'BbMx<2.5', 'BbAv<2.5', 'BbAH', 'BbAHh', 
    'BbMxAHH', 'BbAvAHH', 'BbMxAHA', 'BbAvAHA', 'PSCH', 'PSCD', 'PSCA', 'MaxH', 'MaxD',
    'MaxA', 'AvgH', 'AvgD', 'AvgA', 'B365CH', 'B365CD', 'B365CA', 'BWCH', 'BWCD', 'BWCA',
    'IWCH', 'IWCD', 'IWCA', 'PSCH', 'PSCD', 'PSCA', 'WHCH', 'WHCD', 'WHCA', 'VCCH', 'VCCD',
    'Time','B365>2.5', 'B365<2.5', 'P>2.5', 'P<2.5', 'Max>2.5', 'Max<2.5', 'Avg>2.5', 'Avg<2.5', 'AHh',
    'B365AHH', 'B365AHA', 'PAHH', 'PAHA', 'MaxAHH', 'MaxAHA', 'AvgAHH', 'AvgAHA', 'VCCA',
    'MaxCH', 'MaxCD', 'MaxCA', 'AvgCH', 'AvgCD', 'AvgCA', 'B365C>2.5', 'B365C<2.5', 'PC>2.5', 'PC<2.5',
    'MaxC>2.5', 'MaxC<2.5', 'AvgC>2.5', 'AvgC<2.5', 'AHCh', 'B365CAHH', 'B365CAHA', 'PCAHH', 'PCAHA',
    'MaxCAHH', 'MaxCAHA', 'AvgCAHH', 'AvgCAHA'
]

df = df.drop(columns=columns_to_drop, axis=1)

# Guardar el DataFrame resultante en un archivo CSV
df.to_csv('temporadas.csv', index=False)
