# Quantum Ready Homomorphic Encryption

Quantum-resistant homomorphic encryption scheme that can eventually be used to encrypt data for blind quantum computation. From the paper "Homomorphic Encryption for Distributed Computing" by Nolan Hedglin, Kade Phillips, and Andrew Reilley from MIT.

## Run

`python test.py`

For client-server version first generate ciphertexts cA and cB with demoClient.py

`python demoClient.py`

then run the server interactively

`python -i demoServer.py`