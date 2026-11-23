import asyncio

async def temporizador ():
    print('Iniciado temporizador...')
    await asyncio.sleep(3) #asyncio.sleep() permite que o código pause sua execução de maneira assíncrona, sem bloquear outras tarefas
    print('Tempo finalizado apos 3 segundos!')

asyncio.run(temporizador()) #executar corrotina