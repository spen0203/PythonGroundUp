
def allocate():
    dict_list = [{'x': 1.0*i, 'y': 2.5*i} for i in range(100000)]

    class xy_class(object):
        def __init__(self,x,y):
            self.x,self.y = x,y

    class_list = [xy_class(1.0*i,2.5*i) for i in range(100000)]

    class xy_slots_class(object):
        __slots__ = ['x','y'] 
        def __init__(self,x,y):
            self.x,self.y = x,y

    slots_list = [xy_slots_class(1.0*i,2.5*i) for i in range(100000)]

    xy_namedtuple = collections.namedtuple('xy',['x','y'])

    xytuple = [{1.0*i, 2.5*i} for i in range(100000)]

    xylist = [{1.0*i, 2.5*i} for i in range(100000)]

    record_np = np.fromiter(((1.0*i, 2.5*i)for i in range(100000)), dtype=[('x','d'), ('y','d')])
    
allocate()
