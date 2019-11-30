# DistanceCalculateAPI
##Distance Calculation by using the Python and  REST-API Calls
## Table of contents
* General info
* Technologies/Tools used
* Setup
* Brief about the Code

General info:
This project is to calculate the distance between two different coordinates of the earth. It will felicitate the distance calculation of any moving objects. The result will be written in csv file and its execution is scheduled as automatic.
The calculation is done using normal geographical GMT standards based on approximate radius of the earth while converting the longitudinal and latitudinal points into radian. The function does not use the standard google API.
The schedule and time import function is used to make its run calibration for every 10 minutes and will append the results of each run into a CSV file (outfile.csv)

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
