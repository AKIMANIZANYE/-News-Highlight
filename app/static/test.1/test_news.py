import unittest
from app.models import News

class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the News class
    '''

def setUp(self):
    '''
    Set up method that will run before every Test
    '''
    self.new_news = News("Bitstop","lors de la conférence EuroCIS","MIAMI,on Systemsonnalisées","https://www.prnewswire.com/news-releases/bitstop-4172769.html","https://mma.prnewswire.com/media/628363/Bitstop_Logo.jpg?p=facebook", "2019-02-18T06:03:00Z","La plateforme logicielle des distributeurs automatiques de bitco")

def test_instance(self):
    self.assertTrue(isinstance(self.new_news,News))