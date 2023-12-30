import asyncio
import time


async def call_client(date_from, date_to):
    await asyncio.sleep(1)
    return {"value1": 1, "value2": 2, "value3": 3, "date_from": date_from, "date_to": date_to}


async def call(funct, date_from, date_to, identifier: str, datasource: dict):
    value = await funct(date_from, date_to)
    datasource[f'{identifier}'] = value


async def get_data() -> dict:
    datasource = dict()
    first_element = asyncio.create_task(call(call_client, 2020, 2023, 'first_element', datasource))
    second_element = asyncio.create_task(call(call_client, 2020, 2023, 'second_element', datasource))
    third_element = asyncio.create_task(call(call_client, 2020, 2023, 'third_element', datasource))
    fourth_element = asyncio.create_task(call(call_client, 2020, 2023, 'fourth_element', datasource))
    fifth_element = asyncio.create_task(call(call_client, 2020, 2023, 'fifth_element', datasource))
    await asyncio.gather(first_element, second_element, third_element, fourth_element, fifth_element)
    return datasource


async def build_element():
    data = await get_data()
    print(data)


s = time.perf_counter()
asyncio.run(build_element())
elapsed = time.perf_counter() - s
print(f'{__file__} executed in {elapsed:0.2f} seconds')
