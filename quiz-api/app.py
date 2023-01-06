from flask import Flask
from flask_cors import CORS
from flask import Flask, request
from jwt_utils import *
from werkzeug.exceptions import Unauthorized
import sqlite3
from sqlite3 import Error
from question import *
from participation import *
from operator import itemgetter


app = Flask(__name__)
CORS(app)

def create_connection(db_file):
	connection = None
	try : 
		connection = sqlite3.connect(db_file)
	except Error as e :
		print(e)

@app.route('/')
def hello_world():
	x = 'world'
	return f"charles lemaire , {x}"

@app.route('/quiz-info', methods=['GET'])
def GetQuizInfo():

	size = getNumberOfQuestion()

	scores = getScores()

	sortedScores = sorted(scores, key=itemgetter('score'), reverse=True)   

	info = {"size": size, "scores": sortedScores}

	#return {"size": 0, "scores": [20,30,40]}, 200
	return info,200

@app.route('/login', methods=['POST'])
def login():
	payload = request.get_json()	

	if payload['password'] == 'flask2023':
		token = build_token()
		return {"token":token},200
	else :
		return 'Unauthorized', 401



@app.route('/questions', methods=['POST'])
def postQuestion() :

	token = request.headers.get('Authorization') 

	try: 
		#verification token
		decode_token(token[7:])

		#ajout question 
		payload = request.get_json()
		title = payload['title']
		text = payload['text']
		position = str(payload['position'])
		image = payload['image']
		possibleAnswers = payload['possibleAnswers']

		quest = Question(title,text,position,image,possibleAnswers)
		print("test")
		quest.recordQuestion()

		return payload,200
	except:
		return 'Unauthorized',401


@app.route('/questions/<questionId>', methods=['DELETE'])
def deleteQuestion(questionId):

	token = request.headers.get('Authorization') 

	try: 
		#verification token

		decode_token(token[7:])

		#suppression question 
		
		a,status = deleteQuestionByyId(questionId)

		return a,status
	except:
		return 'Unauthorized',401

@app.route('/questions/all', methods=['DELETE'])
def deleteAllQuestion():

	token = request.headers.get('Authorization') 

	try: 
		#verification token
		decode_token(token[7:])

		deleteEveryQuestion()
		return 'Deleted',204
	except:
		return 'Unauthorized',401

@app.route('/questions', methods=['GET'])
def getQuestionWithPosition():
	pos = request.args.get('position')

	questi,status = getQuestionByyPosition(pos)

	return questi,status


@app.route('/questions/<questionId>', methods=['GET'])
def getQuestionWithId(questionId):

	questi,status = getQuestionById(questionId)	

	return questi,status

@app.route('/questions/<questionId>', methods=['PUT'])
def updateQuestionWithId(questionId):

	token = request.headers.get('Authorization') 

	try: 
		#verification token
		decode_token(token[7:])

		#ajout question 
		payload = request.get_json()
		title = payload['title']
		text = payload['text']
		position = str(payload['position'])
		image = payload['image']
		possibleAnswers = payload['possibleAnswers']

		quest,status = updateQuestionById(title,text,position,image,possibleAnswers,questionId)

		return quest,status
	except:
		return 'Unauthorized',401

@app.route('/participations', methods=['POST'])
def postParticipation() :

	payload = request.get_json()
	playerName = payload['playerName']
	answers = payload['answers']
	score,status = calculateScore(answers)

	partJ ="Couldn't register participation"

	if status == 200:
		part = Participation(playerName,score)
		part.recordParticipation()

		partJ = part.convertToJson()

	return partJ,status

@app.route('/participations/all', methods=['DELETE'])
def deleteAllParticipations():

	token = request.headers.get('Authorization') 

	try: 
		#verification token
		decode_token(token[7:])

		deleteEveryParticipations()
		return 'Deleted',204
	except:
		return 'Unauthorized',401

@app.route('/participationsScore', methods=['GET'])
def getLastRegisteredScore():

	score,status = getLastScore()	

	return score,status


if __name__ == "__main__":
    app.run()

