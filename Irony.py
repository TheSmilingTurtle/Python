import numpy as np
import subprocess

input_string = input("Input a string: ").lower()
product_string = ""

if input_string:
    for i in range(len(input_string)):

        if np.random.random() < 0.5:
            product_string += input_string[i].upper()
        else:
            product_string += input_string[i]
    

    print("\nThe output is: {}".format(product_string))
    subprocess.run("pbcopy", universal_newlines=True, input=product_string)
    print("copied\n")