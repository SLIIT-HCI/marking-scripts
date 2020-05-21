import os
import csv

#print ([name for name in os.listdir(".") if os.path.isdir(name)])
os.chdir('..')

def findID(nameList):
    for i in nameList:
        #print(i)
        if 'it' in i or 'IT' in i:
            return i
    


with open('NameList.csv', 'wb') as csvfile:
    theWriter = csv.writer(csvfile)
    theWriter.writerow(['StudentId'])
    for name in os.listdir("."):
        if os.path.isdir(name):
            name = name.replace('_',' ')
            if (name!='App'):
                id = name.split(' ')        
                theWriter.writerow([findID(id)])
                


    
    