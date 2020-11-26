class X : pass
class Y : pass
class Z : pass

class A(X,Y) : pass
class B(Y,Z) : pass

class N(A,B,Z) : pass

for obj in N.mro():
    print(obj)