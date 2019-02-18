class Hash_Table:
    def __init__(self, N):
        self.N = N
        self.H = [None]*self.N

    def hash(self, key):
        return key % self.N

    def set(self, key, value):
        i = self.hash(key)
        if self.H[i] is None:
            self.H[i] = [(key, value)]
            return 0
        links = self.H[i]
        c_iter = 0
        while c_iter < len(links):
            if links[c_iter][0] == key:
                links[c_iter] = (key, value)
                return 0
            c_iter += 1
        self.H[i].append((key, value))
        return 0

    def search(self, key):
        index = self.hash(key)
        collec = self.H[index]
        if collec is None:
            return -1
        for i in range(len(collec)):
            if collec[i][0] == key:
                return (index, i)
        return -1

    def delete(self, key):
        temp = self.search(key)
        if temp == -1:
            return -1
        index, col_index = temp
        collec = self.H[index]
        k, v = collec.pop(col_index)
        return 0
    
    def print_state(self):
        for i in range(self.N):
            o_str = str(i) + "   "
            collec = self.H[i]
            if collec is None or not len(collec):
                o_str += "None"
                print(o_str)
                continue
            for k,v in collec:
                o_str += "==>{}:{}".format(k,v)
            print(o_str)
