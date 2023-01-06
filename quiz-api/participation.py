from flask import Flask
from flask_cors import CORS
from flask import Flask, request
from jwt_utils import *
from werkzeug.exceptions import Unauthorized
import sqlite3
from sqlite3 import Error
import json
from question import *

class Participation():
    def __init__(self, playerName: str, score: int):
        self.playerName = playerName
        self.score = score
    
    def recordParticipation(self):
        dbconnection = sqlite3.connect('database.db')
        dbconnection.isolation_level = None
        cursor = dbconnection.cursor()

        playerName = self.playerName
        score = self.score

        request = "insert into Participation (playerName,score) values ('"+playerName+"','"+str(score)+"')"
        cursor.execute(request)

        dbconnection.commit()
        dbconnection.close()

    def convertToJson(self):
        part = dict()
        for key, value in self.__dict__.items():
            if value is not None and not key=='possibleAnswers':
                part[key] = value
        return part
        

def calculateScore(answers):

    score = 0

    rightAnswers = getRightAnswers()

    i=0

    if len(rightAnswers) != len(answers):
        return "Wrong number of answers",400    
    else:
        for i in range(len(answers)):
            if answers[i] == rightAnswers[i]:
                score = score +1 

        return score,200

def deleteEveryParticipations():
    dbconnection = sqlite3.connect('database.db')
    dbconnection.isolation_level = None
    cursor = dbconnection.cursor()

    request = "delete from Participation"

    cursor.execute(request)


    dbconnection.commit()
    dbconnection.close()

def getScores():
    dbconnection = sqlite3.connect('database.db')
    dbconnection.isolation_level = None

    request = "select count(*) from Participation"
    cursor = dbconnection.execute(request)

    for row in cursor:
        numberOfParticipation = row[0]

    scores=[]

    for id in range(1,numberOfParticipation+1):
        
        request="select playerName, score from Participation where id= "+str(id)
        cursor = dbconnection.execute(request)

        for row in cursor:
            playerName = row[0]
            score  = row[1]
            
            part = {'playerName':playerName, 'score':score}

            scores.append(part)


            
    
    dbconnection.commit()
    dbconnection.close()  

    return scores

def getLastScore():
        try:
            dbconnection = sqlite3.connect('database.db')
            dbconnection.isolation_level = None

            request = "select count(*) from Participation"
            cursor = dbconnection.execute(request)

            for row in cursor:
                numberOfParticipation = row[0]

            request = "select score from Participation where id = "+str(numberOfParticipation)

            cursor = dbconnection.execute(request)

            for row in cursor :
                score =  row[0]

            return str(score),200
        except:
            return 'Question not found',404


