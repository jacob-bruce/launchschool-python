obj = 42

obj = 'ABcd'        #Resassigns obj
obj.upper()         #Neither
obj = obj.lower()   #Neither
print(len(obj))     #Neither
obj = list(obj)     #Reassigns obj
obj.pop()           #Mutation
obj[2] = 'X'        #Mutation
obj.sort()          #Mutation
set(obj)            #Neither
obj = tuple(obj)    #Reassignment