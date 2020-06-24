# marking-scripts

Scripts to make marking easier and faster at SLIIT. From this repository, you can find all Python Scripts named as Cleanup Codes. This README file and Video Guides are given for explanations. You can use the scripts for pre-processing student submissions before marking, which will save your time. Happy Marking!

### Prerequisites

#### Python Libraries

* patoolib

		$ python -m pip install patool

* pyunpack

		$ python -m pip install pyunpack

* unrar

		$ python -m pip install unrar

* requests

		$ python -m pip install requests
		
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

Instructions:
<br>* create a new empty folder (DO NOT SKIP THIS STEP)
<br>* place this file (convert-csv.py) and the downloaded CSV file from CourseWeb inside it
<br>* run this file from within the folder
<br>* it will create a seperate HTML file for each student submission, and a styles.css file
<br>* if you want to enhance the look&feel of the HTML file, simply modify styles.css to your liking
<br>
How to run:
<br>* command:
<br>	$ cd folder
<br>	$ python convert-csv.py input_file.csv limit
<br>* folder == the folder where everything is located
<br>* input_file.csv == the name of the CSV file downloaded from CourseWeb, ensure it is CSV format
<br>* limit == the number of rows from the CSV file
<br>
Enjoy!




