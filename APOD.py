from mongoengine import connect, StringField, Document, DateTimeField

class APOD(Document): #Inherit from the class Document to inform mongoengine that each instance is a document. 
    copyright = StringField(max_length=5000, required=False)
    date = DateTimeField()
    explanation = StringField(max_length=5000, required=False)
    hdurl = StringField(max_length=1000, required=False)
    media_type = StringField(max_length=50, required=False)
    service_version = StringField(max_length=50, required=False)
    title = StringField(max_length=1000, required=False)
    url = StringField(max_length=1000, required=False)
    meta = {'collection': 'APOD'} #Select the collection linked to this Document definition.By default the collection associated is the class name in lowercase.