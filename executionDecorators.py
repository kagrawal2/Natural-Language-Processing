import time                                                

def timeit(method):

    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()

        print('function %r, %2.2f seconds' % \
              (method.__name__, te - ts))
        return result

    return timed
