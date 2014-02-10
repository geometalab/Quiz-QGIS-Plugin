# -*- coding: utf-8 -*-
"""
/***************************************************************************
 TestGame
                                 A QGIS plugin
 test for quiz
                              -------------------
        begin                : 2013-12-19
        copyright            : (C) 2013 by rkrucker
        email                : rafael_krucker@hotmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

class Question:
	
	def __init__(self, title = '', answersArray = [] , boolArray=[]):
		self.title = title
		for i in range(len(boolArray)):
			if boolArray[i]:
				self.rightAnswer = answersArray[i]
				self.rightAnswerIndex = i
		self.answers = answersArray
		self.nrOfAnswers = len(self.answers)
		
class MatchingQuestion(Question):
	
	def __init__(self, titel = '', answersArray = [] , boolArray=[]):
		Question.__init__(self, titel, answersArray, boolArray)
		self.answersIndexes = {}
		for i in range(len(answersArray)):
			self.answersIndexes[answersArray[i]] = i
			
class MultipleChoiceQuestion(Question):
	
	def __init__(self, titel = '', answersArray = [] , boolArray=[], percentages = []):
		Question.__init__(self, titel, answersArray, boolArray)
		self.percentages = percentages
	
class PicQuestion(Question):

	def __init__(self, titel = '', answersArray = [] , boolArray=[]):
		Question.__init__(self, titel, answersArray, boolArray)
		self.picPath = ":/df/Länder/" + self.rightAnswer +".png"

class MissingWordQuestion(Question):

	def __init__(self, titel ='', answersArray = [], boolArray=[], textArray=[]):
		Question.__init__(self, titel, answersArray, boolArray)
		self.textArray = textArray
		self.title = textArray[0]
		undScores = ''
		for i in range(1, len(textArray)):
			if len(textArray[i]) < 4:
				undScores = '____'
			elif len(textArray[i]) > 20:
				for q in range(20):
					undScores += '_'
			else:
				for q in range(len(textArray[i])):
					undScores += '_'
			self.title += ' ' + undScores +'('+ str(i) + ') ' +textArray[i]
