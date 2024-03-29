import asyncio
@asyncio.coroutine
def init(loop, address, port):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', home)
    handler = app.make_handler()
    server = yield from loop.create_server(handler,
                                            address, port)
    return server.sockets[0].getsockname()

def main(address='127.0.0.1', port=8888):
    port = int(port)
    loop = asyncio.get_event_loop()
    host = loop.run_until_complete(init(loop, address, port))
    print('Serving on {}. Hit CTRL-C to stop.'.format(host))
    try:
        loop.run_forever()
    except KeyboardInterrupt:   # 按CTRL-C键
        pass
    print('Server shutting down.')
    loop.close()

if __name__ == '__main__':
    main(*sys.argv[1:])