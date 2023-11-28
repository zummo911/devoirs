def mood(text):
    lower_text = text.lower()
    words = lower_text.split()
    positive_words = ["good", "excellent", "fine"]
    negative_words = ["bad", "awful", "disgusting"]
    score = 0
    for word in words:
        if word in positive_words:
            score += 1
        if word in negative_words:
            score -= 1
    if score > 0:
        return("positive")
    if score < 0:
        return("negative")
    if score == 0:
        return("neutral")
text = input(str())
print (mood(text))