import json
from datetime import date
import calendar
import requests
class Today:
    def __init__(self):
        self.ayni_damda = date.today()
        self.hozirgi_yil = self.ayni_damda.year
        self.hozirgi_oy_sonda = self.ayni_damda.month
        self.hozirgi_oy_sozda = calendar.month_name[self.hozirgi_oy_sonda]
        self.hozirgi_kun = self.ayni_damda.day
    def hozir(self):
        return self.hozirgi_yil, self.hozirgi_oy_sozda, self.hozirgi_kun
t = Today()
print(t.hozir())

class Show(object):
    @staticmethod
    def show(readfile):
        with open(readfile, 'r') as f:
            return json.load(f)


class Dummy(Show):
    def __init__(self, filename):
        self.filename = filename
    def download(self,url):
        data = []
        response = requests.get(url)
        data.append(response.json())
        with open(self.filename, 'w') as f:
            json.dump(data, f)
dummy = Dummy('new.json')
print(dummy.download('https://dummyjson.com/users'))
print(dummy.show('new.json'))


class Integer:
 
    def __set_name__(self, owner, name):
        self.name = name
 
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]
 
    def __set__(self, instance, value):
        if type(value) != int:
            raise TypeError("qiymat int bo'lishi kerak")
        else:
            instance.__dict__[self.name] = value
class Bool:
        
    def __set_name__(self, owner, name):
        self.name = name
 
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]
 
    def __set__(self, instance, value):
        if type(value) != bool:
            raise TypeError("qiymat boolean bo'lishi kerak")
        instance.__dict__[self.name] = value
class Line:
    height = Integer()
    length = Integer()
    status = Bool()
    def __init__(self, height: int, length: int, status:  bool ):
        self.height = height
        self.length = length
        self.status = status
line = Line(12,123,True)
print(line.height)