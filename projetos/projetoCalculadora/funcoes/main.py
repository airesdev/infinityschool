'''import whole module'''
# import addFunctions
# print(addFunctions.dois(20, 10))

'''import especific functions'''
# from addFunctions import tres
# print(tres(30, 20, 10))

'''questão1'''
# from subFunctions import dois
# print(dois(20, 10))

'''call a module's function by another name'''
from addFunctions import quatro as somarQuatro
print(somarQuatro(40, 30, 20, 10))