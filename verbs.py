
import random
import os
from conjugation import determineConjugation
from conjugate import determineAnswer

persons = {"1st person": 1, "2nd person": 1, "3rd person": 1}
numbers = {"singular": 1, "plural": 1}
tenses = {"present": 3, "perfect": 3, "imperfect": 3, "pluperfect": 1, "future": 2, "future perfect": 1}
voices = {"active": 3, "passive": 2}
moods = {"indicative": 3, "subjunctive": 0}

components = [persons, numbers, tenses, voices, moods]

def weightedChoice(choiceDict):
	total = 0
	for val in choiceDict.values():
		total += val
	choice = int(random.random()*total)+1
	keys = choiceDict.keys()

	current = 0
	while choice > 0:
		choice -= choiceDict[keys[current]]
		if choice > 0:
			current += 1
	return keys[current]

def removeNonAlphaNumeric(word):
	newWord = ""
	for char in word:
		if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789":
			newWord += char
	return newWord

verbParts = []
with open("wheelocks.txt") as verbFile:
	readFile = [verbFile.read()]
	splitN = []
	for item in readFile:
		for piece in item.split("\n"):
			splitN.append(piece)
	splitR = []
	for item in splitN:
		for piece in item.split("\r"):
			splitR.append(piece)
	verbParts = splitR
	for p in range(len(verbParts)):
		verbParts[p] = verbParts[p].split(" ")
		for w in range(len(verbParts[p])):
			verbParts[p][w] = removeNonAlphaNumeric(verbParts[p][w])


while True:



	#IGNORE EVERYTHING ABOVE!!!
	# verbParts is a list of all of the principle parts of each verb

	verbNum = int(random.random()*len(verbParts)) # number of the verb chosen
	chosenVerb = verbParts[verbNum] # the principle parts of the chosen verb
	chosenConjugation = determineConjugation(chosenVerb) # determine the congugation of the verb

	# Make question:
	chosenQuestion = []
	printString = "What is the "
	for component in components:
		chosenComponent = weightedChoice(component)
		printString += chosenComponent + " "
		chosenQuestion.append(chosenComponent)
	printString += "of the verb " + chosenVerb[0] + "?"

	#Make list of verb parts:
	verbString = ""
	for p in range(len(chosenVerb)):
		verbString += chosenVerb[p]
		if (p + 1 != len(chosenVerb)):
			verbString += ", "

	# Determine Answer:

	answer = determineAnswer(chosenConjugation, chosenVerb, chosenQuestion)

	# DISPLAY:
	os.system("clear")
	print(printString)
	print("Principal Parts: " + verbString)
	os.system("say " + printString)
	print("Answer: " + answer)

	# ASK FOR REPEAT:
	print("\n" + '{:^60}'.format("press enter for another question..."))
	raw_input()

