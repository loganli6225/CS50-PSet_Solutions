def print_list():
    input_list = get_inputs()
    sorted = sorts_inputs(input_list)
    final_list = ""
    for key in sorted:
        final_list = f"{final_list}\n{input_list[key]} {key}"
    print(final_list)

def get_inputs():
    dict_of_groc_list = {}
    while True:
        try:
            item = input().upper()
        except EOFError:
            break
        else:
            dict_of_groc_list.setdefault(item, 0)
            dict_of_groc_list[item] += 1
    return dict_of_groc_list

def sorts_inputs(dict):
    list_of_sorted_keys = sorted(dict)
    return list_of_sorted_keys

print_list()
