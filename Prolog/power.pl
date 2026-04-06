power(_,0,1).
power(B,E,R):-E>0,E1 is E-1 , power(B , E1 , R1) , R is B * R1.