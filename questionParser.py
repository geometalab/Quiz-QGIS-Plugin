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
import traceback
from questionClass import (
    PicQuestion,
    MissingWordQuestion,
    Question,
    MultipleChoiceQuestion,
    MatchingQuestion
    )


class QuestionParser(object):
    '''
    Class handling the parsing of quizzes
    '''
    def __init__(self, path):
        '''
        Instantiation with parsing
        '''
        import codecs
        self.dirty = False
        self.failedBlocks = []
        self.path = path
        with codecs.open(self.path, 'r', 'utf-8') as f:
            allQuests = []
            self.questionType = []
            lines = []
            for index, line in enumerate(f):
                if line.strip() == '':
                    line = line.replace('\t', '')
                    line = line.replace(' ', '')
                lines.append(line)
            input_text = ''.join(lines)
            if '\r\n\r\n' in input_text:
                allQuestions = input_text.split('\r\n\r\n')
            else:
                allQuestions = input_text.split('\n\n')
            self.instruction = ''
            self.quizTitle = ''
            for index, question in enumerate(allQuestions):
                try:
                    self.answersArray = []
                    self.boolArray = []
                    self.percentages = []
                    self.textArray = []
                    self.title = ''
                    if question.count('{') >= 1:
                        if question.count('}') == 1:
                            if '::' in question:
                                titleSplit = question.split('::')
                                titleAndAnswers = titleSplit[2].split('{')
                                self.title = titleAndAnswers[0]
                                self.answers = titleAndAnswers[1].split('}')[0]
                            else:
                                titleSplit = question.split('{')
                                self.title = titleSplit[0]
                                self.answers = titleSplit[1].split('}')[0]
                            if '//Picture-Question' in question:
                                currQuestion = self.makePictureQuestion(
                                    self.answers)
                            elif '->' in question:
                                currQuestion = self.makeMatchingQuestion(
                                    self.answers)
                                if len(currQuestion.answers) > 12:
                                    self.failedBlocks.append(
                                        str(index + 1) +
                                        ' Too many match-options')
                                for i in currQuestion.answers:
                                    for k in currQuestion.answers:
                                        if k == i:
                                            self.failedBlocks.append(
                                                str(index + 1))
                            elif '~%' in question:
                                currQuestion = self.makeMultipleChoiceQuestion(
                                    self.answers)
                            elif not '~' in question:
                                currQuestion = self.makeMissingWordQuestion(
                                    self.answers, question)
                            else:
                                currQuestion = self.makeStringQuestion(
                                    self.answers)
                        else:
                            currQuestion = self.makeMissingWordQuestion(
                                self.answers, question)
                        allQuests.append(currQuestion)
                    else:
                        for line in question.split('\r\n'):
                            if "//Title" in line:
                                self.quizTitle = line[9:]
                            if "//Instruction" in line:
                                self.instruction = line[14:]
                except:
                    traceback.print_exc()
                    self.dirty = True
                    self.failedBlocks.append(str(index + 1))
        self.allQuestions = allQuests

    def makePictureQuestion(self, answers):
        '''
        Generates a picture question
        '''
        correct = answers.split('=')
        leftHalf = correct[0].split('~')[1:]
        rightHalf = correct[1].split('~')
        for i in leftHalf:
            if i != '':
                self.boolArray.append(False)
                self.answersArray.append(i.strip())
        self.answersArray.append(rightHalf[0].strip())
        self.boolArray.append(True)
        if len(rightHalf) > 1:
            for i in rightHalf[1:]:
                if i != '':
                    self.boolArray.append(False)
                    self.answersArray.append(i.strip())
        self.questionType.append('pictureQuestion')
        return PicQuestion(
            self.title,
            self.answersArray,
            self.boolArray
            )

    def makeMissingWordQuestion(self, answers, question):
        '''
        Generates a fill-in-the-gap question
        '''
        tempTuples = question.split('::')[2].strip()
        tempTuples = tempTuples.split('{')
        self.textArray.append(tempTuples[0].strip())
        for currentTuple in tempTuples[1:]:
            currentTuple = currentTuple.split('}')
            self.answersArray.append(
                currentTuple[0].split('=')[1].split(
                    '~')[0].strip())
            if len(currentTuple) > 1:
                self.textArray.append(currentTuple[1].strip())
        self.questionType.append('missingWord')
        return MissingWordQuestion(
            '',
            self.answersArray,
            self.boolArray,
            self.textArray
            )

    def makeStringQuestion(self, answers):
        '''
        Generates a normal string question
        '''
        correct = answers.split('=')
        leftHalf = correct[0].split('~')[1:]
        rightHalf = correct[1].split('~')
        for i in leftHalf:
            if i != '':
                i = i.split('#')[0]
                self.boolArray.append(False)
                self.answersArray.append(i.strip())
        self.answersArray.append(
            rightHalf[0].split('#')[0].strip())
        self.boolArray.append(True)
        if len(rightHalf) > 1:
            for i in rightHalf[1:]:
                if i != '':
                    i = i.split('#')[0]
                    self.boolArray.append(False)
                    self.answersArray.append(i.strip())
        self.questionType.append('stringQuestion')
        return Question(
            self.title,
            self.answersArray,
            self.boolArray
            )

    def makeMultipleChoiceQuestion(self, answers):
        '''
        Generates a multiple choice question
        '''
        options = answers.split('~')
        for i in options[1:]:
            part = i.split('%')
            self.percentages.append(part[1])
            self.answersArray.append(part[2].strip())
        self.questionType.append('multipleChoice')
        return MultipleChoiceQuestion(
            self.title,
            self.answersArray,
            [],
            self.percentages
            )

    def makeMatchingQuestion(self, answers):
        '''
        Generatues a matching question
        '''
        pairs = answers.split('=')
        for i in pairs:
            if '->' in i:
                match = i.split('->')
                self.answersArray.append(match[0].strip())
                self.answersArray.append(match[1].strip())
        self.questionType.append('matching')
        return MatchingQuestion(
            self.title,
            self.answersArray,
            []
            )
