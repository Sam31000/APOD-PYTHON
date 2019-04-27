#Put here all attributes needed to configure your script
class Config:
    # Using APOD open API to retreive data
    apiUrl = 'https://api.nasa.gov/planetary/apod'

    # You can specify several API Keys if you have many.
    # You can only perfom 1000 request by hour with an API KEY.
    # You can get your own API_Key here : https://api.nasa.gov/index.html#apply-for-an-api-key
    APIKeys = ['##Set an array of api keys##']

    #The name of your database
    dataBase = '##Set you database name##'

    # Here using the connection string to your mongoDB database
    connectionString = '##Set you connection string##'
    
    #The logfile path
    logPath = './'

#Put here your PRODUCTION configuration
class Production (Config):
    apiUrl = 'https://api.nasa.gov/planetary/apod'
    
    # Note : I found all these api key in github projects. There is not my personal api key. Feel free to use them.
    APIKeys = ['qD7zE6W35kPISoRM0o9srmGTldFuzjt9nrfkEWs7', 
                'UGtXPeXRazFiX8WJIlnon5x8Npbz1qJugdRJq76h',
                '5B6oJsSCQyekXZvNOKpsUhRPl1e7FHqjIAyHpybk',
                'qD7zE6W35kPISoRM0o9srmGTldFuzjt9nrfkEWs7', 
                '3RwXJFXWRPro4tK010f9CzXSQ36XkZWrzFZXhfTl', 
                'NtKofGbrMicAFrCNJLzwKnqur6QiVAV6rCzSauYb',
                'vgiDUqm8Qkcmx1nujPPXNHNCILTZvDQ2iQtF3rNN',
                'Pf1VEatEAan8E7Z5KlsrXYRrqhYRlee1tkapvCzJ']

    dataBase = '##YourProductionDatabase##'

    connectionString = '##YourProductionConnectionString##'

    logPath = './'

#Put here your TEST configuration
class Test (Config):
    apiUrl = 'https://api.nasa.gov/planetary/apod'
    
    # Note : I found all these api key in github projects. There is not my personal api key. Feel free to use them.
    APIKeys = ['qD7zE6W35kPISoRM0o9srmGTldFuzjt9nrfkEWs7', 
                'UGtXPeXRazFiX8WJIlnon5x8Npbz1qJugdRJq76h',
                '5B6oJsSCQyekXZvNOKpsUhRPl1e7FHqjIAyHpybk',
                'qD7zE6W35kPISoRM0o9srmGTldFuzjt9nrfkEWs7', 
                '3RwXJFXWRPro4tK010f9CzXSQ36XkZWrzFZXhfTl', 
                'NtKofGbrMicAFrCNJLzwKnqur6QiVAV6rCzSauYb',
                'vgiDUqm8Qkcmx1nujPPXNHNCILTZvDQ2iQtF3rNN',
                'Pf1VEatEAan8E7Z5KlsrXYRrqhYRlee1tkapvCzJ']

    dataBase = '##YourTestDatabase##'

    connectionString = '##YourTestConnectionString##'

    logPath = './'
    
#Put here your DEVELOPMENT configuration
class Development (Config):
    apiUrl = 'https://api.nasa.gov/planetary/apod'
    
    # Note : I found all these api key in github projects. There is not my personal api key. Feel free to use them ;).
    APIKeys = ['qD7zE6W35kPISoRM0o9srmGTldFuzjt9nrfkEWs7', 
                'UGtXPeXRazFiX8WJIlnon5x8Npbz1qJugdRJq76h',
                '5B6oJsSCQyekXZvNOKpsUhRPl1e7FHqjIAyHpybk',
                'qD7zE6W35kPISoRM0o9srmGTldFuzjt9nrfkEWs7', 
                '3RwXJFXWRPro4tK010f9CzXSQ36XkZWrzFZXhfTl', 
                'NtKofGbrMicAFrCNJLzwKnqur6QiVAV6rCzSauYb',
                'vgiDUqm8Qkcmx1nujPPXNHNCILTZvDQ2iQtF3rNN',
                'Pf1VEatEAan8E7Z5KlsrXYRrqhYRlee1tkapvCzJ']

    dataBase = '##YourDevelopmentDatabase##'

    connectionString = '##YourDevelopmentConnectionString##'

    logPath = './'
