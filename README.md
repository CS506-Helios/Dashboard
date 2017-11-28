# Helios-Solar Dashboard

1. Instruction

(1)Github Repository address: https://github.com/CS506-Helios/Dashboard

(2)TA Jayasruthi Rangaraja(Jayasruthi) and TA Shivanee Nagarajan(Shivanee95) are invited to the repository. Professor would also be invited once her Github username is verified.

2. Run and Complie Command

(1) Front-end

You must have node installed to continue! If you do not, please install node from their website : http://nodejs.org/


go to your command line and enter the following:


npm install -g grunt-cli

npm install -g bower

git clone https://github.com/CS506-Helios/Dashboard.git

cd frontEnd

npm install

npm start

a localhost:9000 should open on one of your browsers upon succesfull npm start.


If this does not work, please contact mrkhan2@wisc.edu to provide a demo of the site


(2) Data Collection

There are two resources for data collection. One is the SunPower website, which provides solar panels for our client. Another one is the Fronius API, which is the manufacterur of the inverters. 

For SunPower, we wrote a Python programm (sunpower_retrieve.py) that use python-selenium to scrape data from its website. It requires these python modules to be installed: selenium, chromedriver, PhantonJS.

Command Line: 

$pip install -U selenium

Download chromedriver from here: https://sites.google.com/a/chromium.org/chromedriver/downloads
and add it to the working directory

Download PhantomJS from here: http://phantomjs.org/download.html and follow the instructions to install it to the working drectory.

Since the website contains flash embeded contents, we are not able to find the id/name/xpath using selenium functions. We will keep improving and testing this code.

For Fronius, we also wrote a Python program (froniusapi.py) to request data from the Fronius API. It requires the remote access to the local network in the WEI building. 


(3) control.py & manipulator.py 

These files do not need to run, as they just contain a library of functions that will be used by other parts of the app. To compile the files enter the following commands:

(assuming you've cloned the project from git)
python -m py_compile control.py manipulator.py 

This should compile both of the files that comprise the intermediate without error.



(4) SQL Database

Compiling and running SQL code could be done by pasting the code into database engine.

Command line: $ mysql -h "server-name" -u "your_username" "-pyour_password" "database-name" < "filename.sql"

This command line can be used in database from terminal to execute SQL script and verify if CREATE TABLE command produces tables as desired.



(5) Testing

You could run tests using the test command in your command line,
$./testing-file-name.py test

