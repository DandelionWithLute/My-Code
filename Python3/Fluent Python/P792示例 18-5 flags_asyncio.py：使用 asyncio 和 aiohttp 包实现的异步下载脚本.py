import asyncio
import aiohttp
from flags import BASE_URL, save_flag, show, main ➋
@asyncio.coroutine ➌
def get_flag(cc):
url = '{}/{cc}/{cc}.gif'.format(BASE_URL, cc=cc.lower())
resp = yield from aiohttp.request('GET', url) ➍
image = yield from resp.read() ➎
return image
@asyncio.coroutine
def download_one(cc): ➏
image = yield from get_flag(cc) ➐
show(cc)
save_flag(image, cc.lower() + '.gif')
return cc
def download_many(cc_list):
loop = asyncio.get_event_loop() ➑
to_do = [download_one(cc) for cc in sorted(cc_list)] ➒
wait_coro = asyncio.wait(to_do) ➓
res, _ = loop.run_until_complete(wait_coro) ⓫
loop.close() ⓬
return len(res)
if __name__ == '__main__':
main(download_many)
