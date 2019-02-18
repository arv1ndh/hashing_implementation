class Hash_Table:
    def __init__(self, N):
        self.N = N
        self.H = [None]*self.N
        self.n = 0

    def hash(self, key):
        return key % self.N

    def search(self, key):
        init_hash = self.hash(key)
        i = 1
        index = init_hash
        count = 0
        while self.H[index] is not None and self.H[index][0] != key:
            if count == self.n:
                return -1
            index = (init_hash + i*i) % self.N
            i = i + 1
            if type(self.H[index]) == int:
                count += 1
        if self.H[index] is None:
            return -1
        return index

    def set(self, key, value):
        if self.n == self.N:
            print("Hash Table is full, no more insertions allowed")
            return -1
        init_hash = self.hash(key)
        i = 1
        index = init_hash
        while self.H[index] is not None and type(self.H[index] == int) and self.H[index][0] != key:
            index = (init_hash + i + i*i) % self.N
            i = i + 1
        self.H[index] = [key, value]
        self.n += 1
        return 0

    def delete(self, key):
        index = self.search(key)
        if index == -1:
            return -1
        k,v = self.H[index]
        self.H[index] = "D"
        self.n -= 1
        return 0

    def print_state(self):
        print("index, key, value")
        for i in range(self.N):
            if self.H[i] is None:
                print(i, None)
            elif type(self.H[i]) == str:
                print(i, "D")
            else:
                print(i, self.H[i][0], self.H[i][1])
