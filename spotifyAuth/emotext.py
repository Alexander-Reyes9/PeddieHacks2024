import text2emotion as emo
#Make sure to create a new spotify playlist based on user's prexisting playlist


# #Change this for spotify API
# with open('lyrics.txt', 'r') as file:
#     # Read the entire contents of the file as a string
#     fileContent = file.read()

# file_contents now holds the entire content of the file as a string
# test = fileContent

def output(text):
    if text is None or text.strip() == "":
        print("Can't find lyrics for this song...")
        return None
    else:
        temp = emo.get_emotion(text)
        highestVal = max(temp, key = temp.get)
        return highestVal