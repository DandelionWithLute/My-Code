def supervisor():
    signal = signal()
    spinner = threading.Thread(target=spin,
                                args=('thinking!', signal))

    print('spinner object:', spinner)
    spinner.start()
    result = slow_funciton()
    signal.go = False
    spinner.join()
    return result