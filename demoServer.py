import numpy as np
np.set_printoptions(threshold=np.inf, linewidth=np.inf)

# Generate ciphertexts cA and cB with demoClient.py
# Then run interactively -> python -i demoServer.py

from util import text2array

homebase = '/tmp/'

fh = open(homebase + 'cA', 'r')
ca = text2array(fh.read())
fh.close()

print('Loaded [ca] from ' + homebase + 'cA')
fh = open(homebase + 'cB', 'r')
cb = text2array(fh.read())
fh.close()

print('Loaded [cb] from ' + homebase + 'cB')

def write2file(c):
	fh = open(homebase + 'fAB', 'w')
	print(c, file=fh)
	fh.close()
	print('Wrote matrix to ' + homebase + 'fAB')