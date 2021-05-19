from bit import PrivateKeyTestnet
import json
import requests
from bit.network import satoshi_to_currency_cached

info = open('key.json',)
res = json.load(info)
my_address = PrivateKeyTestnet(res['wei'])

def key_info():
    print(my_address.version)
    print(my_address.to_wif())
    print(my_address.address)

def get_balance_in_usd(address):
    if address == my_address.address:
        return my_address.get_balance('usd')
    else:
        res = requests.get('https://api.blockcypher.com/v1/btc/test3/addrs/'+address+'/balance')
        return satoshi_to_currency_cached(res.json()['balance'], 'usd')

address1 = '2NCbndYcPYaLWLtiqPSn3HobPkyAEXd7e1G'
amount_in_usd1 = 1
address2 = 'mkH41dfD4S8DEoSfcVSvEfpyZ9siogWWtr'
amount_in_usd2 = 1.1

print('Before transaction, balance: ' + str(get_balance_in_usd(my_address.address)))
print('Before transaction, balance: ' + str(get_balance_in_usd(address1)))
print('Before transaction, balance: ' + str(get_balance_in_usd(address2)))

tx_hash = my_address.send([(address1, amount_in_usd1, 'usd'), (address2, amount_in_usd2, 'usd')])
print(tx_hash)

