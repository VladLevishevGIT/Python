import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
         return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        answer = input("Did you mean %s instead?" % get_close_matches(w, data.keys())[0] + "Y/N: ")
        if answer.lower() == 'y':
            return translate(get_close_matches(w, data.keys())[0])
        else:
            return "Sorry, this word doesn't exist!"
    else:
        answer = input("Incorrect input!\nDo you want to continue? Y/N: ")
        if answer.lower() == "y":
            word = input("Reenter the word: ")
            return translate(word)
        else:
            return "Thank you $ Goodbye!"


word = input("Enter some word: ")

output = translate(word)

if type(output) == list:
    count = 1
    for item in output:
        print(str(count) + " definition of this word: " + item)
        count = count + 1
else:
    print(output)




