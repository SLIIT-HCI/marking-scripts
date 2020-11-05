import os
import sys
import re
import shutil
from zipfile import ZipFile
import patoolib
from pyunpack import Archive
#if you have not installed rar library into the system uncomment the following line to give the part to the downloded file
#os.environ["UNRAR_LIB_PATH"] = "/home/vijani/Desktop/unrar/libunrar.so"
from unrar import rarfile
#for windows, download .dll file and give path to that file
#os.environ["UNRAR_LIB_PATH"] = "/home/vijani/Desktop/unrar/libunrar.dll"
#from unrar import rarfile

# to check the argument is given when executing - the Folder name ex: VersionA
if len(sys.argv)==1:
    sys.exit('no path specified')

cpy_src_path = os.path.abspath(sys.argv[1])

if not os.path.isdir(cpy_src_path):
    sys.exit('path does not exist')

# making 3 new folders to be used in this execution
cpy_out_path = cpy_src_path + "_1allzips"
ext_out_path = cpy_src_path + "_2extracted"
sep_out_path = cpy_src_path + "_3separated"

if os.path.isdir(cpy_out_path):
    shutil.rmtree(cpy_out_path)
os.makedirs(cpy_out_path)
  
if os.path.isdir(ext_out_path):
    shutil.rmtree(ext_out_path)
os.makedirs(ext_out_path)

if os.path.isdir(sep_out_path):
    shutil.rmtree(sep_out_path)
os.makedirs(sep_out_path)
os.makedirs(sep_out_path + "/other")
os.makedirs(sep_out_path + "/cfiles")

# list containing all Archive type, can include any archive type here. (.rar is a special case, so didn't mention it here)
ext = [".zip", ".7z"]

# collect all zip files inside folders
filename_new = "blank"
for dir_path, dirnames, filenames in os.walk(cpy_src_path):
    
    for filename in filenames:

        # taking student ID from the submission folder name
        stu_id = re.search("[0-9]{8}", dir_path)
        if stu_id:
            stu_id_string = stu_id.group(0)
            student_id = "IT" + stu_id_string

            # renaming with correct Student ID
            if(filename.endswith(".zip")):
                filename_new = student_id + ".zip"
            elif(filename.endswith(".7z")):
                filename_new = student_id + ".7z"
            elif(filename.endswith(".rar")):
                filename_new = student_id + ".rar"
            else:
                filename_new = student_id + ".c"
            
            # copying all Archives and other files inside every submission folder into another folder    
            src = os.path.join(dir_path, filename)
            dest = os.path.join(cpy_out_path, filename_new)
            shutil.copy2(src, dest)

# extract the Archives while pre-processing
for file in os.listdir(cpy_out_path):
    fileName = cpy_out_path + '/' + file
    print("Folder Name : " + file)
    ID = file[0:10]
    print("ID is :  " + ID)
    print("File Name : " + fileName)
    
    if file.endswith(tuple(ext)):
        os.mkdir(ext_out_path + "/" + ID)
        Archive(fileName).extractall(ext_out_path + "/" + ID)
        print('extracted ' + fileName)
        files_inside = os.listdir(ext_out_path + "/" + ID)
        file1 = files_inside[0]
        if(os.path.isdir(ext_out_path + "/" + ID+ "/" +file1)):
            print(file1 + ' is a dir')
            files_inside = os.listdir(ext_out_path + "/" + ID + "/" + file1 + "/")
            file2 = files_inside[0]
            print(file2 + ' is a file 2')
            print(ext_out_path + "/" + ID + "/" + file1 + "/" + file2 + "--->"+ ext_out_path + "/" + ID + "/" + ID + ".c")
            os.rename(ext_out_path + "/" + ID + "/" + file1 + "/" + file2, ext_out_path + "/" + ID + "/" + ID + ".c")
            os.rmdir(ext_out_path + "/" + ID + "/" + file1)
        else:
            print(file1 + ' is a file')
            os.rename(ext_out_path + "/" + ID + "/" + file1, ext_out_path + "/" + ID + "/" + ID + ".c")
   
    elif file.endswith(".rar"):
        os.mkdir(ext_out_path + "/" + ID)
        rar = rarfile.RarFile(fileName)
        rar.extractall(ext_out_path + "/" + ID)
        print('extracted ' + fileName)

        files_inside = os.listdir(ext_out_path + "/" + ID + "/")
        file1 = files_inside[0]
        if(os.path.isdir(ext_out_path + "/" + ID+ "/" + file1)):
            files_inside = os.listdir(ext_out_path + "/" + ID + "/" + file1 + "/")
            file2 = files_inside[0]
            os.rename(ext_out_path + "/" + ID + "/" + file1 + "/" + file2, ext_out_path + "/" + ID + "/" + ID + ".c")
            os.rmdir(ext_out_path + "/" + ID + "/" + file1)
        else:
            os.rename(ext_out_path + "/" + ID + "/" + file1, ext_out_path + "/" + ID + "/" + ID + ".c")

    else:
        shutil.copy2(fileName, ext_out_path)
        print('copied... ' + fileName)

# filter out .c files into a folder 
for dir_path, dirnames, filenames in os.walk(ext_out_path):
   for filename in filenames:
       if filename.endswith(".c"):
           src = os.path.join(dir_path, filename)
           dest = os.path.join(sep_out_path + "/cfiles", filename)
           shutil.copy2(src, dest)
       else:
           src = os.path.join(dir_path, filename)
           dest = os.path.join(sep_out_path + "/other", filename)
           shutil.copy2(src, dest)       




