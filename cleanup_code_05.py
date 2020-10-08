import os
import re
from pyunpack import Archive
import csv

# creating a csv file to add data
with open('codeLinesBentley.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(["Number", "Student ID", "Number of Lines in Code"])
    


# path to the original folder contains all bentley submissions 
file_path = "/home/vijani/Documents/SLIIT/research/marking_automated/SEC_uploads/Bentley"
#file_path = "/home/vijani/Documents/SLIIT/research/marking_automated/SEC_uploads/SLIIT"

# path to the folder where we want to extract all .zip files of above folder
extract_path = "/home/vijani/Documents/SLIIT/research/marking_automated/SEC_uploads/extracted_bently"
#extract_path = "/home/vijani/Documents/SLIIT/research/marking_automated/SEC_uploads/extracted_SLIIT"

# extract all .zip files into folders named in each student ID
for file in os.listdir(file_path):

    fileName = file_path + '/' + file
    
    if file.endswith(".zip"):
         # filtering student id from the filename
        stu_id = re.search("[0-9]{8}", file)
        stu_id_string = stu_id.group(0)
        #print("ID is :", stu_id.group(0))

        mkdir_command = "mkdir " + extract_path + "/" + stu_id_string
        os.system(mkdir_command)

        ext_dir = extract_path + "/" + stu_id_string

        Archive(fileName).extractall(ext_dir)
        print('extracted ' + fileName)


# access extracted submissions one by one
# access all java files inside one by one
# count number of lines
students = 0
for dir in os.listdir(extract_path):
    students += 1 
    path = extract_path + "/" + dir
    count = 0
    for dir_path, dirnames, filenames in os.walk(path):
        for filename in filenames:
            if filename.endswith(".java"):
               # print(dir_path)
                count += len(open(dir_path +"/"+filename).readlines(  ))
                print("File name : ", filename)
    print("Student ID : ", dir)
    print("Line Count : ", count)
    print("End of the session")
    with open('codeLinesBentley.csv', 'a') as file:
	    writer = csv.writer(file)
	    writer.writerow([students, dir, count])
        






        
