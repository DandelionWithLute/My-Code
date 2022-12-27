import asyncio
def main(address='127.0.0.1', port=2323):
    port = int(port)
    loop = asyncio.get_event_loop()
    server_coro = asyncio.start_server(handle_queries, address, port,
                                        loop=loop)
    server = loop.run_until_complete(server_coro)
    host = server.sockets[0].getsockname()
    print('Serving on {}. Hit CTRL-C to stop.'.format(host))
    try:
        loop.run_forever()
    except KeyboardInterrupt: # 按CTRL-C键
        pass
    
    print('Server shutting down.')
    server.close()
    loop.run_until_complete(server.wait_close())
    loop.close()

if __name__ == '__main__':
    main(*sys.argv[1:])