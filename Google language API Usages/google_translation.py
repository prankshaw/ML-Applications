# Getting API Key
import getpass
APIKEY =getpass.getpass()

# running Translate API
from googleapiclient.discovery import build
service = build('translate', 'v2', developerKey=APIKEY)

# use the service
inputting = ['The exasperation of my words and the anger of the ink is just dumb expression', 'and I request you']
outputting = service.translations().list(source='en', target='fr', q=inputting).execute()

# converting to french (fr=french)
for i in outputting['translations']:
  print(i['translatedText'])
# L'exaspération de mes mots et la colère de l'encre ne sont qu'une expression stupide
# et je te demande

#Converting to hindi  (hi = hindi)
  outputting = service.translations().list(source='en', target='hi', q=inputting).execute()
for i in outputting['translations']:
  print(i['translatedText'])
  
# मेरे शब्दों की अतिशयता और स्याही का गुस्सा सिर्फ गूंगा अभिव्यक्ति है
# और मैं आपसे निवेदन करता हूं
  
