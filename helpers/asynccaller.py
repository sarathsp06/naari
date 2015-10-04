from multiprocessing import Process
def async(f):
    def async_func(*arg,**argv):
        p = Process(target = f,args = tuple(arg))
        p.start()
        return p
    return async_func
