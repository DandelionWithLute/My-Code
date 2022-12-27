# Z:\>chcp ➊
# Página de código ativa: 850
# Z:\>python default_encodings.py ➋
# locale.getpreferredencoding() -> 'cp1252' ➌
# type(my_file) -> <class '_io.TextIOWrapper'>
# my_file.encoding -> 'cp1252' ➍
# sys.stdout.isatty() -> True ➎
# sys.stdout.encoding -> 'cp850' ➏
# sys.stdin.isatty() -> True
# sys.stdin.encoding -> 'cp850'
# sys.stderr.isatty() -> True
# sys.stderr.encoding -> 'cp850'
# sys.getdefaultencoding() -> 'utf-8'
# sys.getfilesystemencoding() -> 'mbcs