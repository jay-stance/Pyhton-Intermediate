# from collections import Counter
# from sys import modules
# from itertools import permutations, combinations, accumulate, groupby
# import operator
# from functools import reduce

# myName = "Jay Stance"
# counted = Counter(myName)
# # print(counted)
# # print(counted.most_common(2))

# myList  = [1,2,3,4,5,6]
# # print(len(list(permutations(myList))))
# # print(list(accumulate(myList, func=operator.mul)))
# # print(operator.mul)

# # product = list(accumulate(myList, operator.mul))[-1]
# product = reduce(lambda x,y: x*y, myList)
# # print(product)
# print(__name__)
# import json

# myObj = {"name": "jay", "age": 3}
# myjson = json.dumps(myObj, indent=4)
# print(myjson)

# with open("main.json", "w") as file:
#     json.dump(myObj, file, indent=4)


# import numpy as np
# import random, secrets

# myList = list("asccimadimsd")
# # print(random.sample(myList, 3))
# # print(secrets.randbits(4))
# print(np.random.randint(1,3, (3,4)))
