"""Test for my functions.

Note: 
"""

from Functions import ask_question, create_answer, something_else, lets_shake

# tests to make sure input is a string
def test_ask_question():
    assert callable(ask_question)
    assert isinstance(ask_question(), str) 
    
    test_ask_question()
    
def test_create_answer():
    assert callable(create_answer)
    
    test_create_answer()
    
    
def test_something_else():
    assert callable(something_else)
    
    test_something_else()

# ensures all functions work together
def test_lets_shake():
    assert callable(lets_shake)
    assert isinstance(lets_shake(), str)
    
    test_lets_shake()



    



                 
    