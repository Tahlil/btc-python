from bit import PrivateKeyTestnet
import json

info = open('key.json',)
res = json.load(info)

my_key = PrivateKeyTestnet(res['wei'])
print(my_key.version)
print(my_key.to_wif())
print(my_key.address)