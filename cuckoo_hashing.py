class Hash_Table:
    def __init__(self, N):
        self.N = N
        self.H = [[None]*self.N, [None]*self.N]

    def hash(self, key):
        h1 = key % self.N
        h2 = (key//self.N) % self.N
        return (h1,h2)

    def search(self, key):
        hashes = self.hash(key)
        if self.H[0][hashes[0]] is not None and self.H[0][hashes[0]][0] == key:
            return self.H[0][hashes[0]]#[1]
        elif self.H[1][hashes[1]] is not None and self.H[1][hashes[1]][0] == key:
            return self.H[1][hashes[1]]#[1]
        return -1

    def set(self, key, value):
        hashes = self.hash(key)
        i = 0
        count = 0
        while key is not None and value is not None:
            if count >= self.N:
                return -1
            if self.H[i][hashes[i]] is None:
                self.H[i][hashes[i]] = [key, value]
                key = None
                value = None
            else:
                key,self.H[i][hashes[i]][0] = self.H[i][hashes[i]][0], key
                value,self.H[i][hashes[i]][1] = self.H[i][hashes[i]][1], value
            i = 1 - i
            count += 1
        return 0

    def delete(self, key):
        present = self.search(key)
        if present == -1:
            return -1
        present = None
        return 0
        #hashes = self.hash(key)
        #if self.H[0][hashes[0]] is not None and self.H[0][hashes[0]][0] == key:
        #    self.H[0][hashes[0]] = None
        #    return 0
        #elif self.H[1][hashes[1]] is not None and self.H[1][hashes[1]][0] == key:
        #if self.H[1][hashes[1]][0] == key:
        #    self.H[1][hashes[1]] = None
        #    return 0
        return -1

    def print_state(self):
        print("Contents of H0")
        for i in range(self.N):
            if self.H[0][i] is None:
                print(i, None)
                continue
            print(i, self.H[0][i])
        print("Contents of H1")
        for i in range(self.N):
            if self.H[1][i] is None:
                print(i, None)
                continue
            print(i, self.H[1][i])
