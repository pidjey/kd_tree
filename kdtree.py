class Kd_node:

    def __init__(self, a=None, b=None, isX=0):
        self.data = (a,b)
        self.isX = isX
        self.next = None

    def add_child_number(self):
        self.next = [None] * 2

    def add_child(self, a, b, pos=0):
        if (self.next == None) :
            this.add_child_number()
        isX = self.isX
        if(isX==1):
           isX=0
        else:
            isX=isX+1
        self.next[pos] = Kd_node(a, b, isX)

    def get_child(self, pos=0):
        if(pos != 0 and pos != 1):
            return None
        return self.next[pos]

    def get_data(self, pos=0):
        return self.data[self.isX]

    def remove_child(self, pos=0):
        if(pos != 0 and pos != 1):
            return None
        self.next[pos] = None

class Kd_tree:
    def __init__(self):
        self.root = None

    def add_root(self, a,b):
        self.root = Kd_node(a,b)

    def get_root(self):
        return self.root

    def mount_from_points( self, node, points, isX=0):
        if(isX == 0):
            points = sorted(points, key=lambda x: x[1])
        else:
            points = sorted(points)
        n = len(points)-1

        print(points)
        if(n==1 or n==None):

            pivot = points[n]
            node = Kd_node(pivot[0], pivot[1])
            node.add_child_number()
            return
        else:
            leftpoints = points[:int(n/2)]
            pivot = points[int(n/2)]
            rightpoints = points[int(n/2)+1:]
        
        
            node = Kd_node(pivot[0], pivot[1])
            node.add_child_number()
            pivot = points[int(n/2)]
            self.mount_from_points( node.get_child(0),leftpoints)
            self.mount_from_points( node.get_child(1),rightpoints)


points = [(10,9), (7,13), (8,14)]


a = Kd_node(1,2)

a.add_child_number()
a.add_child(2,5,0)
a.add_child(1,100,1)

print(a.get_child(1).get_data())

b = Kd_tree()
b.add_root(1,2)
root = b.get_root()
b.mount_from_points(root, [(1,2), (1,7),(100,2), (3,10), (2,100), (3,1)])

print(b.get_root().get_data())
