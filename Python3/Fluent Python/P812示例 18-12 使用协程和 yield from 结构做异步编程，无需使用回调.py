@asyncio.coroutine
def three_stages(request1):
    response1 = yield from api_call1(request1)
    # 第一步
    request2 = step1(response1)
    response2 = yield from api_call2(reqeust2)
    # 第二步
    request3 = step2(response2)
    response3 = yield from api_call3(request3)
    # 第三步
    step(response3)

loop.create_task(three_stages(request1)) # 必须显式调度执行