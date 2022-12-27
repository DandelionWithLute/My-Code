Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'} 
print("Dictionary:",end='') 
print(Dict)
print(Dict[1])

# Python program to demonstrate
# defaultdict
  
  
from collections import defaultdict
  
  
# Function to return a default
# values for keys that is not
# present
def def_value():
    return "Not Present"
      
# Defining the dict
d = defaultdict(def_value)
d["a"] = 1
d["b"] = 2

print(d)
print(d["a"])
print(d["b"])
print(d["c"])