import pandas as pd
import re

pattern = r'([a-zA-Z\s]+):(.+)'

data = {
    'name': [],
    'line': []
}

with open('All_merged.txt', 'r') as file:
    for line in file.readlines():
        match = re.findall(pattern, line)
        if match:
            name, line = match[0]
            data['name'].append(name)
            data['line'].append(line)

df = pd.DataFrame(data)

df.to_csv('merged.csv', index=False)