#Getting key
import getpass
APIKEY = getpass.getpass()

#using service
from googleapiclient.discovery import build
service = build('translate', 'v2', developerKey=APIKEY)

#ENGLISH
inputting = ["What I do is what I do and I will always do and thus I do what do you do", "Chris Bokari"]
outputting = service.detections().list(q=inputtting).execute()

#output
print(eng)
# {'detections': [[{'confidence': 1, 'isReliable': False, 'language': 'en'}], [{'isReliable': False, 'language': 'en', 'confidence': 0.4350448367989688}]]}

#FRENCH
inputting = ["La conscience noire est une attitude de l'esprit et un mode de vie, l'appel le plus positif à émaner du monde noir pendant longtemps."]
outputting = service.detections().list(q=fr).execute()
print(outputting)
# {'detections': [[{'confidence': 0.9877066016197205, 'isReliable': False, 'language': 'fr'}]]}

