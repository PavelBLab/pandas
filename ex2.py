import numpy as np
print('ok')

newArray = np.arange(0, 36)
newArray.resize(6,6)
print(newArray)
print(newArray[:,::7])
print(newArray.reshape(36))
print(newArray.reshape(36)[::7])
