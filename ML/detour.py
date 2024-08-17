import text2emotion as emo
with open('lyrics3.txt', 'r') as file:
    # Read the entire contents of the file as a string
    file_contents = file.read()

# file_contents now holds the entire content of the file as a string
test = file_contents
print(emo.get_emotion(test))