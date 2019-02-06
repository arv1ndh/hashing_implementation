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
        self.H[i].append((key, value))
        return 0

    def search(self, key):
        index = self.hash(key)
        collec = self.H[index]
        if collec is None:
            print("Key Not found")
            return -1
        for i in range(len(collec)):
            if collec[i][0] == key:
                print("Key found")
                return (index, i)
        return -1

    def delete(self, key):
        temp = self.search(key)
        if temp == -1:
            print("Key is not present to be deleted")
            return -1
        index, col_index = temp
        collec = self.H[index]
        k, v = collec.pop(col_index)
        print(k, " -- ", v, "Has been deleted")
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
                o_str += "{}-{}==>".format(k,v)
            print(o_str)

def main():
    hash_obj = Hash_Table(8)
    hash_obj.set(4, 30)
    hash_obj.set(1, 90)
    hash_obj.set(2, 70)
    hash_obj.set(9, 70)
    hash_obj.print_state()
    hash_obj.search(4)
    hash_obj.search(29)
    hash_obj.delete(3)
    hash_obj.delete(4)
    hash_obj.print_state()
    hash_obj.set(4, 30)
    hash_obj.set(12, 30)
    hash_obj.print_state()


if __name__ == "__main__":
    main()
