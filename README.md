# DistanceCalculateAPI
##Distance Calculation by using the Python and  REST-API Calls
## Table of contents
* General info
* Technologies/Tools used
* Setup
* Brief about the Code

General info:
This is a project where we have to code in the python and calculating the distance between two coordinates by using the REST-API calls (without using the Google Maps module directly)
The input coordinate points, can be passed into the program directly or if we want we can get/read these input coordinate (Lat, Long) points from some data source also.
This Program will be executed automatically for every 10 minutes9if we want we can change this scheduling time) and will append the results from each run into rows of a CSV file (outfile.csv)

Technologies/Tools required:
PyCharm 2.5
Python 3.6

Setup:
1.	Please “clone or download” project  from the below GitHub repository https://github.com/prasanth446/DistanceCalculateAPI
2.	Will get a Zip file and please extract the Zip file into the local computer
3.	open the downloaded CalculateDistance.py program in the PyCharm IDE and run the program
4.	If we are facing issues with the python interpreter, please configure the correct interpreter for this program.
    If Python scheduler is not available, please install the python scheduler by using the below command in command prompt
        "pip install schedule"
5.	Once the Program is executed successfully, Then we can see a new outfile.csv file has been created and the result will be append for      every run of 10 minutes to this CSV file

Brief about the code:
1.	Used the python scheduler to schedule the script to be run for every 10 minutes automatically.
2.	Used the first pair of coordinates (Lat, Long) as a input for this program and built a function (restapifn) to convert the decimal degrees into radian values, calculating the radian distance between the given pair of points and printing the result. And this result will be appended to a CSV file (outfile.csv)

Improvement: we can make a connection to a data source also to get the coordinate (Lat, Lang) values dynamically and execute this program to calculate the distance. 
