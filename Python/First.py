mygrade={("English",1):"A" , ("Maths",1):"B" , ("Science" , 1):"C",
           ("English",2):"B" , ("Maths",2):"A" , ("Science" , 2):"B",
           ("English",3):"A" , ("Maths",3):"B" , ("Science" , 3):"A"}
attempts=[1,2,3]
subjects = ["English" , "Science" , "Maths"]

for s in subjects:  
    print()
    for i in attempts:
        print("My grade for " + s +  " on attempt "+str(i)+": "+ mygrade[(s , i)])
    
