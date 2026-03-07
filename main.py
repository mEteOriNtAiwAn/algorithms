def all_unique(list_num:list)->bool:
    dict_value = {}
    for num in list_num:
        val = dict_value.setdefault(num, 0)
        if(val != 0): return False
        dict_value[num] += 1

    return True

print(all_unique([3,2,3,4]))