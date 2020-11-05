import os
import shutil
from zipfile import ZipFile
import patoolib
from pyunpack import Archive
#os.environ["UNRAR_LIB_PATH"] = "/home/vijani/Desktop/unrar/libunrar.so"
from unrar import rarfile

cpy_src_path = "/Users/Shyam/Downloads/VersionA"
cpy_out_path = "/Users/Shyam/Downloads/VersionA_2allzips"
ext_out_path = "/Users/Shyam/Downloads/VersionA_3extracted"
sep_out_path = "/Users/Shyam/Downloads/VersionA_4separated"

ext = [".zip", ".7z"]

#collect all zip files inside folders

for dir_path, dirnames, filenames in os.walk(cpy_src_path):
    for filename in filenames:
        src = os.path.join(dir_path, filename)
        dest = os.path.join(cpy_out_path, filename)
        shutil.copy2(src, dest)

#extract all zip files

for file in os.listdir(cpy_out_path):
    fileName = cpy_out_path + '/' + file
    if file.endswith(tuple(ext)):
        Archive(fileName).extractall(ext_out_path)
        print('extracted ' + fileName)
    elif file.endswith(".rar"):
        rar = rarfile.RarFile(fileName)
        rar.extractall(ext_out_path)
        print('extracted ' + fileName)
    else:
        shutil.copy2(fileName, ext_out_path)
        print('copied... ' + fileName)

# separate PDF , word and other files into 3 folders
for dir_path, dirnames, filenames in os.walk(ext_out_path):
   for filename in filenames:
       if filename.endswith(".docx"):
           src = os.path.join(dir_path, filename)
           dest = os.path.join(sep_out_path + "/word", filename)
           shutil.copy2(src, dest)
       elif filename.endswith(".pdf"):
           src = os.path.join(dir_path, filename)
           dest = os.path.join(sep_out_path + "/pdf", filename)
           shutil.copy2(src, dest)
       else:
           src = os.path.join(dir_path, filename)
           dest = os.path.join(sep_out_path + "/other", filename)
           shutil.copy2(src, dest)       




