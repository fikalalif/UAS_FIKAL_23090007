import numpy as np

data = np.array([ 
    [90,80],
    [50,60],
    [65,70]
])

total_perbaris = np.sum(data, axis=0)
total_pekolom = np.sum(data, axis=1)

print(total_perbaris)
print(total_pekolom)




