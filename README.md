# Sirex
SiRex - Simple Regex - A package to use regex commands on strings using simple function calls


## Usage

Sirex has many functions that help you do  regex function calls on strings  <br>
Please see the documentation for the different functions

## Installation 
```
pip install sirex
```

## Usage 
```

import sirex.numeric as srnum  #Sirex Numeric functions 
srnum.count_numbers("Hell123ow 123") # Get the count of numbers 
result2d = srnum  .smallest_number("hello123 34")
print("Result_2c = {}".format(result2d))


import sirex.string as srst # String Functions 
result3a = srst.count_occurance("this" , "this is This",True)
print("result3a = {}".format(result3a))

```
You can also find a tester file with sample code for usage of all the functions \
and modules in the home folder of this package ```test_sirex.py```(https://github.com/pythoslabs/sirex/blob/master/test_sirex.py)


## Detailed Documentation

A detailed and updated documentation can be found here : 

[sirex.readthedocs.io](https://sirex.readthedocs.io/en/latest/)
