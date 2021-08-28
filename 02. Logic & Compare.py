#https://www.youtube.com/watch?v=-FqgZRDRuIM&list=PLZS-MHyEIRo59lUBwU-XHH7Ymmb04ffOY&index=13
#1. -----0+++++5-----8+++++11------ 
print('1. Check whether input(x) has the value 0<x<5 and 8<x<11')
inp1 =float(input('Input number:'))
gt0  = inp1>0
lt5  = inp1<5
gt8  = inp1>8
lt11 = inp1<11
ans1 = (gt0 and lt5) or (gt8 and lt11)
print((5*'-')+'0'+(5*'+')+'5'+(5*'-')+'8'+(5*'+')+'11')
print('Check:',ans1)
print(40*'=')
#2. +++++0-----5+++++8-----11++++++
#print('Check whether input(x) has the value x<0, 5<x<8, x>11')
print('2. Check whether input(x) has the value x<0, 5<x<8, x>11')
inp2 =float(input('Input number:'))
lt0  = inp2<0
gt5  = inp2>5
lt8  = inp2<8
gt11 = inp2>11
ans2 = lt0 or (gt5 and lt8) or gt11
print((5*'+')+'0'+(5*'-')+'5'+(5*'+')+'8'+(5*'-')+'11')
print('Check:',ans2)
print(40*'=')