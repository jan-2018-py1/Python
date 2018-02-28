
"""
name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]
"""

"""
def make_dict(list1, list2):
    new_dict = {}
    new_dict_zip = zip(list1, list2)
    new_dict = dict(new_dict_zip)
    return new_dict
"""

name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def make_dict(list1, list2):
    if len(list1) == len(list2) or len(list1) > len(list2):
        new_dict = {}
        new_dict_zip = zip(list1, list2)
        new_dict = dict(new_dict_zip)
        return new_dict
    elif len(list1) < len(list2):
        new_dict = {}
        new_dict_zip = zip(list2, list1)
        new_dict = dict(new_dict_zip)
        return new_dict

x = make_dict(name, favorite_animal)
print x