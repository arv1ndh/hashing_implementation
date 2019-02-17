import chained_hashing
import cuckoo_hashing
import linear_hashing
import quadratic_hashing
import random

HASH_TYPE = ["chained_hashing"]#, "cuckoo_hashing", "linear_hashing", "quadratic_hashing"]
ACTION = ["set"]#, "search", "delete"]

def generate_random_keys(size):
    result_list = []
    i = 0
    while i < size:
        number = random.randint(0, size * 100)
        if number not in result_list:
            result_list.append(number)
            i += 1
    return result_list

def list_randomizer(keys_pool):
    temp_list = keys_pool.copy()
    random.shuffle(temp_list)
    return temp_list

def main():
    action_dict = {}
    size = int(input("Enter Size: "))
    keys_pool = generate_random_keys(size)
    print("Generated Random Keys pool")
    action_dict["set"] = map(lambda x: (x, x*10), keys_pool)
    print("Generate Test cases for set")
    action_dict["delete"] = list_randomizer(keys_pool)
    print("Generate Test cases for delete")
    action_dict["search"] = list_randomizer(keys_pool)
    print("Generate Test cases for search")
    for hash_table in HASH_TYPE:
        hash_obj = eval(hash_table).Hash_Table(size)
        print("Evaluating hash table of size " + str(size) + " using " + hash_table)
        for action in ACTION:
            print("Action--> " + action)
            data = action_dict[action]
            action_obj = getattr(hash_obj, action)
        for value in data:
            if action == "set":
                action_obj(value[0], value[1])
            else:
                action_obj(value)
        hash_obj.print_state()

if __name__ == "__main__":
    main()
