from flask import Flask
from flask_cors import CORS
from flask import Flask, request
from jwt_utils import *
from werkzeug.exceptions import Unauthorized
import sqlite3
from sqlite3 import Error
import json

class Question():
    def __init__(self, title: str, text: str, position: int, image: str, possibleAnswers):
        self.title = title
        self.text = text
        self.position = position
        self.image = image

        self.possibleAnswers= [
            {
            "text" : possibleAnswers[0]['text'],
            "isCorrect" : possibleAnswers[0]['isCorrect']
            },
            {
            "text" : possibleAnswers[1]['text'],
            "isCorrect" : possibleAnswers[1]['isCorrect']
            },
            {
            "text" : possibleAnswers[2]['text'],
            "isCorrect" : possibleAnswers[2]['isCorrect']
            },
            {
            "text" : possibleAnswers[3]['text'],
            "isCorrect" : possibleAnswers[3]['isCorrect']
            }
        ]

    def recordQuestion(self):
        dbconnection = sqlite3.connect('database.db')
        dbconnection.isolation_level = None
        cursor = dbconnection.cursor()

        title = self.title
        text = self.text
        position = self.position
        image = self.image
        possibleAnswers = self.possibleAnswers

        positionIsTaken = positionAlreadyTaken(position)

        if positionIsTaken !=0:
            changePosition(position)

        request = f"insert into Question (title,text,position,image) values ({title!r},{text!r},{position!r},{image!r})"
        cursor.execute(request)

        request2=f"select id from Question where text = {text!r}"
        cursor.execute(request2)

        for row in cursor:
            id = row[0]

        for answer in possibleAnswers :
            text = answer['text']
            isCorrect = answer['isCorrect']
            request2 = f"insert into Answer (text,id,isCorrect) values ({text!r},{id!r},'"+str(isCorrect)+"')"
            cursor.execute(request2)

        dbconnection.commit()
        dbconnection.close()

    def convertToJson(self):
        jquest = json.dumps(self.__dict__)
        return jquest
        # list_question = dict()
        # for key, value in self.__dict__.items():
        #     if value is not None and not key=='possibleAnswers':
        #         list_question[key] = value
        # return list_question

def deleteEveryQuestion():
    dbconnection = sqlite3.connect('database.db')
    dbconnection.isolation_level = None
    cursor = dbconnection.cursor()

    request = "delete from question"
    request2 = "delete from answer"
    cursor.execute(request)
    cursor.execute(request2)

    dbconnection.commit()
    dbconnection.close()

def getQuestionByyPosition(pos):

    try:
        dbconnection = sqlite3.connect('database.db')
        dbconnection.isolation_level = None

        request = "select title, text, position, image, id from Question where position = "+str(pos)

        cursor = dbconnection.execute(request)

        for row in cursor :
            title =  row[0]
            textq = row[1]
            position = row[2]
            image = row[3]
            id = row[4]

        request = "select text, id, isCorrect from Answer where id = "+str(id)        
        
        cursor = dbconnection.execute(request)
        
        possibleAnswers = [
                {
                "text" : "",
                "isCorrect" : 0
                },
                {
                "text" : "",
                "isCorrect" : 0
                },
                {
                "text" : "",
                "isCorrect" : 0
                },
                {
                "text" : "",
                "isCorrect" : 0
                }
            ]


        i=0
        for row in cursor :
            text = row[0]
            id = row[1]
            isCorrect = row[2]
            possibleAnswers[i]['text']= text
            possibleAnswers[i]['isCorrect']=str2bool(isCorrect)
            i = i+1

        quest = {
            "image":image,
            "position":position,
            "text":textq,
            "title":title,
            "possibleAnswers":possibleAnswers
        }

        return quest,200
    except:
        return 'Question not found',404

def str2bool(v):
  return v.lower() in ("True", "true","1")

def getQuestionById(id):
    try:
        dbconnection = sqlite3.connect('database.db')
        dbconnection.isolation_level = None

        request = "select title, text, position, image from Question where id = "+str(id)

        cursor = dbconnection.execute(request)

        for row in cursor :
            title =  row[0]
            textq = row[1]
            position = row[2]
            image = row[3]

        request = "select text, id, isCorrect from Answer where id = "+str(id)        
        
        cursor = dbconnection.execute(request)
        
        possibleAnswers = [
                {
                "text" : "",
                "isCorrect" : 0
                },
                {
                "text" : "",
                "isCorrect" : 0
                },
                {
                "text" : "",
                "isCorrect" : 0
                },
                {
                "text" : "",
                "isCorrect" : 0
                }
            ]


        i=0
        for row in cursor :
            text = row[0]
            id = row[1]
            isCorrect = row[2]
            possibleAnswers[i]['text']= text
            possibleAnswers[i]['isCorrect']=str2bool(isCorrect)
            i = i+1

        quest = {
            "image":image,
            "position":position,
            "text":textq,
            "title":title,
            "possibleAnswers":possibleAnswers
        }

        return quest,200
    except:
        return 'Question not found',404

def deleteQuestionByyId(questionId):
    try:
        
        dbconnection = sqlite3.connect('database.db')
        dbconnection.isolation_level = None

        request = "select position from Question where id = "+str(questionId)
        cursor = dbconnection.execute(request)

        for row in cursor:
            position = row[0]
        
        deletePosition(position)

        request2 = "delete from Question where id = "+str(questionId)
        cursor = dbconnection.execute(request2)

        request3 = "delete from Answer where id = "+str(questionId)
        cursor = dbconnection.execute(request3)

        dbconnection.commit()
        dbconnection.close()
        return "Question deleted",204
    except:
        return "Couldn't delete question",404

def updateQuestionById(title,text,position,image,possibleAnswers,questionId):

    try:
        dbconnection = sqlite3.connect('database.db')
        dbconnection.isolation_level = None

        positionIsTaken = positionAlreadyTaken(position)

        if positionIsTaken !=0:
            updatePosition(position,questionId)

        request2 = f"update Question set title = {title!r} where id = "+str(questionId)
        cursor = dbconnection.execute(request2)

        request3 = f"update Question set text = {text!r} where id = "+str(questionId)
        cursor = dbconnection.execute(request3)
   
        request4 = "update Question set position = "+str(position)+" where id = "+str(questionId)
        cursor = dbconnection.execute(request4)    

        request5 = "update Question set image = '"+image+"' where id = "+str(questionId)
        cursor = dbconnection.execute(request5)        

        request6 = "delete from Answer where id = "+str(questionId)
        cursor = dbconnection.execute(request6)  

        for Answer in possibleAnswers:
            textA = Answer['text']
            isCorrect = Answer['isCorrect']
            request7 = f"insert into Answer (text,id,isCorrect) values ({textA!r},{questionId!r},'"+str(isCorrect)+"')"
            cursor = dbconnection.execute(request7)


        dbconnection.commit()
        dbconnection.close()  
        return "Question updated",204
    except:
        return "Couldn't update question",404

def getNumberOfQuestion():

    dbconnection = sqlite3.connect('database.db')
    dbconnection.isolation_level = None

    request = "select count(*) from question"
    cursor = dbconnection.execute(request)

    for row in cursor:
        number = row[0]

    dbconnection.commit()
    dbconnection.close()  

    return number


def positionAlreadyTaken(position):
    try:
        dbconnection = sqlite3.connect('database.db')
        dbconnection.isolation_level = None

        request = "select text from question where position = "+str(position)
        cursor = dbconnection.execute(request)

        for row in cursor:
            text = row[0]

        dbconnection.commit()
        dbconnection.close()  

        return text
    except:
        return 0

def changePosition(position):
    try:
        position = int(position)
        dbconnection = sqlite3.connect('database.db')
        dbconnection.isolation_level = None

        request = "select count(*) from question"
        cursor = dbconnection.execute(request)

        for row in cursor:
            numberOfQuestion = row[0]

        for i in range(numberOfQuestion):
            request = "select position from Question where id = "+str(i+1)
            cursor = dbconnection.execute(request)

            for row in cursor:
                positionQ = row[0]
            
                if positionQ >= position:
                    newPositionQ = positionQ +1
                    request = "update Question set position = "+str(newPositionQ)+" where position <= "+str(positionQ)+" and id = "+str(i+1)
                    cursor = dbconnection.execute(request)
                
        dbconnection.commit()
        dbconnection.close()  

        return 1
    except:
        return 0

def updatePosition(position,questionId):
    try:
        position = int(position)
        dbconnection = sqlite3.connect('database.db')
        dbconnection.isolation_level = None

        request = "select count(*) from question"
        cursor = dbconnection.execute(request)

        for row in cursor:
            numberOfQuestion = row[0]

        request = "select position from Question where id = "+str(questionId)
        cursor = dbconnection.execute(request)

        for row in cursor:
            oldPosition = row[0]

        for i in range(numberOfQuestion):
            request = "select position from Question where id = "+str(i+1)
            cursor = dbconnection.execute(request)

            for row in cursor:
                positionQ = row[0]
            
                if positionQ > position and positionQ != numberOfQuestion:
                    newPositionQ = positionQ +1
                    request = "update Question set position = "+str(newPositionQ)+" where position <= "+str(positionQ)+" and id = "+str(i+1)
                    cursor = dbconnection.execute(request)

                if positionQ < position and positionQ != 1:
                    newPositionQ = positionQ -1
                    request = "update Question set position = "+str(newPositionQ)+" where position <= "+str(positionQ)+" and id = "+str(i+1)
                    cursor = dbconnection.execute(request)

                if positionQ == position:
                    if position > oldPosition:
                        up = 0
                    else:
                        up = 1

                    if up == 0:
                        newPositionQ = positionQ -1
                    else:
                        newPositionQ = positionQ +1
                    request = "update Question set position = "+str(newPositionQ)+" where position <= "+str(positionQ)+" and id = "+str(i+1)
                    cursor = dbconnection.execute(request)
                
        dbconnection.commit()
        dbconnection.close()  

        return 1
    except:
        return 0

def deletePosition(position):
    try:
        position = int(position)
        dbconnection = sqlite3.connect('database.db')
        dbconnection.isolation_level = None

        request = "select count(*) from question"
        cursor = dbconnection.execute(request)

        for row in cursor:
            numberOfQuestion = row[0]

        for i in range(numberOfQuestion):
            request = "select position from Question where id = "+str(i+1)
            cursor = dbconnection.execute(request)

            for row in cursor:
                positionQ = row[0]
            
                if positionQ > position :
                    newPositionQ = positionQ -1
                    request = "update Question set position = "+str(newPositionQ)+" where position <= "+str(positionQ)+" and id = "+str(i+1)
                    cursor = dbconnection.execute(request)
                
        dbconnection.commit()
        dbconnection.close()  

        return 1
    except:
        return 0

def getRightAnswers(): #return list of right answers by position of question
    answers = []

    numberOfQuestion = getNumberOfQuestion()

    for position in range(1,numberOfQuestion+1):
        rAnswer = rightAnswer(position)
        answers.append(rAnswer)
    
    return answers


def rightAnswer(position): #return correct answer by position
    dbconnection = sqlite3.connect('database.db')
    dbconnection.isolation_level = None

    request = "select id from Question where position = "+str(position)
    cursor = dbconnection.execute(request)

    for row in cursor:
        id = row[0]

    request = "select isCorrect from Answer where id = "+str(id)
    cursor = dbconnection.execute(request)

    answer = 0
    i = 1
    for row in cursor:
        if row[0] == "True":
            answer = i-1
        i = i+1
        



    dbconnection.commit()
    dbconnection.close() 

    return answer 

def deleteQuestionByPosition(pos):
    try:
        
        dbconnection = sqlite3.connect('database.db')
        dbconnection.isolation_level = None

        request = "select id from Question where position = "+str(pos)
        cursor = dbconnection.execute(request)

        for row in cursor:
            id = row[0]
        
        updatePositionWhenDelete(pos,id)
        # deletePosition(position)

        request2 = "delete from Question where id = "+str(id)
        cursor = dbconnection.execute(request2)

        request3 = "delete from Answer where id = "+str(id)
        cursor = dbconnection.execute(request3)

        dbconnection.commit()
        dbconnection.close()
        return "Question deleted",204
    except:
        return "Couldn't delete question",404

def updatePositionWhenDelete(position,questionId):
    try:
        position = int(position)
        dbconnection = sqlite3.connect('database.db')
        dbconnection.isolation_level = None

        request = "select count(*) from question"
        cursor = dbconnection.execute(request)

        for row in cursor:
            numberOfQuestion = row[0]

        request = "select position from Question where id = "+str(questionId)
        cursor = dbconnection.execute(request)

        for row in cursor:
            oldPosition = row[0]

        for i in range(numberOfQuestion):
            request = "select position from Question where id = "+str(i+1)
            cursor = dbconnection.execute(request)

            for row in cursor:
                positionQ = row[0]
            
                if positionQ > position :
                    newPositionQ = positionQ -1
                    request = "update Question set position = "+str(newPositionQ)+" where position <= "+str(positionQ)+" and id = "+str(i+1)
                    cursor = dbconnection.execute(request)
                
        dbconnection.commit()
        dbconnection.close()  

        return 1
    except:
        return 0