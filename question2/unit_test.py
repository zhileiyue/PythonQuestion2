import os
import unittest
import urllib
import re
from view import RepresentsInt, fibo

def getResponse(input):
    response = urllib.urlopen('http://localhost:8000/fibo/'+input)
    
    return response.read()
class SourceFunctionalTests(unittest.TestCase):
    def testRepresentsInt_PositiveInteger(self):
        self.failUnless(RepresentsInt('8'))
    def testRepresentsInt_Float(self):
        self.failUnless(RepresentsInt('9.8')==False)
    def testRepresentsInt_NegativeInteger(self):
        self.failUnless(RepresentsInt('-23'))
    def testRepresentsInt_Zero(self):
        self.failUnless(RepresentsInt('0'))
    def testRepresentsInt_Character(self):
        self.failUnless(RepresentsInt('aaa')==False)
    def testFibo(self):
        testcase = ['1','2','5','8','10','14','38','-4','aa','6.8','%%%']
        for tmp in testcase:
            if RepresentsInt(tmp)==False:
                self.failUnless(fibo(tmp)=="Please input an integer!")
                continue
            if int(tmp)<=0:
                self.failUnless(fibo(tmp)=="Please input a positive integer!")
                continue
            tmplist = fibo(tmp)
            tmplist = tmplist.split(', ')
            print tmplist
            if tmp == '1':
                self.failUnless(tmplist == ['0'])
            if tmp == '2':
                self.failUnless(tmplist == ['0', '1'])
            else:
                for i in range(int(tmp)-2):
                    print str(tmplist[i])+'+'+str(tmplist[i+1])+'='+str(tmplist[i+2])
                    self.failUnless(int(tmplist[i])+int(tmplist[i+1])==int(tmplist[i+2]))
        
        
class InputValidationTests(unittest.TestCase):
    def testFloat(self):
        self.failUnless(getResponse('1.9')=="Please input an integer!")
    def testNegtive(self):
        self.failUnless(getResponse('-10')=="Please input a positive integer!")
    def testZero(self):
        self.failUnless(getResponse('0')=="Please input a positive integer!")
    def testCharacter(self):
        self.failUnless(getResponse('aabb')=="Please input an integer!")
class ServiceFunctionalTests(unittest.TestCase):
    def test1(self):
        print getResponse('1')
        self.failUnless(getResponse('1')=="0")
    def test2(self):
        self.failUnless(getResponse('2')=="0, 1")
    def test5(self):
        self.failUnless(getResponse('5')=="0, 1, 1, 2, 3")


    
if __name__ == '__main__':
    #getResponse('5')
    unittest.main()
