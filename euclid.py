def gcdExtended(a, b):

    rem = a % b

    if rem == 0 and b == 1:

        return (1, 1-a//b)

    elif rem == 0 and b != 1:

        return "gcd != 1"

    temp = gcdExtended(b, rem)

    if temp == "gcd != 1":

        return "not coprime"
               
    else:
        
        return (temp[1], temp[0] - a//b * temp[1])


print(gcdExtended(11, 9))

# class Val:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y

# def gcd_ext(a,b):

#     rem = a % b

#     if rem == 0:
#         return Val(x = 1, y = 1-a//b)
    
#     temp = gcd_ext(b, rem)

#     return Val(x = temp.y, y = temp.x - a//b * temp.y)