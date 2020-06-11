"""Functions for the Magic 8 Ball."""

# Sets up a nice chat box for user to enter their question.

def ask_question():
    """Sets up a chat box for user and Magic 8 Ball to interact.
    
    Parameters
    ----------
    Input string
        Name will = the input string
    
    Returns
    -------
    question
        The name provided will be returned along with a concatenated sentence.
    """
      
    name = input('Hi! I\'m Magic 8 Ball. What\'s your name? ')
    question = input('Nice to meet you '+ name + ', what would you like to ask me? ')
    if '?' not in question:
        out = input('Don\'t be sassy, please ask a question. ')
        

# The random package allows the Magic 8 Ball to randomly assign an answer to the question asked by the user. 

import random

def create_answer():
    """Allows the Magic 8 Ball to randomly select answers from the responses list.
    
    Parameters
    ----------
    No input necessary, function will run if a question is asked from the user.
    
    Returns
    -------
    An answer that is randomly selected from the responses list using the random package.
    """
    
    responses = ['It is certain.', 'As I see it, yes.', 'YES!', 'Without a doubt.',
             'You may rely on it.', 'Signs point to yes.', 'Outlook looks good.',
             'Ask again later.', 'Better not tell you now.', 'Reply hazy, try later.', 
             'Concentrate & ask again.', 'My reply is no.', 'Very doubtful', 'My sources say no',
             'It is certain.', 'Most likely.', 'Outlook not so good.', 'Don\'t count on it.', 'NOPE.']
    
    
    answer = random.choice(responses)
    print(answer)

    

def something_else():
    """Runs a while loop to indenfinitely answer as many questions as the user wants or to end the chat.
    
    Parameters
    ----------
    User can either input yes or no (input must be lowercase)
    
    Returns
    -------
    If '?' is not found, Magic 8 ball will ask for a question.
    If input is a question, Magic 8 ball will provide a randomized answer
    """
    
    
    q2 = input('Want to shake me again? (yes/no) ')
    while 'yes' in q2:
        output = input('Ask away... ')  
        if '?' not in output:    # ensures user asks a question
            out = input('Quit being such a sass, please ask a question. ')
            create_answer()
        q3 = input('Would you like to ask another question? (yes/no) ') # allows user can ask more questions.
        if 'no' in q3:
            q3 == False
            print('Bye, take care.')
            break    # ends the chat w/ Magic 8 Ball when user is done.
        if 'yes' in q3:
            q3 == True
            continue   # loops back to the top so user can ask infinite number of questions.
    
    if 'no' in q2:  # after the first question, user can leave chat.
        print('Thanks for playing, have a great day!')  
   

        
# puts all the functions together to have it all working as 1 function.
def lets_shake():
    """Puts all functions together, to work seamlessly as one function."""
    
    shaking = True 
    
    while shaking:
        ask_question()
        create_answer()
        
        break     # stops the loop from asking questions from the beginning.
    something_else()
    