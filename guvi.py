 #new program 

"""def sum():
    print(x+y)"""
  #-----------
"""list = ['car', 'bus', 'bike', 'scoter']
def loop(x):
    print(x * 3)#this is for only repition of list

def map_simple(crazy, list):
    for items in list:
        crazy(items)  #items contain car bus bike scotter which is etirated over and over again in map function downwards

map_simple(loop, list)
 #crazy is loop i.e it passes x argument"""
        #--------

"""def increment(x,y):           def increment(x,y=1)
    return x+y                    return x+y

print(increment(2,3))"""          # print(increment(2))

                #-------------

"""def list(**list):
    print(list["id"])     
list(id=2, ud=4, tf=5)"""
         #----------------------
         
"""def fizz(input):
    if input==3:
        return "ok1"
    if input==5:
        return "ok2"
    return input
print(fizz(9))"""
   #------------------------
"""dictt={
"Name":"Suhar",
"CLASS":"8TH",
"SECTION":"RED",
 }
dictt["Name"]="tabish"
dictt.pop("CLASS")
print(dictt)   """

   #-------
"""list=["apple","mango","banana"]
newlist=[x.upper() for x in list]
print(newlist)  """  

list=["apple","mango","banana"]                                          
newlist=[x if x!="banana" else "orange" for x in list]
print(newlist)   
