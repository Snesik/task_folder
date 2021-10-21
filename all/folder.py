import json
import os
import os.path
import sys

try:
    there_look = sys.argv[1]
except IndexError:
    pass

def txt(there_look: str):
    with open(there_look) as f:
        try:
            text = f.readlines()
            return str(len(text)) + ' lines'
        except UnicodeDecodeError:
            print('Error decode ' + there_look)


def size(there_look: str):
    return str(os.path.getsize(there_look)) + ' bytes'


def tree(there_look : str):
    results = {}
    for (dirthere_look, dirnames, filenames) in os.walk(there_look):
        parts = dirthere_look.split(os.sep)
        curr = results
        for p in parts:
            if p == '':
                continue
            curr = curr.setdefault(p, {})
            if dirthere_look.split('/')[-1] == p:
                for name in filenames:
                    if name.endswith('.txt'):
                        curr.setdefault(name, {'type': 'txt', 'size': f'{txt(dirthere_look + "/" + name)}'})
                    elif name.endswith('.bin'):
                        curr.setdefault(name, {'type': 'binary', 'size': f'{size(dirthere_look + "/" + name)}'})

    return json.dumps(results)

#print(tree(there_look))


