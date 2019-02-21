import unittest
from Models.News import News
# News = news.News


class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Newz class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_news = News("one","Cryptohopper Just Hit 100k Users on Their Trading Platform","http://businesswire.sys-con.com/node/4376242","ear and t completely automatically. When you sign up and configur…","pa","gekohwgoeg","Cryptohopper just announced that it hit 100k users on their trading ")
    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))
if __name__=='__main__':
    unittest.main()