import text2emotion as emo
def output(text):
    if text is None or text.strip() == "":
        return None
    else:
        temp = emo.get_emotion(text)
        highestVal = max(temp, key = temp.get)
        return highestVal