import requests as r 

url = 'https://api.nasa.gov/planetary/apod?api_key='

def Key():
    key = 'eMgZtSl1bRXcEogBabMmie9ZSvasmw4GMJjRir3N'
    return key

def ImageDay(start_date,end_date):
    urlday = url + str(Key()) + '&start_date=' + str(start_date) + '&end_date=' + str(end_date)
    response = r.get(urlday).json()
    return response

