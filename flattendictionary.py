# Given a dictionary dict, write a function flattenDictionary that returns a
# flattened version of it . (Assume that values are either an integer, string,
# or another dictionary.)

# Example:
# input:  dict = {
#             "Key1" : "1",
#             "Key2" : {
#                 "a" : "2",
#                 "b" : "3",
#                 "c" : {
#                     "d" : "3",
#                     "e" : "1"
#                 }
#             }
#         }
#
# output: {
#             "Key1" : "1",
#             "Key2.a" : "2",
#             "Key2.b" : "3",
#             "Key2.c.d" : "3",
#             "Key2.c.e" : "1"
#         }

# Important: when you concatenate keys, make sure to add the dot character
# between them. For instance concatenating Key2, c and d the result key would
# be Key2.c.d.

def flatten_dictionary(dictionary):
  flattened = {}
  recurse(dictionary, flattened, '')
  return flattened

def recurse(dictionary, flattened, prefix):
  for key in dictionary:
    if prefix == '':
      new_key = key
    else:
      new_key = prefix + "." + key
    if not isinstance(dictionary[key],dict):
      flattened[new_key] = dictionary[key]
    else:
      recurse(dictionary[key], flattened, new_key)
