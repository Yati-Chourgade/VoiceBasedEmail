from ssl import SSL_ERROR_INVALID_ERROR_CODE
from typing import Text
import speech_recognition as sr
import yagmail
#import smtplib

recognizer=sr.Recognizer()
with sr.Microphone() as source:
    print("Clearing Background noise")
    recognizer.adjust_for_ambient_noise(source,duration=1)
    print("Waiting for your message")
    recordedaudio=recognizer.listen(source)
    print("Done recording...!")
    
try:
      print("Printing the message")
      Text=recognizer.recognize_google(recordedaudio,language='en-US')

      print('Your message:{}'.format(Text))
    
except Exception as ex:
        print(ex)

#AUTOMATED MAIL

'''
server = smtplib.SMTP_SSL("smtp.gmail.com", 587)
server.login("sender mail", 'password')
server.sendemail("to","message")

server.quit()
'''
reciever='sanjanasingh7774@gmail.com'
message=Text
sender=yagmail.SMTP('demousercse@gmail.com')
sender.send(to=reciever,subject="This is an automated mail", contents=message)