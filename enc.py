from util import *
import numpy as np
from scipy.linalg import block_diag

def buildGadget(l, n):
	# the secret vector [s] is an (n-1)-dimensional vector,
	# the secret key [t] is -s‖1, an n-dimensional vector
	# the error vector [e] is an m-dimensional vector
	# the matrix [A] is an (n-1)×m matrix (n-1 rows, m = n×l columns)
	# the public key [B] is ( A) which is an n×m matrix
	# 						( sA+e )

	g = 2**np.arange(l)
	return block_diag(*[g for null in range(n)])

def encrypt(keys, message):
	stat("Encrypting message")
	# the gadget matrix [G] is an n×m matrix (n rows, m = n×l columns)
	# the matrix R is an m×m matrix (n×l rows, n×l columns)
	# the ciphertext is (n×m)⋅(m×m) *> an n×m matrix

	R = np.random.randint(2, size=(keys.m, keys.m), dtype=np.int64).astype(keys.datatype)
	G = buildGadget(keys.l, keys.n)
	return (np.dot(keys.PK, R) + message*G) % keys.q

