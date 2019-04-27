#!/usr/local/bin/python3
'''
    The purpose of this script is to automatically retreive data from Nasa APOD open API and save it in a database.
'''
__author__ = "CHIDIAC Sami"
__copyright__ = "Nop"
__credits__ = ["CHIDIAC Sami"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "CHIDIAC Sami"
__email__ = "sami.chidiac87@gmail.com"
__status__ = "Production"

from mongoengine import connect, StringField, Document, DateTimeField
from datetime import datetime,timedelta
import sys
import requests

# Using APOD open API to retreive data
apiUrl = 'https://api.nasa.gov/planetary/apod'

# You can specify several API Keys if you have many.
# You can only perfom 1000 request by hour with an API KEY.
# You can get your own API Key here : https://api.nasa.gov/index.html#apply-for-an-api-key
APIKeys = ['qD7zE6W35kPISoRM0o9srmGTldFuzjt9nrfkEWs7', 
            'Bz1nWv4Jjitq6ua2HFThkcIGkNQKHOkbYY3lDi0Y', #<-My key
            'UGtXPeXRazFiX8WJIlnon5x8Npbz1qJugdRJq76h',
            '5B6oJsSCQyekXZvNOKpsUhRPl1e7FHqjIAyHpybk',
            'qD7zE6W35kPISoRM0o9srmGTldFuzjt9nrfkEWs7', 
            '3RwXJFXWRPro4tK010f9CzXSQ36XkZWrzFZXhfTl', 
            'NtKofGbrMicAFrCNJLzwKnqur6QiVAV6rCzSauYb',
            'vgiDUqm8Qkcmx1nujPPXNHNCILTZvDQ2iQtF3rNN',
            'Pf1VEatEAan8E7Z5KlsrXYRrqhYRlee1tkapvCzJ']

# Connection to the database.
# Here using the connection string provided by Azure comos db working with a MongoDB database.
connect('NasaDatabase', host='mongodb://cosmoaccount:5pSnawF74Q3mP0qwcEWrhnZbrURGlVGz623kVuSFtB8YFLIZo4GJDLPRqiRsbRqwhbVZdmLERlL6rxj26CwPhw==@cosmoaccount.documents.azure.com:10255/NasaDatabase?ssl=true&replicaSet=globaldb')

class APOD(Document): #Inherit from the class Document to inform mongoengine that each instance is a document. 
    copyright = StringField(max_length=5000, required=False)
    date = DateTimeField()
    explanation = StringField(max_length=5000, required=False)
    hdurl = StringField(max_length=1000, required=False)
    media_type = StringField(max_length=50, required=False)
    service_version = StringField(max_length=50, required=False)
    title = StringField(max_length=1000, required=False)
    url = StringField(max_length=1000, required=False)
    meta = {'collection': 'APOD'} #Select the collection linked to this Document definitionBy default the collection associated is the class name in lowercase

#16 June 1995 is the date of the first APOD
#We start from that date to parse the whole APOD set.
currentDate = datetime (1995, 6, 16)

#If there already have APODs in the current collection then the next day to treat is the day after the last APOD saved
if APOD.objects.count() > 0:
    currentDate = (APOD.objects.order_by('-date').first()['date'] + timedelta(days=1))

#The APIKey array index
#For each iteration we use a different API_KEY (Only if you defined many in the APIKeys array)
apiKeyIndex = 0

#While we haven't reached today we go ahead and we parse the and save the asset in the database.
while currentDate.strftime("%Y-%m-%d") != datetime.now().strftime("%Y-%m-%d") :

    print ("Working on date : {} using API Key : {}".format(currentDate, APIKeys[apiKeyIndex]))
    #Set the http query parameters date and api_key.
    #For more detail, you can refer to the offical Nasa documentation : https://api.nasa.gov/api.html
    params = dict(
        date = currentDate.strftime("%Y-%m-%d"),
        api_key = APIKeys[apiKeyIndex]
    )

    resp = requests.get(url = apiUrl, params = params)
    data = resp.json()
    
    if 'code' not in data and 'error' not in data :
        #Create the document and init data
        newApod = APOD()
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
    else :
        print ("No Apod found with a compliante format on : {}".format(currentDate))

    #Go to the next date
    currentDate = (currentDate + timedelta(days=1))

    #Increment the apiKeyindex without going out of range of the API_keys array
    apiKeyIndex = (apiKeyIndex + 1) % len(APIKeys)

