import string
import math


class Leo:
    def __init__(self, status):
        if(status == "full") or (status == "hungry"):
            self.status = status
        else:
            self.status = ''
            ##print("not found status")

    def antelope(self, antelope):
        if self.status != '':
            if antelope == antelope:
                if self.status == "hungry":
                    print('eat -> full')
                    self.status = 'full'
                    print ("current status is " + self.status)

                else:
                    print("Sleep -> hungry")
                    self.status = 'hungry'
                    print ("current status is " + self.status)
            else:
                print ("error")
        else:
             print 'not found status'

    def tree(self, tree):
        if self.status != '':
            if tree == tree:
                if self.status == "hungry":
                    self.status = 'hungry'
                    print("sleep")
                    print ("current status is " + self.status)
                else:
                    print("look -> hungry")
                    self.status = 'hungry'
                    print ("current status is " + self.status)
        else:
            print('not found status')

    def hunter(self, hunter):
        if self.status != '':
            if hunter == hunter:
                if self.status == "hungry":
                    self.status = 'hungry'
                    print("run")
                    print ("current status is " + self.status)
                else:
                    print("run -> hungry")
                    self.status = 'hungry'
                    print ("current status is " + self.status)

        else:
            print('not found status')

##a = Leo('full')
##a.antelope('antelope')
