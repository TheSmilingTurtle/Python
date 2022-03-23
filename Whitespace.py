import subprocess
import numpy as np
data = ""
while len(data)<2000:
    if np.random.random()<len(data)/2000:
        data+="A"
    else:
        data+="a"
subprocess.run("pbcopy", universal_newlines=True, input=data)