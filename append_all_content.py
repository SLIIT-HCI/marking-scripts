import os
import shutil
from zipfile import ZipFile
import patoolib
from pyunpack import Archive
os.environ["UNRAR_LIB_PATH"] = "/home/vijani/Desktop/unrar/libunrar.so"
from unrar import rarfile
import re



print("Extract code by Vijani")

src_path = "/home/vijani/Documents/SLIIT/research/marking_automated/OOP_Thilmi/Malabe_Foreign"

cpy_path = "/home/vijani/Documents/SLIIT/research/marking_automated/OOP_Thilmi/all_zipz"

ext_path = "/home/vijani/Documents/SLIIT/research/marking_automated/OOP_Thilmi/extracted"

txt_path = "/home/vijani/Documents/SLIIT/research/marking_automated/OOP_Thilmi/text_files"

arc_ext = [".zip", ".7z"]

fil_ext = [".java", ".txt"] # some students had saved java content on .txt files, so take .txt as well. 

count = 0




#collect all zip files inside folders into another folder cpy_path

for dir_path, dirnames, filenames in os.walk(src_path):
    for filename in filenames:
        src = os.path.join(dir_path, filename)
        dest = os.path.join(cpy_path, filename)
        shutil.copy2(src, dest)




#extract all zip files into another folder ext_path

for file in os.listdir(cpy_path):
    fileName = cpy_path + '/' + file

    #print("File is: ", file)
    #ID = file[:-4]
    #print("ID is: ", ID)

    ID = file[0:10]     # take first 10 charactors of file name, which is the student ID

    mkdir_command = "mkdir " + ext_path + "/" + ID
    os.system(mkdir_command)

    ext_dir = ext_path + "/" + ID

    if file.endswith(tuple(arc_ext)):
        Archive(fileName).extractall(ext_dir)
        #print('extracted ' + fileName)
    elif file.endswith(".rar"):
        rar = rarfile.RarFile(fileName)
        rar.extractall(ext_dir)
        #print('extracted ' + fileName)
    else:
        shutil.copy2(fileName, ext_dir)
        #print('copied... ' + fileName)




# access each student submission in extracted folder

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

for dir_path, dirnames, filenames in os.walk(ext_path):
    for filename in filenames: 
        text_file = dir_path + '/' + filename
        if filename.endswith(".txt"):
            x = re.search("^IT|it|It|iT" , filename) 
            # some students had typed their index number in different ways, this is to check all possibilities
            if (x!=None): 
                shutil.copy2(text_file, txt_path)
           




