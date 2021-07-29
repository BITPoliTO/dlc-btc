from schnorr_lib import *
import hashlib
import os


# priv key of Alice as bytes adn int
a = os.urandom(32)
aint = (int(a.hex(), 16) % n)

# priv key of Bob as bytes adn int
b = os.urandom(32)
bint = (int(b.hex(), 16) % n)

# priv key of Olivia as bytes adn int
v = os.urandom(32)
vint = (int(v.hex(), 16) % n)

# priv key of Alice and Bob for multisig address as bytes adn int
amulti = os.urandom(32)
amultiint = (int(amulti.hex(), 16) % n)
bmulti = os.urandom(32)
bmultiint = (int(bmulti.hex(), 16) % n)


# pubkey of Alice Bob and Olivia as point-bytes
pubkeyA = pubkey_gen_from_int(aint)
pubkeyB = pubkey_gen_from_int(bint)
pubkeyV = pubkey_gen_from_int(vint)

pubkeyA_aspoint=point_mul(G,aint)
pubkeyB_aspoint=point_mul(G,bint)
pubkeyV_aspoint=point_mul(G,vint)

pubkeyAmulti_aspoint = pubkey_gen_from_int(amultiint)
pubkeyBmulti_aspoint = pubkey_gen_from_int(bmultiint)

print("\nThese points are published by all parties")
print("Alice's pubkey is:\t",pubkeyA.hex())
print("Bob's pubkey is:\t",pubkeyB.hex())
print("Olivia's pubkey is:\t",pubkeyV.hex())

print("\nThese points are Alice's and Bob's multisig")
print("Alice's pubkey is:\t",pubkeyAmulti_aspoint.hex())
print("Bob's pubkey is:\t",pubkeyBmulti_aspoint.hex())

# nonce creation
k = os.urandom(32)
kint = (int(k.hex(), 16) % n)

R = pubkey_gen_from_int(kint)
R_aspoint = point_mul(G,kint)
print("\nThis point is published by Olivia")
print("Point from nonce:\t",R.hex())

print("\nLet's say the price of the Yen on Friday is around 1000 satoshis. Therefore possible transactions are")

SiG_array = []
Si_array = []
prices = [925,950,1000,1025,1050]

print("\nPrice\ts_iG\tPubAi\tPubBi")
for i in  prices:
    i_as_bytes = i.to_bytes(32,'big') # this is a spec thing, we try
    hiR = hash_sha256(i_as_bytes+bytes_from_point(R_aspoint))
    hiR_V = point_mul(pubkeyV_aspoint,int_from_bytes(hiR))

    siG = point_add(R_aspoint,opposite(hiR_V))
    SiG_array.append(siG)
    PubAi = point_add(pubkeyA_aspoint,siG)
    PubBi = point_add(pubkeyB_aspoint,siG)
    print(i,"\t",siG,"\t",PubAi,"\t",PubBi)

print("\nPrice\ts_i")
for i in prices:
    i_as_bytes = i.to_bytes(32,'big') # this is a spec thing, we try
    hiR = hash_sha256(i_as_bytes+bytes_from_point(R_aspoint))
    si = (kint - int_from_bytes(hiR)*vint) % n
    Si_array.append(si)
    print(i,"\t",si)

print ("\nCompare s_iG with s_i * G: are they equal?")
for i in range(len(prices)):
    print(prices[i],":\t",point_mul(G,Si_array[i])==SiG_array[i])



