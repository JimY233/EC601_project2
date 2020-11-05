import pytest
from NLPAPI import NLP_analyze

    
def test_NLP1():
    text = 'Hello world!'
    sentiment = NLP_analyze(text)
    assert hasattr(sentiment,'score') == True

#def test_NLP2():
#    text = 'Hello world!'
#    sentiment = NLP_analyze(text)
#    assert hasattr(sentiment,'magnitude') == True
        
if __name__ == '__main__':
    pytest.main()

