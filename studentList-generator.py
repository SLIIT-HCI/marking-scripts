import os
import csv

#print ([name for name in os.listdir(".") if os.path.isdir(name)])
os.chdir('..')

#This function will filter the it number from the folder name
def findID(nameList):
    for i in nameList:
        #print(i)
        if 'it' in i or 'IT' in i:
            return i
    

#Write the data into the CSV file
with open('NameList.csv', 'wb') as csvfile:
    theWriter = csv.writer(csvfile)
    theWriter.writerow(['StudentId'])
    for name in os.listdir("."):
        if os.path.isdir(name):
            name = name.replace('_',' ')#remove the '_' from the folder name
            if (name!='App'):
                id = name.split(' ')#Split the name         
                theWriter.writerow([findID(id)])# this will filter the it number
                


    
    
