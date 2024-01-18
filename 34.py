f1=open("Doctors.txt","r")
list1=f1.readlines()
f2=open("1.html","r")
info1=f2.read()
for item in list1:
    with open(f"{item.rstrip()}.html","w") as file:
        file.write(info1.replace("DOCTOR",item))
        
