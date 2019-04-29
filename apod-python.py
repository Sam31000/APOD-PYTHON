#!/usr/local/bin/python3
'''
    The purpose of this script is to automatically retrieve data from Nasa Astronomic Picture Of the Day (APOD) open API and save it in a mongo db database.
    Phyton Version : 3.7
    Usage : python main.py
'''
__author__ = "CHIDIAC Sami"
__copyright__ = "Nop"
__credits__ = ["CHIDIAC Sami"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "CHIDIAC Sami"
__email__ = "sami.chidiac.development@gmail.com"
__status__ = "Production"

from mongoengine import connect, StringField, Document, DateTimeField
from datetime import datetime,timedelta
import sys
import requests
import logging
import getopt

#Contain all the script configuration
import config

#Mongodbengine document definition of an APOD.
import APOD

#Retrieve cli option
options, remainder = getopt.getopt(sys.argv[1:],'dh',['delta', 'help'])

#The default option retrieve all data. The script retreive the younger APOD saved in the database and start to retrieve data from this APOD date.
delta = False

for opt, arg in options:
    if opt in ['-h', '--help']: # Display the help
        print ("\n-- APOD-PYTHON version {} --".format(__version__))
        print ("\nThis script retrieve data from NASA Astronomic Picture Of the Day (APOD) API and saves them into a mongodb database.")
        print ("By default the script check the APOD in the database with the nearest date of today and start to retrieve data since it")
        print ("\n\tOptions :")
        print ("\t\t-h, --help\tDisplay this help")
        print ("\t\t-d, --delta\tWill check since 6/16/1995 if there is an APOD saved in the database. If not it will rertrieve it from NASA APOD Api\n")
        exit()
    if opt in ['-d', '--delta']: # Set the parameter delta to True
        delta = True

# Using APOD open API to retrieve data
apiUrl = config.Production.apiUrl

# Setting your api key array
APIKeys =  config.Production.APIKeys

# Setting the log configuration
logging.basicConfig(filename='{}Apod_{}.log'.format(config.Production.logPath, datetime.now().strftime("%Y-%m-%d")),level=logging.DEBUG)

# Connection to the database.
connect(config.Production.dataBase, host=config.Production.connectionString)

#16 June 1995 is the date of the first APOD
#We start from that date to parse the whole APOD set.
currentDate = datetime (1995, 6, 16)

#If there already have APODs in the current collection then the next day to treat is the day after the last APOD saved
if APOD.APOD.objects.count() > 0 and not delta:
    currentDate = (APOD.APOD.objects.order_by('-date').first()['date'] + timedelta(days=1))

#The APIKey array index
#For each iteration we use a different apiKey (Only if you defined many in the APIKeys array)
apiKeyIndex = 0

#While we haven't reached today we go ahead and we parse the and save the asset in the database.
while currentDate.strftime("%Y-%m-%d") != datetime.now().strftime("%Y-%m-%d") :

    #If the delta option is set, we check if an APOD exist in the database for the current date.
    if (delta):
        apodExist = APOD.APOD.objects(date = currentDate.strftime("%Y-%m-%d"))

    if((delta and apodExist.count() == 0) or not delta):
        print ("Working on date : {} using API Key : {}".format(currentDate, APIKeys[apiKeyIndex]))
        #Set the http query parameters date and api_key.
        #For more detail, you can refer to the offical Nasa documentation : https://api.nasa.gov/api.html
        params = dict(
            date = currentDate.strftime("%Y-%m-%d"),
            api_key = APIKeys[apiKeyIndex]
        )

        resp = requests.get(url = apiUrl, params = params)
        data = resp.json()
        
        if 'code' not in data and 'error' not in data : #If there is no error we save the apod in the database
            #Create the document and init data
            newApod = APOD.APOD()
            if 'copyright' in data :
                newApod.copyright = data['copyright']
            if 'date' in data :
                newApod.date = data['date']
            if 'explanation' in data :
                newApod.explanation= data['explanation']
            if 'hdurl' in data :
                newApod.hdurl = data['hdurl']
            if 'media_type' in data :
                newApod.media_type = data['media_type']
            if 'service_version' in data :
                newApod.service_version = data['service_version']
            if 'title' in data :
                newApod.title = data['title']
            if 'url' in data :
                newApod.url = data['url']
            #Save the object in the database
            newApod.save()
            print ("Date done : {}".format(currentDate))
        else : #If there is an error retrieving the APOD error is logged and the next APOD is treated
            print ("No Apod found with a compliante format on : {}".format(currentDate))
            logging.debug('{} : Error when trying to retrieve APOD for the date "{}" with api key : {}'.format(datetime.now().strftime("%m/%d/%Y, %H:%M:%S"), currentDate, APIKeys[apiKeyIndex]))
            logging.debug(data)
    else : #If the apod already exist in the database we do not
        print("APOD at the date {} already exist in the database.".format(currentDate))

    #Go to the next date
    currentDate = (currentDate + timedelta(days=1))

    #Increment the apiKeyindex without going out of range of the API_keys array
    apiKeyIndex = (apiKeyIndex + 1) % len(APIKeys)

