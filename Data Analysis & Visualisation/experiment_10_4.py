import pandas as pd
import numpy as np
data = {'X': [78, 85, 96, 80, 86], 
        'Y': [84, 94, 89, 83, 86], 
        'Z': [86, 97, 96, 72, 83]}
df = pd.DataFrame(data)
result = pd.DataFrame({
    'X': df['X'],
    'Y': df['Y'],
    'Z': df['Z']
})
print(result)