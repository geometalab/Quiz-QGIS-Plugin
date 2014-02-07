				
				
				
				
				
				for line in question.split('\r\n'):
					if "//Titel" in line:
						self.quizTitle = line[8:]
					if "//Anleitung" in line:
						self.instruction = line[12:]
					
					if line[0] == ':':
						titleSeperator = line.rsplit('::',1)
						
						if len(titleSeperator) == 2 and titleSeperator[1] != '':
							multipleWord = True
							title = titleSeperator[1]
					
					if '->' in line and multipleWord:
						self.questionType.append('matching')
						answersArray = []
						matchPairs = line.split('=')
						
						for i in range(0, len(matchPairs)):
							if '->' in matchPairs[i]:
								if '}' in matchPairs[i]:
									temp = matchPairs[i].split('}')
									matchPair = temp[0].split('->')
								else:
									matchPair = matchPairs[i].split('->')
								answersArray.append(matchPair[0])
								answersArray.append(matchPair[1].lstrip())
						self.currQuestion = MatchingQuestion(title, answersArray, [])
						allQuests.append(self.currQuestion)
						
					elif line[0] == '{' and multipleWord:
						tokens = line.split()
						if tokens[2][1] == '%':
							self.questionType.append('multipleChoice')
							percentages = []
							answersArray = []
							for i in range(0, len(tokens)):
						
								if tokens[i][0]=='~':
									percentage = tokens[i].split('%')
									percentages.append(percentage[1])
									answerString = ''
									answerString += percentage[2]

									k = 1
									while (tokens[i + k][0] != '=') and (tokens[i + k][0] != '~') and (tokens[i + k][0] != '}'):
										answerString += ' '
										answerString += tokens[i+k]
										k += 1
									answersArray.append(answerString)
							self.currQuestion = MultipleChoiceQuestion(title, answersArray, [], percentages)
							allQuests.append(self.currQuestion)
						else:
							self.questionType.append('stringQuestion')
							boolArray = []
							answersArray = []
							for i in range(0, len(tokens)):
								if tokens[i][0]== '=':
									boolArray.append(True)
									answerString = ''
									answerString += tokens[i][1:]
							
									k =1
									while ((tokens[i + k][0]) != '=') and (tokens[i + k][0]) != '~' and (tokens[i + k][0] != '}'):
										answerString += ' '
										answerString += tokens[i+k]
										k += 1
									answersArray.append(answerString)

								elif tokens[i][0]=='~':
									boolArray.append(False)
									answerString = ''
									answerString += tokens[i][1:]

									k = 1
									while (tokens[i + k][0] != '=') and (tokens[i + k][0] != '~') and (tokens[i + k][0] != '}'):
										answerString += ' '
										answerString += tokens[i+k]
										k += 1
									answersArray.append(answerString)
							self.currQuestion = Question(title, answersArray, boolArray)	
							allQuests.append(self.currQuestion)
					
					if line[0] != '{' and line[0] != ':' and line[0] != '/' and (not line.strip()==''):
						self.questionType.append('missingWord')
						firstQuestionPart = line.split('{')
						secondQuestionPart = firstQuestionPart[1].split('}')
						title = firstQuestionPart[0]  +' '+ '____________' +' '+ secondQuestionPart[1]
						tokens = secondQuestionPart[0].split()
						boolArray = []
						answersArray = []
						
						for i in range(0, len(tokens)):
						
							if tokens[i][0]== '=':
								boolArray.append(True)
								answerString = ''
								answerString += tokens[i][1:]
		
								k =1
								while ( ( (k+i) != len(tokens)-1)and(tokens[i + k][0]) != '=') and (tokens[i + k][0]) != '~' and (tokens[i + k][0] != '}'):
									answerString += ' '
									answerString += tokens[i+k]
									k += 1
								answersArray.append(answerString)

							elif tokens[i][0]=='~':
								boolArray.append(False)
								answerString = ''
								answerString += tokens[i][1:]

								k = 1
								while ( (k+i) != len(tokens) and tokens[i + k][0] != '=') and (tokens[i + k][0] != '~') and (tokens[i + k][0] != '}'):
									answerString += ' '
									answerString += tokens[i+k]
									k += 1
								
								answersArray.append(answerString)	
						
						self.currQuestion = Question(title, answersArray, boolArray)	
						allQuests.append(self.currQuestion)
					
					if '{pic' in line:
						self.questionType.append('pictureQuestion')
						tokens = line.split()
						answersArray = []
						boolArray = []
						for i in range(0, len(tokens)):
							
							if tokens[i][0:5] == '{pic?':
								questionString = ''
								questionString += tokens[i][5:]
								
								k =1
								while ((tokens[i + k][0]) != '=') and (tokens[i + k][0]) != '~' and (tokens[i + k][0] != '}'):
									questionString += ' '
									questionString += tokens[i+k]
									k += 1
								
								
							if tokens[i][0]== '=':
								boolArray.append(True)
								answerString = ''
								answerString += tokens[i][1:]
							
								k =1
								while ((tokens[i + k][0]) != '=') and (tokens[i + k][0]) != '~' and (tokens[i + k][0] != '}'):
									answerString += ' '
									answerString += tokens[i+k]
									k += 1
								answersArray.append(answerString)

							elif tokens[i][0]=='~':
								boolArray.append(False)
								answerString = ''
								answerString += tokens[i][1:]

								k = 1
								while (tokens[i + k][0] != '=') and (tokens[i + k][0] != '~') and (tokens[i + k][0] != '}'):
									answerString += ' '
									answerString += tokens[i+k]
									k += 1
								answersArray.append(answerString)
								
						title = questionString
						self.currQuestion = PicQuestion(title, answersArray, boolArray)	
						allQuests.append(self.currQuestion)
				