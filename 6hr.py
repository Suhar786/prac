'''name=input("Whats Your Name: ")
color=input("Whats your Fav Color")
print(name,"likes",color)'''

'''----------------------------------------------'''

'''if ,else:,elif,
    AND=and
    Or=or
    not=not            #changes false true or true false'''

'''if cash and bank    #if cash is true and bank is true 
     print("qualify")   #then it will print this
    
   if cash or bank      #if cash or bank anyone true
      print("qualify")   #then it will print this '''

'''---------------------------------------

char=input("enter character")
if len(char)<=(3):
    print("it must be 3 charater long")
elif len(char)>=(50):
    print("it must be max 50 character")
else:
    print("looks good")  
------------------------------------------'''

'''
while condition
   ..... 
         
   i=1
   while i<=5:
   print(i)
   i=i+1       '''

'''secret=9
guesscount=0
guesslimit=3
while guesscount < guesslimit:       #taking limit as three time as from gc to gl interatng 3 times
    guess=int(input("guess: "))       #this will be done three times 
    guesscount+=1
    if guess==secret:                 #checking if  guessinput == 9 
        print("you won")              #if it is print you won and then break
        break
else:
   print("sorry you failed")          #or if "if" condition didnt is true print this'''



number=input("Do you agree").lower()
if number=="y":
    print("you agree")
elif number=="n":
      print("not agree")






