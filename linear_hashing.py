import os

class Hash_Table:
    def __init__(self, N):
        self.N = N
        self.H = [None]*self.N
        #self.no_of_elements = 0

    def hash(self, key):
        return key % self.N

    def search(self, key):
        i = self.hash(key)
        while self.H[i] is not None and self.H[i][0] != key:
            i = (i+1) % self.N
            if i == self.hash(key):
                print("Key not Found")
                return -1
        if H[i] is None:
            print("Key not Found")
            return -1
        return self.H[i][1]

    def set(self, key, value):
        i = self.hash(key)
        while self.H[i] is not None and self.H[i][0] != key:
            i = (i+1) % self.N
            if i == self.hash(key):
                print("Hash Table is full, no more insertions allowed")
                return -1
        self.H[i] = [key, value]
        return 0

    def print_state(self):
        print("index, key, value")
        for i in range(self.N):
            if self.H[i] is None:
                print(i, None)
            else:
                print(i, self.H[i][0], self.H[i][1])


def main():
    hash_obj = Hash_Table(7)
    hash_obj.set(4, 30)
    hash_obj.set(1, 90)
    hash_obj.set(2, 70)
    hash_obj.print_state()

if __name__ == "__main__":
    main()
