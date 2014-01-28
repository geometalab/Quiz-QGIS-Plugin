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
from __future__ import unicode_literals
import io
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
import resources_rc
from testgamedialog import TestGameDialog
from startGameDialog import StartGameDialog
import os.path
from noPathNotification import *
from pointsDialog import PointsDialog
from trainingQuizDialog import TrainingQuizDialog
from ui_chooseTrainingQuizDialog import ChooseTrainingQuizDialog
from helpDialog import HelpDialog
import time
import sys
import math
import codecs
import random
from uberBoxDialog import UberBoxDialog

class TestGame:
	
	Score = 0
	path = ''
	questionNumber = 0
	questions = []
	questionType = []
	questionTitle = []
	answers = []
	questionFrame = 0
	frameQuestionAnswered = []
	timeElapsed = 0
	dirPath = ''
	log = ''
	quizTitle = ''
	instruction =''
	language = 0
	translator = [[],[],[]]
	rightListShuffled = []
	siteVisitedMatching = []
	leftChoiceMatching = ''
	linesForMatching = []
	lines = []
	buttonList = []
	windowList = []
	
	def __init__(self, iface):
		
		global dirPath
		global translator
		
		reload(sys)
		sys.setdefaultencoding('utf-8')
	   
		self.iface = iface

		self.plugin_dir = os.path.dirname(__file__)

		locale = QSettings().value("locale/userLocale")[0:2]
		localePath = os.path.join(self.plugin_dir, 'i18n', 'testgame_{}.qm'.format(locale))
		self.user_plugin_dir = QFileInfo(QgsApplication.qgisUserDbFilePath()).path() + "python/plugins/TestGame"
		self.dirPath = self.user_plugin_dir
		
		if os.path.exists(localePath):
			self.translator = QTranslator()
			self.translator.load(localePath)

			if qVersion() > '4.3.3':
				QCoreApplication.installTranslator(self.translator)
		
		
		self.translator = [[],[], []]
		
		with codecs.open(self.dirPath +'/germanText.txt','r','utf-8') as f:
			for line in f:
				self.translator[0].append(line[:-1])
			f.close()
		
		with codecs.open(self.dirPath +'/englishText.txt','r','utf-8') as f:
			for line in f:
				self.translator[1].append(line[:-1])
			f.close()
		
		with codecs.open(self.dirPath +'/frenchText.txt','r','utf-8') as f:
			for line in f:
				self.translator[2].append(line[:-1])
			f.close()
	
		self.dlg = TestGameDialog()
			
	def initGui(self):

		self.action = QAction(QIcon(":/df/Länder/icon.png"),u"Euroquiz", self.iface.mainWindow())
		self.action.triggered.connect(self.run)
		self.iface.addToolBarIcon(self.action)
		self.iface.addPluginToMenu(u"&EuroQuiz", self.action)

	def unload(self):

		self.iface.removePluginMenu(u"&EuroQuiz", self.action)
		self.iface.removeToolBarIcon(self.action)

	def run(self):
		global buttonList
		global language
		global globalFont
		global windowList
		
		if QSettings().value("locale/userLocale")[0:2] == 'de':
			self.language = 0
		elif QSettings().value("locale/userLocale")[0:2] == 'fr':
			self.language = 2
		else:
			self.language = 1
		
		globalFont = self.dlg.ui.startGame.font()
		self.dlg.ui.startGame.setText(self.translator[self.language][0])
		self.buttonList.append(self.dlg.ui.startGame)
		self.dlg.ui.startTraining.setText(self.translator[self.language][1])
		self.buttonList.append(self.dlg.ui.startTraining)
		self.dlg.ui.chooseQuiz.setText(self.translator[self.language][2])
		self.buttonList.append(self.dlg.ui.chooseQuiz)
		self.dlg.ui.pushButton.setText(self.translator[self.language][3])
		self.buttonList.append(self.dlg.ui.pushButton)
		self.dlg.ui.menuOptions_2.setTitle(self.translator[self.language][37])
		self.dlg.ui.language.setTitle(self.translator[self.language][4])
		self.dlg.ui.fontMenu.setTitle(self.translator[self.language][40])
		self.dlg.ui.german.setText(self.translator[self.language][42])
		self.dlg.ui.english.setText(self.translator[self.language][41])
		self.dlg.ui.french.setText(self.translator[self.language][61])
		self.dlg.ui.menuGames.setTitle(self.translator[self.language][43])
		self.dlg.ui.geogame.setText(self.translator[self.language][38])
		self.dlg.ui.quizPlatform.setText(self.translator[self.language][39])
		self.dlg.ui.menuHilf.setTitle(self.translator[self.language][3])
		self.dlg.ui.actionAbout.setText(self.translator[self.language][46])
		self.dlg.ui.actionWebhelp.setText(self.translator[self.language][45])
		self.dlg.ui.actionContact.setText(self.translator[self.language][44])
		self.dlg.ui.actionSmaller.setText(self.translator[self.language][63])
		self.dlg.ui.actionBigger.setText(self.translator[self.language][62])
		self.buttonList.append(self.dlg.ui.startTitel)
		self.buttonList.append(self.dlg.ui.startImage)
		'''self.dlg.ui.label.setText(self.translator[self.language][4])
		self.dlg.ui.label_2.setText(self.translator[self.language][31])'''
		'''self.dlg.ui.comboBox.setCurrentIndex(self.language)'''
		'''print self.dlg.ui.label.font()
		print self.dlg.ui.label.font().pixelSize()
		print self.dlg.ui.label.font().pointSize()
		@self.dlg.ui.comboBox.currentIndexChanged.connect
		def handle(index):
			self.changeLanguage()'''
		
		self.dlg.ui.actionContact.triggered.connect(lambda: QDesktopServices.openUrl(QUrl("mailto:rkrucker@hsr.ch")))
		self.dlg.ui.actionWebhelp.triggered.connect(lambda: QDesktopServices.openUrl(QUrl("http://giswiki.hsr.ch/QGIS-Materialien")))
		self.dlg.ui.geogame.triggered.connect(lambda: QDesktopServices.openUrl(QUrl("http://giswiki.hsr.ch/GeoGames") ) )
		self.dlg.ui.quizPlatform.triggered.connect(lambda: QDesktopServices.openUrl(QUrl("http://giswiki.hsr.ch/QGIS-Materialien")))
		self.dlg.ui.actionAbout.triggered.connect(self.about)
		self.dlg.ui.english.triggered.connect(lambda: self.changeLanguage(1))
		self.dlg.ui.german.triggered.connect(lambda: self.changeLanguage(0))	
		self.dlg.ui.french.triggered.connect(lambda: self.changeLanguage(2))
		self.dlg.ui.startGame.setEnabled(False)
		self.dlg.ui.startTraining.setEnabled(False)
		self.dlg.ui.startGame.clicked.connect(self.startQuiz)
		self.dlg.ui.startTraining.clicked.connect(self.training)
		self.dlg.ui.chooseQuiz.clicked.connect(self.selectQuiz)
		self.dlg.ui.pushButton.clicked.connect(self.help)
		self.dlg.ui.actionSmaller.triggered.connect(self.fontSmaller)
		self.dlg.ui.actionBigger.triggered.connect(self.fontBigger)
		self.dlg.show()
		self.windowList.append(self.dlg)
		
		
		
		
		
	def changeLanguage(self, lang):
		
		global language
		
		self.language = lang
		self.dlg.ui.startGame.setText(self.translator[self.language][0])
		self.dlg.ui.startTraining.setText(self.translator[self.language][1])
		self.dlg.ui.chooseQuiz.setText(self.translator[self.language][2])
		self.dlg.ui.pushButton.setText(self.translator[self.language][3])
		self.dlg.ui.menuOptions_2.setTitle(self.translator[self.language][37])
		self.dlg.ui.language.setTitle(self.translator[self.language][4])
		self.dlg.ui.fontMenu.setTitle(self.translator[self.language][40])
		self.dlg.ui.actionSmaller.setText(self.translator[self.language][63])
		self.dlg.ui.actionBigger.setText(self.translator[self.language][62])
		self.dlg.ui.german.setText(self.translator[self.language][42])
		self.dlg.ui.english.setText(self.translator[self.language][41])
		self.dlg.ui.french.setText(self.translator[self.language][61])
		self.dlg.ui.menuGames.setTitle(self.translator[self.language][43])
		self.dlg.ui.geogame.setText(self.translator[self.language][38])
		self.dlg.ui.quizPlatform.setText(self.translator[self.language][39])
		self.dlg.ui.menuHilf.setTitle(self.translator[self.language][3])
		self.dlg.ui.actionAbout.setText(self.translator[self.language][46])
		self.dlg.ui.actionWebhelp.setText(self.translator[self.language][45])
		self.dlg.ui.actionContact.setText(self.translator[self.language][44])
	
	def fontSmaller(self):
		
		global globalFont
		
		for i in self.buttonList:
			tempFont = i.font()
			tempFont.setPointSize(tempFont.pointSize() - 2)
			i.setFont(tempFont)
		
	def fontBigger(self):
		
		global globalFont
		
		for i in self.buttonList:
			tempFont = i.font()
			tempFont.setPointSize(tempFont.pointSize() + 2)
			i.setFont(tempFont)
	
	def selectQuiz(self):
		
		global path
		
		self.path = QFileDialog.getOpenFileName(self.dlg, 'Open File', self.dirPath + '\quizes','*.txt')
		
		if self.path != '':
			self.questions = self.parseQuestion()
			self.dlg.ui.actionQuiz_trainieren.setEnabled(True)	
			self.dlg.ui.actionQuiz_starten.setEnabled(True)
			self.dlg.ui.startGame.setEnabled(True)
			self.dlg.ui.startTraining.setEnabled(True)
			self.dlg.ui.startTitel.setFont(globalFont)
			self.dlg.ui.startTitel.setText(u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; font-style:normal; color:#000000;\">" + self.quizTitle+"</span></p></body></html>")
			self.dlg.ui.startImage.setFont(globalFont)
			self.dlg.ui.startImage.setWordWrap(True)
			self.dlg.ui.startImage.setText("<html><head/><body><p align = \"center\">"+self.instruction+"<br/></p></body></html>")
			
			
	
	def parseQuestion(self):
		
		global quizTitle
		global instruction
		global questionType 
		global questionTitle 
		
		with codecs.open(self.path,'r','utf-8') as f:
					
			allQuests = []
			self.questionType = []
			self.questionTitle = []
			allQuestions = f.read().split('\r\n\r\n')
			
			for question in allQuestions:
				multipleWord = False
				quest = [[],[]]
				
				for line in question.split('\r\n'):
					if "//Titel" in line:
						self.quizTitle = line[8:]
					if "//Anleitung" in line:
						self.instruction = line[12:]
					
					if line[0] == ':':
						titleSeperator = line.rsplit('::',1)
						self.questionTitle.append(titleSeperator[2:len(titleSeperator)-3])
						
						if len(titleSeperator) == 2 and titleSeperator[1] != '':
							multipleWord = True
							quest[0].append(titleSeperator[1])
					
					if '->' in line and multipleWord:
						self.questionType.append('matching')
						quest[1].append(0)
						matchPairs = line.split('=')
						
						for i in range(0, len(matchPairs)):
							if '->' in matchPairs[i]:
								if '}' in matchPairs[i]:
									temp = matchPairs[i].split('}')
									matchPair = temp[0].split('->')
								else:
									matchPair = matchPairs[i].split('->')
								quest[0].append(matchPair[0])
								quest[1].append(matchPair[1].lstrip())
					
					
					elif line[0] == '{' and multipleWord:
						ans = line.split()
						if ans[2][1] == '%':
							self.questionType.append('multipleChoice')
							quest[1].append(0)
							
							for i in range(0, len(ans)):
						
								if ans[i][0]=='~':
									percentage = ans[i].split('%')
									
									quest[1].append(percentage[1])
									answerString = ''
									answerString += percentage[2]

									k = 1

									while (ans[i + k][0] != '=') and (ans[i + k][0] != '~') and (ans[i + k][0] != '}'):
										answerString += ' '
										answerString += ans[i+k]
										k += 1
									quest[0].append(answerString)
						
						else:
							self.questionType.append('stringQuestion')
							quest[1].append(False)
							for i in range(0, len(ans)):
							
								if ans[i][0]== '=':
									quest[1].append(True)
									answerString = ''
									answerString += ans[i][1:]
							
									k =1
									while ((ans[i + k][0]) != '=') and (ans[i + k][0]) != '~' and (ans[i + k][0] != '}'):
										answerString += ' '
										answerString += ans[i+k]
										k += 1
									quest[0].append(answerString)

								elif ans[i][0]=='~':
									quest[1].append(False)
									answerString = ''
									answerString += ans[i][1:]

									k = 1
									
									while (ans[i + k][0] != '=') and (ans[i + k][0] != '~') and (ans[i + k][0] != '}'):
										answerString += ' '
										answerString += ans[i+k]
										k += 1
									quest[0].append(answerString)
					
					if line[0] != '{' and line[0] != ':' and line[0] != '/' and (not line.strip()==''):
						self.questionType.append('missingWord')
						firstQuestionPart = line.split('{')
						secondQuestionPart = firstQuestionPart[1].split('}')
						quest[0].append(firstQuestionPart[0]  +' '+ '____________' +' '+ secondQuestionPart[1])
						quest[1].append(False)
						ans = secondQuestionPart[0].split()
					
						for i in range(0, len(ans)):
						
							if ans[i][0]== '=':
								quest[1].append(True)
								answerString = ''
								answerString += ans[i][1:]
		
								k =1
						
								while ( ( (k+i) != len(ans)-1)and(ans[i + k][0]) != '=') and (ans[i + k][0]) != '~' and (ans[i + k][0] != '}'):
									answerString += ' '
									answerString += ans[i+k]
									k += 1
								quest[0].append(answerString)

							elif ans[i][0]=='~':
								quest[1].append(False)
								answerString = ''
								answerString += ans[i][1:]

								k = 1
						
								while ( (k+i) != len(ans) and ans[i + k][0] != '=') and (ans[i + k][0] != '~') and (ans[i + k][0] != '}'):
									answerString += ' '
									answerString += ans[i+k]
									k += 1
								
								quest[0].append(answerString)	
						
					
					if '{pic' in line:
						self.questionType.append('pictureQuestion')
						ans = line.split()
						for i in range(0, len(ans)):
				
							if ans[i][0]== '=':
								quest[1].append(True)
								answerString = ''
								answerString += ans[i][1:]
							
								k =1
								while ((ans[i + k][0]) != '=') and (ans[i + k][0]) != '~' and (ans[i + k][0] != '}'):
									answerString += ' '
									answerString += ans[i+k]
									k += 1
								quest[0].append(answerString)

							elif ans[i][0]=='~':
								quest[1].append(False)
								answerString = ''
								answerString += ans[i][1:]

								k = 1

								while (ans[i + k][0] != '=') and (ans[i + k][0] != '~') and (ans[i + k][0] != '}'):
									answerString += ' '
									answerString += ans[i+k]
									k += 1
								quest[0].append(answerString)	
				if not (len(quest[0]) < 2):
					allQuests.append(quest)
		
		
		
		return allQuests
	
	def help(self):
		
		global buttonList
		global windowList
		
		self.help = HelpDialog()
		self.help.ui.label_3.setText(self.translator[self.language][53])
		self.help.ui.label_3.setFont(globalFont)
		self.help.ui.label_4.setText(self.translator[self.language][54])
		self.help.ui.label_4.setOpenExternalLinks(True)
		self.help.ui.label_5.setText(self.translator[self.language][55])
		self.help.ui.label_6.setText(self.translator[self.language][56])
		self.help.ui.label_6.setOpenExternalLinks(True)
		self.help.ui.label_7.setText(self.translator[self.language][57])
		self.help.ui.label_8.setText(self.translator[self.language][58])
		self.help.ui.label_8.setOpenExternalLinks(True)
		self.help.ui.label_9.setText(self.translator[self.language][59])
		self.help.ui.label_10.setText(self.translator[self.language][60])
		self.help.ui.label_4.setFont(globalFont)
		self.help.ui.label_5.setFont(globalFont)
		self.help.ui.label_6.setFont(globalFont)
		self.help.ui.label_7.setFont(globalFont)
		self.help.ui.label_8.setFont(globalFont)
		self.help.ui.label_9.setFont(globalFont)
		self.help.ui.label_10.setFont(globalFont)
		self.windowList.append(self.help)
		self.buttonList.append(self.help.ui.label_3)
		self.buttonList.append(self.help.ui.label_4)
		self.buttonList.append(self.help.ui.label_5)
		self.buttonList.append(self.help.ui.label_6)
		self.buttonList.append(self.help.ui.label_7)
		self.buttonList.append(self.help.ui.label_8)
		self.buttonList.append(self.help.ui.label_9)
		self.buttonList.append(self.help.ui.label_10)
		
		self.help.show()
	
	def about(self):
	
		global windowList
		
		self.aboutWindow = UberBoxDialog()
		self.aboutWindow.ui.label_3.setText(self.translator[self.language][47])
		self.aboutWindow.ui.label_4.setText(self.translator[self.language][48])
		self.aboutWindow.ui.label_5.setText(self.translator[self.language][49])
		self.aboutWindow.ui.label_6.setText(self.translator[self.language][50])
		self.aboutWindow.ui.label_7.setText(self.translator[self.language][51])
		self.aboutWindow.ui.label_8.setText(self.translator[self.language][52])
		self.aboutWindow.ui.label_8.setOpenExternalLinks(True)
		self.aboutWindow.ui.label_3.setFont(globalFont)
		self.aboutWindow.ui.label_4.setFont(globalFont)
		self.aboutWindow.ui.label_5.setFont(globalFont)
		self.aboutWindow.ui.label_6.setFont(globalFont)
		self.aboutWindow.ui.label_7.setFont(globalFont)
		self.aboutWindow.ui.label_8.setFont(globalFont)
		self.buttonList.append(self.aboutWindow.ui.label_3)
		self.buttonList.append(self.aboutWindow.ui.label_4)
		self.buttonList.append(self.aboutWindow.ui.label_5)
		self.buttonList.append(self.aboutWindow.ui.label_6)
		self.buttonList.append(self.aboutWindow.ui.label_7)
		self.buttonList.append(self.aboutWindow.ui.label_8)
		self.windowList.append(self.aboutWindow)
		self.aboutWindow.show()
		
	def addWidgets(self):
	
		self.currWindow.ui.checkBoxes = []
		self.currWindow.ui.matches = []
		self.currWindow.ui.matchingLabels = []
		self.currWindow.ui.matchingButtons = []
		self.currWindow.ui.matchingLabelsLeft = []
		self.currWindow.ui.matchingButtonsLeft = []
		self.currWindow.ui.matchingLabelsRight = []
		self.currWindow.ui.matchingButtonsRight = []
		
		for i in range(0,12):
			horizontalLayout = QtGui.QHBoxLayout()
			horizontalLayout.setObjectName("horizontalLayout")
			spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
			label = QtGui.QLabel()
			label.setObjectName("label")
			self.currWindow.ui.matchingLabels.append(label)
			pushButton = QtGui.QPushButton()
			pushButton.setText("")
			pushButton.setObjectName("pushButton")
			pushButton.setAutoFillBackground(True)
			self.currWindow.ui.matchingButtons.append(pushButton)
			if i % 2 == 0:
				horizontalLayout.addItem(spacerItem)
				horizontalLayout.addWidget(label)
				horizontalLayout.addWidget(pushButton)
				self.currWindow.ui.matchingButtonsLeft.append(pushButton)
				self.currWindow.ui.matchingLabelsLeft.append(label)
			else:
				horizontalLayout.addWidget(pushButton)
				horizontalLayout.addWidget(label)
				horizontalLayout.addItem(spacerItem)
				self.currWindow.ui.matchingButtonsRight.append(pushButton)
				self.currWindow.ui.matchingLabelsRight.append(label)
			self.currWindow.ui.matches.append(horizontalLayout)
			
			checkBox = QtGui.QCheckBox()
			self.currWindow.ui.checkBoxes.append(checkBox)
		
		for currBox in range(0, len(self.currWindow.ui.checkBoxes)):
			height = currBox / 2
			width = (currBox % 2) * 2
			self.currWindow.ui.gridLayout.addWidget(self.currWindow.ui.checkBoxes[currBox], height, width + 1, 1, 1 )	
			self.currWindow.ui.gridLayout.addLayout(self.currWindow.ui.matches[currBox], height, width + 1, 1, 1 )	
		
		self.currWindow.ui.buttonArray = []
		self.currWindow.ui.buttonArray.append(self.currWindow.ui.pushButton)
		self.currWindow.ui.buttonArray.append(self.currWindow.ui.pushButton_2)
		self.currWindow.ui.buttonArray.append(self.currWindow.ui.pushButton_3)
		self.currWindow.ui.buttonArray.append(self.currWindow.ui.pushButton_4)
		self.currWindow.ui.buttonArray.append(self.currWindow.ui.pushButton_5)
		self.currWindow.ui.buttonArray.append(self.currWindow.ui.pushButton_6)
		self.currWindow.ui.buttonArray.append(self.currWindow.ui.pushButton_7)
		self.currWindow.ui.buttonArray.append(self.currWindow.ui.pushButton_8)
		self.currWindow.ui.buttonArray.append(self.currWindow.ui.pushButton_9)
		self.currWindow.ui.buttonArray.append(self.currWindow.ui.pushButton_10)
		self.currWindow.ui.buttonArray.append(self.currWindow.ui.pushButton_11)
		self.currWindow.ui.buttonArray.append(self.currWindow.ui.pushButton_12)
		
		
			
	def startQuiz(self):
		
		global Score
		global questions
		global frameQuestionAnswered
		global timeElapsed
		global siteVisitedMatching
		global rightListShuffeld
		global linesForMatching
		
		self.timeElapsed = time.time()
		self.Score = 0
		self.questionNumber = 0
		self.frameQuestionAnswered = [0 for x in range(len(self.questions))]
		for i in range(0, len(self.questions)):
			self.frameQuestionAnswered[i] = False
		
		self.siteVisitedMatching = [0 for x in range(len(self.questions))]
		for i in range(0, len(self.questions)):
			self.siteVisitedMatching[i] =  False

		self.rightListShuffeld = []
		self.linesForMatching = []
		self.lines = []
		for i in range(0, len(self.questions)):
			self.rightListShuffeld.append([])
			self.linesForMatching.append([])
			self.lines.append([])
		self.currWindow = StartGameDialog()
		self.addWidgets()
		
		for i in self.currWindow.ui.buttonArray:
			i.setVisible(False)
			i.clicked.connect(self.scorePenalty)
			
		for i in self.currWindow.ui.checkBoxes:
			i.stateChanged.connect(self.checkState)
			i.setVisible(False)
		
		for i in self.currWindow.ui.matchingLabelsLeft:
			i.setVisible(False)
			i.setText('')
			
		for i in self.currWindow.ui.matchingLabelsRight:
			i.setVisible(False)
			i.setText('')
			
		for i in self.currWindow.ui.matchingButtonsLeft:
			i.setVisible(False)
			i.clicked.connect(self.matchingLeftButtonClicked)
			
		for i in self.currWindow.ui.matchingButtonsRight:
			i.setVisible(False)
			i.clicked.connect(self.matchingRightButtonClicked)
			
		if self.questionType[0] == 'multipleChoice':
			self.currWindow.ui.label.setText("<html><head/><body><p align=\"center\">" + self.questions[0][0][0] +"</p></body></html>")
			
			for i in range(1,len(self.questions[0][0])):
				self.currWindow.ui.checkBoxes[i-1].setText(self.questions[0][0][i])
				self.currWindow.ui.checkBoxes[i-1].setVisible(True)

					
		if self.questionType[0] == 'pictureQuestion' :
			for i in range(0,len(self.questions[0][0])):
				self.currWindow.ui.buttonArray[i].setText(self.questions[0][0][i])
				self.currWindow.ui.buttonArray[i].setVisible(True)
				
				if self.questions[0][1][i]:
					self.currWindow.ui.label.setText("<html><head/><body><p align=\"center\"><img src=\":/df/Länder/" + self.questions[0][0][i] +".png\"/></p></body></html>")
					self.currWindow.ui.buttonArray[i].clicked.disconnect()
					self.currWindow.ui.buttonArray[i].clicked.connect(self.scoreBonus)
				
				
		if  self.questionType[0] == 'stringQuestion' or self.questionType[0] == 'missingWord':
			self.currWindow.ui.label.setText("<html><head/><body><p align=\"center\">" + self.questions[0][0][0] +"</p></body></html>")
			
			for i in range(1,len(self.questions[0][0])):
				self.currWindow.ui.buttonArray[i-1].setText(self.questions[0][0][i])
				self.currWindow.ui.buttonArray[i-1].setVisible(True)	
				
				if self.questions[0][1][i-1]:
					self.currWindow.ui.buttonArray[i-1].clicked.disconnect()
					self.currWindow.ui.buttonArray[i-1].clicked.connect(self.scoreBonus)
		
		
		if self.questionType[0] == 'matching':
			self.currWindow.ui.label.setText("<html><head/><body><p align=\"center\">" + self.questions[0][0][0] +"</p></body></html>")
			rightListShuffeld = []
			
			for i in range(1,len(self.questions[0][0])):
					self.currWindow.ui.matchingLabels[(i-1) * 2].setVisible(True)
					self.currWindow.ui.matchingLabels[(i-1) * 2].setText(self.questions[0][0][i])
					self.currWindow.ui.matchingButtons[(i-1)*2].setVisible(True)
					self.currWindow.ui.matchingButtons[(i-1)*2].setObjectName(self.questions[0][0][i])
					self.currWindow.ui.matchingButtons[((i-1)*2)+1].setVisible(True)
					self.currWindow.ui.matchingButtons[((i-1)*2)+1].setEnabled(False)
					self.currWindow.ui.matchingButtons[((i-1)*2)+1].setObjectName(self.questions[0][0][i])
					rightListShuffeld.append(self.questions[0][1][i])
					self.linesForMatching[0].append([])
					
			random.shuffle(rightListShuffeld)
			for i in range(0, len(rightListShuffeld)):
				self.currWindow.ui.matchingLabels[((i) * 2)+1].setVisible(True)
				self.currWindow.ui.matchingLabels[((i) * 2)+1].setText(rightListShuffeld[i])
		
		self.currWindow.ui.label_2.setText(self.translator[self.language][29] + ' ' + str(self.questionNumber +1) + ' ' + self.translator[self.language][30]+ ' ' + str(len(self.questions)))
		self.currWindow.ui.pushButton_14.clicked.connect(self.nextQuestion)
		self.currWindow.ui.pushButton_14.setText(self.translator[self.language][6])
		self.currWindow.ui.pushButton_13.setEnabled(False)
		self.currWindow.ui.pushButton_13.clicked.connect(self.previousQuestion)
		self.currWindow.ui.pushButton_13.setText(self.translator[self.language][5])
		self.currWindow.show()
		
		
		
		self.paintPanel = Painter(self, self.lines)
		#self.paintPanel.close()
		self.currWindow.ui.stackedWidget.insertWidget(0,self.paintPanel)
		self.currWindow.ui.stackedWidget.setCurrentWidget(self.paintPanel)
	
	def nextQuestion(self):
		
		global questionNumber
		global frameQuestionAnswered
		global siteVisitedMatching
		global rightListShuffeld

		self.questionNumber += 1

		if self.questionNumber == len(self.questions) -1:
			self.currWindow.ui.pushButton_14.setText(self.translator[self.language][7])
			self.currWindow.ui.pushButton_14.clicked.disconnect()
			self.currWindow.ui.pushButton_14.clicked.connect(self.showNormalResults)
			finished = True
			
			for i in range(0, len(self.questions)):
				if not self.frameQuestionAnswered[i]:
					finished = False
			
			if finished or self.questionType[self.questionNumber-1]==2:
				self.currWindow.ui.pushButton_14.setEnabled(True)	
			else:
				self.currWindow.ui.pushButton_14.setEnabled(False)
		else:
			self.currWindow.ui.pushButton_14.setText(self.translator[self.language][6])
			self.currWindow.ui.pushButton_14.clicked.disconnect()
			self.currWindow.ui.pushButton_14.clicked.connect(self.nextQuestion)
		
		if self.questionNumber == 0:
			self.currWindow.ui.pushButton_13.setEnabled(False)
		else: 
			self.currWindow.ui.pushButton_13.setEnabled(True)
		
		for i in self.currWindow.ui.buttonArray:
			i.setText('')
			i.setVisible(False)	
		
		for i in self.currWindow.ui.checkBoxes:
			i.setText('')
			i.setVisible(False)	
		
		for i in self.currWindow.ui.matchingButtons:
			i.setVisible(False)
		
		for i in self.currWindow.ui.matchingLabels:
			i.setText('')
			i.setVisible(False)	
			
		if self.questionType[self.questionNumber] == 'multipleChoice':
			self.currWindow.ui.label.setText("<html><head/><body><p align=\"center\">" + self.questions[self.questionNumber][0][0] +"</p></body></html>")
			self.frameQuestionAnswered[self.questionNumber] = True
			for nr in range(1,len(self.questions[self.questionNumber][0])):
				self.currWindow.ui.checkBoxes[nr-1].setText(self.questions[self.questionNumber][0][nr])
				self.currWindow.ui.checkBoxes[nr-1].setObjectName(str(self.questions[self.questionNumber][1][nr]))
				self.currWindow.ui.checkBoxes[nr-1].setVisible(True)
				
				
		if self.questionType[self.questionNumber] == 'pictureQuestion' :
			for nr in range(0,len(self.questions[self.questionNumber][1])):
				self.currWindow.ui.buttonArray[nr].setVisible(True)
				self.currWindow.ui.buttonArray[nr].setText(self.questions[self.questionNumber][0][nr])
				self.currWindow.ui.buttonArray[nr].clicked.disconnect()
				
				if self.questions[self.questionNumber][1][nr]:
					self.currWindow.ui.label.setText("<html><head/><body><p align=\"center\"><img src=\":/df/Länder/" + self.questions[self.questionNumber][0][nr] +".png\"/></p></body></html>")
					self.currWindow.ui.buttonArray[nr].clicked.connect(self.scoreBonus)		
				else:
					self.currWindow.ui.buttonArray[nr].clicked.connect(self.scorePenalty)		
		
			if not self.frameQuestionAnswered[self.questionNumber]:
				for nr in range(0,len(self.questions[self.questionNumber][1])):
					self.currWindow.ui.buttonArray[nr].setEnabled(True)					
			else:
				self.currWindow.ui.pushButton_14.setEnabled(True)	
				for nr in range(0,len(self.questions[self.questionNumber][1])):
					self.currWindow.ui.buttonArray[nr].setEnabled(False)
				
		
			
		if self.questionType[self.questionNumber] == 'missingWord' or self.questionType[self.questionNumber] == 'stringQuestion':
			self.currWindow.ui.label.setText("<html><head/><body><p align=\"center\">" + self.questions[self.questionNumber][0][0] + "</p></body></html>")
			
			for nr in range(1,len(self.questions[self.questionNumber][1])):
				self.currWindow.ui.buttonArray[nr-1].setVisible(True)
				self.currWindow.ui.buttonArray[nr-1].setText(self.questions[self.questionNumber][0][nr])
				self.currWindow.ui.buttonArray[nr-1].clicked.disconnect()
				
				if self.questions[self.questionNumber][1][nr]:									
					self.currWindow.ui.buttonArray[nr-1].clicked.connect(self.scoreBonus)				
				else:
					self.currWindow.ui.buttonArray[nr-1].clicked.connect(self.scorePenalty)	
		
			if not self.frameQuestionAnswered[self.questionNumber]:
				for nr in range(1,len(self.questions[self.questionNumber][1])):
					self.currWindow.ui.buttonArray[nr-1].setEnabled(True)
			else:
				self.currWindow.ui.pushButton_14.setEnabled(True)
				for nr in range(1,len(self.questions[self.questionNumber][1])):
					self.currWindow.ui.buttonArray[nr-1].setEnabled(False)
				
		
		if self.questionType[self.questionNumber] == 'matching':
			self.currWindow.ui.label.setText("<html><head/><body><p align=\"center\">" + self.questions[self.questionNumber][0][0] +"</p></body></html>")
			rightListShuffeldTemp = []
			for i in range(1,len(self.questions[self.questionNumber][0])):
					self.currWindow.ui.matchingLabels[(i-1) * 2].setText(self.questions[self.questionNumber][0][i])
					self.currWindow.ui.matchingLabels[(i-1) * 2].setVisible(True)
					self.currWindow.ui.matchingButtons[(i-1)*2].setVisible(True)
					self.currWindow.ui.matchingButtons[((i-1)*2)+1].setVisible(True)
					rightListShuffeldTemp.append(self.questions[self.questionNumber][1][i])
					if not self.siteVisitedMatching[self.questionNumber]:
						self.linesForMatching[self.questionNumber].append([])
						self.lines[self.questionNumber].append([])
					
			random.shuffle(rightListShuffeldTemp)
			
			if not self.siteVisitedMatching[self.questionNumber]:
				self.rightListShuffeld[self.questionNumber] = rightListShuffeldTemp
			for i in range(0, len(self.rightListShuffeld[self.questionNumber])):
				if not self.siteVisitedMatching[self.questionNumber]:
					self.linesForMatching[self.questionNumber][i] = []
				self.currWindow.ui.matchingLabels[((i) * 2)+1].setVisible(True)
				self.currWindow.ui.matchingLabels[((i) * 2)+1].setText(self.rightListShuffeld[self.questionNumber][i])
				self.currWindow.ui.matchingButtons[(i)*2].setObjectName(self.questions[self.questionNumber][0][i+1])
				self.currWindow.ui.matchingButtons[((i)*2)+1].setObjectName(self.rightListShuffeld[self.questionNumber][i])
				self.currWindow.ui.matchingButtons[((i)*2)+1].setEnabled(False)
			
			self.drawMatchingLines()

			self.siteVisitedMatching[self.questionNumber] = True
		
		self.currWindow.ui.label_2.setText(self.translator[self.language][29] + ' ' + str(self.questionNumber +1) + ' ' + self.translator[self.language][30]+ ' ' + str(len(self.questions)))
		
	def previousQuestion(self):
	
		global questionNumber
		global siteVisitedMatching
		global rightListShuffeld
		self.questionNumber -=1
		self.currWindow.ui.pushButton_14.setEnabled(True)
		self.currWindow.ui.pushButton_14.setText(self.translator[self.language][6])
		self.currWindow.ui.pushButton_14.clicked.disconnect()
		self.currWindow.ui.pushButton_14.clicked.connect(self.nextQuestion)
		self.currWindow.ui.label_2.setText(self.translator[self.language][29] + ' ' + str(self.questionNumber +1) + ' ' + self.translator[self.language][30]+ ' ' + str(len(self.questions)))
		
		if self.questionNumber == 0:
			self.currWindow.ui.pushButton_13.setEnabled(False)
		else: 
			self.currWindow.ui.pushButton_13.setEnabled(True)
			
		for i in self.currWindow.ui.buttonArray:
			i.setVisible(False)
			i.setText('')
		
		for i in self.currWindow.ui.checkBoxes:
			i.setVisible(False)
			i.setText('')
		
		for i in self.currWindow.ui.matchingButtons:
			i.setVisible(False)
		
		for i in self.currWindow.ui.matchingLabels:
			i.setText('')
			i.setVisible(False)	
			
		if self.questionType[self.questionNumber] == 'multipleChoice':
			self.currWindow.ui.label.setText("<html><head/><body><p align=\"center\">" + self.questions[self.questionNumber][0][0] +"</p></body></html>")
			
			for nr in range(1,len(self.questions[self.questionNumber][0])):
				self.currWindow.ui.checkBoxes[nr-1].setText(self.questions[self.questionNumber][0][nr])
				self.currWindow.ui.checkBoxes[nr-1].setObjectName(str(self.questions[self.questionNumber][1][nr]))
				self.currWindow.ui.checkBoxes[nr-1].setVisible(True)
		
		
		if self.questionType[self.questionNumber] == 'pictureQuestion':	
			if not self.frameQuestionAnswered[self.questionNumber]:			
	
				for nr in range(0,len(self.questions[self.questionNumber][1])):
					self.currWindow.ui.buttonArray[nr].setVisible(True)
					self.currWindow.ui.buttonArray[nr].setText(self.questions[self.questionNumber][0][nr])
					self.currWindow.ui.buttonArray[nr].setEnabled(True)
					self.currWindow.ui.buttonArray[nr].clicked.disconnect()
					
					if self.questions[self.questionNumber][1][nr]:
						self.currWindow.ui.label.setText("<html><head/><body><p align=\"center\"><img src=\":/df/Länder/" + self.questions[self.questionNumber][0][nr] +".png\"/></p></body></html>")
						self.currWindow.ui.buttonArray[nr].clicked.connect(self.scoreBonus)				
					else:
						self.currWindow.ui.buttonArray[nr].clicked.connect(self.scorePenalty)					
			else:
				for nr in range(0,len(self.questions[self.questionNumber][1])):
					self.currWindow.ui.buttonArray[nr].setText(self.questions[self.questionNumber][0][nr])
					self.currWindow.ui.buttonArray[nr].setVisible(True)
					self.currWindow.ui.buttonArray[nr].setEnabled(False)
					if self.questions[self.questionNumber][1][nr]:
						self.currWindow.ui.label.setText("<html><head/><body><p align=\"center\"><img src=\":/df/Länder/" + self.questions[self.questionNumber][0][nr] +".png\"/></p></body></html>")

		
		if self.questionType[self.questionNumber] == 'missingWord' or self.questionType[self.questionNumber] == 'stringQuestion':
			for nr in range(1,len(self.questions[self.questionNumber][1])):
				self.currWindow.ui.buttonArray[nr-1].setText(self.questions[self.questionNumber][0][nr])
				self.currWindow.ui.buttonArray[nr-1].setVisible(True)
			
			if not self.frameQuestionAnswered[self.questionNumber]:
				for nr in range(1,len(self.questions[self.questionNumber][1])):
					self.currWindow.ui.buttonArray[nr-1].setEnabled(True)
					self.currWindow.ui.buttonArray[nr-1].clicked.disconnect()
					
					if self.questions[self.questionNumber][1][nr-1]:
						self.currWindow.ui.label.setText("<html><head/><body><p align=\"center\">" + self.questions[self.questionNumber][0][0] +"</p></body></html>")
						self.currWindow.ui.buttonArray[nr-1].clicked.connect(self.scoreBonus)				
					else:
						self.currWindow.ui.buttonArray[nr-1].clicked.connect(self.scorePenalty)				
			else:
				for nr in range(1,len(self.questions[self.questionNumber][1])):
					self.currWindow.ui.buttonArray[nr-1].setEnabled(False)
					if self.questions[self.questionNumber][1][nr-1]:
						self.currWindow.ui.label.setText("<html><head/><body><p align=\"center\">" + self.questions[self.questionNumber][0][0] +"</p></body></html>")
		
		
		if self.questionType[self.questionNumber] == 'matching':
			self.currWindow.ui.label.setText("<html><head/><body><p align=\"center\">" + self.questions[self.questionNumber][0][0] +"</p></body></html>")
			rightListShuffeldTemp = []
			
			for i in range(1,len(self.questions[self.questionNumber][0])):
					self.currWindow.ui.matchingLabels[(i-1) * 2].setText(self.questions[self.questionNumber][0][i])
					self.currWindow.ui.matchingLabels[(i-1) * 2].setVisible(True)
					self.currWindow.ui.matchingButtons[(i-1)*2].setVisible(True)
					self.currWindow.ui.matchingButtons[((i-1)*2)+1].setVisible(True)
					self.currWindow.ui.matchingButtons[(i-1)*2].setObjectName(self.questions[self.questionNumber][0][i])
					self.currWindow.ui.matchingButtons[((i-1)*2)+1].setObjectName(self.questions[self.questionNumber][1][i])
					self.currWindow.ui.matchingButtons[((i-1)*2)+1].setEnabled(False)
					rightListShuffeldTemp.append(self.questions[self.questionNumber][1][i])

			random.shuffle(rightListShuffeldTemp)
			
			if not self.siteVisitedMatching[self.questionNumber]:
				self.rightListShuffeld[self.questionNumber] = rightListShuffeldTemp
			for i in range(0, len(self.rightListShuffeld[self.questionNumber])):
				self.currWindow.ui.matchingLabels[((i) * 2)+1].setVisible(True)
				self.currWindow.ui.matchingLabels[((i) * 2)+1].setText(self.rightListShuffeld[self.questionNumber][i])
				
			self.drawMatchingLines()
			
			self.siteVisitedMatching[self.questionNumber] = True
	
	def drawMatchingLines(self):
		self.paintPanel.update(self.questionNumber)
		'''
		#self.paintPanel.update()
		for i in self.lines:
			if not i == []:
				self.currWindow.ui.newLine = QFrame()
				self.currWindow.ui.newLine.setGeometry(QRect(i[0].pos().x(), i[0].pos().y(), i[1].pos().x(), i[1].pos().y()))
				self.currWindow.ui.newLine.setFrameShape(QFrame.HLine)
				self.currWindow.ui.gridLayout.addWidget(self.currWindow.ui.newLine)
				#.drawLine(i[0].pos().x(), i[0].pos().y(), i[1].pos().x(), i[1].pos().y())
				print 'huhu'
		'''
		#print 'hello'
		
	def matchingLeftButtonClicked(self):
		
		global leftChoiceMatching
		global linesForMatching
		
		button = self.currWindow.sender()
		
		self.leftChoiceMatching = button.objectName()
		
		for i in range(0, len(self.questions[self.questionNumber][0])):			
			if self.questions[self.questionNumber][0][i] == button.objectName():
				indexOfLeftButton = i-1

		if self.linesForMatching[self.questionNumber][indexOfLeftButton] == []:
		
			for i in range(1,len(self.questions[self.questionNumber][0])+1):
				if self.currWindow.ui.matchingButtons[(i-1) * 2].isVisible():
					self.currWindow.ui.matchingButtons[((i-1) * 2) + 1].setEnabled(True)
					self.currWindow.ui.matchingButtons[(i-1) * 2].setEnabled(False)
					if self.currWindow.ui.matchingLabels[(i-1)*2].text() == self.leftChoiceMatching:
						self.linesForMatching[self.questionNumber][(i-1)].append(self.leftChoiceMatching)
						self.currWindow.ui.matchingLabels[(i-1)*2].setStyleSheet(u"color: rgb(0, 0, 255)")
						tempFont = self.currWindow.ui.matchingLabels[(i-1)*2].font()
						tempFont.setBold(True)
						self.currWindow.ui.matchingLabels[(i-1)*2].setFont(tempFont)
						#self.currWindow.ui.matchingLabels[(i-1)*2].update()
		else: 
			self.linesForMatching[self.questionNumber][indexOfLeftButton] = []
			self.lines[self.questionNumber][indexOfLeftButton] = []
			
		self.drawMatchingLines()

	
	def matchingRightButtonClicked(self):
		
		global linesForMatching
		
		buttonRight = self.currWindow.sender()

		for i in range(0,len(self.questions[self.questionNumber][1])*2):
			
			if self.currWindow.ui.matchingButtons[i].isVisible():
				if i % 2 == 0:
					self.currWindow.ui.matchingButtons[i].setEnabled(True)
					self.currWindow.ui.matchingLabels[i].setStyleSheet('')
					tempFont = self.currWindow.ui.matchingLabels[i].font()
					tempFont.setBold(False)
					self.currWindow.ui.matchingLabels[i].setFont(tempFont)
				else:
					self.currWindow.ui.matchingButtons[i].setEnabled(False)
					
		for i in range(0, len(self.questions[self.questionNumber][0])):			
			if self.currWindow.ui.matchingLabels[i*2].text() == self.leftChoiceMatching:
				buttonLeft = self.currWindow.ui.matchingButtons[i*2]
				indexOfLeftButton = i

		self.linesForMatching[self.questionNumber][indexOfLeftButton].append(buttonRight.objectName())
		if self.questions[self.questionNumber][1][indexOfLeftButton + 1] == buttonRight.objectName():
			self.linesForMatching[self.questionNumber][indexOfLeftButton].append(1)
		else:
			self.linesForMatching[self.questionNumber][indexOfLeftButton].append(0)


		#print self.lines
		self.lines[self.questionNumber][indexOfLeftButton].append(buttonLeft)
		self.lines[self.questionNumber][indexOfLeftButton].append(buttonRight)
		
		
		print self.lines
		print self.linesForMatching
		
		self.drawMatchingLines()
		self.currWindow.repaint()
		#self.drawMatchingLines()
		
		'''self.currWindow.paintEvent(buttonLeft.pos().x(),buttonLeft.pos().y(),buttonRight.pos().x(),buttonRight.pos().y())'''

	def checkState(self):
		
		global Score
		global frameQuestionAnswered
		
		self.frameQuestionAnswered[self.questionNumber] = True
		
		button = self.currWindow.sender()
		
		if button.objectName()[0] == '-':
			sign = -1
			scoreTemp = float(button.objectName()[1:6])
		else:
			sign = 1
			scoreTemp = float(button.objectName()[0:5])
		
		scoreDiff = (sign * scoreTemp) / 100
		
		if button.isChecked():
			self.updateScoreCheckboxCheck(scoreDiff)
		else:
			self.updateScoreCheckboxUncheck(scoreDiff)
	
	def updateScoreCheckboxCheck(self, scoreDiff):
		
		global Score
		
		if self.Score + scoreDiff >= 0:
			self.Score += scoreDiff
		else:
			self.Score = 0
			
	def updateScoreCheckboxUncheck(self, scoreDiff):
		
		global Score

		if self.Score - scoreDiff >= 0 :
			self.Score -= scoreDiff
		else:
			self.Score = 0
			
	def scoreBonus(self):
		
		global Score
		global frameQuestionAnswered
		
		self.currWindow.ui.pushButton_14.setEnabled(True)	
		self.Score += 1
		self.frameQuestionAnswered[self.questionNumber] = True
		
		for i in self.currWindow.ui.buttonArray:
			i.setEnabled(False)

	def scorePenalty(self):

		global Score
		global frameQuestionAnswered
		
		self.currWindow.ui.pushButton_14.setEnabled(True)	
		penalty = 0
		
		if self.Score - penalty >= 0:
			self.Score -= penalty
		
		self.frameQuestionAnswered[self.questionNumber] = True
		
		for i in self.currWindow.ui.buttonArray:
			i.setEnabled(False)
				
	def training(self):

		global Score
		global questions
		global frameQuestionAnswered
		global questionFrame
		
		self.Score = 0
		self.questionNumber = 0
		self.questions = self.parseQuestion()
		self.answers =[]
		self.questionFrame = 0
		self.frameQuestionAnswered = [0 for x in range(len(self.questions))]
		self.answers = [0 for x in range(len(self.questions))]
		self.siteVisitedMatching = [0 for x in range(len(self.questions))]
		
		for i in range(0, len(self.questions)):
			self.siteVisitedMatching[i] =  False

		self.rightListShuffeld = []
		self.linesForMatching = []
		for i in range(0, len(self.questions)):
			self.rightListShuffeld.append([])
			self.linesForMatching.append([])
		for i in range(0, len(self.questions)):
			self.frameQuestionAnswered[i] = False
			self.answers[i] =''
		
		self.currWindow = TrainingQuizDialog()
		self.addWidgets()
		
		self.currWindow.ui.pushButton_13.setText(self.translator[self.language][28])
		self.currWindow.ui.pushButton_13.setVisible(False)
		self.currWindow.ui.pushButton_13.clicked.connect(self.evaluateCheckBoxesTraining)
		self.currWindow.ui.label_5.setText(self.translator[self.language][29] + ' ' + str(self.questionNumber +1) + ' ' + self.translator[self.language][30]+ ' ' + str(len(self.questions)))
		
		for i in self.currWindow.ui.buttonArray:
			i.setVisible(False)
			i.clicked.connect(self.scorePenaltyQuiz)
		
		for i in self.currWindow.ui.checkBoxes:
			i.setVisible(False)	
			i.setObjectName(' ')
			
		for i in self.currWindow.ui.matchingLabelsLeft:
			i.setVisible(False)
			i.setText('')
			
		for i in self.currWindow.ui.matchingLabelsRight:
			i.setVisible(False)
			i.setText('')
			
		for i in self.currWindow.ui.matchingButtonsLeft:
			i.setVisible(False)
			i.clicked.connect(self.matchingLeftButtonClicked)
			
		for i in self.currWindow.ui.matchingButtonsRight:
			i.setVisible(False)
			i.clicked.connect(self.matchingRightButtonClickedQuiz)
			
		if self.questionType[0] == 'multipleChoice':
			self.currWindow.ui.label.setText("<html><head/><body><p align=\"center\">" + self.questions[0][0][0] +"</p></body></html>")
			self.currWindow.ui.pushButton_13.setVisible(True)
			self.currWindow.ui.pushButton_13.clicked.disconnect()
			self.currWindow.ui.pushButton_13.clicked.connect(self.evaluateCheckBoxesTraining)
			for i in range(1,len(self.questions[0][0])):
				self.currWindow.ui.checkBoxes[i-1].setText("<html><head/><body><p align=\"center\">" + self.questions[0][0][i] +"</p></body></html>")
				self.currWindow.ui.checkBoxes[i-1].setVisible(True)
				self.currWindow.ui.checkBoxes[i-1].setObjectName(self.questions[0][1][i])
			
			
		if self.questionType[0] == 'pictureQuestion':
			for i in range(0,len(self.questions[0][0])):
				self.currWindow.ui.buttonArray[i].setText(self.questions[0][0][i])
				self.currWindow.ui.buttonArray[i].setVisible(True)
				if self.questions[0][1][i]:
					self.currWindow.ui.label.setText("<html><head/><body><p align=\"center\"><img src=\":/df/Länder/" + self.questions[0][0][i] +".png\"/></p></body></html>")
					self.currWindow.ui.buttonArray[i].clicked.disconnect()
					self.currWindow.ui.buttonArray[i].clicked.connect(self.scoreBonusQuiz)
			
		
		if self.questionType[0] == 'missingWord' or self.questionType[self.questionNumber] == 'stringQuestion':
			self.currWindow.ui.label.setText("<html><head/><body><p align=\"center\">" + self.questions[0][0][0] +"</p></body></html>")
			for i in range(1,len(self.questions[0][0])):
				self.currWindow.ui.buttonArray[i-1].setText(self.questions[0][0][i])
				self.currWindow.ui.buttonArray[i-1].setVisible(True)
				if self.questions[0][1][i]:
					self.currWindow.ui.buttonArray[i-1].clicked.disconnect()
					self.currWindow.ui.buttonArray[i-1].clicked.connect(self.scoreBonusQuiz)

		
		if self.questionType[0] == 'matching':
			self.currWindow.ui.label.setText("<html><head/><body><p align=\"center\">" + self.questions[0][0][0] +"</p></body></html>")
			rightListShuffeld = []
			self.currWindow.ui.pushButton_13.setVisible(True)
			self.currWindow.ui.pushButton_13.clicked.disconnect()
			self.currWindow.ui.pushButton_13.clicked.connect(self.evaluateMatchingTraining)
			
			for i in range(1,len(self.questions[0][0])):
					self.currWindow.ui.matchingLabels[(i-1) * 2].setVisible(True)
					self.currWindow.ui.matchingLabels[(i-1) * 2].setText(self.questions[0][0][i])
					self.currWindow.ui.matchingButtons[(i-1)*2].setVisible(True)
					self.currWindow.ui.matchingButtons[(i-1)*2].setObjectName(self.questions[0][0][i])
					self.currWindow.ui.matchingButtons[((i-1)*2)+1].setVisible(True)
					self.currWindow.ui.matchingButtons[((i-1)*2)+1].setEnabled(False)
					self.currWindow.ui.matchingButtons[((i-1)*2)+1].setObjectName(self.questions[0][0][i])
					rightListShuffeld.append(self.questions[0][1][i])
					self.linesForMatching[0].append([])
					
			random.shuffle(rightListShuffeld)
			for i in range(0, len(rightListShuffeld)):
				self.currWindow.ui.matchingLabels[((i) * 2)+1].setVisible(True)
				self.currWindow.ui.matchingLabels[((i) * 2)+1].setText(rightListShuffeld[i])
				
				
		self.currWindow.ui.pushButton_14.setText(self.translator[self.language][14])
		self.currWindow.ui.pushButton_14.clicked.connect(self.previousQuizQuestion)
		self.currWindow.ui.pushButton_14.setVisible(False)
		self.currWindow.ui.pushButton_15.clicked.connect(self.currWindow.close)
		self.currWindow.ui.pushButton_15.setText(self.translator[self.language][16])
		self.currWindow.ui.pushButton_16.setText(self.translator[self.language][15])
		self.currWindow.ui.pushButton_16.clicked.connect(self.quizNextQuestion)
		
		self.currWindow.show()
	
	def quizRefresh(self, wasCorrect, answerGiven):
		
		self.roundScore()
		
		for i in self.currWindow.ui.buttonArray:
			i.setEnabled(False)
			
		if self.questionType[self.questionNumber] == 'pictureQuestion':
			for nr in range(0,len(self.questions[self.questionNumber][1])):
				
				if self.questions[self.questionNumber][1][nr]:
					correctAnswer = self.currWindow.ui.buttonArray[nr].text()
					self.currWindow.ui.buttonArray[nr].setStyleSheet(u"color:rgb(0, 184, 0)")
				
				if self.questions[self.questionNumber][0][nr] == answerGiven:
					buttonPressed = self.currWindow.ui.buttonArray[nr]
		
		
		if self.questionType[self.questionNumber] == 'missingWord' or self.questionType[self.questionNumber] == 'stringQuestion':
			for nr in range(1,len(self.questions[self.questionNumber][1])):
				
				if self.questions[self.questionNumber][1][nr]:
					correctAnswer = self.currWindow.ui.buttonArray[nr-1].text()
					self.currWindow.ui.buttonArray[nr-1].setStyleSheet(u"color:rgb(0, 184, 0)")
				
				if self.questions[self.questionNumber][0][nr] == answerGiven:
					buttonPressed = self.currWindow.ui.buttonArray[nr-1]
		
		if self.Score == 1:
			points = self.translator[self.language][18] + str(self.Score) + self.translator[self.language][19] + str(len(self.questions))
		else:
			points = self.translator[self.language][20] + str(self.Score) + self.translator[self.language][21] + str(len(self.questions))
		
		if wasCorrect:
			self.currWindow.ui.label_2.setText( "<html><head/><body><p align=\"center\"> " + self.translator[self.language][22] +  "<br/></p></body></html>")
		else:
			self.currWindow.ui.label_2.setText("<html><head/><body><p align=\"center\"> " + self.translator[self.language][23] + "<br/></p></body></html>")
			self.currWindow.ui.label_3.setText( "<html><head/><body><p align=\"center\"> " + self.translator[self.language][24] + correctAnswer +"<br/></p></body></html>")
			buttonPressed.setStyleSheet(u"color:rgb(255, 0, 0)")
		
		self.currWindow.ui.label_4.setText( "<html><head/><body><p align=\"center\"> " + points + "<br/></p></body></html>")
		self.frameQuestionAnswered[self.questionFrame] = True		
	
	def quizNextQuestion(self):
		
		global questionFrame
		global frameQuestionAnswered
		global questionNumber
		
		self.questionFrame += 1
		self.questionNumber += 1
		
		self.currWindow.ui.label_5.setText(self.translator[self.language][29] + ' ' + str(self.questionNumber +1) + ' ' + self.translator[self.language][30]+ ' ' + str(len(self.questions)))
		if self.questionFrame == len(self.questions) - 1:
			self.currWindow.ui.pushButton_16.setText(self.translator[self.language][17])
			self.currWindow.ui.pushButton_16.clicked.disconnect()
			self.currWindow.ui.pushButton_16.clicked.connect(self.showQuizResults)
		
		if self.frameQuestionAnswered[self.questionFrame]:
			self.showOldQuestion()										
		
		else:
			self.currWindow.ui.label_2.setText('')
			self.currWindow.ui.label_3.setText('')
			self.currWindow.ui.pushButton_14.setVisible(True)		
			self.currWindow.ui.pushButton_13.setVisible(False)			
			
			for i in self.currWindow.ui.buttonArray:
				i.setVisible(False)
				i.setText('')
				i.setEnabled(True)
				i.setStyleSheet("")
			
			for i in self.currWindow.ui.checkBoxes:
				i.setVisible(False)
				i.setText('')
				i.setStyleSheet("")
				i.setObjectName(' ')
			
			for i in self.currWindow.ui.matchingLabels:
				i.setVisible(False)
				i.setText('')
				i.setStyleSheet("")
			
			for i in self.currWindow.ui.matchingButtons:
				i.setVisible(False)
				i.setText('')
				i.setStyleSheet("")
				i.setEnabled(True)
				
			if self.questionType[self.questionNumber] == 'multipleChoice':
				self.currWindow.ui.label.setText("<html><head/><body><p align=\"center\">" + self.questions[self.questionNumber][0][0] +"</p></body></html>")
				self.currWindow.ui.pushButton_13.setVisible(True)
				self.currWindow.ui.pushButton_13.setEnabled(True)
				self.currWindow.ui.pushButton_13.clicked.disconnect()
				self.currWindow.ui.pushButton_13.clicked.connect(self.evaluateCheckBoxesTraining)
				
				for nr in range(1,len(self.questions[self.questionNumber][0])):
					self.currWindow.ui.checkBoxes[nr-1].setText(self.questions[self.questionNumber][0][nr])
					self.currWindow.ui.checkBoxes[nr-1].setObjectName(str(self.questions[self.questionNumber][1][nr]))
					self.currWindow.ui.checkBoxes[nr-1].setVisible(True)
			
						
			if self.questionType[self.questionNumber] == 'pictureQuestion':
				for nr in range(0,len(self.questions[self.questionNumber][1])):
					self.currWindow.ui.buttonArray[nr].setText(self.questions[self.questionNumber][0][nr])
					self.currWindow.ui.buttonArray[nr].setVisible(True)
					self.currWindow.ui.buttonArray[nr].clicked.disconnect()
					
					if self.questions[self.questionNumber][1][nr]:
						self.currWindow.ui.label.setText("<html><head/><body><p align=\"center\"><img src=\":/df/Länder/" + self.questions[self.questionNumber][0][nr] +".png\"/></p></body></html>")
						self.currWindow.ui.buttonArray[nr].clicked.connect(self.scoreBonusQuiz)
					else:
						self.currWindow.ui.buttonArray[nr].clicked.connect(self.scorePenaltyQuiz)
			
			
			if self.questionType[self.questionNumber] == 'missingWord' or self.questionType[self.questionNumber] == 'stringQuestion':
				self.currWindow.ui.label.setText("<html><head/><body><p align=\"center\">" + self.questions[self.questionNumber][0][0] +"</p></body></html>")
				
				for nr in range(1,len(self.questions[self.questionNumber][1])):
					self.currWindow.ui.buttonArray[nr-1].setText(self.questions[self.questionNumber][0][nr])
					self.currWindow.ui.buttonArray[nr-1].setVisible(True)
					self.currWindow.ui.buttonArray[nr-1].clicked.disconnect()
					
					if self.questions[self.questionNumber][1][nr]:
						self.currWindow.ui.buttonArray[nr-1].clicked.connect(self.scoreBonusQuiz)
					else:
						self.currWindow.ui.buttonArray[nr-1].clicked.connect(self.scorePenaltyQuiz)	
			
			
			if self.questionType[self.questionNumber] == 'matching':
				self.currWindow.ui.label.setText("<html><head/><body><p align=\"center\">" + self.questions[self.questionNumber][0][0] +"</p></body></html>")
				rightListShuffeldTemp = []
				self.currWindow.ui.pushButton_13.setVisible(True)
				self.currWindow.ui.pushButton_13.clicked.disconnect()
				self.currWindow.ui.pushButton_13.clicked.connect(self.evaluateMatchingTraining)
				
				for i in range(1,len(self.questions[self.questionNumber][0])):
					self.currWindow.ui.matchingLabels[(i-1) * 2].setText(self.questions[self.questionNumber][0][i])
					self.currWindow.ui.matchingLabels[(i-1) * 2].setVisible(True)
					self.currWindow.ui.matchingButtons[(i-1)*2].setVisible(True)
					self.currWindow.ui.matchingButtons[((i-1)*2)+1].setVisible(True)
					rightListShuffeldTemp.append(self.questions[self.questionNumber][1][i])
					if not self.siteVisitedMatching[self.questionNumber]:
						self.linesForMatching[self.questionNumber].append([])
					
				random.shuffle(rightListShuffeldTemp)
			
				if not self.siteVisitedMatching[self.questionNumber]:
					self.rightListShuffeld[self.questionNumber] = rightListShuffeldTemp
				for i in range(0, len(self.rightListShuffeld[self.questionNumber])):
					if not self.siteVisitedMatching[self.questionNumber]:
						self.linesForMatching[self.questionNumber][i] = []
					self.currWindow.ui.matchingLabels[((i) * 2)+1].setVisible(True)
					self.currWindow.ui.matchingLabels[((i) * 2)+1].setText(self.rightListShuffeld[self.questionNumber][i])
					self.currWindow.ui.matchingButtons[(i)*2].setObjectName(self.questions[self.questionNumber][0][i+1])
					self.currWindow.ui.matchingButtons[((i)*2)+1].setObjectName(self.rightListShuffeld[self.questionNumber][i])
					self.currWindow.ui.matchingButtons[((i)*2)+1].setEnabled(False)
			
				self.drawMatchingLines()
			
				self.siteVisitedMatching[self.questionNumber] = True
			
			
	def previousQuizQuestion(self):
		
		global questionFrame
		global questionNumber
		
		self.questionNumber -= 1
		self.questionFrame -= 1
		self.currWindow.ui.pushButton_16.setText(self.translator[self.language][15])
		self.currWindow.ui.pushButton_16.clicked.disconnect()
		self.currWindow.ui.pushButton_16.clicked.connect(self.quizNextQuestion)
		
		self.showOldQuestion()
		
	def showOldQuestion(self):
		
		if self.questionFrame == 0:
			self.currWindow.ui.pushButton_14.setVisible(False)
		else:
			self.currWindow.ui.pushButton_14.setVisible(True)
		
		if self.questionFrame == len(self.questions) - 1:
			self.currWindow.ui.pushButton_16.setText(self.translator[self.language][17])
			self.currWindow.ui.pushButton_16.clicked.disconnect()
			self.currWindow.ui.pushButton_16.clicked.connect(self.showQuizResults)
		
		if self.Score == 1:
			points = self.translator[self.language][18] + str(self.Score) + self.translator[self.language][19] + str(len(self.questions))
		else:
			points = self.translator[self.language][20] + str(self.Score) + self.translator[self.language][21] + str(len(self.questions))
		
		for i in self.currWindow.ui.buttonArray:
			i.setVisible(False)
			i.setText('')
			i.setStyleSheet("")
			i.setEnabled(True)
		for i in self.currWindow.ui.checkBoxes:
			i.setVisible(False)
			i.setText('')
			i.setStyleSheet("")
			i.setEnabled(True)
			i.setObjectName(' ')
		for i in self.currWindow.ui.matchingButtons:
			i.setVisible(False)
		for i in self.currWindow.ui.matchingLabels:
			i.setVisible(False)
			i.setStyleSheet("")
			
		
		self.currWindow.ui.label_5.setText(self.translator[self.language][29] + ' ' + str(self.questionNumber +1) + ' ' + self.translator[self.language][30]+ ' ' + str(len(self.questions)))
		self.currWindow.ui.pushButton_13.setVisible(False)
		
		
		if self.questionType[self.questionNumber] == 'multipleChoice':
			self.currWindow.ui.label.setText("<html><head/><body><p align=\"center\">" + self.questions[self.questionNumber][0][0] +"</p></body></html>")
			self.currWindow.ui.pushButton_13.clicked.disconnect()
			self.currWindow.ui.pushButton_13.clicked.connect(self.evaluateCheckBoxesTraining)
			self.currWindow.ui.pushButton_13.setVisible(True)

			for nr in range(1,len(self.questions[self.questionNumber][0])):
				self.currWindow.ui.checkBoxes[nr-1].setText(self.questions[self.questionNumber][0][nr])
				self.currWindow.ui.checkBoxes[nr-1].setObjectName(str(self.questions[self.questionNumber][1][nr]))
				self.currWindow.ui.checkBoxes[nr-1].setEnabled(False)
				self.currWindow.ui.checkBoxes[nr-1].setVisible(True)
			
			if self.frameQuestionAnswered[self.questionFrame]:
				self.updateCheckBoxesTraining()
				self.currWindow.ui.pushButton_13.setEnabled(False)
				
				for i in self.answers[self.questionFrame].split():
					for k in self.currWindow.ui.checkBoxes:
						if i == k.objectName():
							k.setCheckState(Qt.Checked)				
			else:
				self.currWindow.ui.pushButton_13.clicked.disconnect()
				self.currWindow.ui.pushButton_13.clicked.connect(self.evaluateCheckBoxesTraining)
				self.currWindow.ui.pushButton_13.setEnabled(True)
				self.currWindow.ui.label_2.setText("")
				self.currWindow.ui.label_3.setText("")
				self.currWindow.ui.label_4.setText( "<html><head/><body><p align=\"center\"> " + points + "<br/></p></body></html>")
				
				for nr in range(1,len(self.questions[self.questionFrame][1])):
					self.currWindow.ui.checkBoxes[nr-1].setEnabled(True)
				
		
		if self.questionType[self.questionNumber] == 'pictureQuestion':
			for nr in range(0,len(self.questions[self.questionNumber][1])):
				self.currWindow.ui.buttonArray[nr].setVisible(True)
				self.currWindow.ui.buttonArray[nr].setEnabled(False)
				self.currWindow.ui.buttonArray[nr].setText(self.questions[self.questionFrame][0][nr])
				self.currWindow.ui.buttonArray[nr].clicked.disconnect()
				
				if self.questions[self.questionFrame][1][nr]:
					rightAnswer = self.questions[self.questionFrame][0][nr]
					self.currWindow.ui.label.setText("<html><head/><body><p align =\"center\"><img src=\":/df/Länder/" + self.questions[self.questionFrame][0][nr] +".png\"/></p></body></html>")
					self.currWindow.ui.buttonArray[nr].clicked.connect(self.scoreBonusQuiz)
				else:
					self.currWindow.ui.buttonArray[nr].clicked.connect(self.scorePenaltyQuiz)
			
			if self.frameQuestionAnswered[self.questionFrame]:
				for nr in range(0,len(self.questions[self.questionFrame][1])):
					if self.questions[self.questionFrame][1][nr]:
						self.currWindow.ui.buttonArray[nr].setStyleSheet(u"color:rgb(0, 184, 0)")		
				
				if self.answers[self.questionFrame] == rightAnswer:
					self.currWindow.ui.label_2.setText( "<html><head/><body><p align=\"center\"> " + self.translator[self.language][27] + "<br/></p></body></html>")
					self.currWindow.ui.label_3.setText('')
					self.currWindow.ui.label_4.setText( "<html><head/><body><p align=\"center\"> " + points + "<br/></p></body></html>")
				else:
					rightAnswer = self.translator[self.language][25] + rightAnswer + self.translator[self.language][26]
					self.currWindow.ui.label_2.setText( "<html><head/><body><p align=\"center\"> " + self.translator[self.language][23] + "<br/></p></body></html>")
					self.currWindow.ui.label_3.setText( "<html><head/><body><p align=\"center\"> " + rightAnswer + "<br/></p></body></html>")
					self.currWindow.ui.label_4.setText( "<html><head/><body><p align=\"center\"> " + points + "<br/></p></body></html>")						
					
					for nr in range(0,len(self.questions[self.questionFrame][1])):
						if self.questions[self.questionFrame][0][nr] == self.answers[self.questionFrame]:
							wrongButton = self.currWindow.ui.buttonArray[nr]
					wrongButton.setStyleSheet(u"color:rgb(255, 0, 0)")
			else:
				self.currWindow.ui.label_2.setText("")
				self.currWindow.ui.label_3.setText("")
				self.currWindow.ui.label_4.setText( "<html><head/><body><p align=\"center\"> " + points + "<br/></p></body></html>")
				for nr in range(0,len(self.questions[self.questionFrame][1])):
					self.currWindow.ui.buttonArray[nr].setEnabled(True)
					
					
		if self.questionType[self.questionNumber] == 'missingWord' or self.questionType[self.questionNumber] == 'stringQuestion':
			for nr in range(1,len(self.questions[self.questionNumber][1])):
				self.currWindow.ui.buttonArray[nr-1].setVisible(True)
				self.currWindow.ui.buttonArray[nr-1].setEnabled(False)
				self.currWindow.ui.buttonArray[nr-1].setText(self.questions[self.questionFrame][0][nr])
				self.currWindow.ui.buttonArray[nr].clicked.disconnect()
				
				if self.questions[self.questionFrame][1][nr]:
					rightAnswer = self.questions[self.questionFrame][0][nr]
					self.currWindow.ui.label.setText("<html><head/><body><p align =\"center\">" + self.questions[self.questionFrame][0][0] +"</p></body></html>")
					self.currWindow.ui.buttonArray[nr].clicked.connect(self.scoreBonusQuiz)
				else:
					self.currWindow.ui.buttonArray[nr].clicked.connect(self.scorePenaltyQuiz)
			
			if self.frameQuestionAnswered[self.questionFrame]:
				for nr in range(1,len(self.questions[self.questionFrame][1])):
					if self.questions[self.questionFrame][1][nr]:
						self.currWindow.ui.buttonArray[nr-1].setStyleSheet(u"color:rgb(0, 184, 0)")		
				
				if self.answers[self.questionFrame] == rightAnswer:
					self.currWindow.ui.label_2.setText( "<html><head/><body><p align=\"center\"> " + self.translator[self.language][27] + "<br/></p></body></html>")
					self.currWindow.ui.label_3.setText('')
					self.currWindow.ui.label_4.setText( "<html><head/><body><p align=\"center\"> " + points + "<br/></p></body></html>")
				else:
					rightAnswer = self.translator[self.language][25] + rightAnswer + self.translator[self.language][26]
					self.currWindow.ui.label_2.setText( "<html><head/><body><p align=\"center\"> " + self.translator[self.language][23] + "<br/></p></body></html>")
					self.currWindow.ui.label_3.setText( "<html><head/><body><p align=\"center\"> " + rightAnswer + "<br/></p></body></html>")
					self.currWindow.ui.label_4.setText( "<html><head/><body><p align=\"center\"> " + points + "<br/></p></body></html>")						
					
					for nr in range(1,len(self.questions[self.questionFrame][1])):
						if self.questions[self.questionFrame][0][nr] == self.answers[self.questionFrame]:
							wrongButton = self.currWindow.ui.buttonArray[nr-1]	
					wrongButton.setStyleSheet(u"color:rgb(255, 0, 0)")	
			else:
				self.currWindow.ui.label_2.setText("")
				self.currWindow.ui.label_3.setText("")
				self.currWindow.ui.label_4.setText( "<html><head/><body><p align=\"center\"> " + points + "<br/></p></body></html>")
				
				for nr in range(1,len(self.questions[self.questionFrame][1])):
					self.currWindow.ui.buttonArray[nr-1].setEnabled(True)
		

		if self.questionType[self.questionNumber] == 'matching':
			self.currWindow.ui.label.setText("<html><head/><body><p align=\"center\">" + self.questions[self.questionNumber][0][0] +"</p></body></html>")
			self.currWindow.ui.pushButton_13.clicked.disconnect()
			self.currWindow.ui.pushButton_13.clicked.connect(self.evaluateMatchingTraining)
			self.currWindow.ui.pushButton_13.setVisible(True)
			
			for i in range(1,len(self.questions[self.questionNumber][0])):
				self.currWindow.ui.matchingLabels[(i-1) * 2].setText(self.questions[self.questionNumber][0][i])
				self.currWindow.ui.matchingLabels[(i-1) * 2].setVisible(True)
				self.currWindow.ui.matchingButtons[(i-1)*2].setVisible(True)
				self.currWindow.ui.matchingButtons[((i-1)*2)+1].setVisible(True)
				self.currWindow.ui.matchingButtons[(i-1)*2].setEnabled(False)
				self.currWindow.ui.matchingButtons[((i-1)*2)+1].setEnabled(False)
			
			for i in range(0, len(self.rightListShuffeld[self.questionNumber])):
				self.currWindow.ui.matchingLabels[((i) * 2)+1].setVisible(True)
				self.currWindow.ui.matchingLabels[((i) * 2)+1].setText(self.rightListShuffeld[self.questionNumber][i])
				self.currWindow.ui.matchingButtons[(i)*2].setObjectName(self.questions[self.questionNumber][0][i+1])
				self.currWindow.ui.matchingButtons[((i)*2)+1].setObjectName(self.rightListShuffeld[self.questionNumber][i])
				self.currWindow.ui.matchingButtons[((i)*2)+1].setEnabled(False)
				
			self.drawMatchingLines()	
			
			if self.frameQuestionAnswered[self.questionFrame]:
				self.updateMatchingLines()
				self.currWindow.ui.pushButton_13.setEnabled(False)
							
			else:
				self.currWindow.ui.label_2.setText("")
				self.currWindow.ui.label_3.setText("")
				self.currWindow.ui.label_4.setText( "<html><head/><body><p align=\"center\"> " + points + "<br/></p></body></html>")
				
				for i in range(1,len(self.questions[self.questionNumber][0])):
					self.currWindow.ui.matchingButtons[(i-1)*2].setEnabled(True)

				
	def scoreBonusQuiz(self):
		
		global Score
		global answers
	
		button = self.currWindow.sender()
		self.answers[self.questionNumber]=button.text()
		self.Score += 1
		
		self.quizRefresh(True, '')
	
	def scorePenaltyQuiz(self):

		global Score
		global answers

		button = self.currWindow.sender()
		answerGiven = button.text()
		self.answers[self.questionNumber]=answerGiven
		penalty = 0
		
		if self.Score - penalty >= 0:
			self.Score -= penalty
		else:
			self.Score = 0
		
		self.quizRefresh(False, answerGiven)					
	
	def evaluateMatchingTraining(self):
	
		global Score
		global frameQuestionAnswered

		self.frameQuestionAnswered[self.questionNumber] = True
		allCorrectlyAnswered = True
		
		for i in range(0, len(self.linesForMatching[self.questionNumber])):
			self.currWindow.ui.matchingButtons[i * 2].setEnabled(False)
			self.currWindow.ui.matchingButtons[(i * 2) + 1].setEnabled(False)
			
			if len(self.linesForMatching[self.questionNumber][i]) == 3:
				for k in self.currWindow.ui.matchingLabels:
					if k.text() == self.linesForMatching[self.questionNumber][i][1]:
						rightLabel = k
			
			if len(self.linesForMatching[self.questionNumber][i]) < 3 or not (self.linesForMatching[self.questionNumber][i][2] == 1):
				allCorrectlyAnswered = False
				self.currWindow.ui.matchingLabels[i * 2].setStyleSheet(u"color:rgb(255, 0, 0)")
			else: 
				self.currWindow.ui.matchingLabels[i * 2].setStyleSheet(u"color:rgb(0, 184, 0)")
				rightLabel.setStyleSheet(u"color:rgb(0, 184, 0)")
		
		for i in range(0, len(self.linesForMatching[self.questionNumber])):
			if self.currWindow.ui.matchingLabels[(i * 2)+ 1].styleSheet() == '':
				self.currWindow.ui.matchingLabels[(i * 2)+ 1].setStyleSheet(u"color:rgb(255, 0, 0)")
			
		if allCorrectlyAnswered:
			self.Score += 1
			
		self.roundScore()
		
		if self.Score == 1:
			points = self.translator[self.language][18] + str(self.Score) + self.translator[self.language][19] + str(len(self.questions))
		else:
			points = self.translator[self.language][20] + str(self.Score) + self.translator[self.language][21] + str(len(self.questions))
		
		if allCorrectlyAnswered:
			self.currWindow.ui.label_2.setText( "<html><head/><body><p align=\"center\"> " + self.translator[self.language][22] +  "<br/></p></body></html>")
		else:
			self.currWindow.ui.label_2.setText("<html><head/><body><p align=\"center\"> " + self.translator[self.language][23] + "<br/></p></body></html>")
			
		self.currWindow.ui.label_4.setText( "<html><head/><body><p align=\"center\"> " + points + "<br/></p></body></html>")
		self.currWindow.ui.pushButton_13.setEnabled(False)
		
	
	def matchingRightButtonClickedQuiz(self):
		
		global linesForMatching
		
		buttonRight = self.currWindow.sender()

		for i in range(0,len(self.questions[self.questionNumber][1])*2):
			
			if self.currWindow.ui.matchingButtons[i].isVisible():
				if i % 2 == 0:
					self.currWindow.ui.matchingButtons[i].setEnabled(True)
					self.currWindow.ui.matchingLabels[i].setStyleSheet('')
					tempFont = self.currWindow.ui.matchingLabels[i].font()
					tempFont.setBold(False)
					self.currWindow.ui.matchingLabels[i].setFont(tempFont)
				else:
					self.currWindow.ui.matchingButtons[i].setEnabled(False)
					
		for i in range(0, len(self.questions[self.questionNumber][0])):			
			if self.currWindow.ui.matchingLabels[i*2].text() == self.leftChoiceMatching:
				buttonLeft = self.currWindow.ui.matchingButtons[i*2]
				indexOfLeftButton = i

		self.linesForMatching[self.questionNumber][indexOfLeftButton].append(buttonRight.objectName())
		if self.questions[self.questionNumber][1][indexOfLeftButton + 1] == buttonRight.objectName():
			self.linesForMatching[self.questionNumber][indexOfLeftButton].append(1)
		else:
			self.linesForMatching[self.questionNumber][indexOfLeftButton].append(0)

		self.drawMatchingLines
	
	def updateMatchingLines(self):
		
		
		global frameQuestionAnswered

		allCorrectlyAnswered = True
		
		for i in range(0, len(self.linesForMatching[self.questionNumber])):
			self.currWindow.ui.matchingButtons[i * 2].setEnabled(False)
			self.currWindow.ui.matchingButtons[(i * 2) + 1].setEnabled(False)
			
			if len(self.linesForMatching[self.questionNumber][i]) == 3:
				for k in self.currWindow.ui.matchingLabels:
					if k.text() == self.linesForMatching[self.questionNumber][i][1]:
						rightLabel = k
			
			if len(self.linesForMatching[self.questionNumber][i]) < 3 or not (self.linesForMatching[self.questionNumber][i][2] == 1):
				allCorrectlyAnswered = False
				self.currWindow.ui.matchingLabels[i * 2].setStyleSheet(u"color:rgb(255, 0, 0)")
			else: 
				self.currWindow.ui.matchingLabels[i * 2].setStyleSheet(u"color:rgb(0, 184, 0)")
				rightLabel.setStyleSheet(u"color:rgb(0, 184, 0)")
		
		for i in range(0, len(self.linesForMatching[self.questionNumber])):
			if self.currWindow.ui.matchingLabels[(i * 2)+ 1].styleSheet() == '':
				self.currWindow.ui.matchingLabels[(i * 2)+ 1].setStyleSheet(u"color:rgb(255, 0, 0)")
			
		self.roundScore()
		
		if self.Score == 1:
			points = self.translator[self.language][18] + str(self.Score) + self.translator[self.language][19] + str(len(self.questions))
		else:
			points = self.translator[self.language][20] + str(self.Score) + self.translator[self.language][21] + str(len(self.questions))
		
		if allCorrectlyAnswered:
			self.currWindow.ui.label_2.setText( "<html><head/><body><p align=\"center\"> " + self.translator[self.language][22] +  "<br/></p></body></html>")
		else:
			self.currWindow.ui.label_2.setText("<html><head/><body><p align=\"center\"> " + self.translator[self.language][23] + "<br/></p></body></html>")
			
		self.currWindow.ui.label_4.setText( "<html><head/><body><p align=\"center\"> " + points + "<br/></p></body></html>")
		self.currWindow.ui.pushButton_13.setEnabled(False)
		self.drawMatchingLines()
		
	def evaluateCheckBoxesTraining(self):
		
		global Score
		global frameQuestionAnswered
		
		self.frameQuestionAnswered[self.questionNumber] = True
		tempScore = 0
		allCorrectlyAnswered = True
		
		for i in self.currWindow.ui.checkBoxes:
			i.setEnabled(False)
			
			if i.isChecked():
				self.answers[self.questionNumber] +=(' ')
				self.answers[self.questionNumber] +=(i.text())
				
				if i.objectName()[0] == '-':
					allCorrectlyAnswered = False
					i.setStyleSheet(u"color:rgb(255, 0, 0)")
					tempScore -= float(i.objectName()[1:6]) 
				else:
					i.setStyleSheet(u"color:rgb(0, 184, 0)")
					tempScore += float(i.objectName()[0:5])	
			else:
				if i.objectName()[0] != '-' and i.objectName()[0] != ' ':
					allCorrectlyAnswered = False
					i.setStyleSheet(u"color:rgb(255, 0, 0)")
					tempScore -= float(i.objectName()[1:6])
		
		if tempScore < 0:
			tempScore = 0
		
		tempScore = tempScore / 100.0
		self.Score += tempScore
		self.roundScore()
		
		if self.Score == 1:
			points = self.translator[self.language][18] + str(self.Score) + self.translator[self.language][19] + str(len(self.questions))
		else:
			points = self.translator[self.language][20] + str(self.Score) + self.translator[self.language][21] + str(len(self.questions))
		
		if allCorrectlyAnswered:
			self.currWindow.ui.label_2.setText( "<html><head/><body><p align=\"center\"> " + self.translator[self.language][22] +  "<br/></p></body></html>")
		else:
			self.currWindow.ui.label_2.setText("<html><head/><body><p align=\"center\"> " + self.translator[self.language][23] + "<br/></p></body></html>")
			
		self.currWindow.ui.label_4.setText( "<html><head/><body><p align=\"center\"> " + points + "<br/></p></body></html>")
		self.currWindow.ui.pushButton_13.setEnabled(False)
	
	def updateCheckBoxesTraining(self):
		
		global Score

		allCorrectlyAnswered = True
		
		for i in self.currWindow.ui.checkBoxes:
			i.setEnabled(False)
			
			if i.isChecked():
				if i.objectName()[0] == '-':
					allCorrectlyAnswered = False
					i.setStyleSheet(u"color:rgb(255, 0, 0)")
				else:
					i.setStyleSheet(u"color:rgb(0, 184, 0)")
			else:
				if i.objectName()[0] != '-' and i.objectName()[0] != ' ':
					allCorrectlyAnswered = False
					i.setStyleSheet(u"color:rgb(255, 0, 0)")

		self.roundScore()

		if self.Score == 1:
			points = self.translator[self.language][18] + str(self.Score) + self.translator[self.language][19] + str(len(self.questions))
		else:
			points = self.translator[self.language][20] + str(self.Score) + self.translator[self.language][21] + str(len(self.questions))
		
		if allCorrectlyAnswered:
			self.currWindow.ui.label_2.setText( "<html><head/><body><p align=\"center\"> " + self.translator[self.language][22] +  "<br/></p></body></html>")
		else:
			self.currWindow.ui.label_2.setText("<html><head/><body><p align=\"center\"> " + self.translator[self.language][23] + "<br/></p></body></html>")
			
		self.currWindow.ui.label_4.setText( "<html><head/><body><p align=\"center\"> " + points + "<br/></p></body></html>")
	
	def roundScore (self):
		
		global Score
		
		tempScore = self.Score %1 
		self.Score = int(self.Score-tempScore)
		tempScore *= 100
		
		if tempScore >=30 and tempScore <=36:
			tempScore = 33.3
		elif tempScore >=63 and tempScore <=69:
			tempScore = 66.6
		elif tempScore < 6.25:
			tempScore = 0
		elif tempScore >= 6.25 and tempScore < 18.75:
			tempScore = 12.5
		elif tempScore >= 18.75 and tempScore < 31.25:
			tempScore = 25
		elif tempScore >= 31.25 and tempScore < 43.75:
			tempScore = 37.5
		elif tempScore >= 43.75 and tempScore < 56.25:
			tempScore = 50
		elif tempScore >= 56.25 and tempScore < 68.75:
			tempScore = 62.5
		elif tempScore >= 68.75 and tempScore < 81.25:
			tempScore = 75
		elif tempScore >= 81.25 and tempScore < 93.75:
			tempScore = 87.5
		else:
			tempScore = 100
	
		tempScore = tempScore / 100.0
		self.Score += tempScore
	
	def evaluateLines(self):
		allMatchingCorrect = True
		for i in range(0,len(self.questions)):
			if self.questionType[i] == 'matching':
				allMatchingCorrect = True
				for currLine in self.linesForMatching[i]:
					if len(currLine) < 3  or not(currLine[2]  == 1):
						allMatchingCorrect = False
				if allMatchingCorrect:
					self.Score += 1
	
	def showScore(self):
		
		global log
				
		self.roundScore()
		self.currWindow = PointsDialog(self.Score, len(self.questions))
		self.currWindow.ui.pushButton_2.clicked.connect(self.goToTraining)
		self.currWindow.ui.pushButton.clicked.connect(self.currWindow.close)
		self.currWindow.show()
		
		end = time.time()
		self.timeElapsed = end - self.timeElapsed 
		self.log = open(self.user_plugin_dir + '/log.csv', 'a')
		logString = ''
		logString = self.path.split('/')[len(self.path.split('/'))-1]
		logString +=';'
		logString += self.quizTitle
		logString += ';'
		logString += str(len(self.questions))
		logString += ';'
		logString += str(self.Score)
		logString += ';'
		logString += str(self.timeElapsed)
		self.log.write('\n' + logString)
		self.log.close()
	
	def showNormalResults(self):
		self.evaluateLines()
		self.showScore()
	def showQuizResults(self):
		
		self.currWindow.close()
		self.showScore()
	
	def goToTraining(self):
		
		self.currWindow.close()
		self.training()		
			
	


class Painter(QtGui.QWidget):
	

	def __init__(self, parent, lines):
		self.parent = parent
		self.lines = lines
		self.xOffset = 0
		self.yOffset = 0
		self.questionNumber = 0
		super(Painter, self).__init__()
		
	def update(self, questionNumber):
		self.repaint()
		self.questionNumber=questionNumber
	
	def paintEvent(self, event):
		painter = QtGui.QPainter(self)
		painter.begin(self)
		painter.setRenderHint(QPainter.Antialiasing)
		self.drawLines(event, painter)
		painter.end()
		
	def drawLines(self, event, painter):
		
		pen = QtGui.QPen(QtCore.Qt.blue, 2, QtCore.Qt.SolidLine)
		painter.setPen(pen)
		
		#xOffset = self.currWindow.ui.stackedWidget.mapTo(self.currWindow,QPoint(0,0)).x()
		#yOffset = self.currWindow.ui.stackedWidget.mapTo(self.currWindow,QPoint(0,0)).y()
		
		self.xOffset = self.parentWidget().mapTo(self.parentWidget().parentWidget(), QPoint(0,0)).x()
		self.yOffset = self.parentWidget().mapTo(self.parentWidget().parentWidget(), QPoint(0,0)).y()
		
		i = self.lines[self.questionNumber]
		print i
		for line in i:
			if not line == []:
				painter.drawLine(line[0].mapTo(self.parentWidget().parentWidget(),QPoint(line[0].width(),line[0].height()/2)).x()-self.xOffset, line[0].mapTo(self.parentWidget().parentWidget(),QPoint(line[0].width(),line[0].height()/2)).y()-self.yOffset, line[1].mapTo(self.parentWidget().parentWidget(),QPoint(0,line[1].height()/2)).x()-self.xOffset, line[1].mapTo(self.parentWidget().parentWidget(),QPoint(0,line[1].height()/2)).y()-self.yOffset)
				#painter.drawLine(line[0].pos().x()-self.xOffset, line[0].pos().y()-self.yOffset, line[1].pos().x()-self.xOffset, line[1].pos().y()-self.yOffset)
				#painter.drawLine(0, 0, line[1].pos().x()-self.xOffset, line[1].pos().y()-self.yOffset)
				
				print 'huhu'
		
