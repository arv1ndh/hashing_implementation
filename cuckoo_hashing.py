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
            print("FOUND")
            return self.H[0][hashes[0]][1]
        elif self.H[1][hashes[1]] is not None and self.H[1][hashes[1]][0] == key:
            return self.H[1][hashes[1]][1]
        print("NOT FOUND")
        return -1

    def set(self, key, value):
        hashes = self.hash(key)
        i = 0
        #print(self.H[0][hashes[0]])
        #import sys
        #sys.exit()
        while key is not None and value is not None:
            if self.H[i][hashes[i]] is None:
                self.H[i][hashes[i]] = [key, value]
                key = None
                value = None
            else:
                key,self.H[i][hashes[i]][0] = self.H[i][hashes[i]][0], key
                value,self.H[i][hashes[i]][1] = self.H[i][hashes[i]][1], value
            i = 1 - i

    def delete(self, key):
        hashes = self.hash(key)
        if self.H[0][hashes[0]] == key:
            H1[hashes[0]] = None
            return 0
        if self.H[1][hashes[1]] == key:
            H1[hashes[1]] = None
            return 0
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

def main():
    hash_obj = Hash_Table(8)
    hash_obj.set(4, 30)
    hash_obj.set(1, 90)
    hash_obj.set(2, 70)
    hash_obj.print_state()
    hash_obj.search(4)
    hash_obj.search(29)
    hash_obj.delete(3)
    hash_obj.delete(4)
    hash_obj.print_state()

if __name__ == "__main__":
    main()
