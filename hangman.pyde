import random
def setup():
    size(750, 500)
    background(225, 200, 100, 127)
    

def draw():
    #stroke(20)
    #line(mouseX, mouseY, 255, 255)
    fill(255)
    font = loadFont("Courier-55.vlw")
    textFont(font)
    text("Hangman", 270, 230)
    font = loadFont("Courier-25.vlw")
    textFont(font)
    text("Press 'enter' to start", 220, 300)
    if (key ==  ENTER):
        noStroke()
        fill(225, 200, 100)
        rect(100, 100, 550, 550)
        delay(100)
        
        
        #sets variable as False to see if the letter guessed exists at all in the word
        letterInWord = False
        #creates a list for the blanks in the words
        wordList = []
        #sets the wrong guesses variable
        wrongGuesses = 0
        #list of possible words to guess
        possibleWords = ["salem", "nymph", "boston", "stocks", "pentagram", "occult", "devil", "witchcraft", "rituals"]
        #picks a random number for list
        word = random.randint(0,8)
        wordToGuess = (possibleWords[word])
        font = loadFont("Courier-55.vlw")
        textFont(font)
        fill(255)
        space = 200
        for x in wordToGuess:
            text("_", space, 300)
            
            print("1")
            delay(10)
        
#def keyPressed():
 #   if (key ==  ENTER):
#        noStroke()
 #       fill(225, 200, 100)
  #      rect(100, 100, 550, 550)
   #     delay(10)
        
    
    #text("Hi, my name is Robert, and I'm a man that might be hanged.", 110, 200)
    #text("Your job is to correctly guess the word to save my life.", 130, 240)

#sets the story

        
