#!/usr/bin/python

import sys

# Represents how we define a question.
class Question:
  # Question identifier
  id = None
  # Related users
  users = []

  def __init__(self, id, author):
    self.id = id
    self.users = [int(author)]

  # Add an user.
  def addUser(self, user):
    self.users.append(int(user))

  # Print the result
  def printResult(self):
    print self.id, '\t', self.users

question = None

for line in sys.stdin:
  mappedData = line.strip().split("\t")
  if len(mappedData) != 2:
    # Something has gone wrong. Skip this line.
    continue
  
  # Load line to variables
  questionId, user = mappedData
  
  if question == None:
    question = Question(questionId, user)
  elif question.id == questionId:
    question.addUser(user)
  else:
    question.printResult()
    question = Question(questionId, user)

# Print last question
if question != None:
  question.printResult()
