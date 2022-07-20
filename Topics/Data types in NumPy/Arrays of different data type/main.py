import numpy as np


array = np.array([[-34, 2, 0],
                  [0, -4, 123],
                  [-201, 0, -3]], dtype=np.int64)
i1 = int(input())
i2 = int(input())
print(array[i1].astype(np.str_))
print(array[i2].astype(np.float64))
