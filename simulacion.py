import simpy
import random
import numpy as np
from tabulate import tabulate

# -----------------------
# PARÁMETROS
# -----------------------
SIM_TIME = 480  # 8 horas
INTERVALO_LLEGADA = 3
NUM_FARMACEUTICOS = 2

random.seed(42)

# -----------------------
# ESTADÍSTICAS
# -----------------------
esperas = []
tiempos_sistema = []
tiempos_atencion = []
clientes_atendidos = 0


# -----------------------
# FARMACIA
# -----------------------
class Farmacia:
    def __init__(self, env):
        self.recurso = simpy.Resource(env, capacity=NUM_FARMACEUTICOS)
        self.env = env

    def atender(self, tipo):
        # tiempos más realistas según tipo de cliente
        if tipo == "rapido":
            tiempo = random.triangular(1, 2, 3)
        elif tipo == "receta":
            tiempo = random.triangular(3, 5, 7)
        else:
            tiempo = random.triangular(5, 7, 10)

        yield self.env.timeout(tiempo)
        return tiempo


# -----------------------
# CLIENTE
# -----------------------
def cliente(env, nombre, farmacia):
    global clientes_atendidos

    llegada = env.now

    # tipo de cliente
    tipo = random.choices(
        ["rapido", "receta", "consulta"],
        weights=[0.5, 0.3, 0.2]
    )[0]

    with farmacia.recurso.request() as req:
        yield req

        espera = env.now - llegada
        esperas.append(espera)

        tiempo_servicio = yield env.process(farmacia.atender(tipo))
        tiempos_atencion.append(tiempo_servicio)

        tiempos_sistema.append(env.now - llegada)

        clientes_atendidos += 1


# -----------------------
# GENERADOR DE CLIENTES
# -----------------------
def generador(env, farmacia):
    i = 0

    while True:
        yield env.timeout(random.expovariate(1 / INTERVALO_LLEGADA))
        i += 1
        env.process(cliente(env, f"Cliente {i}", farmacia))


# -----------------------
# EJECUCIÓN
# -----------------------
env = simpy.Environment()
farmacia = Farmacia(env)

env.process(generador(env, farmacia))
env.run(until=SIM_TIME)


# -----------------------
# RESULTADOS
# -----------------------
utilizacion = (np.sum(tiempos_atencion) / (SIM_TIME * NUM_FARMACEUTICOS)) * 100

data = [
    ["Clientes atendidos", clientes_atendidos],
    ["Promedio espera", round(np.mean(esperas), 2)],
    ["Promedio atención", round(np.mean(tiempos_atencion), 2)],
    ["Promedio sistema", round(np.mean(tiempos_sistema), 2)],
    ["Máxima espera", round(np.max(esperas), 2)],
    ["Utilización (%)", round(utilizacion, 2)]
]

print("\n================ RESULTADOS =================\n")
print(tabulate(data, headers=["Indicador", "Valor"], tablefmt="fancy_grid"))
print("\n=============================================\n")