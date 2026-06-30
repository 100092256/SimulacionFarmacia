Simulación de Atención en Farmacia (SimPy)
Descripción del proyecto

Este proyecto implementa una simulación de eventos discretos del proceso de atención en una farmacia utilizando Python y la librería SimPy.

El objetivo es analizar el comportamiento del sistema de colas, midiendo indicadores como el tiempo de espera, tiempo en el sistema, utilización de recursos y número de clientes atendidos.

El modelo representa una farmacia donde los clientes llegan de forma aleatoria, esperan en una cola FIFO y son atendidos por un número limitado de farmacéuticos.

Tecnologías utilizadas
Python 3
SimPy (simulación de eventos discretos)
NumPy (cálculos estadísticos)
Tabulate (formato de salida en tabla)
Características del modelo
Simulación de llegada aleatoria de clientes
Sistema de cola FIFO (First In, First Out)
Atención por recursos limitados (farmacéuticos)
Tiempos de servicio variables mediante distribución triangular
Cálculo automático de métricas del sistema
Comparación de escenarios con distintos números de empleados
Parámetros de simulación
Parámetro	Valor
Tiempo de simulación	480 minutos (8 horas)
Tiempo entre llegadas	Distribución exponencial (media = 3 min)
Tiempo de atención	Distribución triangular (2, 5, 8 min)
Número de empleados	2 y 3 (escenarios)
Disciplina de cola	FIFO
Indicadores calculados
Clientes atendidos
Tiempo promedio de espera
Tiempo promedio en el sistema
Máxima espera registrada
Utilización de los empleados
