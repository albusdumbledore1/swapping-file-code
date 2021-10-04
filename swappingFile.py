def swapData():
    file1=input("enter your file1 : ")
    file2=input("enter your file2 : ")
    f1=open(file1,'r')
    data_f1=f1.read()
    f2=open(file2,'r')
    data_f2=f2.read()
    f1=open(file1,'w')
    f1.write(data_f2)
    f2=open(file2,'w')
    f2.write(data_f1)
    
swapData()
