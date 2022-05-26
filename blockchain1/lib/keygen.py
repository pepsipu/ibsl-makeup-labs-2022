from os import urandom
from bitcoin import SelectParams
from bitcoin.wallet import CBitcoinSecret, P2PKHBitcoinAddress

SelectParams("testnet")

seckey = CBitcoinSecret.from_secret_bytes(urandom(32))

# idk why but this wasn't working for me, i made some small changes
# nvm i didnt realize i needed SelectParams testnet :skull:
print(f"Private key: {seckey}")
print(f"Address: {P2PKHBitcoinAddress.from_pubkey(seckey.pub)}")
