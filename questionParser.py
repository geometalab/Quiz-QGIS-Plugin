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
from QuestionClass import *


class QuestionParser:

    def __init__(self, path):
        import codecs
        self.dirty = False
        self.failedBlocks = []
        self.path = path
        with codecs.open(self.path, 'r', 'utf-8') as f:
            allQuests = []
            self.questionType = []
            input = f.read()
            if '\r\n\r\n' in input:
                allQuestions = input.split('\r\n\r\n')
            else:
                allQuestions = input.split('\n\n')
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
                                for i in currQuestion.answers:
                                    for k in currQuestion.answers:
                                        if k == i:
                                            self.failedBlocks.append(
                                                str(index + 1))
                                            pass
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
                                self.quizTitle = line[8:]
                            if "//Instruction" in line:
                                self.instruction = line[14:]
                except:
                    self.dirty = True
                    self.failedBlocks.append(str(index + 1))
        self.allQuestions = allQuests

    def makePictureQuestion(self, answers):
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
        tempTuples = question.split('::')[2].strip()
        tempTuples = tempTuples.split('{')
        self.textArray.append(tempTuples[0].strip())
        for tuple in tempTuples[1:]:
            tuple = tuple.split('}')
            self.answersArray.append(
                tuple[0].split('=')[1].split(
                    '~')[0].strip())
            if len(tuple) > 1:
                self.textArray.append(tuple[1].strip())
        self.questionType.append('missingWord')
        return MissingWordQuestion(
            '',
            self.answersArray,
            self.boolArray,
            self.textArray
            )

    def makeStringQuestion(self, answers):
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

    def isDirty(self):
        return self.dirty
