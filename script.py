import os
import copy
print("\033c\033[47;31m\ngive me file .class: ? \n")
a=input().strip()
rrr=a.replace(".class","")
ttt="javap -c -private $1 > /tmp/$2.jbat".replace("$1",a).replace("$2",rrr)
os.system(ttt)
f1=open("/tmp/$2.jbat".replace("$2",rrr),"r")
bodys=f1.read()
f1.close()

b=bodys.split("\n")
line=1
aa=False
cc=False
for bb in b:
    if line==1:
        ll=bb.find("Compiled from")
        if ll<0:
            print("not a jbat file...")
            exit(1)
        else:
            print(bb)
            aa=True
    else:
        if cc:
            print(bb)
            hh=bb.find(": return")
            if hh>-1:
                print("end program")
                exit(0)
        if aa:
            hh=bb.find("public")
            if hh>-1:
                hh=bb.find("main")
                if hh>-1:
                    print(bb)
                    cc=True
    line=line+1
        