import asyncio

async def baixar_dados():
    print("Iniciando download...")
    await asyncio.sleep(2)
    print("Download concluído!")

async def analisar_dados():
    print("Iniciando análise de dados...")
    await asyncio.sleep(3)
    print("Análise de dados concluída!")

async def main():
    await asyncio.gather(
        baixar_dados(),
        analisar_dados()
    )

asyncio.run(main())