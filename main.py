import chained_hashing
import cuckoo_hashing
import linear_hashing
import quadratic_hashing


def main():
    with open("test_cases", "r") as fp:
        contents = fp.read().split("\n")
    hashing_info = contents.pop(0)
    hash_table, size = hashing_info.split()
    size = int(size)
    hash_obj = eval(hash_table).Hash_Table(size)
    for line in contents:
        data_list = line.split()
        action = getattr(hash_obj, data_list[0])
        if len(data_list) == 3:
            action(int(data_list[1]), int(data_list[2]))
        else:
            action(int(data_list[1]))

if __name__ == "__main__":
    main()
