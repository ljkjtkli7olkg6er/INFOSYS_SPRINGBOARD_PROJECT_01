D1={"apple":"red","mango":"yellow","grapes":"green"}
#accessing key value pairs
D1["apple"]
print(D1["apple"])
print("__________")
#modify values
D1["apple"]="Berry"
print(D1["apple"])
print("__________")

#loops where i is keys 
for i in D1:
    print(i,D1[i])

print("__________")
#add
D1["orange"]="orange"

del D1["mango"]    
for i in D1:
    print(i,D1[i])

print("__________")    

