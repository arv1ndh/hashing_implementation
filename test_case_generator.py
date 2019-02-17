import random

def list_filler(size, flag = 0):
    numbers_pool = [ _ for _ in range(size)]
    i = 0
    result_list = []
    while i < size:
        n_l = len(numbers_pool)
        r_index = random.randint(0, n_l-1)
        key = numbers_pool.pop(r_index)
        if flag == 1:
            value = key * 10
            fmt_string = "{} {}".format(str(key), str(value))
        else:
            fmt_string = str(key)
        result_list.append(fmt_string)
        i += 1
    return result_list



def main():
    size = int(input("Enter Size: "))
    set_list = list_filler(size, 1)
    del_list = list_filler(size)
    search_list = list_filler(size)
    with open("insert_test_cases", "w") as fp:
        fp.write("\n".join(set_list))
    with open("delete_test_cases", "w") as fp:
        fp.write("\n".join(del_list))
    with open("search_test_cases", "w") as fp:
        fp.write("\n".join(search_list))

if __name__ == "__main__":
    main()
