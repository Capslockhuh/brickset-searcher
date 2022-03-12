#! Python 3
import webbrowser
#main code:
print('Please enter a LEGO set number')
setNumber = input()
webbrowser.open('https://brickset.com/sets/' + setNumber)
