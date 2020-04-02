def weight_on_planets():
   # write your code here
   weight = input('What do you weigh on earth? ')
   weight = float(weight)
   print(f'\nOn Mars you would weigh {.38*weight} pounds.\nOn Jupiter you would weigh {2.34*weight} pounds.')
   
   
if __name__ == '__main__':
   weight_on_planets()