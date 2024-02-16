from typing import List, Tuple
from blend import computeColor, blendColor, id_color_map, color_list
from json import dumps

gen_map = {}
search_list = [(list(color_list[index]), [index]) for index in range(len(color_list))]
f = open('data', 'w')

while search_list:
    present:Tuple[List[int], List[int]] = search_list.pop(0)
    key = tuple(present[0])
    color_way = gen_map.get(key, None)
    if color_way == None:
        f.write(dumps(present) + '\n')
        gen_map[key] = len(present[1])
    
    if len(present[1]) <= 5:
        for index in range(len(color_list)):
            method = present[1][:]
            method.append(index)
            search_list.append((blendColor(present[0], color_list[index]), method))
    
f.close()