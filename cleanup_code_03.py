import os
import codecs
import requests
from bs4 import BeautifulSoup

# path to filtered submissions
file_path = "/home/vijani/Documents/SLIIT/PAF/viva/practical-test/1selected"

#getting all folder names of the original location into a list
name_list = os.listdir(file_path)

# filter
filter_path = "/home/vijani/Documents/SLIIT/PAF/viva/practical-test/1filtered"

count = 0 

# function to clone projects
def clone_projects(count):

    for folder_name in name_list:

        subm_dir = file_path + "/" + folder_name

        # remove existing directory named "project" : [optional]
        rm_command = 'rm -rf ' + subm_dir + '/project'
        os.system(rm_command)

        # make a new directory inside submission folder to clone the project
        mkdir_command = 'mkdir ' + subm_dir + '/project'
        os.system(mkdir_command)

        # getting full path of the cloning directory
        clone_dir = subm_dir + "/project"

        # getting full path of the html file
        html_file = subm_dir + "/onlinetext.html"

        # read html file content    
        with open(html_file, "rb") as f:
            page = f.read()
        html_content = page
   
        # Parse the html content
        soup = BeautifulSoup(html_content, "lxml")
    
        # increment processed file count by one
        count = count + 1
        print("count : ", count)

        #getting repository link from the html file inside the submission folder
        link = soup.find_all('a')[0].get('href')
        print(link)

        #cloning the project
        git_command = 'git clone ' + link + ' ' + clone_dir
        os.system(git_command)

# call functions

clone_projects(count)



    


