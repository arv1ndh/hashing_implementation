import random

H_TYPE = ["chained_hashing", "cuckoo_hashing", "linear_hashing", "quadratic_hashing"]
ACTION = ["delete", "search", "set"]

def main():
    size = int(input("Enter Size: "))
    numbers_pool = [ _ for _ in range(size)]
    keys_pool = []
    action_string = H_TYPE[random.randint(0,3)] + " " + str(size)
    random_actions = [action_string]
    i = 0
    while i < size:
        action = ACTION[random.randint(0,2)]
        if action == "set":
            n_l = len(numbers_pool)
            r_index = random.randint(0,n_l-1)
            key = numbers_pool.pop(r_index)
            #except:
            #    print("HIT")
            #    print(r_index)
            #    print(numbers_pool)
            #    import sys
            #    sys.exit()
            value = key * 10
            keys_pool.append(key)
            action_string = "{} {} {}".format(action,str(key),str(value))
        else:
            k_l = len(keys_pool)
            if k_l == 0:
                continue
            r_index = random.randint(0,k_l-1)
            if action == "delete":
                key = keys_pool.pop(r_index)
                numbers_pool.append(key)
            else:
                key = keys_pool[r_index]
            action_string = "{} {}".format(action, str(key))
        random_actions.append(action_string)
        i += 1
    with open("test_cases", "w") as fp:
        fp.write("\n".join(random_actions))

if __name__ == "__main__":
    main()
