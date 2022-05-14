import pyttsx3                       #for changing text to voice
import datetime                      # for getting date time
import speech_recognition as sr      # for changing voice to text
import wikipedia                     # for opening wikipedia
import webbrowser                    #for opening things like google , youtube or gmail on browser
import os                            #for opening files or folder at different directoris
import random                        #for generating random data
import smtplib                       #  for sending mails using program


engine=pyttsx3.init('sapi5')
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)
rate = engine.getProperty('rate')
engine.setProperty('rate',190)

                                                # What is sapi5?
                                                # Microsoft developed speech API.
                                                # Helps in synthesis and recognition of voice.

def voice(audio):                               # this function changes text to audio

    engine.say(audio)
    engine.runAndWait()


def wishme():                                    #this function wishes
    hour=datetime.datetime.now().hour

    if(hour>0 and hour <12):
        voice("good morning sir ")

    elif(hour>=12 and hour <=18):
        voice("good afternoon sir ")

    else:
        voice("good evening sir ")

    voice("i am hixi ..your personal voice assistant ..... ")



def take_query():                                 # this function would take user query
    x=input("enter your query sir  :")
    return x.lower()


def wikipedia2():
    voice("what you want to search  :")
    print("--->",end=" ")
    find=input()
    voice("searching sir..")

    results = wikipedia.summary(find, sentences=1)  # this line enables us to searc it on wikipedia
                                                    # here sentences argument means number of line u want
    voice(results)
    voice("so this was all about it sir ..")



def sendEmail(to, content):     # this function is used for sending emails
                                #587 is default mail submission port used while sending  its a port of smtp

                                #smtp is simple mail transfer protocol is an application used to send ,recieve
                                # mailsbetween sender and receiver


    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()                                       #email protocol
    server.starttls()                                   #email protocol

    voice("please enter your email id")
    print("--->",end=" ")
    id=input()
    voice("please enter the password")
    print("--->",end=" ")
    lock = input()

    server.login(id, lock)
    server.sendmail(id, to, content)
    server.close()
    voice("mail sent sir")



if __name__ == '__main__':
    wishme()

    while(1):

        voice("so  how may i help you ")
        choice=take_query()

        if "wikipedia" in choice:
            try:
                wikipedia2()
            except Exception as e:
                voice("please try again sir")


        elif "youtube" in choice:                       # code for opening youtube

            try:
                webbrowser.open("www.youtube.com")      #simple write this and this module open this
                voice("youtube opened sir")
            except Exception as e:
                voice("please try again sir")

        elif "google" in choice:
            try:
                webbrowser.open("www.google.com")
                voice("google opened sir")
            except Exception as e:
                voice("please try again sir")

        elif "gmail" in choice:
            try:
                webbrowser.open("www.gmail.com")
                voice("gmail opened sir")
            except Exception as e:
                voice("please try again sir")

        elif "song" in choice:
            try:
                music="D:\songs"
                gaane=os.listdir(music)                                # command to show file of that directory
                voice("playing your music sir")

                song_choice=random.choice([0,1,2])                     # this random function for
                                                                       # random selection of a song

                os.startfile(os.path.join(music, gaane[song_choice]))  # command to play a song
                                                                       # which is on number "song_choice

            except Exception as e:
                voice("please try again sir")


        elif "time" in choice:

            try:
                nowtime=datetime.datetime.now().strftime("%H:%M:%S")  #usiing datetime to tell time
                                                                      # and strftime("%H:%M:%S") as specifier
                                                                      #to give time in that format
                voice("the time is....")
                voice(nowtime)

            except Exception as e:
                voice("please try again sir")

        elif "code" in choice:
            try:
                path = "C:\\Users\\Ravi\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                                                                        #path of  file

                os.startfile(path)                                      #function for opening something
                voice("opened sir")

            except Exception as e:
                voice("please try again sir")


        elif "mail" in choice:

            try:
                voice("just a reminder sir ...you need to give .....less secure apps access..from "
                      "the id you want to send mail")
                voice("enter the content of email sir")
                print("--->",end=" ")
                content=input()
                to="mehixder@gmail.com"
                sendEmail(to,content)


            except Exception as e:
                print(e)
                voice("please try again sir , the mail cannot be sent")


        elif "quit" in choice:                                            #code for quiting
            try:
                voice("shuting down ...bye sir  ")
                quit()
            except Exception as e:
                voice("please try again sir")







