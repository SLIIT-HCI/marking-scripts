import os
import shutil
from zipfile import ZipFile
import patoolib
from pyunpack import Archive
os.environ["UNRAR_LIB_PATH"] = "/home/vijani/Desktop/unrar/libunrar.so"
from unrar import rarfile
import re
import pyfiglet


ascii_banner = pyfiglet.figlet_format("Welcome!!!")
print(ascii_banner)

print("************ Cleanup Code for OOP marking **************\n\nYou need to have following folders: \n\t1. src - Folder contains all submissions\n\t2. cpy - Folder to copy zip files inside submissions\n\t3. ext - Folder to extract zip files\n\t4. txt - Folder to take all merged text files\n\t5. rjc - Folder to have rejected files\n\n")

src_path = ""
cpy_path = "" 
ext_path = ""
txt_path = ""
rjc_path = ""

# get folder paths as user input

# work for any Python version

def get_input_paths():
    try:
        get_input_paths_py27()
    except:
        get_input_paths_py3()

def get_input_paths_py27():
    global src_path, cpy_path, ext_path, txt_path, rjc_path
    src_path = raw_input("Enter full path for your 'src' folder : ")
    cpy_path = raw_input("Enter full path for your 'cpy' folder : ")
    ext_path = raw_input("Enter full path for your 'ext' folder : ")
    txt_path = raw_input("Enter full path for your 'txt' folder : ")
    rjc_path = raw_input("Enter full path for your 'rjc' folder : ")

def get_input_paths_py3():
    global src_path, cpy_path, ext_path, txt_path, rjc_path
    src_path = input("Enter full path for your 'src' folder : ")
    cpy_path = input("Enter full path for your 'cpy' folder : ")
    ext_path = input("Enter full path for your 'ext' folder : ")
    txt_path = input("Enter full path for your 'txt' folder : ")
    rjc_path = input("Enter full path for your 'rjc' folder : ")


arc_ext = [".zip", ".7z"]

fil_ext = [".java", ".txt"] # some students had saved java content on .txt files, so take .txt as well. 



#collect all zip files inside folders into another folder 

def collectAll():
     for dir_path, dirnames, filenames in os.walk(src_path):
        for filename in filenames:
            src = os.path.join(dir_path, filename)
            dest = os.path.join(cpy_path, filename)
            shutil.copy2(src, dest)
     print("All copied...!")
   
        

#extract all zip files into another folder ext_path

def extractAll():
    count = 0
    for file in os.listdir(cpy_path):
        fileName = cpy_path + '/' + file

        # check is the zip file name is in correct format
        x = re.search("(^IT|it|It|iT)([0-9])([0-9])([0-9])([0-9])([0-9])([0-9])([0-9])([0-9])" , file) 
        if(x!=None):

            ID = file[0:10]     # take first 10 charactors of file name, which is the student ID

            mkdir_command = "mkdir " + ext_path + "/" + ID
            os.system(mkdir_command)

            ext_dir = ext_path + "/" + ID

            if file.endswith(tuple(arc_ext)):
                Archive(fileName).extractall(ext_dir)
      
            elif file.endswith(".rar"):
                rar = rarfile.RarFile(fileName)
                rar.extractall(ext_dir)
        
            else:
                shutil.copy2(fileName, rjc_path)
        else:
            count = count + 1
            shutil.copy2(fileName, rjc_path)
   
    print("Total rejected files : " , count)



# access each student submission in extracted folder

def combineAll():
    for file in os.listdir(ext_path):
        fileName = ext_path + '/' + file
        with open(ext_path + '/' + file + '/' + file + '.txt', 'w') as fp: 
            pass

        # access each file inside the current student submission

        for dir_path, dirnames, filenames in os.walk(fileName):
            fo = open(ext_path + '/' + file + '/' + file + '.txt', 'a')
            for filename in filenames:   
                if filename.endswith(tuple(fil_ext)):
                    #print("File name : ", filename)
                    fo.write("\n\n*********************************" + filename + "\n\n") 
                    with open(dir_path + '/' + filename, 'rb') as fi:
                        shutil.copyfileobj(fi, fo)
            #print("\n")           
            fo.close()





# filter all text files processed

def filterAllCombinedFiles():
    for dir_path, dirnames, filenames in os.walk(ext_path):
        for filename in filenames: 
            text_file = dir_path + '/' + filename
            if filename.endswith(".txt"):
                x = re.search("^IT|it|It|iT" , filename) 
                # some students had typed their index number in different ways, this is to check all possibilities
                if (x!=None): 
                    shutil.copy2(text_file, txt_path)
               

#function calls

get_input_paths()

collectAll()

extractAll()

combineAll()

filterAllCombinedFiles()


