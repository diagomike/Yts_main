import asyncio
import httpx

async def log_request(request):
        print(f"Request: {request.method} {request.url}")

async def log_response(respose):
    request = respose.request
    print(f"Response: {request.method} {request.url} - Status {respose.status_code}")


async def get_episode(ep_id: int):
    async with httpx.AsyncClient(event_hooks={'request': [log_request], 'response':[log_response]}) as client:
        r = await client.get(f'https://rickandmortyapi.com/api/episode/{ep_id}')
        results.append(r.json())
        return

async def main():
    tasks = []
    for ep_id in range(1,11):
        tasks.append(get_episode(ep_id))
    await asyncio.gather(*tasks)

results = []
asyncio.run(main())

print(len(results))