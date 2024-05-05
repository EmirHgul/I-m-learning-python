# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 12:26:50 2023

@author: hatice
"""



#QUIZ UYGULAMASİ


class Questions:
    def __init__(self,text,choices,answer):
        self.text = text
        self.choices = choices
        self.answer = answer

    def checkAnswer(self, answer):
        return self.answer == answer 
        


# print(q1.checkAnswer("python"))  -> true


class Quiz:
    def __init__(self,questions):
        self.questions = questions
        self.score = 0
        self.questionIndex = 0

    def getQuestion(self):
        return self.questions[self.questionIndex]

    def displayQuestion(self):
        question = self.getQuestion()
        print(f'Soru {self.questionIndex + 1}: {question.text}')

        for q in question.choices:  #siklari bu kod blogu ile yazdirdik.
            print("-" + q)
            
        answer = input("cevap: ")       #cevap secenegini sunan kod blogu
        self.guess(answer)
        self.loadQuestion()
        
    def guess(self, answer):
        question = self.getQuestion()
        
        if question.checkAnswer(answer):
            self.score += 1
        self.questionIndex += 1
        
        
        
        
    def loadQuestion(self):        #bu kod blogu ile soru sayisi olan index bittigi zaman hata vermek yerine showScor gösterilir.
        if len(self.questions) == self.questionIndex:
            self.showScore()
        else:
            self.displayProgress()
            self.displayQuestion()
            
            
    def showScore(self):     #bu kod blogu scoru gosterir.
        print("score: ", self.score)
        
        
    def displayProgress(self):         #bu kod blogu da kacinci soruda oldugumuzu gosterir
        totalQuestion = len(self.questions)
        questionNumber = self.questionIndex + 1
        
        if questionNumber > totalQuestion:
            print("quiz bitti.")
        else:
            print(f'Question {questionNumber} of {totalQuestion}'.center(100,"*"))
        
        

q1 = Questions("En iyi programlama dili hangisidir?",["C#","python","javascript","java"],"python")
q2 = Questions("En populer programlama dili hangisidir?",["C#","python","javascript","java"],"python")
q3 = Questions("En cok kazandiran programlama dili hangisidir?",["C#","python","javascript","java"],"python")

questions = [q1,q2,q3]


quiz = Quiz(questions)

quiz.loadQuestion()
































