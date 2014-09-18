#!/usr/bin/python

import sys

# Represents how we define a question.
class Question:
  # Question identifier
  id = None
  # Question body length
  questionLength = None
  # Total of answer
  answers = 0
  # Sum of all answer's body
  sumAnswersLength = 0

  def __init__(self, id, questionLength):
    self.id = id
    self.questionLength = questionLength

  # Add an answer. It increments our answers count and sum its length to our accumulator.
  def addAnswer(self, answerLength):
    self.answers += 1
    self.sumAnswersLength += float(answerLength)

  # Print the result
  def printResult(self):
    if self.answers > 0:
      print self.id, '\t', self.questionLength, '\t', self.sumAnswersLength / self.answers
    else:
      print self.id, '\t', self.questionLength, '\t', self.answers

question = None

for line in sys.stdin:
  data_mapped = line.strip().split("\t")
  if len(data_mapped) != 3:
    # Something has gone wrong. Skip this line.
    continue
  
  # Load line to variables
  identifier, type, bodyLength = data_mapped
  
  # If it is a question
  if type == 'A':
    if question != None:
      question.printResult()
    question = Question(identifier, bodyLength)

  # If it is an answer
  elif type == 'B':
    question.addAnswer(bodyLength)

# Print last question
if question != None:
  question.printResult()
