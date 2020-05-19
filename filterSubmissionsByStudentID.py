'''

Filter Submissions of a given list of Student ID's from a whole set of submissions, into another folder
Version 1- Student ID list is hard coded 

Problem: Had to search for submissions one by one using student ID, to mark 130 submissions which were assigned to me, out of 510 submissions. 

Vijani Piyawardnaa

'''
import os
import shutil

#original files
file_path = "/home/vijani/Documents/SLIIT/PAF/viva/practical-test"

#filter and copy into
copy_path = "/home/vijani/Documents/SLIIT/PAF/viva/practical-test/1selected"

#student ID list to filter
s_id_list = [
    "IT18022698",	"IT18066708",	"IT18022902",	"IT18003642",	"IT18119404",	"IT18009446",	
    "IT16037984",	"IT18115994",	"IT18121384",	"IT18071894",	"IT18156720",	"IT18158328",	
    "IT18091830",	"IT18162738",	"IT18143232",	"IT18120080",	"IT18123128",	"IT18155426",	
    "IT18050622",	"IT18191820",	"IT18362886",	"IT18061444",	"IT18038088",	"IT18005486",	
    "IT18033106",	"IT18136234",	"IT18112474",	"IT18185126",	"IT18167160",	"IT18162974",	
    "IT18126198",	"IT18160826",	"IT18145458",	"IT18118582",	"IT18195262",	"IT18119190",	
    "IT18152524",	"IT18074796",	"IT18084382",	"IT18095418",	"IT18112092",	"IT18123364",	
    "IT18083224",	"IT18152388",	"IT18188028",	"IT18187106",	"IT18027716",	"IT18159486",	
    "IT18119022",	"IT18144536",	"IT17184090",	"IT18157574",	"IT18019896",	"IT17032902",	
    "IT17125826",	"IT18162592",	"IT17006576",	"IT17147224",	"IT17176316",	"IT18174786",	
    "IT18121902",	"IT18117738",	"IT18121452",	"IT18126884",	"IT17181648",	"IT16144804",	
    "IT15131898",	"IT17134118",	"IT17251174",	"IT17110662",	"IT17168632",	"IT17022002",	
    "IT17021012",	"IT18059564",	"IT18135626",	"IT18007220",	"IT18152838",	"IT18396164",	
    "IT18195194",	"IT18006230",	"IT18128796",	"IT18067170",	"IT18052466",	"IT18003574",	
    "IT17181402",	"IT18110494",	"IT18389784",   "IT17180962",	"IT18026894",	"IT18027952",	
    "IT18062816",	"IT18061130",	"IT18082548",	"IT18130430",	"IT18194722",	"IT18137842",	
    "IT18191134",	"IT18060904",	"IT18502466",	"IT18109290",	"IT18028188",	"IT18052152",	
    "IT18183450",	"IT18006858",	"IT18087048",	"IT16143982",	"IT18116298",	"IT17109536",	
    "IT18081794",	"IT18030068",	"IT18118414",	"IT17057820",	"IT18366082",	"IT18017120",	
    "IT17021326",	"IT17022620",	"IT17023238",	"IT17147392",	"IT16143050",	"IT17077248",	
    "IT17106320",	"IT17096430",	"IT17058810",	"IT17095204",	"IT17004978",	"IT17142656",	
    "IT15089700",	"IT17041126",	"IT17049382",	"IT16109254"
]

#sample to test
#s_id_list = ['IT0000000', 'IT1111111','IT17043892']

#list of files not found
not_found = [] 

#counter to count copied files
count = 0
n_count = 0
a = ""

#getting all file/folder names of the original location into a list
name_list = os.listdir(file_path)

print("first a values is", a)

for s_id in s_id_list:
    print("....................."+ s_id)
    found = False 
    for name in name_list:
        print("..."+name)
        fileName = file_path + '/' + name
        if(s_id in name):
            a = shutil.copytree(fileName, copy_path + '/' + name)
            print("copied..." + name + "a value" )
            count = count + 1
            found = True
            break  
    if not found:
        if s_id not in not_found:
            n_count = n_count + 1
            not_found.append(s_id)



print("Total files copied : ", count)
print("Total files not found : ", n_count)

print("Not found list : ", not_found)

'''
References

https://automatetheboringstuff.com/chapter9/
https://www.studytonight.com/post/how-to-check-for-an-empty-string
https://www.programiz.com/python-programming/break-continue
'''


