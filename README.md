# marking-scripts

Scripts to make marking easier and faster at SLIIT. From this repository, you can find all Python Scripts named as Cleanup Codes. This README file and Video Guides are given for explanations. You can use the scripts for pre-processing student submissions before marking, which will save your time. Happy Marking!<br><br>
*Note: Please find the prerequisites for these scripts at the end of the README file.


## Cleanup Code 01
_Development Contribution : Ms. Vijani Piyawardana_

Script to organize files inside student submissions for IP module which will make marking easier. When we download a set of student submissions for an IP assignment, it will give us a .zip file. The structure of the files and folders organized inside that .zip file is represented in the Overall Structure Diagram below. For marking, need to open individual submissions one by one including folder navigation. From this script, the files need to be marked can be filtered out named with student ID and can be categorized files as needed (ex: files of Question 1, files of Question 2, etc or .docs files, .pdf files, etc). This will save time. 
<br><br>
Video Guide : https://web.microsoftstream.com/video/820442b1-3891-4a58-8b10-52622989e662 <br>

Overall Structure Diagram : <br>
https://github.com/SLIIT-HCI/marking-scripts/blob/master/overall_structure_diagrams/cleanup_code_1-IP.jpg

## Cleanup Code 02
_Development Contribution : Ms. Vijani Piyawardana_

Filter Submissions of a given list of Student ID's from a whole set of submissions, into another folder.
Version 1- Student ID list is hard coded.

Video Guide : https://web.microsoftstream.com/video/ecc32bcf-1125-4c1d-8ade-06331f419c78?list=studio

## Cleanup Code 03
_Development Contribution : Ms. Vijani Piyawardana_

This will access a set of GitHub repository urls inside student submissions and clone the project into relevant folder.

Video Guide : https://web.microsoftstream.com/video/add55c47-98db-4cf0-9988-d28ff115f0f8?list=studio

## Cleanup Code 04
_Development Contribution : Ms. Vijani Piyawardana_

This script is to merge the content of all the .java files in a student submission, into one text file, which will reduce time in folder navigation and file opening. All submissions are processed, newest version can be found here in Github, no any student submission is rejected. 

Video Guide : https://web.microsoftstream.com/video/6d25ca77-5256-40db-b9bb-d65284200766<br><br>
Overall Structure Diagram :<br>
https://github.com/SLIIT-HCI/marking-scripts/blob/master/overall_structure_diagrams/cleanup_code_4-OOP.jpg

## Cleanup Code 05
_Development Contribution : Ms. Vijani Piyawardana_

This code extracts student projects into folders named with student ID, and looks for all .java files, counts all lines of code in the .java files and gives as a sum. Final output is a .CSV containing total number of lines for each student id for all student submissions.

Video Guide : https://web.microsoftstream.com/video/b8629cc4-ce1d-47a5-9b3c-01f04e341274

## Cleanup Code 06
_Development Contribution : Ms. Vijani Piyawardana_

This python script will pre-process all the IP student submissions and filter out the .c files which are ready to be uploaded into gradescope for plagiarism checking. These student submissions has so many issues which are explained in the Overall Structure Diagram mentioned below, nd all these issues are finely handled and solved from this python script. This code need to import some of the python libraries, they are mentioned at the end of this README file.

Video Guide : https://web.microsoftstream.com/video/3559ad67-b2e7-4215-9667-067fe9de7c2f
Overall Structure Diagram :<br>
https://github.com/SLIIT-HCI/marking-scripts/blob/master/overall_structure_diagrams/cleanup_code_6-IP.jpg 

## Student List Generator
_Development Contribution : Mr. Thusithanjana Thilakarathne_

This will generate a student-list CSV from a submission folder downloaded from CourseWeb
1. Create a folder called 'app' in the Downloded submission folder
2. Copy the code into the 'app' folder
3. run the script
4. NameList.csv will be henerated outside the 'app' folder

## Generate Student Info in a CSV file 
_Development Contribution : Ms. Janani Tharmaseelan_

This will generate Student ID and Student Name in a CSV file from the downloaded courseweb submissions. 
courseweb downloaded file name  pattern is : (StudentID) (StudentName) (StudenId)_(RandomNo)_assignsubmission_file_

1. Download and copy the "GenerateStudentInfo" java file into your working directory
2. create a folder called "Submissions" in the working directory
3. copy the downloaded students submissions in to "Submissions" folder
4. run the script 
5. You can find an excel sheet "Student Info" in your working directory which has StudentId and Names 


## convert-csv.py 
_Development Contribution : Dr. Shyam Reyal_

Students have to answer MCQs in online exams, and we can download only one file with all the student answer records (either in excel or csv format) from the system, which is difficult to access and mark it. This script will generate individual file with MCQ answers in an essay format for each student.

Instructions:
 * create a new empty folder (DO NOT SKIP THIS STEP)
 * place this file (convert-csv.py) and the downloaded CSV file from CourseWeb inside it
 * run this file from within the folder
 * it will create a seperate HTML file for each student submission, and a styles.css file
 * if you want to enhance the look&feel of the HTML file, simply modify styles.css to your liking

How to run:
 * command:
  > `$ cd folder`
  > `$ python convert-csv.py input_file.csv limit`
 * folder == the folder where everything is located
 * input_file.csv == the name of the CSV file downloaded from CourseWeb, ensure it is CSV format
 * limit == the number of rows from the CSV file

Video Guide : https://web.microsoftstream.com/video/652fa76b-8534-4605-8670-75c58be261ba

## Prerequisites 

### Python Libraries

<br>For Cleanup Code 01 , 04 , 06<br><br>
* patoolib -- `$ python -m pip install patool`
* pyunpack -- `$ python -m pip install pyunpack`
* unrar -- `$ python -m pip install unrar`

<br>For Cleanup Code 03<br><br>
* requests -- `$ python -m pip install requests`

<br>For Windows users - installing UnRAR
* dowload <b>UnRAR.dll</b>	"UnRAR dynamic library for Windows software developers" from the following link:
https://www.rarlab.com/rar_add.htm?fbclid=IwAR11ns-_Wx1YPXyOb_9Fs4ugYEyHcsoNOZ7voa0vhY8UP4XWJcvFRwfjdBY
* install it
* give path to the .dll file inside the installation folder into the correct place in the cleanup code


