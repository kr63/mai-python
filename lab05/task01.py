import argparse
import asyncio
import re
import time

import aiofile
import aiohttp


def get_filename(response: aiohttp.ClientResponse) -> str:
    d = response.headers['content-disposition']
    return re.findall('filename="(.+)"', d)[0]


async def write_file(fname: str, data: bytes):
    async with aiofile.async_open(fname, 'wb') as f:
        await f.write(data)


async def get_url(semaphore_, url_):
    async with semaphore_:
        async with aiohttp.ClientSession() as session:
            async with session.get(url_) as response:
                data = await response.read()
                filename = get_filename(response)
                await write_file(filename, data)


def get_links(filename_):
    with open(filename_, 'r', encoding='UTF-8') as file:
        return [link for link in file.readlines()]


async def main(filename_, requests_):
    start = time.time()
    semaphore = asyncio.BoundedSemaphore(requests_)
    tasks = [asyncio.create_task(get_url(semaphore, url_)) for url_ in get_links(filename_)]
    await asyncio.wait(tasks)
    end = time.time()
    print(f'Time to complete: {end - start}')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='URLs fetcher')
    parser.add_argument('-f', '--file', type=str,
                        help='Файл с ссылками', default='file.txt')
    parser.add_argument('-r', '--requests', type=int, default=10,
                        help='Количество запросов')
    args = parser.parse_args()

    asyncio.run(main(args.file, args.requests))
