from bitcoinlib.wallets import Wallet, wallet_delete

from bitcoinlib.mnemonic import Mnemonic

passphrase = Mnemonic().generate()

with open('passphrase.txt', 'w+') as f:
    f.write(passphrase)

wallet = Wallet.create("mWallet1", keys=passphrase, network='bitcoin')

key1 = wallet.new_key()

print(key1.address)