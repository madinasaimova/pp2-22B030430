import json

with open('sample.json', 'r') as f:
    data = json.load(f)
print("""Interface Status
================================================================================
DN                                                 Description           Speed    MTU  
-------------------------------------------------- --------------------  ------  ------""")
if 'imdata' in data:
    for x in data['imdata']:
        print(x['l1PhysIf']['attributes']['dn'], end= '                               ')
        print(x['l1PhysIf']['attributes']['speed'], end= '  ')
        print(x['l1PhysIf']['attributes']['mtu'], end= '\n')