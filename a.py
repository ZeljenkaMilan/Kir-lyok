print("a*x+b=0")
a=float(input("Add meg az a értékét"))
b=float(input("Add meg az b értékét"))
if a!=0:
    x=-b/a
    print("Megoldás: ",x)
else:
    if b!=0:
        print("Nincs megoldás")
    else:
        print("Minden valós szám megoldás")
    
