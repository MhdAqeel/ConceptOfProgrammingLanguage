%facts
parent(john, mary).
parent(john, peter).
parent(mary, ann).
parent(peter, sally).


%rules

child(X,Y):-parent(Y,X).
sibling(X,Y):-parent(Z,X),parent(Z,Y),X\=Y.
ancestor(A, D) :- parent(A, D).
ancestor(A, D) :- parent(A, X), ancestor(X, D).