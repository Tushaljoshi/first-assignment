# -*- coding: utf-8 -*-
"""assignment1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/103HhZHqqtAzYgsrSA9ShSgAGUkfZINgi
"""

import random # library provide for generating random numbers
import matplotlib.pyplot as plt # used to creating static , animated and interactive visualization in python

mapping_dict = dict(zip(range(0,10),range(0,10))) #this line of code create a dictionary using "zip" function and the "range" function

mapping_dict

for k in mapping_dict.keys(): #this loop iterates through all the keys in the 'mapping_dict'

  mapping_dict[k] = str(mapping_dict[k])

mapping_dict

for i in range(0,26): #loop that iterates over the values of'i'from 0 to 26
  mapping_dict[10+i] = chr(65+i) #this line new key_value pairs to the 'mapping_dict'

mapping_dict

sample_size = 5000000 #this variable is set to 5000000

random_numbers = list() #the number of random string the code will generate

for i in range(0,sample_size): #lopp that iterates "sample_size" times for each iteration

  blank_str = str() #it initializes an empty string "blanks_str" to store the random string

  random_digit = random.randint(0,35) # geneate random nunber between (0 to 35)
  blank_str = blank_str + mapping_dict[random_digit] #The value is appended in the blank_str.

  random_digit = random.randint(0,35)
  blank_str = blank_str + mapping_dict[random_digit]

  for i in range(0,8): #loop is initiated, which runs 8 times. In each iteration
    coin_toss = random.randint(0,1) # A coin toss is simulated by generating a random number (0 or 1).

    if coin_toss == 1:

      random_digit = random.randint(0,35)
      blank_str = blank_str + mapping_dict[random_digit]

    else:
      break

  random_numbers.append(blank_str)

reverse_mapping_dict = dict() #This initializes an empty dictionary, which is storyin reversed mapping

for k in mapping_dict.keys():
  reverse_mapping_dict[mapping_dict[k]] = k # for each key 'k',it retrieves the corresponding value from 'mapping_dict'

base_frequency = dict() #Initializes an empty dictionary called base_frequency that will store the frequency of each highest base.

for blank_str in random_numbers:
  highest_digit = max(blank_str) #it finds the highest digit in the current blank_str
  highest_base = reverse_mapping_dict[highest_digit] + 1 #it looks up the corresponding base for the highest digit
  if highest_base in base_frequency.keys():
    base_frequency[highest_base] += (1/sample_size)
  else:
    base_frequency[highest_base] = (1/sample_size)

plt.bar(x=base_frequency.keys(),height=base_frequency.values())
#his code snippet uses Matplotlib to create a bar chart based on the frequency data stored in the base_frequency

