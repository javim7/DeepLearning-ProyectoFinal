# Proyecto de Predicción de Resultados en la Liga BBVA

## Tabla de Contenido

1. [Descripción General del Proyecto](#descripción-general-del-proyecto)
2. [Dataset](#dataset)
   - [Origen y Recopilación](#origen-y-recopilación)
   - [Estructura del Dataset](#estructura-del-dataset)
   - [Variables Importantes](#variables-importantes)
3. [Modelos Implementados](#modelos-implementados)
4. [Autores](#autores)

## Descripción General del Proyecto

Para nuestro proyecto final, hemos decidido crear una serie de modelos capaces de predecir el resultado de un partido de la Liga BBVA. Cada uno de los modelos tiene diferentes características y estructuras, pero la misma finalidad (a excepción del último modelo), lo cual se hizo para poder comparar los modelos y poder ver cuál era el que sobresalía. El último modelo es algo diferente, ya que este no es como los demás, que predice cuál será el resultado de un partido de la liga, sino que este predice si el Barcelona ganará o no un partido.

La razón por la cual decidimos abarcar este tema fue porque ambos somos fanáticos del fútbol. Toda la vida hemos jugado el deporte y siempre hemos sido seguidores de la Liga BBVA y más específicamente del F.C. Barcelona. Por lo tanto, se nos hizo una muy buena idea mezclar la inteligencia artificial con la liga española, ya que esto mezcla dos áreas que nos interesan, y hasta podría sernos de utilidad para poder obtener información de la temporada actual, lo cual nos podría servir incluso para apostar.

## Dataset

### Origen y Recopilación

Los datos utilizados en este proyecto fueron recopilados de diversas fuentes para abarcar las últimas 10 temporadas de la Liga BBVA. Los registros de cada temporada se consolidaron en un solo archivo CSV para facilitar el manejo y análisis. Adicionalmente se eliminaron varias columnas, las cuales incluian informacion sobre apuestas de los partidos, las cuales consideramos que no eran importantes para nuestros modelos. 

### Estructura del Dataset

El dataset consiste en información detallada sobre los partidos de la Liga BBVA, incluyendo variables como la fecha del partido, los equipos locales y visitantes, goles marcados por cada equipo (tanto en tiempo completo como en medio tiempo), estadísticas de tiros, faltas, tarjetas y expulsiones, entre otras.

```python
|------------|-------------|-------------|------|------|-----|------|------|-----|----|----|-----|-----|----|----|----|----|----|----|----|----|
| Date       | HomeTeam    | AwayTeam    | FTHG | FTAG | FTR | HTHG | HTAG | HTR | HS | AS | HST | AST | HF | AF | HC | AC | HY | AY | HR | AR |
|------------|-------------|-------------|------|------|-----|------|------|-----|----|----|-----|-----|----|----|----|----|----|----|----|----|
```

### Variables Importantes

Algunas de las variables más relevantes utilizadas en los modelos son:

- **'Date'**: Fecha del partido.
- **'HomeTeam' y 'AwayTeam'**: Equipos locales y visitantes, respectivamente.
- **'FTHG' y 'FTAG'**: Goles marcados por el equipo local y visitante a tiempo completo.
- **'FTR'**: Resultado final del partido (H: Local gana, A: Visitante gana, D: Empate).
- **'PH' y 'PA'**: Puntos acumulados por el equipo local y visitante.
- **'GDH' y 'GDA'**: Diferencia de goles del equipo local y visitante.
- **'HHHW' y 'HHAW'**: Número de victorias head-to-head para el equipo local y visitante.

Estas variables se utilizaron para entrenar y evaluar los diferentes modelos de predicción implementados en el proyecto.

## Modelos Implementados

1. **Modelo 1: Red Neuronal Recurrente (RNN) con Capa SimpleRNN**
   - Arquitectura: SimpleRNN(32) → Dropout(0.2) → Dense(16) → Dropout(0.2) → Dense(Salida)
   - Resultados: Pérdida: 0.9251, Precisión: 0.5740

2. **Modelo 2: Red Neuronal con Capas Densas y Promedios de Datos**
   - Arquitectura: Dense(64) → Dropout(0.1) → Dense(32) → Dropout(0.1) → Dense(Salida)
   - Resultados: Pérdida: 1.0097, Precisión: 0.5114

3. **Modelo 3: Red Neuronal Recurrente con Capas LSTM**
   - Arquitectura: LSTM(64) → Dropout(0.2) → Dense(32) → Dropout(0.2) → Dense(Salida)
   - Resultados: Pérdida: 1.0101, Precisión: 0.5090

4. **Modelo 4: Red Neuronal Recurrente con Puntos y Diferencia de Goles**
   - Arquitectura: SimpleRNN(32) → Dropout(0.2) → Dense(16) → Dropout(0.2) → Dense(Salida)
   - Resultados: Pérdida: 1.0446, Precisión: 0.4724

5. **Modelo 5: Red Neuronal para Predicción del FC Barcelona**
   - Arquitectura: Dense(32) → Dense(16) → Dense(1, activación sigmoide)
   - Resultados: Pérdida: 0.5858, Precisión: 0.6926

## Autores

- **Javier Mombiela** - [GitHub: javim7](https://github.com/javim7)
- **Roberto Rios** - [GitHub: robertriosm](https://github.com/robertriosm)

