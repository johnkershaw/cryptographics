import re

text = ''' 
 // Lowe's fixed version of Needham-Schroder Public Key 
  
 A,B,S :                     Principal     
 Na,Nb :                     Nonce         
 KPa,KPb,KPs,KSa,KSb,KSs :   Key           
 KPa,KSa :                   is a key pair 
 KPb,KSb :                   is a key pair 
 KPs,KSs :                   is a key pair 
  
  
 1.   A -> S  :   A,B            
 2.   S -> A  :   {KPb, B}KSs    
 3.   A -> B  :   {Na, A}KPb     
 4.   B -> S  :   B,A            
 5.   S -> B  :   {KPa, A}KSs    
 6.   B -> A  :   {Na, Nb, B}KPa 
 7.   A -> B  :   {Nb}KPb        
   
 // Security Protocols Open Repository 
 // http://www.lsv.ens-cachan.fr/spore 
   
-----------------------------------------------------------------------
  
   
              This document was translated from LaTeX by HeVeA
              (http://pauillac.inria.fr/~maranget/hevea/index.html). 
'''

pattern = r" (\d+)\. +(\w) -> (\w) +: +({?)([A-z, ]+[A-z])(}K[A-z]+|)"

template = r'{"stage": \1, "from": "\2", "to": "\3", "payload": "\5", "encryption", "\4\6"}\n'

matches = re.findall(pattern, text)
stages = []
for m in matches:
    stages.append({'stage': m[0]})
    print(m)

print(stages)