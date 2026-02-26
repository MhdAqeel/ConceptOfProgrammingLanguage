mygrade={("English",1):"A" , ("Maths",1):"B" , ("Science" , 1):"C",
           ("English",2):"B" , ("Maths",2):"A" , ("Science" , 2):"B",
           ("English",3):"A" , ("Maths",3):"B" , ("Science" , 3):"A"}
attempts=[1,2,3]
for i in attempts:
    print("My grade for Science: " + mygrade[("Science" , i)])
    print("My grade for Maths: " + mygrade[("Maths" , i)])
    print("My grade for English: " + mygrade[("English" , i)])
    print()
