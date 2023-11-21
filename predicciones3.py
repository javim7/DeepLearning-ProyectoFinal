import json
import numpy as np
import pandas as pd
from keras.models import load_model

def preparar_datos(jornada, partido, tabla):
    # Obtener el Home y AwayTeam
    homeTeam = partido['HomeTeam']
    awayTeam = partido['AwayTeam']
    homeTeamMapping = team_mapping[partido['HomeTeam']]
    awayTeamMapping = team_mapping[partido['AwayTeam']]

    if jornada == 1:
        PointsHome = 0
        PointsAway = 0
        GoalDiffHome = 0
        GoalDiffAway = 0
    else:
        # Obtener los puntos y diferencia de goles del HomeTeam
        puntos_home = tabla.loc[tabla['Equipo'] == homeTeam, 'Puntos']
        if puntos_home.empty:
            PointsHome = 0
        else:
            PointsHome = puntos_home.values[0]
        # Obtener los goles a favor y en contra del HomeTeam
        goles_favor_home = tabla.loc[tabla['Equipo'] == homeTeam, 'Favor']
        goles_contra_home = tabla.loc[tabla['Equipo'] == homeTeam, 'Contra']

        if goles_favor_home.empty or goles_contra_home.empty:
            GoalDiffHome = 0
        else:
            GoalDiffHome = goles_favor_home.values[0] - goles_contra_home.values[0]


        # Obtener los puntos y diferencia de goles del AwayTeam
        PointsAway = tabla.loc[tabla['Equipo'] == awayTeam, 'Puntos'].values[0]
        GoalDiffAway = tabla.loc[tabla['Equipo'] == awayTeam, 'Favor'].values[0] - tabla.loc[tabla['Equipo'] == awayTeam, 'Contra'].values[0]

    # Obtener los H2H wins de cada uno
    print(f"'{homeTeam}', '{awayTeam}', {PointsHome}, {PointsAway}")

    return homeTeamMapping, awayTeamMapping, PointsHome, PointsAway

def predecir_resultado(model, datos_partido):
    # Convertir los datos del partido a un array de numpy y cambiar su forma para que sea aceptado por el modelo
    datos_partido = np.array(datos_partido).reshape((1, 1, len(datos_partido)))

    # Realizar la predicción con el modelo
    prediccion = model.predict(datos_partido)

    # Devolver el resultado de la predicción
    return np.argmax(prediccion)

def actualizar_tabla(tabla_predicciones, partido, resultado, result_mapping):
    # Mapear el resultado a su representación de cadena
    resultado = result_mapping[resultado]

    # Mapear los equipos a sus nombres
    homeTeam = partido['HomeTeam']
    awayTeam = partido['AwayTeam']

    # Si el equipo local ganó, agregar 3 puntos a su total
    if resultado == 'H':
        tabla_predicciones.loc[tabla_predicciones['Equipo'] == homeTeam, 'Puntos'] += 3
    # Si el equipo visitante ganó, agregar 3 puntos a su total
    elif resultado == 'A':
        tabla_predicciones.loc[tabla_predicciones['Equipo'] == awayTeam, 'Puntos'] += 3
    # Si el partido terminó en empate, agregar 1 punto al total de cada equipo
    else:
        tabla_predicciones.loc[tabla_predicciones['Equipo'] == homeTeam, 'Puntos'] += 1
        tabla_predicciones.loc[tabla_predicciones['Equipo'] == awayTeam, 'Puntos'] += 1

if __name__ == "__main__":
    # Cargar el modelo y sus datos
    model = load_model('modelos/modelo3.h5')
    dataModel = pd.read_csv('modelos/data3.csv')
    # print(dataModel.head)
    with open('modelos/team_mapping.json', 'r') as f:
        team_mapping = json.load(f)
    # print(team_mapping['Alaves'])
    
    result_mapping = {0: 'A', 1: 'D', 2: 'H'}

    # Cargar los partidos de esta temporadas
    partidos = pd.read_csv('predicciones/23-24.csv')

    # Inicializar la tabla de predicciones
    tabla_predicciones = pd.DataFrame(columns=['Equipo', 'Puntos'])
    
    # Inicializar la tabla de predicciones con todos los equipos
    equipos = partidos['HomeTeam'].unique()
    tabla_predicciones = pd.DataFrame({'Equipo': equipos, 'Puntos': [0]*len(equipos)})


    # Recorrer los partidos
    for jornada in partidos['Jor'].unique():
    # for jornada in range (1,2):

        # Cargar la tabla de la jornada
        if jornada == 1:
            tabla = pd.read_csv(f'predicciones/jornadasMod/{jornada}.csv')
        else:
            tabla = pd.read_csv(f'predicciones/jornadasMod/{jornada-1}.csv')

        # seleccionar los partidos de la jornada
        partidos_jornada = partidos[partidos['Jor'] == jornada]

        # Recorrer los partidos de la jornada
        for i, partido in partidos_jornada.iterrows():
            datos_partido = preparar_datos(jornada, partido, tabla)
            # print(datos_partido)

            resultado = predecir_resultado(model, datos_partido)
            print(resultado)

            actualizar_tabla(tabla_predicciones, partido, resultado, result_mapping)

            # Ordenar la tabla de predicciones por puntos de mayor a menor
            tabla_predicciones = tabla_predicciones.sort_values(by='Puntos', ascending=False)

            # Guardar la tabla de predicciones en un archivo
            tabla_predicciones.to_csv(f'predicciones/jornadasPred3/{jornada}.csv', index=False)
