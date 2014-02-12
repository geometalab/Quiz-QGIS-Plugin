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
	
class QuestionParser:
	
	def __init__(self, path):
		from QuestionClass import *
		import codecs
		self.path = path
		

	
		
		
		with codecs.open(self.path,'r','utf-8') as f:
					
			allQuests = []
			self.questionType = []

			allQuestions = f.read().split('\r\n\r\n')

			for question in allQuestions:
				answersArray = []
				boolArray = []
				percentages = []
				textArray = []
				title = ''

				if question.count('{') >=1:
					if question.count('}') == 1:
						titleSplit = question.split('::')
						titleAndAnswers = titleSplit[2].split('{')
						title = titleAndAnswers[0]
						answers = titleAndAnswers[1].split('}')[0]

						if '//Picture-Question' in question:
							self.questionType.append('pictureQuestion')
							correct = answers.split('=')
							leftHalf = correct[0].split('~')[1:]
							rightHalf = correct[1].split('~')
							for i in leftHalf:
								if i != '':
									boolArray.append(False)
									answersArray.append(i.strip())
							answersArray.append(rightHalf[0].strip())
							boolArray.append(True)
							if len(rightHalf) > 1:
								for i in rightHalf[1:]:
									if i != '':
										boolArray.append(False)
										answersArray.append(i.strip())
							currQuestion = PicQuestion(title, answersArray, boolArray)	
						
						elif '->' in question:
							self.questionType.append('matching')
							pairs = answers.split('=')
							for i in pairs:
								if '->' in i:
									match = i.split('->')
									answersArray.append(match[0].strip())
									answersArray.append(match[1].strip())
							currQuestion = MatchingQuestion(title, answersArray, [])
						
						elif '~%' in question:
							self.questionType.append('multipleChoice')
							options = answers.split('~')
							for i in options[1:]:
								part = i.split('%')
								percentages.append(part[1])
								answersArray.append(part[2].strip())
							currQuestion = MultipleChoiceQuestion(title, answersArray, [], percentages)
						
						else:
							self.questionType.append('stringQuestion')
							correct = answers.split('=')
							leftHalf = correct[0].split('~')[1:]
							rightHalf = correct[1].split('~')
							for i in leftHalf:
								if i != '':
									boolArray.append(False)
									answersArray.append(i.strip())
							answersArray.append(rightHalf[0].strip())
							boolArray.append(True)
							if len(rightHalf) > 1:
								for i in rightHalf[1:]:
									if i != '':
										boolArray.append(False)
										answersArray.append(i.strip())
							currQuestion = Question(title, answersArray, boolArray)	
					
					else:
						self.questionType.append('missingWord')
						tempTuples = question.split('::')[2].strip()
						tempTuples = tempTuples.split('{')
						textArray.append(tempTuples[0].strip())
						for tuple in tempTuples[1:]:
							tuple = tuple.split('}')
							answersArray.append(tuple[0].split('=')[1].split('~')[0].strip())
							if len(tuple)>1:
								textArray.append(tuple[1].strip())
						currQuestion = MissingWordQuestion('', answersArray, boolArray, textArray)
					allQuests.append(currQuestion)
				else:
					for line in question.split('\r\n'):
						if "//Title" in line:
							self.quizTitle = line[8:]
						if "//Instruction" in line:
							self.instruction = line[14:]
		
	
		self.allQuestions = allQuests