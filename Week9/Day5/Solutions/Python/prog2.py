import numpy as np
string = input().replace(" ","")
string = np.array([i for i in string])
print("Output:",*string)
