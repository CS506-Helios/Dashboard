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


(2) Data Scraping

There are two websites for data scraping. These websites contain solar energy information from two different solar panels. 
We need to add data together to get the total amount of solar energy produced. 
We wrote Python programs for scraping the data, it requires these python modules to be installed: BeautifulSoup, selenium, chromedriver.

However, since the website has dynamic contents with javascript objects, it always redirect to another page of the company. This issue makes the program incompleted. After consulting with the TA, we decided to push the data scraping part to iteration 2 and rewrite the code using Java to solve the issue of session timeout.

(3) Intermediate Python
The intermediate python does not need to run, as it is just a library of functions that will be used by other parts of the app. To compile the files enter the following commands:

(assuming you've cloned the project from git)
python -m py_compile control.py manipulator.py 

This should compile both of the files that comprise the intermediate without error.



(4) SQL Database

Compiling and running SQL code could be done by pasting the code into database engine.

Command line: $ mysql -h "server-name" -u "your_username" "-pyour_password" "database-name" < "filename.sql"

This command line can be used in database from terminal to execute SQL script and verify if CREATE TABLE command produces tables as desired.

