# Discreet Log Contracts

From [Discreet Log Contracts](https://adiabat.github.io/dlc.pdf) by Thaddeus Dryja. Goal of this repository is to give a educational implementation of the technical note.

Note that this works only with Schnorr signatures. 

## Scenario

Alice and Bob must first find each other and agree on the terms of the contract. Alice is buying Yen for satoshis with delivery on Friday, while Bob is selling Yen for satoshis. Both need to know the price of Yen in satoshis on Friday.

Alice and Bob have funds in a multisignature address.

## Steps

The "contract" is a large number of transaction spending the funding output: one transaction per possible price of the yen in satoshis on Friday.

The steps of the protocol (not summarized in the technical note) can be summarized as follows:

1. Alice and Bob want to stipulate a contract. They agree on using Olivia as oracle
1. Olivia publishes $R$, a curve point specific for this contract
1. Alice and Bob then proceed to create a large number of transactions spending the funding output. The output of the multisignature can only be spent once, so **only one of the transactions which make up the contract will ever appear on the blockchain**
    1. Alice and Bob do not yet know which and so multiple transactions need to be signed and stored by both of them
    1. In practice,  parties agree on the contract state but hold variations of the same transaction (same as Lighning Network): each closing transaction is based on a different possible price at closing time

## Files

- `schnorr_lib.py` is the same library of the [Schnorr signature repository](https://github.com/BITPoliTO/schnorr-sig)
- `main.py` is the main file, a demo of the steps of the discreet logaritm contract described in the mentioned technical note
