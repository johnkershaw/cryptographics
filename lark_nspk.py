# pip install lark --upgrade
# or 
# sudo apt install python3-lark

from lark import Lark

l = Lark('''
         A|B|S :                     Principal     
 Na,Nb :                     Nonce         
 KPa,KPb,KPs,KSa,KSb,KSs :   Key           
 KPa,KSa :                   is a key pair 
 KPb,KSb :                   is a key pair 
 KPs,KSs :                   is a key pair 
 ''') 

protocol = ''' 
 1.   A -> S  :   A,B         
 2.   S -> A  :   {KPb, B}KSs 
 3.   A -> B  :   {Na, A}KPb  
 4.   B -> S  :   B,A         
 5.   S -> B  :   {KPa, A}KSs 
 6.   B -> A  :   {Na, Nb}KPa 
 7.   A -> B  :   {Nb}KPb     
'''

print( l.parse(protocol) )