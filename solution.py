import matplotlib.pyplot as plt

from tabulate import tabulate
from typing import Callable

def range_kutta(y: float, x: float, h: float, n: int, 
                f: Callable[[float, float], float]) -> tuple[list[float], list[float]]:
    cur_y, cur_x = y, x
    result = ([cur_x], [cur_y])
    k1, k2, k3, k4 = 0, 0, 0, 0
    for _ in range(0, n):
        k1 = f(cur_x, cur_y)
        k2 = f(cur_x + 0.5 * h, cur_y + 0.5 * h * k1)
        k3 = f(cur_x + 0.5 * h, cur_y + 0.5 * h * k2)
        k4 = f(cur_x + h, cur_y + h * k3)
        cur_y += (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
        cur_x += h
        result[0].append(cur_x)
        result[1].append(cur_y)
    return result

def sum_digits(num: int) -> int:
    return sum([int(x) for x in str(num)])

def average(values: list[float]) -> float:
    return sum(values) / len(values)

def generate_table(points: tuple[list[float], list[float]]) -> str:
   return tabulate(list(zip(range(0,table_rows + 1), points[0][:table_rows + 1], 
                        points[1][:table_rows + 1])), 
               headers=["Iteração", "Tempo [min]", "Temperatura [°C]"], 
               tablefmt="fancy_grid")
    
K = 0.25
N = 200

initial_temp = round(sum_digits(11202130847) * 1.5)
print(f"Temperatura especificada: {initial_temp}°C")

_, ax_h1 = plt.subplots()
ax_h1.set_xlabel("Tempo [min]")
ax_h1.set_ylabel("Temperatura [°C]")
ax_h1.autoscale()

points_h1 = range_kutta(90, 0, 0.1, N, lambda _, y: -K * (y - 20)) 

avg_timestamp, avg_temp = 0, 0
for i in range(0, len(points_h1[0])):
    if points_h1[1][i] <= initial_temp:
        avg_timestamp = average(points_h1[0][i - 1:i + 1])
        avg_temp = average(points_h1[1][i - 1:i + 1])
        ax_h1.scatter(avg_timestamp, avg_temp, color='red')
        # Não é necessário verificar o tamanho do array para acessar o valor
        # da posição i + 1, pois a temperatura final (com N iterações) é menor 
        # do que a especificada.
        break

table_rows = 5
print(f"Tempo de resfriamento aproximado: {avg_timestamp:.2f}s")
print(f"Temperatura após o tempo de resfriamento aproximado: {avg_temp:.2f}°C")
print("Tabela (h=0.1s):")        
print(generate_table(points_h1))

ax_h1.plot(points_h1[0], points_h1[1], scalex=False, scaley=False)
plt.savefig("graph-h1.png")

_, ax_h2 = plt.subplots()
ax_h2.set_xlabel("Tempo [min]")
ax_h2.set_ylabel("Temperatura [°C]")
ax_h2.autoscale()

points_h2 = range_kutta(90, 0, 0.25, N, lambda _, y: -K * (y - 20)) 

table_rows = 5
print("Tabela (h=0.25s):")        
print(generate_table(points_h2))
ax_h2.plot(points_h2[0], points_h2[1], scalex=False, scaley=False)
plt.savefig("graph-h2.png")

