import random
import os,sys


class station():
    def __init__(self,name):
        self.agari=0
        self.kudari=0
        self.name=name
        
class Time():
    def __init__(self,hour=0,minute=0):
        self.hour=hour
        self.minute=minute
    def sub(self,b):
        h=self.minute-b.minute
        if h>0:
            return h
        else: return 60+h
    def set(self,b):
        self.hour=b.hour
        self.minute=b.minute
    def add1(self):
        if self.minute==59:
            self.minute=0
            self.hour+=1
        else:
            self.minute+=1

class trainSimul():
    def __init__(self):
        self.time=Time(5,58)
        self.lastB1_A7=Time(5,54)
        self.trainAtA7_B1=1
        self.lastA7_B1=Time(6,5)
        self.A=[station("A1"),station(""),station(""),\
                station("A2"),station(""),station(""),station(""),station(""),\
                station("A3"),station(""),\
                station("A4"),station(""),station(""),\
                station("A5"),station(""),station(""),station(""),\
                station("A6"),station(""),station(""),\
                station("A7"),station(""),station(""),station(""),\
                station("A8"),station(""),\
                station("A9"),station(""),\
                station("A10"),station(""),station(""),\
                station("A11"),station(""),station(""),station(""),station(""),station(""),\
                station("A12"),station(""),\
                station("A13")]
        
        self.B=[station("B1"),station(""),station(""),station(""),
                station("B2"),station(""),station(""),
                station("B3"),station(""),station(""),
                station("B4"),station(""),
                station("B5"),station(""),station(""),
                station("A7")]
        
    def nextMinute(self):
        self.time.add1()
        for Line in (self.A,self.B):
            for i in range(1,len(Line)):
                if Line[i].kudari==1:
                    Line[i-1].kudari=1
                    Line[i].kudari=0
            for i in range(len(Line)-1,-1,-1):
                if Line[i].agari==1:
                    Line[i+1].agari=1
                    Line[i].agari=0
        if self.B[-1].agari==1:
            self.trainAtA7_B1+=1
            self.B[-1].agari=0
        if self.time.sub(self.lastB1_A7)==6 and self.time.hour<23:
            self.B[0].agari=1
            self.lastB1_A7.set(self.time)
        if self.trainAtA7_B1>=1 and self.time.sub(self.lastA7_B1)==6:
            self.B[-1].kudari=1
            self.lastA7_B1.set(self.time)

    def printMap(self):
       for Line in (self.B,): 
            print("%2d:%2d"%(self.time.hour,self.time.minute))
            for i in Line:
                print("[%1s:%d%d]"%(i.name,i.agari,i.kudari),end="")
            print("")

 


S=trainSimul()
S.printMap()
S.nextMinute()
S.printMap()
S.nextMinute()
S.printMap()
S.nextMinute()
S.printMap()
S.nextMinute()
S.printMap()
S.nextMinute()
S.printMap()
S.nextMinute()
S.printMap()
S.nextMinute()
S.printMap()
S.nextMinute()
S.printMap()
S.nextMinute()
S.printMap()
S.nextMinute()
S.printMap()
S.nextMinute()
S.printMap()
S.nextMinute()
S.printMap()
S.nextMinute()
S.printMap()
S.nextMinute()
S.printMap()
S.nextMinute()
S.printMap()
S.nextMinute()
S.printMap()
S.nextMinute()
S.printMap()
S.nextMinute()
S.printMap()
S.nextMinute()
S.printMap()
S.nextMinute()
S.printMap()