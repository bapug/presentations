def f(a, b, k1='k1', k2='k2', *args, **kwargs):
    print('a: {!r}, b: {!r}, '
         'k1: {!r}, k2: {!r}'
         .format(a, b, k1, k2))
    print("args:{}".format( repr(args)))
    print('kwargs: {}'.format( repr(kwargs)))