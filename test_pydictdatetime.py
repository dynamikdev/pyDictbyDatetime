from pyDictbyDatetime import pydictdatetime

__author__ = 'philippe'

import unittest
from datetime import datetime,timedelta

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.basedict = pydictdatetime.DictByDatetime()
        self.yesterday = datetime.now() - timedelta(days=1)
        self.tomorrow = datetime.now() + timedelta(days=1)
        self.beforeyesterday = datetime.now() - timedelta(days=2)
    def test_addingFullConfigurate(self):

        key = "MyKey"
        value= "SomeData"
        self.basedict[key,(self.yesterday,self.tomorrow)]= value
        self.assertEqual(self.basedict.get(key,date=datetime.now())[0], value)
    def test_addingStartConfigurate(self):

        key = "MyKey"
        value= "SomeData"
        self.basedict[key,self.yesterday]= value
        self.assertEqual(self.basedict.get(key,date=datetime.now())[0], value)
    def test_addingEndConfigurate(self):

        key = "MyKey"
        value= "SomeData"
        self.basedict[key,(None,self.tomorrow)]= value
        self.assertEqual(self.basedict.get(key,date=datetime.now())[0], value)


    def test_addingStartConfigurateAfter(self):
        key = "MyKey"
        value= "SomeData"
        self.basedict[key,self.tomorrow]= value
        self.assertEqual(self.basedict.get(key,date=datetime.now())[0], [])
    def test_addingEndConfigurateBefore(self):

        key = "MyKey"
        value= "SomeData"
        self.basedict[key,(None,self.yesterday)]= value
        self.assertEqual(self.basedict.get(key,date=datetime.now())[0], [])

    def test_notInInterval(self):

        key = "MyKey"
        value= "SomeData"
        self.basedict[key,(self.beforeyesterday,self.yesterday)]= value
        self.assertEqual(self.basedict.get(key,date=datetime.now())[0], [])
if __name__ == '__main__':
    unittest.main()
