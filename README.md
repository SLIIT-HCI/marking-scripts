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

Script to organize files inside student submissions for IP module which will make marking easier. When we download a set of student submissions for an IP assignment, it will give us a .zip file. The structure of the files and folders organized inside that .zip file is represented in the Overall Structure Diagram below. For marking, need to open individual submissions one by one including folder navigation. From this script, the files need to be marked can be filtered out named with student ID and can be categorized files as needed (ex: files of Question 1, files of Question 2, etc or .docs files, .pdf files, etc). This will save time. 
<br><br>
Video Guide : https://web.microsoftstream.com/video/820442b1-3891-4a58-8b10-52622989e662 <br>

Overall Structure Diagram : <br>
https://github.com/SLIIT-HCI/marking-scripts/blob/master/overall_structure_diagrams/cleanup_code_1-IP.jpg

## Cleanup Code 02

Filter Submissions of a given list of Student ID's from a whole set of submissions, into another folder.
Version 1- Student ID list is hard coded.

Video Guide : https://web.microsoftstream.com/video/ecc32bcf-1125-4c1d-8ade-06331f419c78?list=studio

## Cleanup Code 03

This will access a set of GitHub repository urls inside student submissions and clone the project into relevant folder.

Video Guide : https://web.microsoftstream.com/video/add55c47-98db-4cf0-9988-d28ff115f0f8?list=studio

## Cleanup Code 04

This script is to merge the content of all the .java files in a student submission, into one text file, which will reduce time in folder navigation and file opening. 

Video Guide : https://web.microsoftstream.com/video/6d25ca77-5256-40db-b9bb-d65284200766<br><br>
Overall Structure Diagram :<br>
https://github.com/SLIIT-HCI/marking-scripts/blob/master/overall_structure_diagrams/cleanup_code_4-OOP.jpg

# Generate Student Info in a CSV file 

This will generate Student ID and Student Name in a CSV file from the downloaded courseweb submissions. 
courseweb downloaded file name will pattern is : (StudentID) (StudentName) (StudenId)_(RandomNo)_assignsubmission_file_
Steps to follow : 

1. Download and copy the "GenerateStudentInfo" java file into your working directory
2. create a folder called "Submissions" in the working directory
3. copy the downloaded students submissions in to "Submissions" folder
4. run the script 
5. You can find an excel sheet "Student Info" in your working directory which has StudentId and Names 

	
