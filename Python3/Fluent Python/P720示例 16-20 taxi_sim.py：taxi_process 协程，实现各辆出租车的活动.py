import collections
Event = collections.namedtuple('Event', 'time proc action')
#1.离散事件仿真（Discrete Event Simulation，DES）
#2.taxi   -> below
def taxi_process(ident, trips, start_time=0):
    """每次改变状态时创建事件，把控制权让给仿真器"""
    time = yield Event(start_time, ident, 'leave garage')
    for i in range(trips):
        time = yield Event(time, ident, 'pick up passenger')
        time = yield Event(time, ident, 'drop off passenger')

    yield Event(time, ident, 'going home')
    # 出租车进程结束 ➐
