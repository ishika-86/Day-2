def interchange(new_list):
    new_list[0], new_list[-1] = new_list[-1], new_list[0]
    return new_list


lst = [3, 6, 9, 12, 15]
print(interchange(lst))
