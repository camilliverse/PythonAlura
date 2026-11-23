# fatorial roda como uma tarefa assíncrona separada. Inclusive, 
# você pode utilizar a função asyncio.current_task() para verificar o id da tarefa atual. Utilizamos asyncio.gather() para rodar todas ao mesmo tempo

import asyncio
import math

numeros = [5, 3, 7, 4, 6]

async def calcular_fatorial(n):
    await asyncio.sleep(n) 
    print(f"Fatorial de {n} = {math.factorial(n)}")

async def main():
    tarefas = [asyncio.create_task(calcular_fatorial(n)) for n in numeros]
    await asyncio.gather(*tarefas)

asyncio.run(main())