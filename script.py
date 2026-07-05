import os
import copy
print("\033c\033[47;31m\ngive me file .class: ? \n")
a=input().strip()
rrr=a.replace(".class","")
ttt="/usr/bin/openjdk-asmtools-jdis $1 -w /tmp/".replace("$1",a)
os.system(ttt)
f1=open("/tmp/$2.jasm".replace("$2",rrr),"r")
bodys=f1.read()
f1.close()

b=bodys.split("\n")
line=1
aa=False
cc=False
for bb in b:
    if line==1:
        
        
            
        aa=True
    else:
        if cc:
            print(bb)
            hh=bb.find("return")
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
        