import chained_hashing
import cuckoo_hashing
import linear_hashing
import quadratic_hashing
import random
import time

HASH_TYPE = ["cuckoo_hashing", "chained_hashing", "linear_hashing", "quadratic_hashing"]
ACTION = ["set", "search", "delete"]

def generate_random_keys(size, load_factor):
    result_list = []
    i = 0
    while i < size * load_factor:
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
    size = int(input("Enter Size(0-100000): "))
    if size < 0  or size > 100000:
        print("Invalid Size")
        exit()
    load_factor = float(input("Enter Load Factor(0-1.0): "))
    if load_factor < 0.0 or load_factor > 1.0:
        print("Invalid Load Factor")
        exit()
    keys_pool = generate_random_keys(size,load_factor)
    max_n = len(keys_pool)
    print("Generated Random Keys pool of size: ", max_n)
    action_dict["set"] = list(map(lambda x: (x, x*10+1), keys_pool))
    print("Generated Test cases for set")
    action_dict["delete"] = list_randomizer(keys_pool)
    print("Generated Test cases for delete")
    action_dict["search"] = list_randomizer(keys_pool)
    print("Generated Test cases for search")
    for hash_table in HASH_TYPE:
        hash_obj = eval(hash_table).Hash_Table(size)
        print("Evaluating hash table of size: " + str(size) + " with max load factor: " + str(load_factor) + " using " + hash_table)
        for action in ACTION:
            success = 0
            failure = 0
            print("Action--> " + action)
            data = action_dict[action]
            action_obj = getattr(hash_obj, action)
            start = time.time()
            for value in data:
                if action == "set":
                    ret = action_obj(value[0], value[1])
                else:
                    ret = action_obj(value)
                if ret != -1:
                    success += 1
                else:
                    failure += 1
            print("Time Elapsed: ", str((time.time()-start)*1000), "ms")
            print("Successes: ",success," Failures: ",failure)
            print("Accuracy: ", round(success*100/max_n,2), "%") 

if __name__ == "__main__":
    main()
