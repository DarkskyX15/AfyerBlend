from blend import hexColorTuple, computeColor, interpretPreCal, agree_list
from typing import Dict, List
from base64 import b64decode
from json import loads
from os import system

with open('clrdt', 'rb') as f:
    precomc: Dict[str, List] = loads(b64decode(f.read()))

while True:
    raw_input = input('Input #HEX of a color or RGB values seperated by space:\n>')
    try:
        if raw_input[0] != '#':
            res = precomc.get(hexColorTuple(map(int, raw_input.split())), None)
        else:
            res = precomc.get(raw_input.lower(), None)
        if res == None:
            print('No pre-calculated result found, use computed result:')
            computeColor(raw_input)
        else:
            print('Found pre-calculated result:')
            interpretPreCal(res)
    except Exception as e:
        print('[ERROR]:', e.args)
    finally:
        if input('Continue to blend other colors? [Y(es)/Other]: \n>') in agree_list:
            system('cls')
        else: break
