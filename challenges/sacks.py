'''
Created on 10 Jun 2018

@author: katharinemurphy
'''
sack_type = input('Please enter the type of sack, C, G or S :')
#validate input type
sack_weight = float(input('Please enter the weight of the sack: '))
#validate input weight


class sack:
    type = ''
    weight = 0.0
    
    def validate_sack(type, weight):
        if (type == 'S' or type =='G'):
            print("weight is between 49.9 and 50.1 kg")
        #weight must be between 49.9 and 50.1 kg
        elif type == 'C':
            print("weight is between 24.9 and 25.1 kg")
        #weight must be between 24.9 and 25.1 kg
        else:
            print("weight is incorrect, please check")
    


sack.validate_sack(sack_type, sack_weight)




#create order
order_cement = int(input('How many sacks of cement do you need? : '))
order_gravel = int(input('How many sacks of gravel do you need? : '))
order_sand = int(input('How many sacks of sand do you need? : '))

cement_sacks = sack[order_cement]
gravel_sacks = sack[order_gravel]
sand_sacks = sack[order_sand]

validate_sack('C', 25.0)
validate_sack('S', 50.0)
validate_sack('G', 50.0)

