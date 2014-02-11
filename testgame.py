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
import PyQt4
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
import resources_rc
from testgamedialog import TestGameDialog
from startGameDialog import StartGameDialog
import os.path
from pointsDialog import PointsDialog
from trainingQuizDialog import TrainingQuizDialog
import time
import sys
import math
import codecs
import random
from uberBoxDialog import UberBoxDialog
from QuestionClass import *
from questionParser import QuestionParser

class TestGame:
	
	Score = 0
	language = 0
	timeElapsed = 0
	questionNumber = 0
	questionsAnswered = 0
	log = ''
	path = ''
	dirPath = ''
	quizTitle = ''
	instruction =''
	leftChoiceMatching = ''
	lines = []
	answers = []
	questions = []
	buttonList = []
	questionType = []
	linesForMatching = []
	rightListShuffled = []
	siteVisitedMatching = []
	frameQuestionAnswered = []
	translator = [[],[],[]]
	
	def __init__(self, iface):
		
		reload(sys)
		sys.setdefaultencoding('utf-8')
	   
		self.iface = iface
		self.plugin_dir = os.path.dirname(__file__)

		locale = QSettings().value("locale/userLocale")[0:2]
		localePath = os.path.join(self.plugin_dir, 'i18n', 'testgame_{}.qm'.format(locale))
		self.user_plugin_dir = QFileInfo(QgsApplication.qgisUserDbFilePath()).path() + "python/plugins/Quiz"
		
		if os.path.exists(localePath):
			self.translator = QTranslator()
			self.translator.load(localePath)

			if qVersion() > '4.3.3':
				QCoreApplication.installTranslator(self.translator)
		
		
		self.translator = [[],[], []]
		
		with codecs.open(self.user_plugin_dir +'/germanText.txt','r','utf-8') as f:
			for line in f:
				self.translator[0].append(line[:-1])
			f.close()
		
		with codecs.open(self.user_plugin_dir +'/englishText.txt','r','utf-8') as f:
			for line in f:
				self.translator[1].append(line[:-1])
			f.close()
		
		with codecs.open(self.user_plugin_dir +'/frenchText.txt','r','utf-8') as f:
			for line in f:
				self.translator[2].append(line[:-1])
			f.close()
				
	def initGui(self):

		self.action = QAction(QIcon(":/df/Länder/icon.png"),u"Quiz", self.iface.mainWindow())
		self.action.triggered.connect(self.run)
		self.iface.addToolBarIcon(self.action)
		self.iface.addPluginToMenu(u"Quiz", self.action)

	def unload(self):

		self.iface.removePluginMenu(u"Quiz", self.action)
		self.iface.removeToolBarIcon(self.action)

	def run(self):

		if QSettings().value("locale/userLocale")[0:2] == 'de':
			self.language = 0
		elif QSettings().value("locale/userLocale")[0:2] == 'fr':
			self.language = 2
		else:
			self.language = 1

		self.dlg = TestGameDialog()
		
		self.globalFont = self.dlg.ui.startTest.font()
	
		self.dlg.ui.startTest.setText(self.translator[self.language][0])
		self.dlg.ui.startTest.setEnabled(False)
		self.dlg.ui.startTraining.setText(self.translator[self.language][1])
		self.dlg.ui.startTraining.setEnabled(False)
		self.dlg.ui.chooseQuiz.setText(self.translator[self.language][2])
		self.dlg.ui.chooseQuiz.clicked.connect(self.selectQuiz)
		self.dlg.ui.pushButton.setText(self.translator[self.language][3])
		self.dlg.ui.pushButton.clicked.connect(self.help)
		self.dlg.ui.startTest.clicked.connect(self.startQuiz)
		self.dlg.ui.startTraining.clicked.connect(self.training)
		
		self.dlg.ui.label_3.setText(self.translator[self.language][53])
		self.dlg.ui.label_3.setFont(self.globalFont)
		self.dlg.ui.label_4.setText(self.translator[self.language][54])
		self.dlg.ui.label_4.setOpenExternalLinks(True)
		self.dlg.ui.label_4.setFont(self.globalFont)
		self.dlg.ui.label_5.setText(self.translator[self.language][55])
		self.dlg.ui.label_5.setFont(self.globalFont)
		self.dlg.ui.label_6.setText(self.translator[self.language][56])
		self.dlg.ui.label_6.setOpenExternalLinks(True)
		self.dlg.ui.label_6.setFont(self.globalFont)
		self.dlg.ui.label_7.setText(self.translator[self.language][57])
		self.dlg.ui.label_7.setFont(self.globalFont)
		self.dlg.ui.label_8.setText(self.translator[self.language][58])
		self.dlg.ui.label_8.setOpenExternalLinks(True)
		self.dlg.ui.label_8.setFont(self.globalFont)
		self.dlg.ui.label_9.setText(self.translator[self.language][59])
		self.dlg.ui.label_9.setFont(self.globalFont)
		self.dlg.ui.label_10.setText("<a href='mailto:rkrucker@hsr.ch'>Rafael Krucker</a>")
		self.dlg.ui.label_10.setOpenExternalLinks(True)
		self.dlg.ui.label_10.setFont(self.globalFont)
		
		self.buttonList.append(self.dlg.ui.startTest)
		self.buttonList.append(self.dlg.ui.startTraining)
		self.buttonList.append(self.dlg.ui.chooseQuiz)
		self.buttonList.append(self.dlg.ui.pushButton)
		self.buttonList.append(self.dlg.ui.startTitel)
		self.buttonList.append(self.dlg.ui.startImage)
		self.buttonList.append(self.dlg.ui.label_3)
		self.buttonList.append(self.dlg.ui.label_4)
		self.buttonList.append(self.dlg.ui.label_5)
		self.buttonList.append(self.dlg.ui.label_6)
		self.buttonList.append(self.dlg.ui.label_7)
		self.buttonList.append(self.dlg.ui.label_8)
		self.buttonList.append(self.dlg.ui.label_9)
		self.buttonList.append(self.dlg.ui.label_10)
		
		self.dlg.ui.menuOptions_2.setTitle(self.translator[self.language][37])
		self.dlg.ui.language.setTitle(self.translator[self.language][4])
		self.dlg.ui.fontMenu.setTitle(self.translator[self.language][40])
		self.dlg.ui.menuGames.setTitle(self.translator[self.language][43])
		self.dlg.ui.menuHilf.setTitle(self.translator[self.language][3])
		
		self.dlg.ui.german.setText(self.translator[self.language][42])
		self.dlg.ui.german.triggered.connect(lambda: self.changeLanguage(0))
		self.dlg.ui.english.setText(self.translator[self.language][41])
		self.dlg.ui.english.triggered.connect(lambda: self.changeLanguage(1))
		self.dlg.ui.french.setText(self.translator[self.language][61])
		self.dlg.ui.french.triggered.connect(lambda: self.changeLanguage(2))
		self.dlg.ui.geogame.setText(self.translator[self.language][38])
		self.dlg.ui.geogame.triggered.connect(lambda: QDesktopServices.openUrl(QUrl("http://giswiki.hsr.ch/GeoGames") ) )
		self.dlg.ui.quizPlatform.setText(self.translator[self.language][39])
		self.dlg.ui.quizPlatform.triggered.connect(lambda: QDesktopServices.openUrl(QUrl("http://giswiki.hsr.ch/QGIS-Materialien")))
		self.dlg.ui.actionAbout.setText(self.translator[self.language][46])
		self.dlg.ui.actionAbout.triggered.connect(self.about)
		self.dlg.ui.actionWebhelp.setText(self.translator[self.language][45])
		self.dlg.ui.actionWebhelp.triggered.connect(lambda: QDesktopServices.openUrl(QUrl("http://giswiki.hsr.ch/QGIS-Materialien")))
		self.dlg.ui.actionContact.setText(self.translator[self.language][44])
		self.dlg.ui.actionContact.triggered.connect(lambda: QDesktopServices.openUrl(QUrl("mailto:rkrucker@hsr.ch")))
		self.dlg.ui.actionSmaller.setText(self.translator[self.language][63])
		self.dlg.ui.actionSmaller.triggered.connect(self.fontSmaller)
		self.dlg.ui.actionBigger.setText(self.translator[self.language][62])
		self.dlg.ui.actionBigger.triggered.connect(self.fontBigger)
		self.dlg.ui.actionStandard_2.setText(self.translator[self.language][75])
		self.dlg.ui.actionStandard_2.triggered.connect(self.fontStandard)

		self.dlg.show()
		
	def changeLanguage(self, lang):
		
		self.language = lang
		
		self.dlg.ui.label_3.setText(self.translator[self.language][53])
		self.dlg.ui.label_4.setText(self.translator[self.language][54])
		self.dlg.ui.label_4.setOpenExternalLinks(True)
		self.dlg.ui.label_5.setText(self.translator[self.language][55])
		self.dlg.ui.label_6.setText(self.translator[self.language][56])
		self.dlg.ui.label_6.setOpenExternalLinks(True)
		self.dlg.ui.label_7.setText(self.translator[self.language][57])
		self.dlg.ui.label_8.setText(self.translator[self.language][58])
		self.dlg.ui.label_8.setOpenExternalLinks(True)
		self.dlg.ui.label_9.setText(self.translator[self.language][59])
		self.dlg.ui.startTest.setText(self.translator[self.language][0])
		self.dlg.ui.startTraining.setText(self.translator[self.language][1])
		self.dlg.ui.chooseQuiz.setText(self.translator[self.language][2])
		self.dlg.ui.pushButton.setText(self.translator[self.language][3])
		self.dlg.ui.menuOptions_2.setTitle(self.translator[self.language][37])
		self.dlg.ui.language.setTitle(self.translator[self.language][4])
		self.dlg.ui.fontMenu.setTitle(self.translator[self.language][40])
		self.dlg.ui.actionSmaller.setText(self.translator[self.language][63])
		self.dlg.ui.actionBigger.setText(self.translator[self.language][62])
		self.dlg.ui.actionStandard_2.setText(self.translator[self.language][75])
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
		
		self.globalFont.setPointSize(self.globalFont.pointSize() - 2) 
		for i in self.buttonList:
			tempFont = i.font()
			tempFont.setPointSize(tempFont.pointSize() - 2)
			i.setFont(tempFont)
		
	def fontBigger(self):
		
		self.globalFont.setPointSize(self.globalFont.pointSize() + 2) 
		for i in self.buttonList:
			tempFont = i.font()
			tempFont.setPointSize(tempFont.pointSize() + 2)
			i.setFont(tempFont)
	
	def fontStandard(self):
		
		self.globalFont.setPointSize(8) 
		for i in self.buttonList:
			tempFont = i.font()
			tempFont.setPointSize(8)
			i.setFont(tempFont)
			
	def selectQuiz(self):
		
		self.path = QFileDialog.getOpenFileName(self.dlg, 'Open File', self.user_plugin_dir + '\quizzes')

		if self.path != '':
			parser = QuestionParser(self.path)
			self.questions = parser.allQuestions
			self.questionType = parser.questionType
			self.instruction = parser.instruction
			self.quizTitle = parser.quizTitle
			self.dlg.ui.startTest.setEnabled(True)
			self.dlg.ui.startTraining.setEnabled(True)
			self.dlg.ui.startTitel.setText(u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; font-style:normal; color:#000000;\">" + self.quizTitle+"</span></p></body></html>")
			self.dlg.ui.startImage.setWordWrap(True)
			self.dlg.ui.startImage.setText("<html><head/><body><p>"+self.instruction+"<br/></p></body></html>")
	
	def help(self):
		
		if self.dlg.ui.stackedWidget.currentIndex() == 0:
			self.dlg.ui.stackedWidget.setCurrentIndex(1)
		else:
			self.dlg.ui.stackedWidget.setCurrentIndex(0)
	
	def about(self):
		
		self.aboutWindow = UberBoxDialog(self.dlg)
		
		self.aboutWindow.ui.label_3.setText(self.translator[self.language][47])
		self.aboutWindow.ui.label_3.setFont(self.globalFont)
		self.aboutWindow.ui.label_4.setText(self.translator[self.language][48])
		self.aboutWindow.ui.label_4.setFont(self.globalFont)
		self.aboutWindow.ui.label_5.setText(self.translator[self.language][49])
		self.aboutWindow.ui.label_5.setFont(self.globalFont)
		self.aboutWindow.ui.label_6.setText(self.translator[self.language][50])
		self.aboutWindow.ui.label_6.setFont(self.globalFont)
		self.aboutWindow.ui.label_7.setText(self.translator[self.language][51])
		self.aboutWindow.ui.label_7.setFont(self.globalFont)
		self.aboutWindow.ui.label_8.setText(self.translator[self.language][52])
		self.aboutWindow.ui.label_8.setFont(self.globalFont)
		self.aboutWindow.ui.label_8.setOpenExternalLinks(True)
		self.aboutWindow.ui.label_9.setText(self.translator[self.language][68])
		self.aboutWindow.ui.label_9.setFont(self.globalFont)
		self.aboutWindow.ui.label_10.setText(self.translator[self.language][69])
		self.aboutWindow.ui.label_10.setFont(self.globalFont)
		
		self.aboutWindow.exec_()
		
	def addWidgets(self):
		
		self.currWindow.ui.matches = []
		self.currWindow.ui.checkBoxes = []
		self.currWindow.ui.matchingLabels = []
		self.currWindow.ui.matchingButtons = []
		self.currWindow.ui.matchingLabelsLeft = []
		self.currWindow.ui.matchingButtonsLeft = []
		self.currWindow.ui.matchingLabelsRight = []
		self.currWindow.ui.matchingButtonsRight = []
		
		for i in range(12):
			horizontalLayout = PyQt4.QtGui.QHBoxLayout()
			horizontalLayout.setObjectName("horizontalLayout")
			spacerItem = PyQt4.QtGui.QSpacerItem(40, 20, PyQt4.QtGui.QSizePolicy.Expanding, PyQt4.QtGui.QSizePolicy.Minimum)
			label = PyQt4.QtGui.QLabel()
			label.setFont(self.globalFont)
			label.setObjectName("label")
			self.currWindow.ui.matchingLabels.append(label)
			pushButton = PyQt4.QtGui.QPushButton()
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
			checkBox = PyQt4.QtGui.QCheckBox()
			checkBox.setFont(self.globalFont)
			self.currWindow.ui.checkBoxes.append(checkBox)
		
		for currIndex in range(0, len(self.currWindow.ui.checkBoxes)):
			height = currIndex / 2
			width = (currIndex % 2) * 2
			self.currWindow.ui.gridLayout.addWidget(self.currWindow.ui.checkBoxes[currIndex], height, width + 1, 1, 1 )	
			self.currWindow.ui.gridLayout.addLayout(self.currWindow.ui.matches[currIndex], height, width + 1, 1, 1 )	
		
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
		
		self.currWindow.ui.editLabels = []
		self.currWindow.ui.editLabels.append(self.currWindow.ui.editLabel)
		self.currWindow.ui.editLabels.append(self.currWindow.ui.editLabel_2)
		self.currWindow.ui.editLabels.append(self.currWindow.ui.editLabel_3)
		self.currWindow.ui.editLabels.append(self.currWindow.ui.editLabel_4)
		self.currWindow.ui.editLabels.append(self.currWindow.ui.editLabel_5)
		self.currWindow.ui.editLabels.append(self.currWindow.ui.editLabel_6)
		self.currWindow.ui.editLabels.append(self.currWindow.ui.editLabel_7)
		self.currWindow.ui.editLabels.append(self.currWindow.ui.editLabel_8)
		self.currWindow.ui.editLabels.append(self.currWindow.ui.editLabel_9)
		self.currWindow.ui.editLabels.append(self.currWindow.ui.editLabel_10)
		self.currWindow.ui.editLabels.append(self.currWindow.ui.editLabel_11)
		self.currWindow.ui.editLabels.append(self.currWindow.ui.editLabel_12)
		
		self.currWindow.ui.editGaps = []
		self.currWindow.ui.editGaps.append(self.currWindow.ui.lineEditGap)
		self.currWindow.ui.editGaps.append(self.currWindow.ui.lineEditGap_2)
		self.currWindow.ui.editGaps.append(self.currWindow.ui.lineEditGap_3)
		self.currWindow.ui.editGaps.append(self.currWindow.ui.lineEditGap_4)
		self.currWindow.ui.editGaps.append(self.currWindow.ui.lineEditGap_5)
		self.currWindow.ui.editGaps.append(self.currWindow.ui.lineEditGap_6)
		self.currWindow.ui.editGaps.append(self.currWindow.ui.lineEditGap_7)
		self.currWindow.ui.editGaps.append(self.currWindow.ui.lineEditGap_8)
		self.currWindow.ui.editGaps.append(self.currWindow.ui.lineEditGap_9)
		self.currWindow.ui.editGaps.append(self.currWindow.ui.lineEditGap_10)
		self.currWindow.ui.editGaps.append(self.currWindow.ui.lineEditGap_11)
		self.currWindow.ui.editGaps.append(self.currWindow.ui.lineEditGap_12)
		
		for i in range(len(self.currWindow.ui.editGaps)):
			self.currWindow.ui.editGaps[i].textEdited.connect(self.gapStoreAnswers)
			self.currWindow.ui.editGaps[i].setObjectName(str(i))
			self.currWindow.ui.editGaps[i].setFont(self.globalFont)
			self.currWindow.ui.editLabels[i].setFont(self.globalFont)
		
		self.currWindow.ui.labelGap.setFont(self.globalFont)
			
		for i in self.currWindow.ui.buttonArray:
			if not self.trainingMode:
				i.clicked.connect(self.scorePenalty)
			else:
				i.clicked.connect(self.scorePenaltyQuiz)
			i.setFont(self.globalFont)
		
	def initializeSettings(self):
	
		self.Score = 0
		self.questionNumber = 0
		self.questionsAnswered = 0
		self.currMatchingButtonClicked = ''
		self.lines = []
		self.linesForMatching = []
		self.rightListShuffeld = []
		self.answers = [0 for x in range(len(self.questions))]
		self.siteVisitedMatching = [0 for x in range(len(self.questions))]
		self.frameQuestionAnswered = [0 for x in range(len(self.questions))]
		
		for i in range(0, len(self.questions)):
			self.answers[i] = ''
			self.siteVisitedMatching[i] =  False
			self.frameQuestionAnswered[i] = False
			self.lines.append([])
			self.linesForMatching.append([])
			self.rightListShuffeld.append([])
			
		self.addWidgets()	
		
		for i in self.currWindow.ui.matchingButtons:
			i.clicked.connect(self.matchingButtonClicked)	
		
		self.paintPanel = Painter(self, self.lines)
		self.currWindow.ui.stackedWidget.insertWidget(0,self.paintPanel)
		self.currWindow.ui.stackedWidget.setCurrentWidget(self.paintPanel)
		self.currWindow.ui.label.setFont(self.globalFont)
		self.currWindow.ui.label.setWordWrap(True)
		self.currWindow.ui.label_2.setFont(self.globalFont)
		self.currWindow.ui.label_3.setFont(self.globalFont)
		self.currWindow.ui.pushButton_13.setFont(self.globalFont)
		self.currWindow.ui.pushButton_13.setVisible(False)
		self.currWindow.ui.pushButton_14.setFont(self.globalFont)
		
	def startQuiz(self):
		
		self.trainingMode = False
	
		self.currWindow = StartGameDialog(self.translator[self.language][74])

		self.initializeSettings()
		self.currWindow.setWindowTitle(self.translator[self.language][76]+' '+self.translator[self.language][66]+ ' - ' +self.quizTitle)
		self.currWindow.ui.pushButton_13.clicked.connect(self.previousQuestion)
		self.currWindow.ui.pushButton_13.setText(self.translator[self.language][5])
		self.currWindow.ui.pushButton_14.clicked.connect(self.nextQuestion)
		self.currWindow.ui.pushButton_14.setText(self.translator[self.language][6])
		
		for i in self.currWindow.ui.checkBoxes:
			i.stateChanged.connect(self.checkState)
		
		self.instantiateQuestion()
		
		self.currWindow.exec_()
			
	def nextQuestion(self):

		self.questionNumber += 1
		self.currWindow.ui.pushButton_13.setVisible(True)
		if self.questionNumber == len(self.questions) -1:
			self.currWindow.ui.pushButton_14.setText(self.translator[self.language][7])
			self.currWindow.ui.pushButton_14.clicked.disconnect()
			self.currWindow.ui.pushButton_14.clicked.connect(self.showNormalResults)
		
		self.instantiateQuestion()
				
	def previousQuestion(self):
	
		self.questionNumber -=1
		if self.questionNumber == 0:
			self.currWindow.ui.pushButton_13.setVisible(False)
		else: 
			self.currWindow.ui.pushButton_13.setVisible(True)
		self.currWindow.ui.pushButton_14.setText(self.translator[self.language][6])
		self.currWindow.ui.pushButton_14.clicked.disconnect()
		self.currWindow.ui.pushButton_14.clicked.connect(self.nextQuestion)	
		
		self.instantiateQuestion()
	
	def instantiateQuestion(self):
	
		self.currQuestion = self.questions[self.questionNumber]
		self.drawMatchingLines(self.questionNumber)
		self.currWindow.ui.label_2.setText(self.translator[self.language][29] + ' ' + str(self.questionNumber +1) + ' ' + self.translator[self.language][30]+ ' ' + str(len(self.questions)))
		self.currWindow.ui.label_3.setText(self.translator[self.language][77] + ' ' + str(self.questionsAnswered) + ' ' + self.translator[self.language][30] + ' ' + str(len(self.questions)))
		
		self.currWindow.ui.stackedWidget_2.setCurrentWidget(self.currWindow.ui.page_3)
		
		for i in self.currWindow.ui.buttonArray:
			tempFont = i.font()
			tempFont.setBold(False)
			i.setFont(tempFont)
			i.setText('')
			i.setStyleSheet('')
			i.setVisible(False)
		
		for i in self.currWindow.ui.checkBoxes:
			i.setVisible(False)
			i.setText('')
		
		for i in self.currWindow.ui.matchingButtons:
			i.setVisible(False)
		
		for i in self.currWindow.ui.matchingLabels:
			i.setText('')
			i.setVisible(False)	
		
		self.currWindow.ui.labelGap.setVisible(False)
		
		for i in self.currWindow.ui.editLabels:
			i.setVisible(False)
		
		for i in self.currWindow.ui.editGaps:
			i.setVisible(False)
			i.setText('')
	
		if self.questionType[self.questionNumber] == 'multipleChoice':
			self.currWindow.ui.label.setText("<html><head/><body><p align=\"center\">" + self.currQuestion.title +"</p></body></html>")
			
			for nr in range(len(self.currQuestion.answers)):
				self.currWindow.ui.checkBoxes[nr].setText(self.currQuestion.answers[nr])
				self.currWindow.ui.checkBoxes[nr].setObjectName(str(self.currQuestion.percentages[nr]))
				self.currWindow.ui.checkBoxes[nr].setVisible(True)
			
			
		if self.questionType[self.questionNumber] == 'pictureQuestion':	
			self.currWindow.ui.label.setText("<html><head/><body><p align=\"center\"><img src=\""+ self.currQuestion.picPath+"\"/></p><p align=\"center\">" + self.currQuestion.title+"</p></body></html>")
			for nr in range(len(self.currQuestion.answers)):
				self.currWindow.ui.buttonArray[nr].setVisible(True)
				self.currWindow.ui.buttonArray[nr].setText(self.currQuestion.answers[nr])
				self.currWindow.ui.buttonArray[nr].clicked.disconnect()
				self.currWindow.ui.buttonArray[nr].clicked.connect(self.scorePenalty)	
				
				if not self.frameQuestionAnswered[self.questionNumber]:			
					self.currWindow.ui.buttonArray[nr].setEnabled(True)					
				else:
					self.currWindow.ui.buttonArray[nr].setEnabled(False)
					if self.currWindow.ui.buttonArray[nr].text() == self.answers[self.questionNumber]:
						self.currWindow.ui.buttonArray[nr].setStyleSheet('color: rgb(0,0,255)')
						tempFont = self.currWindow.ui.buttonArray[nr].font()
						tempFont.setBold(True)
						self.currWindow.ui.buttonArray[nr].setFont(tempFont)
						
			self.currWindow.ui.buttonArray[self.currQuestion.rightAnswerIndex].clicked.disconnect()
			self.currWindow.ui.buttonArray[self.currQuestion.rightAnswerIndex].clicked.connect(self.scoreBonus)	
			
			
		if self.questionType[self.questionNumber] == 'missingWord':
			self.currWindow.ui.labelGap.setText(self.currQuestion.title)
			self.currWindow.ui.labelGap.setVisible(True)
			self.currWindow.ui.stackedWidget_2.setCurrentWidget(self.currWindow.ui.page_4)
			for nr in range(len(self.currQuestion.answers)):
				self.currWindow.ui.editGaps[nr].setVisible(True)
				self.currWindow.ui.editLabels[nr].setVisible(True)
			
			if self.frameQuestionAnswered[self.questionNumber]:			
				for i in range(len (self.currQuestion.answers)):
					self.currWindow.ui.editGaps[i].setText(self.answers[self.questionNumber][i])
			else:
				self.answers[self.questionNumber] = []
				for i in range(len (self.currQuestion.answers)):
					self.answers[self.questionNumber].append('')

			
		if self.questionType[self.questionNumber] == 'stringQuestion':
			self.currWindow.ui.label.setText("<html><head/><body><p align=\"center\">" + self.currQuestion.title +"</p></body></html>")
			for nr in range(0,len(self.currQuestion.answers)):
				self.currWindow.ui.buttonArray[nr].setText(self.currQuestion.answers[nr])
				self.currWindow.ui.buttonArray[nr].setVisible(True)
				self.currWindow.ui.buttonArray[nr].clicked.disconnect()
				self.currWindow.ui.buttonArray[nr].clicked.connect(self.scorePenalty)	
				
				if not self.frameQuestionAnswered[self.questionNumber]:
						self.currWindow.ui.buttonArray[nr].setEnabled(True)
				else:
					self.currWindow.ui.buttonArray[nr].setEnabled(False)
					if self.currWindow.ui.buttonArray[nr].text() == self.answers[self.questionNumber]:
						self.currWindow.ui.buttonArray[nr].setStyleSheet('color: rgb(0,0,255)')
						tempFont = self.currWindow.ui.buttonArray[nr].font()
						tempFont.setBold(True)
						self.currWindow.ui.buttonArray[nr].setFont(tempFont)
						
			self.currWindow.ui.buttonArray[self.currQuestion.rightAnswerIndex].clicked.disconnect()				
			self.currWindow.ui.buttonArray[self.currQuestion.rightAnswerIndex].clicked.connect(self.scoreBonus)			
				
				
		if self.questionType[self.questionNumber] == 'matching':
			
			self.currWindow.ui.label.setText("<html><head/><body><p align=\"center\">" + self.currQuestion.title +"</p></body></html>")
			rightListShuffeldTemp = []

			for i in range(0,len(self.currQuestion.answers)):
				self.currWindow.ui.matchingLabels[i].setText(self.currQuestion.answers[i])
				self.currWindow.ui.matchingLabels[i].setVisible(True)
				self.currWindow.ui.matchingButtons[i].setVisible(True)
				if i % 2 == 1:	
					rightListShuffeldTemp.append(self.currQuestion.answers[i])
					if not self.siteVisitedMatching[self.questionNumber]:
						self.linesForMatching[self.questionNumber].append([])
						self.lines[self.questionNumber].append([])
						
			random.shuffle(rightListShuffeldTemp)
			
			if not self.siteVisitedMatching[self.questionNumber]:
				self.rightListShuffeld[self.questionNumber] = rightListShuffeldTemp
			
			for i in range(len(self.rightListShuffeld[self.questionNumber])):
				self.currWindow.ui.matchingLabels[((i) * 2)+1].setText(self.rightListShuffeld[self.questionNumber][i])
				self.currWindow.ui.matchingButtons[(i)*2].setObjectName(self.currQuestion.answers[i * 2])
				self.currWindow.ui.matchingButtons[((i)*2)+1].setObjectName(self.rightListShuffeld[self.questionNumber][i])
			
			self.siteVisitedMatching[self.questionNumber] = True
			
	def drawMatchingLines(self, qNumber):
		self.paintPanel.update(qNumber)
	
	def matchingButtonClicked(self):

		if not self.frameQuestionAnswered[self.questionNumber] and not self.training:
			self.questionsAnswered += 1
			self.frameQuestionAnswered[self.questionNumber] = True
		
		if not self.trainingMode:
			self.currWindow.ui.label_3.setText(self.translator[self.language][77] + ' ' + str(self.questionsAnswered) + ' ' + self.translator[self.language][30] + ' ' + str(len(self.questions)))
		else:
			self.currWindow.ui.label_6.setText(self.translator[self.language][77] + ' ' + str(self.questionsAnswered) + ' ' + self.translator[self.language][30] + ' ' + str(len(self.questions)))
		
		button = self.currWindow.sender()
		
		for i in range (len(self.currWindow.ui.matchingButtons)):
			if self.currWindow.ui.matchingButtons[i] == button:
				positionButton = i
		
		if self.currMatchingButtonClicked == '':
			delete = False
			for i in self.lines[self.questionNumber]:
				if button in i:
					delete = True
			
			if delete:
				for i in range(len(self.lines[self.questionNumber])):
					if button in self.lines[self.questionNumber][i]:
						deletePos = i
				self.lines[self.questionNumber][deletePos] = []
				self.linesForMatching[self.questionNumber][deletePos] = [] 
			else:
				self.currMatchingButtonClicked = button
				self.currWindow.ui.matchingLabels[positionButton].setStyleSheet('color: rgb(0,0,255)')
				tempFont = self.currWindow.ui.matchingLabels[positionButton].font()
				tempFont.setBold(True)
				self.currWindow.ui.matchingLabels[positionButton].setFont(tempFont)
			
		else:
			for i in range (len(self.currWindow.ui.matchingButtons)):
				if self.currWindow.ui.matchingButtons[i] == self.currMatchingButtonClicked:
					positionButtonOld = i
					
			if button == self.currMatchingButtonClicked:
				self.currWindow.ui.matchingLabels[positionButton].setStyleSheet('')
				tempFont = self.currWindow.ui.matchingLabels[positionButton].font()
				tempFont.setBold(False)
				self.currWindow.ui.matchingLabels[positionButton].setFont(tempFont)
				self.currMatchingButtonClicked = ''
			
			elif (button in self.currWindow.ui.matchingButtonsLeft and self.currMatchingButtonClicked in self.currWindow.ui.matchingButtonsLeft) or (button in self.currWindow.ui.matchingButtonsRight and self.currMatchingButtonClicked in self.currWindow.ui.matchingButtonsRight):
				self.currWindow.ui.matchingLabels[positionButtonOld].setStyleSheet('')
				tempFont = self.currWindow.ui.matchingLabels[positionButtonOld].font()
				tempFont.setBold(False)
				self.currWindow.ui.matchingLabels[positionButtonOld].setFont(tempFont)
				self.currMatchingButtonClicked = button
				self.currWindow.ui.matchingLabels[positionButton].setStyleSheet('color: rgb(0,0,255)')
				tempFont = self.currWindow.ui.matchingLabels[positionButton].font()
				tempFont.setBold(True)
				self.currWindow.ui.matchingLabels[positionButton].setFont(tempFont)
			
			else:
				if button in self.currWindow.ui.matchingButtonsLeft:
					buttonLeft = button
					buttonRight = self.currMatchingButtonClicked
					arrayPosition = positionButton 
				else:
					buttonLeft = self.currMatchingButtonClicked
					buttonRight = button
					arrayPosition = positionButtonOld 

				self.lines[self.questionNumber][arrayPosition/2].append(buttonLeft)
				self.lines[self.questionNumber][arrayPosition/2].append(buttonRight)
				self.linesForMatching[self.questionNumber][arrayPosition/2].append(buttonLeft.objectName())
				self.linesForMatching[self.questionNumber][arrayPosition/2].append(buttonRight.objectName())
				if self.currQuestion.answers[arrayPosition + 1] == buttonRight.objectName():
					self.linesForMatching[self.questionNumber][arrayPosition/2].append(1)
				else:
					self.linesForMatching[self.questionNumber][arrayPosition/2].append(0)
				tempFont = self.currWindow.ui.matchingLabels[positionButtonOld].font()
				tempFont.setBold(False)
				self.currWindow.ui.matchingLabels[positionButtonOld].setFont(tempFont)
				self.currWindow.ui.matchingLabels[positionButtonOld].setStyleSheet('')
				self.currMatchingButtonClicked = ''
		
		self.drawMatchingLines(self.questionNumber)
		self.currWindow.repaint()
		
	def checkState(self):

		if not self.frameQuestionAnswered[self.questionNumber]:
			self.questionsAnswered += 1
			self.frameQuestionAnswered[self.questionNumber] = True
			self.currWindow.ui.label_3.setText(self.translator[self.language][77] + ' ' + str(self.questionsAnswered) + ' ' + self.translator[self.language][30] + ' ' + str(len(self.questions)))

		button = self.currWindow.sender()
		scoreTemp = float(button.objectName())
		scoreDiff = scoreTemp/ 100

		if button.isChecked():
			self.updateScoreCheckboxCheck(scoreDiff)
		else:
			self.updateScoreCheckboxUncheck(scoreDiff)
	
	def updateScoreCheckboxCheck(self, scoreDiff):
		
		if self.Score + scoreDiff >= 0:
			self.Score += scoreDiff
		else:
			self.Score = 0
	
	def updateScoreCheckboxUncheck(self, scoreDiff):

		if self.Score - scoreDiff >= 0 :
			self.Score -= scoreDiff
		else:
			self.Score = 0

	def scoreBonus(self):

		button = self.currWindow.sender()
		self.questionsAnswered += 1
		self.currWindow.ui.label_3.setText(self.translator[self.language][77] + ' ' + str(self.questionsAnswered) + ' ' + self.translator[self.language][30] + ' ' + str(len(self.questions)))
		self.answers[self.questionNumber] = button.text()
		button.setStyleSheet('color: rgb(0, 0, 255)')
		tempFont = button.font()
		tempFont.setBold(True)
		button.setFont(tempFont)
		self.Score += 1
		self.frameQuestionAnswered[self.questionNumber] = True
		for i in self.currWindow.ui.buttonArray:
			i.setEnabled(False)
			
	def scorePenalty(self):

		button = self.currWindow.sender()
		self.questionsAnswered += 1
		self.currWindow.ui.label_3.setText(self.translator[self.language][77] + ' ' + str(self.questionsAnswered) + ' ' + self.translator[self.language][30] + ' ' + str(len(self.questions)))
		self.answers[self.questionNumber] = button.text()
		button.setStyleSheet('color: rgb(0, 0, 255)')
		self.answers[self.questionNumber] = button.text()
		tempFont = button.font()
		tempFont.setBold(True)
		button.setFont(tempFont)	
		penalty = 0
		if self.Score - penalty >= 0:
			self.Score -= penalty
		self.frameQuestionAnswered[self.questionNumber] = True
		for i in self.currWindow.ui.buttonArray:
			i.setEnabled(False)
			
	def gapStoreAnswers(self):
		
		if not self.frameQuestionAnswered[self.questionNumber] and not self.trainingMode:
			self.questionsAnswered += 1
			self.frameQuestionAnswered[self.questionNumber] = True
			self.currWindow.ui.label_3.setText(self.translator[self.language][77] + ' ' + str(self.questionsAnswered) + ' ' + self.translator[self.language][30] + ' ' + str(len(self.questions)))
		
		editor = self.currWindow.sender()
		editorIndex = int(editor.objectName())
		self.answers[self.questionNumber][editorIndex] = editor.text()
				
	def training(self):
		
		self.trainingMode = True
		
		self.currWindow = TrainingQuizDialog(self.translator[self.language][74])
		self.initializeSettings()
		self.currQuestion = self.questions[self.questionNumber]
		self.currWindow.setWindowTitle(self.translator[self.language][76]+' '+self.translator[self.language][67]+ ' - ' +self.quizTitle)
		
		self.currWindow.ui.label_4.setFont(self.globalFont)
		self.currWindow.ui.label_5.setFont(self.globalFont)
		self.currWindow.ui.label_5.setText(self.translator[self.language][29] + ' ' + str(self.questionNumber +1) + ' ' + self.translator[self.language][30]+ ' ' + str(len(self.questions)))
		self.currWindow.ui.label_6.setFont(self.globalFont)
		self.currWindow.ui.label_6.setText(self.translator[self.language][77] + ' '+ str(self.questionsAnswered)+' ' + self.translator[self.language][30] + ' ' + str(len(self.questions)))
		self.currWindow.ui.pushButton_13.setText(self.translator[self.language][28])
		self.currWindow.ui.pushButton_13.clicked.connect(self.evaluateCheckBoxesTraining)
		self.currWindow.ui.pushButton_14.setText(self.translator[self.language][14])
		self.currWindow.ui.pushButton_14.clicked.connect(self.previousQuizQuestion)
		self.currWindow.ui.pushButton_14.setVisible(False)
		self.currWindow.ui.pushButton_16.setText(self.translator[self.language][15])
		self.currWindow.ui.pushButton_16.clicked.connect(self.quizNextQuestion)
		self.currWindow.ui.pushButton_16.setFont(self.globalFont)
		
		self.instantiateQuestionTraining()
				
		self.currWindow.exec_()
	
	def quizRefresh(self, wasCorrect, answerGiven):
		
		self.roundScore()
		
		for nr in range(len(self.currQuestion.answers)):
			self.currWindow.ui.buttonArray[nr].setEnabled(False)
			if self.currQuestion.answers[nr] == answerGiven:
				buttonPressed = self.currWindow.ui.buttonArray[nr]
		
		correctAnswer = self.currWindow.ui.buttonArray[self.currQuestion.rightAnswerIndex].text()
		self.currWindow.ui.buttonArray[self.currQuestion.rightAnswerIndex].setStyleSheet(u"color:rgb(0, 184, 0)")
		tempFont = self.currWindow.ui.buttonArray[self.currQuestion.rightAnswerIndex].font()
		tempFont.setBold(True)
		self.currWindow.ui.buttonArray[self.currQuestion.rightAnswerIndex].setFont(tempFont)
		
		if self.Score == 1:
			points = self.translator[self.language][18] +' '+ str(self.Score) +' '+ self.translator[self.language][19] +' '+ str(len(self.questions)) + ' ' + self.translator[self.language][79]
		else:
			points = self.translator[self.language][20] +' '+ str(self.Score) +' '+ self.translator[self.language][21] +' '+ str(len(self.questions)) + ' ' + self.translator[self.language][79]
		
		if wasCorrect:
			self.currWindow.ui.label_2.setText( "<html><head/><body><p align=\"center\"> " + self.translator[self.language][22] +  "<br/></p></body></html>")
		else:
			self.currWindow.ui.label_2.setText("<html><head/><body><p align=\"center\"> " + self.translator[self.language][23] + "<br/></p></body></html>")
			self.currWindow.ui.label_3.setText( "<html><head/><body><p align=\"center\"> " + self.translator[self.language][24] +' '+ correctAnswer +"<br/></p></body></html>")
			buttonPressed.setStyleSheet(u"color:rgb(255, 0, 0)")
			tempFont = buttonPressed.font()
			tempFont.setBold(True)
			buttonPressed.setFont(tempFont)
		
		self.currWindow.ui.label_4.setText( "<html><head/><body><p align=\"center\"> " + points + "<br/></p></body></html>")
		self.frameQuestionAnswered[self.questionNumber] = True		
	
	def quizNextQuestion(self):

		self.questionNumber += 1
		self.currQuestion = self.questions[self.questionNumber]
		self.drawMatchingLines(self.questionNumber)
		self.currWindow.ui.label_5.setText(self.translator[self.language][29] + ' ' + str(self.questionNumber +1) + ' ' + self.translator[self.language][30]+ ' ' + str(len(self.questions)))
		self.currWindow.ui.label_6.setText(self.translator[self.language][77] + ' '+ str(self.questionsAnswered)+' ' + self.translator[self.language][30] + ' ' + str(len(self.questions)))
		
		if self.questionNumber == len(self.questions) - 1:
			self.currWindow.ui.pushButton_16.setText(self.translator[self.language][17])
			self.currWindow.ui.pushButton_16.clicked.disconnect()
			self.currWindow.ui.pushButton_16.clicked.connect(self.showQuizResults)
		
		if self.frameQuestionAnswered[self.questionNumber]:
			self.showOldQuestion()										
		else:
			self.instantiateQuestionTraining()
			
	def previousQuizQuestion(self):

		self.questionNumber -= 1
		
		self.currWindow.ui.pushButton_16.setText(self.translator[self.language][15])
		self.currWindow.ui.pushButton_16.clicked.disconnect()
		self.currWindow.ui.pushButton_16.clicked.connect(self.quizNextQuestion)
		
		self.showOldQuestion()
		
	def showOldQuestion(self):
		
		self.drawMatchingLines(self.questionNumber)
		self.currQuestion = self.questions[self.questionNumber]
		
		if self.questionNumber == 0:
			self.currWindow.ui.pushButton_14.setVisible(False)
		else:
			self.currWindow.ui.pushButton_14.setVisible(True)
		
		if self.questionNumber == len(self.questions) - 1:
			self.currWindow.ui.pushButton_16.setText(self.translator[self.language][17])
			self.currWindow.ui.pushButton_16.clicked.disconnect()
			self.currWindow.ui.pushButton_16.clicked.connect(self.showQuizResults)
		
		if self.Score == 1:
			points = self.translator[self.language][18] +' '+ str(self.Score) +' '+ self.translator[self.language][19] +' '+ str(len(self.questions))+ ' ' + self.translator[self.language][79]
		else:
			points = self.translator[self.language][20] +' '+ str(self.Score) +' '+ self.translator[self.language][21] +' '+ str(len(self.questions))+ ' ' + self.translator[self.language][79]
	
		for i in self.currWindow.ui.buttonArray:
			i.setVisible(False)
			i.setEnabled(True)
			i.setText('')
			i.setStyleSheet("")
			tempFont = i.font()
			tempFont.setBold(False)
			i.setFont(tempFont)
			
		for i in self.currWindow.ui.checkBoxes:
			i.setVisible(False)
			i.setEnabled(True)
			i.setText('')
			i.setStyleSheet("")
			i.setObjectName(' ')
		
		for i in self.currWindow.ui.matchingButtons:
			i.setVisible(False)
			
		for i in self.currWindow.ui.matchingLabels:
			i.setVisible(False)
			i.setStyleSheet("")
		
		self.currWindow.ui.stackedWidget_2.setCurrentWidget(self.currWindow.ui.page_3)
		
		for i in self.currWindow.ui.editLabels:
			i.setVisible(False)
		
		for i in self.currWindow.ui.editGaps:
			i.setVisible(False)
			i.setText('')
			i.setToolTip('')
			i.setStyleSheet('')
			tempFont = i.font()
			tempFont.setBold(False)
			i.setFont(tempFont)
			
		self.currWindow.ui.label_5.setText(self.translator[self.language][29] + ' ' + str(self.questionNumber +1) + ' ' + self.translator[self.language][30]+ ' ' + str(len(self.questions)))
		self.currWindow.ui.label_6.setText(self.translator[self.language][77] + ' '+ str(self.questionsAnswered)+' ' + self.translator[self.language][30] + ' ' + str(len(self.questions)))
		self.currWindow.ui.pushButton_13.setVisible(False)
		
		
		if self.questionType[self.questionNumber] == 'multipleChoice':
			self.currWindow.ui.label.setText("<html><head/><body><p align=\"center\">" + self.currQuestion.title +"</p></body></html>")
			self.currWindow.ui.pushButton_13.clicked.disconnect()
			self.currWindow.ui.pushButton_13.clicked.connect(self.evaluateCheckBoxesTraining)
			self.currWindow.ui.pushButton_13.setVisible(True)

			for nr in range(len(self.currQuestion.answers)):
				self.currWindow.ui.checkBoxes[nr].setText(self.currQuestion.answers[nr])
				self.currWindow.ui.checkBoxes[nr].setObjectName(str(self.currQuestion.percentages[nr]))
				self.currWindow.ui.checkBoxes[nr].setVisible(True)
			
			if self.frameQuestionAnswered[self.questionNumber]:
				self.updateCheckBoxesTraining()
				self.currWindow.ui.pushButton_13.setEnabled(False)
				for i in self.answers[self.questionNumber].split():
					for k in self.currWindow.ui.checkBoxes:
						k.setEnabled(False)
						if i == k.objectName():
							k.setCheckState(Qt.Checked)				
			else:
				self.currWindow.ui.pushButton_13.setEnabled(True)
				self.currWindow.ui.label_2.setText("")
				self.currWindow.ui.label_3.setText("")
				self.currWindow.ui.label_4.setText( "<html><head/><body><p align=\"center\"> " + points + "<br/></p></body></html>")
				for nr in range(len(self.currQuestion.answers)):
					self.currWindow.ui.checkBoxes[nr].setEnabled(True)
				
		
		if self.questionType[self.questionNumber] == 'pictureQuestion':
			self.currWindow.ui.label.setText("<html><head/><body><p align =\"center\"><img src=\"" + self.currQuestion.picPath +"\"/></p><p align=\"center\">" + self.currQuestion.title+"</p></body></html>")
			for nr in range(len(self.currQuestion.answers)):
				self.currWindow.ui.buttonArray[nr].setVisible(True)
				self.currWindow.ui.buttonArray[nr].setText(self.currQuestion.answers[nr])
				self.currWindow.ui.buttonArray[nr].clicked.disconnect()
				self.currWindow.ui.buttonArray[nr].clicked.connect(self.scorePenaltyQuiz)
			rightAnswer = self.currQuestion.rightAnswer
			self.currWindow.ui.buttonArray[self.currQuestion.rightAnswerIndex].clicked.connect(self.scoreBonusQuiz)
				
			if self.frameQuestionAnswered[self.questionNumber]:
				for nr in range(len(self.currQuestion.answers)):
					self.currWindow.ui.buttonArray[nr].setEnabled(False)
				self.currWindow.ui.buttonArray[self.currQuestion.rightAnswerIndex].setStyleSheet(u"color:rgb(0, 184, 0)")
				tempFont = self.currWindow.ui.buttonArray[self.currQuestion.rightAnswerIndex].font()
				tempFont.setBold(True)
				self.currWindow.ui.buttonArray[self.currQuestion.rightAnswerIndex].setFont(tempFont)
				
				
				if self.answers[self.questionNumber] == rightAnswer:
					self.currWindow.ui.label_2.setText( "<html><head/><body><p align=\"center\"> " + self.translator[self.language][27] + "<br/></p></body></html>")
					self.currWindow.ui.label_3.setText('')
					self.currWindow.ui.label_4.setText( "<html><head/><body><p align=\"center\"> " + points + "<br/></p></body></html>")
				else:
					rightAnswer = self.translator[self.language][25] +' '+ rightAnswer +' '+ self.translator[self.language][26]
					self.currWindow.ui.label_2.setText( "<html><head/><body><p align=\"center\"> " + self.translator[self.language][23] + "<br/></p></body></html>")
					self.currWindow.ui.label_3.setText( "<html><head/><body><p align=\"center\"> " + rightAnswer + "<br/></p></body></html>")
					self.currWindow.ui.label_4.setText( "<html><head/><body><p align=\"center\"> " + points + "<br/></p></body></html>")						
					
					for nr in range(len(self.currQuestion.answers)):
						if self.currQuestion.answers[nr] == self.answers[self.questionNumber]:
							wrongButton = self.currWindow.ui.buttonArray[nr]
					wrongButton.setStyleSheet(u"color:rgb(255, 0, 0)")
					tempFont = wrongButton.font()
					tempFont.setBold(True)
					wrongButton.setFont(tempFont)
			else:
				self.currWindow.ui.label_2.setText("")
				self.currWindow.ui.label_3.setText("")
				self.currWindow.ui.label_4.setText( "<html><head/><body><p align=\"center\"> " + points + "<br/></p></body></html>")
				for nr in range(len(self.currQuestion.answers)):
					self.currWindow.ui.buttonArray[nr].setEnabled(True)
					
					
		if self.questionType[self.questionNumber] == 'stringQuestion':
			self.currWindow.ui.label.setText("<html><head/><body><p align =\"center\">" + self.currQuestion.title +"</p></body></html>")
			for nr in range(len(self.currQuestion.answers)):
				self.currWindow.ui.buttonArray[nr].setVisible(True)
				self.currWindow.ui.buttonArray[nr].setEnabled(False)
				self.currWindow.ui.buttonArray[nr].setText(self.currQuestion.answers[nr])
				self.currWindow.ui.buttonArray[nr].clicked.disconnect()
				self.currWindow.ui.buttonArray[nr].clicked.connect(self.scorePenaltyQuiz)
			self.currWindow.ui.buttonArray[self.currQuestion.rightAnswerIndex].clicked.connect(self.scoreBonusQuiz)
			rightAnswer = self.currWindow.ui.buttonArray[self.currQuestion.rightAnswerIndex].text()
			
			if self.frameQuestionAnswered[self.questionNumber]:
				self.currWindow.ui.buttonArray[self.currQuestion.rightAnswerIndex].setStyleSheet(u"color:rgb(0, 184, 0)")
				tempFont = self.currWindow.ui.buttonArray[self.currQuestion.rightAnswerIndex].font()
				tempFont.setBold(True)
				self.currWindow.ui.buttonArray[self.currQuestion.rightAnswerIndex].setFont(tempFont)
				if self.answers[self.questionNumber] == rightAnswer:
					self.currWindow.ui.label_2.setText( "<html><head/><body><p align=\"center\"> " + self.translator[self.language][27] + "<br/></p></body></html>")
					self.currWindow.ui.label_3.setText('')
					self.currWindow.ui.label_4.setText( "<html><head/><body><p align=\"center\"> " + points + "<br/></p></body></html>")
				else:
					rightAnswer = self.translator[self.language][25] +' '+ rightAnswer +' '+ self.translator[self.language][26]
					self.currWindow.ui.label_2.setText( "<html><head/><body><p align=\"center\"> " + self.translator[self.language][23] + "<br/></p></body></html>")
					self.currWindow.ui.label_3.setText( "<html><head/><body><p align=\"center\"> " + rightAnswer + "<br/></p></body></html>")
					self.currWindow.ui.label_4.setText( "<html><head/><body><p align=\"center\"> " + points + "<br/></p></body></html>")						
					for nr in range(len(self.currQuestion.answers)):
						if self.currQuestion.answers[nr] == self.answers[self.questionNumber]:
							wrongButton = self.currWindow.ui.buttonArray[nr]	
					wrongButton.setStyleSheet(u"color:rgb(255, 0, 0)")	
					tempFont = wrongButton.font()
					tempFont.setBold(True)
					wrongButton.setFont(tempFont)
			else:
				self.currWindow.ui.label_2.setText("")
				self.currWindow.ui.label_3.setText("")
				self.currWindow.ui.label_4.setText( "<html><head/><body><p align=\"center\"> " + points + "<br/></p></body></html>")
				for nr in range(len(self.currQuestion.answers)):
					self.currWindow.ui.buttonArray[nr].setEnabled(True)
		
		
		if self.questionType[self.questionNumber] == 'missingWord':
			self.currWindow.ui.labelGap.setText(self.currQuestion.title)
			self.currWindow.ui.labelGap.setVisible(True)
			self.currWindow.ui.stackedWidget_2.setCurrentWidget(self.currWindow.ui.page_4)
			self.currWindow.ui.pushButton_13.setVisible(True)
			self.currWindow.ui.pushButton_13.clicked.disconnect()
			self.currWindow.ui.pushButton_13.clicked.connect(self.evaluateGapsTraining)
			
			for nr in range(len(self.currQuestion.answers)):
				self.currWindow.ui.editGaps[nr].setVisible(True)
				self.currWindow.ui.editLabels[nr].setVisible(True)
				self.currWindow.ui.editGaps[nr].setText(self.answers[self.questionNumber][nr])
				
			if self.frameQuestionAnswered[self.questionNumber]:			
				self.currWindow.ui.pushButton_13.setEnabled(False)
				allCorrect = True
				for nr in range(len(self.currQuestion.answers)):
					if self.currWindow.ui.editGaps[nr].text().strip().lower() == self.currQuestion.answers[nr].strip().lower():
						tempFont = self.currWindow.ui.editGaps[nr].font()
						tempFont.setBold(True)
						self.currWindow.ui.editGaps[nr].setFont(tempFont)
						self.currWindow.ui.editGaps[nr].setStyleSheet(u"color:rgb(0, 184, 0)")	
					else:
						allCorrect = False
						tempFont = self.currWindow.ui.editGaps[nr].font()
						tempFont.setBold(True)
						self.currWindow.ui.editGaps[nr].setFont(tempFont)
						self.currWindow.ui.editGaps[nr].setStyleSheet(u"color:rgb(255, 0, 0)")	
						self.currWindow.ui.editGaps[nr].setToolTip(self.currQuestion.answers[nr])
						
						self.currWindow.ui.label_3.setText("<html><head/><body><p align=\"center\"> " + self.translator[self.language][78] + "<br/></p></body></html>")
				self.currWindow.ui.label_4.setText( "<html><head/><body><p align=\"center\"> " + points + "<br/></p></body></html>")
				if allCorrect:
					self.currWindow.ui.label_2.setText( "<html><head/><body><p align=\"center\"> " + self.translator[self.language][27] + "<br/></p></body></html>")
				else:
					self.currWindow.ui.label_2.setText( "<html><head/><body><p align=\"center\"> " + self.translator[self.language][23] + "<br/></p></body></html>")
			else:
				self.currWindow.ui.pushButton_13.setEnabled(True)
				self.currWindow.ui.label_2.setText("")
				self.currWindow.ui.label_3.setText("")
				self.currWindow.ui.label_4.setText( "<html><head/><body><p align=\"center\"> " + points + "<br/></p></body></html>")
					
					
		if self.questionType[self.questionNumber] == 'matching':
			self.currWindow.ui.label.setText("<html><head/><body><p align=\"center\">" + self.currQuestion.title +"</p></body></html>")
			self.currWindow.ui.pushButton_13.clicked.disconnect()
			self.currWindow.ui.pushButton_13.clicked.connect(self.evaluateMatchingTraining)
			self.currWindow.ui.pushButton_13.setVisible(True)
			
			for i in range(len(self.currQuestion.answers)):
				self.currWindow.ui.matchingLabels[i].setText(self.currQuestion.answers[i])
				self.currWindow.ui.matchingLabels[i].setVisible(True)
				self.currWindow.ui.matchingButtons[i].setVisible(True)

			for i in range(len(self.rightListShuffeld[self.questionNumber])):
				self.currWindow.ui.matchingLabels[((i) * 2)+1].setText(self.rightListShuffeld[self.questionNumber][i])
				self.currWindow.ui.matchingButtons[(i)*2].setObjectName(self.currQuestion.answers[2*i])
				self.currWindow.ui.matchingButtons[((i)*2)+1].setObjectName(self.rightListShuffeld[self.questionNumber][i])

			if self.frameQuestionAnswered[self.questionNumber]:
				self.updateMatchingLines()
				self.currWindow.ui.pushButton_13.setEnabled(False)
							
			else:
				self.currWindow.ui.pushButton_13.setEnabled(True)
				self.currWindow.ui.label_2.setText("")
				self.currWindow.ui.label_3.setText("")
				self.currWindow.ui.label_4.setText( "<html><head/><body><p align=\"center\"> " + points + "<br/></p></body></html>")
				
		self.drawMatchingLines(self.questionNumber)
	
	def instantiateQuestionTraining(self):
	
		self.currWindow.ui.label_2.setText('')
		self.currWindow.ui.label_3.setText('')

		self.currWindow.ui.pushButton_13.setVisible(False)
		if not self.questionNumber == 0:
			self.currWindow.ui.pushButton_14.setVisible(True)					
		
		self.currWindow.ui.stackedWidget_2.setCurrentWidget(self.currWindow.ui.page_3)
		
		for i in self.currWindow.ui.buttonArray:
			i.setVisible(False)
			i.setEnabled(True)
			i.setText('')
			i.setStyleSheet("")
			tempFont = i.font()
			tempFont.setBold(False)
			i.setFont(tempFont)
			
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
			i.setEnabled(True)
			i.setText('')
			i.setStyleSheet("")
		
		for i in self.currWindow.ui.editLabels:
			i.setVisible(False)
		
		for i in self.currWindow.ui.editGaps:
			i.setVisible(False)
			i.setText('')
			i.setToolTip('')
			i.setStyleSheet('')
			tempFont = i.font()
			tempFont.setBold(False)
			i.setFont(tempFont)
			
			
		if self.questionType[self.questionNumber] == 'multipleChoice':
			self.currWindow.ui.label.setText("<html><head/><body><p align=\"center\">" + self.currQuestion.title +"</p></body></html>")
			self.currWindow.ui.pushButton_13.setVisible(True)
			self.currWindow.ui.pushButton_13.setEnabled(True)
			self.currWindow.ui.pushButton_13.clicked.disconnect()
			self.currWindow.ui.pushButton_13.clicked.connect(self.evaluateCheckBoxesTraining)
				
			for nr in range(len(self.currQuestion.answers)):
				self.currWindow.ui.checkBoxes[nr].setText(self.currQuestion.answers[nr])
				self.currWindow.ui.checkBoxes[nr].setObjectName(str(self.currQuestion.percentages[nr]))
				self.currWindow.ui.checkBoxes[nr].setVisible(True)
			
						
		if self.questionType[self.questionNumber] == 'pictureQuestion':
			for nr in range(len(self.currQuestion.answers)):
				self.currWindow.ui.buttonArray[nr].setText(self.currQuestion.answers[nr])
				self.currWindow.ui.buttonArray[nr].setVisible(True)
				self.currWindow.ui.buttonArray[nr].clicked.disconnect()
				self.currWindow.ui.buttonArray[nr].clicked.connect(self.scorePenaltyQuiz)	
				
			self.currWindow.ui.label.setText("<html><head/><body><p align=\"center\"><img src=\""+self.currQuestion.picPath +"\"/></p><p align=\"center\">" + self.currQuestion.title +"</p></body></html>")
			self.currWindow.ui.buttonArray[self.currQuestion.rightAnswerIndex].clicked.disconnect()
			self.currWindow.ui.buttonArray[self.currQuestion.rightAnswerIndex].clicked.connect(self.scoreBonusQuiz)
				
			
		if self.questionType[self.questionNumber] == 'stringQuestion':
			self.currWindow.ui.label.setText("<html><head/><body><p align=\"center\">" + self.currQuestion.title +"</p></body></html>")
			for nr in range(len(self.currQuestion.answers)):
				self.currWindow.ui.buttonArray[nr].setText(self.currQuestion.answers[nr])
				self.currWindow.ui.buttonArray[nr].setVisible(True)
				self.currWindow.ui.buttonArray[nr].clicked.disconnect()
				self.currWindow.ui.buttonArray[nr].clicked.connect(self.scorePenaltyQuiz)	
			self.currWindow.ui.buttonArray[self.currQuestion.rightAnswerIndex].clicked.disconnect()
			self.currWindow.ui.buttonArray[self.currQuestion.rightAnswerIndex].clicked.connect(self.scoreBonusQuiz)
			
		
		if self.questionType[self.questionNumber] == 'missingWord':
			self.currWindow.ui.labelGap.setText(self.currQuestion.title)
			self.currWindow.ui.labelGap.setVisible(True)
			self.currWindow.ui.stackedWidget_2.setCurrentWidget(self.currWindow.ui.page_4)
			self.currWindow.ui.pushButton_13.setVisible(True)
			self.currWindow.ui.pushButton_13.setEnabled(True)
			self.currWindow.ui.pushButton_13.clicked.disconnect()
			self.currWindow.ui.pushButton_13.clicked.connect(self.evaluateGapsTraining)
			
			for nr in range(len(self.currQuestion.answers)):
				self.currWindow.ui.editGaps[nr].setVisible(True)
				self.currWindow.ui.editLabels[nr].setVisible(True)
			
			if not self.answers[self.questionNumber] == '':			
				for i in range(len (self.currQuestion.answers)):
					self.currWindow.ui.editGaps[i].setText(self.answers[self.questionNumber][i])
			else:
				self.answers[self.questionNumber] = []
				for i in range(len (self.currQuestion.answers)):
					self.answers[self.questionNumber].append('')
					
					
		if self.questionType[self.questionNumber] == 'matching':
			self.currWindow.ui.label.setText("<html><head/><body><p align=\"center\">" + self.currQuestion.title +"</p></body></html>")
			rightListShuffeldTemp = []
			self.currWindow.ui.pushButton_13.setVisible(True)
			self.currWindow.ui.pushButton_13.setEnabled(True)
			self.currWindow.ui.pushButton_13.clicked.disconnect()
			self.currWindow.ui.pushButton_13.clicked.connect(self.evaluateMatchingTraining)
				
			for i in range(len(self.currQuestion.answers)):
				self.currWindow.ui.matchingLabels[i].setText(self.currQuestion.answers[i])
				self.currWindow.ui.matchingLabels[i].setVisible(True)
				self.currWindow.ui.matchingButtons[i].setVisible(True)
				
				if not self.siteVisitedMatching[self.questionNumber]:
					if i % 2 == 1:
						rightListShuffeldTemp.append(self.currQuestion.answers[i])
						self.linesForMatching[self.questionNumber].append([])
						self.lines[self.questionNumber].append([])
					
			random.shuffle(rightListShuffeldTemp)
			
			if not self.siteVisitedMatching[self.questionNumber]:
				self.rightListShuffeld[self.questionNumber] = rightListShuffeldTemp
			for i in range(len(self.rightListShuffeld[self.questionNumber])):
				if not self.siteVisitedMatching[self.questionNumber]:
					self.linesForMatching[self.questionNumber][i] = []
				self.currWindow.ui.matchingLabels[((i) * 2)+1].setText(self.rightListShuffeld[self.questionNumber][i])
				self.currWindow.ui.matchingButtons[(i)*2].setObjectName(self.currQuestion.answers[i * 2])
				self.currWindow.ui.matchingButtons[((i)*2)+1].setObjectName(self.rightListShuffeld[self.questionNumber][i])
			
			self.drawMatchingLines(self.questionNumber)
			self.siteVisitedMatching[self.questionNumber] = True
				
	def scoreBonusQuiz(self):

		self.questionsAnswered += 1
		self.Score += 1
		button = self.currWindow.sender()
		self.answers[self.questionNumber]=button.text()
		self.currWindow.ui.label_6.setText(self.translator[self.language][77] + ' '+ str(self.questionsAnswered)+' ' + self.translator[self.language][30] + ' ' + str(len(self.questions)))
		self.quizRefresh(True, '')
	
	def scorePenaltyQuiz(self):
		
		self.questionsAnswered += 1
		penalty = 0
		if self.Score - penalty >= 0:
			self.Score -= penalty
		else:
			self.Score = 0
		button = self.currWindow.sender()
		answerGiven = button.text()
		self.answers[self.questionNumber]=answerGiven
		self.currWindow.ui.label_6.setText(self.translator[self.language][77] + ' '+ str(self.questionsAnswered)+' ' + self.translator[self.language][30] + ' ' + str(len(self.questions)))
		self.quizRefresh(False, answerGiven)					
	
	def evaluateMatchingTraining(self):

		self.questionsAnswered += 1
		self.currWindow.ui.label_6.setText(self.translator[self.language][77] + ' '+ str(self.questionsAnswered)+' ' + self.translator[self.language][30] + ' ' + str(len(self.questions)))
		self.frameQuestionAnswered[self.questionNumber] = True
		
		self.updateMatchingLines()
		
		allCorrectlyAnswered = True
		for i in range(len(self.linesForMatching[self.questionNumber])):
			if len(self.linesForMatching[self.questionNumber][i]) < 3 or not (self.linesForMatching[self.questionNumber][i][2] == 1):
				allCorrectlyAnswered = False
		
		if allCorrectlyAnswered:
			self.Score += 1
		if self.Score == 1:
			points = self.translator[self.language][18] + ' '+str(self.Score) +' '+ self.translator[self.language][19] +' '+ str(len(self.questions))+ ' ' + self.translator[self.language][79]
		else:
			points = self.translator[self.language][20] +' '+ str(self.Score) +' '+ self.translator[self.language][21] +' '+ str(len(self.questions))+ ' ' + self.translator[self.language][79]
		self.currWindow.ui.label_4.setText( "<html><head/><body><p align=\"center\"> " + points + "<br/></p></body></html>")
	
	def evaluateGapsTraining(self):
		
		self.questionsAnswered += 1
		self.currWindow.ui.label_6.setText(self.translator[self.language][77] + ' '+ str(self.questionsAnswered)+' ' + self.translator[self.language][30] + ' ' + str(len(self.questions)))
		self.frameQuestionAnswered[self.questionNumber] = True
		
		allCorrectlyAnswered = True
		
		for nr in range(len(self.currQuestion.answers)):
			if self.currWindow.ui.editGaps[nr].text().strip().lower() == self.currQuestion.answers[nr].strip().lower() :
				self.currWindow.ui.editGaps[nr].setStyleSheet(u"color:rgb(0, 184, 0)")
				tempFont = self.currWindow.ui.editGaps[nr].font()
				tempFont.setBold(True)
				self.currWindow.ui.editGaps[nr].setFont(tempFont)
			else:
				allCorrectlyAnswered = False
				self.currWindow.ui.editGaps[nr].setToolTip(self.currQuestion.answers[nr])
				self.currWindow.ui.editGaps[nr].setStyleSheet(u"color:rgb(255, 0, 0)")
				tempFont = self.currWindow.ui.editGaps[nr].font()
				tempFont.setBold(True)
				self.currWindow.ui.editGaps[nr].setFont(tempFont)

		if allCorrectlyAnswered:
			self.Score += 1
			self.currWindow.ui.label_2.setText( "<html><head/><body><p align=\"center\"> " + self.translator[self.language][22] +  "<br/></p></body></html>")
		else:
			self.currWindow.ui.label_2.setText("<html><head/><body><p align=\"center\"> " + self.translator[self.language][23] + "<br/></p></body></html>")
			self.currWindow.ui.label_3.setText("<html><head/><body><p align=\"center\"> " + self.translator[self.language][78] + "<br/></p></body></html>")
		self.roundScore()
		
		if self.Score == 1:
			points = self.translator[self.language][18] + ' '+str(self.Score) +' '+ self.translator[self.language][19] +' '+ str(len(self.questions))+ ' ' + self.translator[self.language][79]
		else:
			points = self.translator[self.language][20] +' '+ str(self.Score) +' '+ self.translator[self.language][21] +' '+ str(len(self.questions))+ ' ' + self.translator[self.language][79]
		
		self.currWindow.ui.label_4.setText( "<html><head/><body><p align=\"center\"> " + points + "<br/></p></body></html>")
		self.currWindow.ui.pushButton_13.setEnabled(False)
		
	def updateMatchingLines(self):

		allCorrectlyAnswered = True

		for i in range(len(self.linesForMatching[self.questionNumber])):
			self.currWindow.ui.matchingButtons[i * 2].setEnabled(False)
			self.currWindow.ui.matchingButtons[(i * 2) + 1].setEnabled(False)
			
			if len(self.linesForMatching[self.questionNumber][i]) == 3:
				for k in self.currWindow.ui.matchingLabels:
					if k.text() == self.linesForMatching[self.questionNumber][i][1]:
						rightLabel = k
			
			if len(self.linesForMatching[self.questionNumber][i]) < 3 or not (self.linesForMatching[self.questionNumber][i][2] == 1):
				allCorrectlyAnswered = False
				self.currWindow.ui.matchingLabels[i * 2].setStyleSheet(u"color:rgb(255, 0, 0)")
				tempFont = self.currWindow.ui.matchingLabels[i * 2].font()
				tempFont.setBold(True)
				self.currWindow.ui.matchingLabels[i * 2].setFont(tempFont)
			else: 
				self.currWindow.ui.matchingLabels[i * 2].setStyleSheet(u"color:rgb(0, 184, 0)")
				rightLabel.setStyleSheet(u"color:rgb(0, 184, 0)")
				tempFont = self.currWindow.ui.matchingLabels[i * 2].font()
				tempFont.setBold(True)
				self.currWindow.ui.matchingLabels[i * 2].setFont(tempFont)
				tempFont = rightLabel.font()
				tempFont.setBold(True)
				rightLabel.setFont(tempFont)
		
		for i in range(0, len(self.linesForMatching[self.questionNumber])):
			if self.currWindow.ui.matchingLabels[(i * 2)+ 1].styleSheet() == '':
				self.currWindow.ui.matchingLabels[(i * 2)+ 1].setStyleSheet(u"color:rgb(255, 0, 0)")
				tempFont = self.currWindow.ui.matchingLabels[(i * 2)+ 1].font()
				tempFont.setBold(True)
				self.currWindow.ui.matchingLabels[(i * 2)+ 1].setFont(tempFont)
		
		if allCorrectlyAnswered:
			self.currWindow.ui.label_2.setText( "<html><head/><body><p align=\"center\"> " + self.translator[self.language][22] +  "<br/></p></body></html>")
		else:
			self.currWindow.ui.label_2.setText("<html><head/><body><p align=\"center\"> " + self.translator[self.language][23] + "<br/></p></body></html>")
		
		self.roundScore()
		if self.Score == 1:
			points = self.translator[self.language][18] + ' '+str(self.Score) +' '+ self.translator[self.language][19] +' '+ str(len(self.questions))+ ' ' + self.translator[self.language][79]
		else:
			points = self.translator[self.language][20] +' '+ str(self.Score) +' '+ self.translator[self.language][21] +' '+ str(len(self.questions))+ ' ' + self.translator[self.language][79]
		
		self.currWindow.ui.label_4.setText( "<html><head/><body><p align=\"center\"> " + points + "<br/></p></body></html>")
		self.currWindow.ui.pushButton_13.setEnabled(False)
		
		self.drawMatchingLines(self.questionNumber)
		
	def evaluateCheckBoxesTraining(self):

		self.questionsAnswered += 1
		self.currWindow.ui.label_6.setText(self.translator[self.language][77] + ' '+ str(self.questionsAnswered)+' ' + self.translator[self.language][30] + ' ' + str(len(self.questions)))
		self.frameQuestionAnswered[self.questionNumber] = True
		tempScore = 0
		allCorrectlyAnswered = True
		for i in self.currWindow.ui.checkBoxes:
			i.setEnabled(False)
			if i.isChecked():
				self.answers[self.questionNumber] +=(' ')
				self.answers[self.questionNumber] +=(i.text())
				tempScore += float(i.objectName())	
				if i.objectName()[0] == '-':
					allCorrectlyAnswered = False
					i.setStyleSheet(u"color:rgb(255, 0, 0)")
					tempFont = i.font()
					tempFont.setBold(True)
					i.setFont(tempFont)
				else:
					i.setStyleSheet(u"color:rgb(0, 184, 0)")	
					tempFont = i.font()
					tempFont.setBold(True)
					i.setFont(tempFont)
			else:
				if i.objectName()[0] != '-' and i.objectName() != ' ':
					allCorrectlyAnswered = False
					i.setStyleSheet(u"color:rgb(255, 0, 0)")
					tempFont = i.font()
					tempFont.setBold(True)
					i.setFont(tempFont)
		
		if tempScore < 0:
			tempScore = 0
		
		tempScore = tempScore / 100.0
		self.Score += tempScore
		self.roundScore()

		if self.Score == 1:
			points = self.translator[self.language][18] +' '+ str(self.Score) +' '+ self.translator[self.language][19] +' '+ str(len(self.questions))+ ' ' + self.translator[self.language][79]
		else:
			points = self.translator[self.language][20] +' '+ str(self.Score) +' '+ self.translator[self.language][21] +' '+ str(len(self.questions))+ ' ' + self.translator[self.language][79]
		
		if allCorrectlyAnswered:
			self.currWindow.ui.label_2.setText( "<html><head/><body><p align=\"center\"> " + self.translator[self.language][22] +  "<br/></p></body></html>")
		else:
			self.currWindow.ui.label_2.setText("<html><head/><body><p align=\"center\"> " + self.translator[self.language][23] + "<br/></p></body></html>")
			
		self.currWindow.ui.label_4.setText( "<html><head/><body><p align=\"center\"> " + points + "<br/></p></body></html>")
		self.currWindow.ui.pushButton_13.setEnabled(False)
	
	def updateCheckBoxesTraining(self):
		
		allCorrectlyAnswered = True
		
		for i in self.currWindow.ui.checkBoxes:
			i.setEnabled(False)
			if i.isChecked():
				if i.objectName()[0] == '-':
					allCorrectlyAnswered = False
					i.setStyleSheet(u"color:rgb(255, 0, 0)")
					tempFont = i.font()
					tempFont.setBold(True)
					i.setFont(tempFont)
				else:
					i.setStyleSheet(u"color:rgb(0, 184, 0)")
					tempFont = i.font()
					tempFont.setBold(True)
					i.setFont(tempFont)
			else:
				if i.objectName()[0] != '-' and i.objectName() != ' ':
					allCorrectlyAnswered = False
					i.setStyleSheet(u"color:rgb(255, 0, 0)")
					tempFont = i.font()
					tempFont.setBold(True)
					i.setFont(tempFont)

		self.roundScore()

		if self.Score == 1:
			points = self.translator[self.language][18] +' '+ str(self.Score) +' '+ self.translator[self.language][19] +' '+ str(len(self.questions))+ ' ' + self.translator[self.language][79]
		else:
			points = self.translator[self.language][20] +' '+ str(self.Score) +' '+ self.translator[self.language][21] +' '+ str(len(self.questions))+ ' ' + self.translator[self.language][79]
		
		if allCorrectlyAnswered:
			self.currWindow.ui.label_2.setText( "<html><head/><body><p align=\"center\"> " + self.translator[self.language][22] +  "<br/></p></body></html>")
		else:
			self.currWindow.ui.label_2.setText("<html><head/><body><p align=\"center\"> " + self.translator[self.language][23] + "<br/></p></body></html>")
			
		self.currWindow.ui.label_4.setText( "<html><head/><body><p align=\"center\"> " + points + "<br/></p></body></html>")
	
	def roundScore (self):

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
		for i in range(len(self.questionType)):
			if self.questionType[i] == 'matching':
				allMatchingCorrect = True
				for currLine in self.linesForMatching[i]:
					if len(currLine) < 3  or not(currLine[2]  == 1):
						allMatchingCorrect = False
				if allMatchingCorrect:
					self.Score += 1
	
	def evaluateGaps(self):
		
		allGapsCorrect = True
		for i in range(len(self.questionType)):
			if self.questionType[i] == 'missingWord':
				allGapsCorrect = True
				for nr in range (len(self.answers[i])):
					if not self.answers[i][nr].strip().lower() == self.questions[i].answers[nr].strip().lower():
						allGapsCorrect = False
				if allGapsCorrect:
					self.Score += 1
					
	def showScore(self):
		
		import time
		
		self.roundScore()
		self.dlg2 = PointsDialog()
		self.dlg2.setWindowTitle(self.translator[self.language][7])
		self.dlg2.ui.pushButton.clicked.connect(self.dlg2.close)
		percentage = int((self.Score / len(self.questions))*100)
		date = time.strftime("%d/%m/%Y")
		end = time.time()
		self.timeElapsed = end - self.timeElapsed 
		self.log = open(self.user_plugin_dir + '/quiz.csv', 'a')
		logString = '' 
		logString = date + self.path.split('/')[len(self.path.split('/'))-1]
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
		
		if percentage > 90.0:
			evaluation = self.translator[self.language][70]
		elif percentage > 80.0:
			evaluation = self.translator[self.language][71]
		elif percentage > 70.0:
			evaluation = self.translator[self.language][72]
		else:
			evaluation = self.translator[self.language][73]
		
		self.dlg2.ui.label.setFont(self.globalFont)
		self.dlg2.ui.label.setText( "<html><head/><body><p align=\"center\"> " + self.translator[self.language][64]+ ' ' + str(self.Score) + ' ' + self.translator[self.language][21]+ str(len(self.questions))+ "<br/><br/>"+ self.translator[self.language][65] + str(percentage) +'% !' +'  ' + evaluation + "</p></body></html>")
		self.dlg2.exec_()
		
	def showNormalResults(self):
		
		if self.currWindow.close():
			self.evaluateLines()
			self.evaluateGaps()
			self.showScore()
		
	def showQuizResults(self):
		
		if self.currWindow.close():
			self.showScore()
	

class Painter(PyQt4.QtGui.QWidget):
	

	def __init__(self, parent, lines):
		
		self.parent = parent
		self.lines = lines
		self.xOffset = 0
		self.yOffset = 0
		self.questionNumber = 0
		super(Painter, self).__init__()
		
	def update(self, questionNumber):
		
		self.repaint()
		self.questionNumber = questionNumber
	
	def paintEvent(self, event):
		
		painter = PyQt4.QtGui.QPainter(self)
		painter.setRenderHint(QPainter.Antialiasing)
		painter.begin(self)
		self.drawLines(event, painter)
		painter.end()
		
	def drawLines(self, event, painter):
		
		pen = PyQt4.QtGui.QPen(PyQt4.QtCore.Qt.blue, 2, PyQt4.QtCore.Qt.SolidLine)
		painter.setPen(pen)
		
		self.xOffset = self.parentWidget().mapTo(self.parentWidget().parentWidget(), QPoint(0,0)).x()
		self.yOffset = self.parentWidget().mapTo(self.parentWidget().parentWidget(), QPoint(0,0)).y()
	
		i = self.lines[self.questionNumber]

		for line in i:
			if not line == [] :
				painter.drawLine(line[0].mapTo(self.parentWidget().parentWidget(),QPoint(line[0].width(),line[0].height()/2)).x()-self.xOffset, line[0].mapTo(self.parentWidget().parentWidget(),QPoint(line[0].width(),line[0].height()/2)).y()-self.yOffset, line[1].mapTo(self.parentWidget().parentWidget(),QPoint(0,line[1].height()/2)).x()-self.xOffset, line[1].mapTo(self.parentWidget().parentWidget(),QPoint(0,line[1].height()/2)).y()-self.yOffset)
