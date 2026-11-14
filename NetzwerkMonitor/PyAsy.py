import asyncio

async def fetch_data():
    print("Fetching data...")
    # Instead of Task.Delay(2000) like in C#, Python uses asyncio.sleep
    await asyncio.sleep(2) 
    return "Data package received!"

async def main():
    # We 'await' the async function to get the result
    result = await fetch_data()
    print(result)

# To kick off the async world in Python, you must explicitly run the loop:
asyncio.run(main())
