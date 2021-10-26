d1 = {1: 2, 3: 4, 5: 6}
d2 = {'bob': 'marley', 'mariah': 'carey'}
d3 = {'jack': 1, 'michael': 2}
d4 = {}
d5 = {"who was in paris?": "niggas"}



def combine_5_dicts(dict1, dict2, dict3, dict4, dict5):
    new_dict = {}
    for key1 in dict1:
        value1 = dict1[key1]
        new_dict[key1] = value1

    for key2 in dict2:
        value2 = dict2[key2]
        new_dict[key2] = value2

    for key3 in dict3:
        value3 = dict3[key3]
        new_dict[key3] = value3

    for key4 in dict4:
        value4 = dict4[key4]
        new_dict[key4] = value4

    for key5 in dict5:
        value5 = dict5[key5]
        new_dict[key5] = value5

    return new_dict

def combine_2(dict1, dict2):
    new_dict1 = {}
    for key1 in dict1:
        value1 = dict1[key1]
        new_dict1[key1] = value1
        print(new_dict1)
        for key2 in dict2:
            value2 = dict2[key2]
            new_dict1[key2] = value2
            print(new_dict1)
    return new_dict1
print(combine_2({1: 2}, {3: 4}))
