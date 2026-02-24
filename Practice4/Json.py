import json

with open('Practice4\sample-data.json', 'r') as file:
    data = json.load(file)

print("Interface Status")
print("=" * 80)

print(f"{'DN':<50} {'Description':<20} {'Speed':<7} {'MTU':<6}")

print(f"{'-' * 49} {'-' * 20} {'-' * 7} {'-' * 6}")

for item in data['imdata'][:3]:
    attributes = item['l1PhysIf']['attributes']
    
    dn = attributes['dn']
    descr = attributes['descr']
    speed = attributes['speed']
    mtu = attributes['mtu']
    
    print(f"{dn:<50} {descr:<20} {speed:<7} {mtu:<6}")