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
import os

class Question(object):
    '''
    Base class for all questiontypes
    '''
    def __init__(self, title=None, answersArray=None, boolArray=None):
        '''
        Instantiation
        '''
        self.title = title
        for i in range(len(boolArray)):
            if boolArray[i]:
                self.rightAnswer = answersArray[i]
                self.rightAnswerIndex = i
        self.answers = answersArray
        self.nrOfAnswers = len(self.answers)


class MatchingQuestion(Question):
    '''
    Class representing matching questions
    '''
    def __init__(self, titel=None, answersArray=None, boolArray=None):
        '''
        Instantiation
        '''
        Question.__init__(self, titel, answersArray, boolArray)
        self.answersIndexes = {}
        for i in range(len(answersArray)):
            self.answersIndexes[answersArray[i]] = i


class MultipleChoiceQuestion(Question):
    '''
    Class representing multiple choice questions
    '''
    def __init__(
            self,
            titel=None,
            answersArray=None,
            boolArray=None,
            percentages=None):
        '''Instantiation
        '''
        Question.__init__(self, titel, answersArray, boolArray)
        self.percentages = percentages
        self.answersChecked = []
        self.answersIndexes = {}
        for i in range(len(answersArray)):
            self.answersIndexes[self.percentages[i]] = i
            self.answersChecked.append('')


class PicQuestion(Question):
    '''
    Class representing picture question
    '''
    def __init__(self, titel=None, answersArray=None, boolArray=None):
        '''
        Instantiation
        '''
        Question.__init__(self, titel, answersArray, boolArray)
        self.picPath = os.path.dirname(__file__) + "/quizzes/images/" + self.rightAnswer + ".png"


class MissingWordQuestion(Question):
    '''
    Class representing missing word questions
    '''
    def __init__(
            self,
            titel=None,
            answersArray=None,
            boolArray=None,
            textArray=None):
        '''
        Instantiation
        '''
        Question.__init__(self, titel, answersArray, boolArray)
        self.textArray = textArray
        self.title = textArray[0]
        for i in range(1, len(textArray)):
            underscores = ''
            if len(answersArray[i-1]) < 4:
                underscores = '____'
            elif len(answersArray[i-1]) > 20:
                for q in range(20):
                    underscores += '_'
            else:
                for q in range(len(answersArray[i-1])):
                    underscores += '_'
            self.title += ' ' + underscores + '(' + str(i) + ') ' + textArray[i]
