import emoji

# user input
user = input("Input: ").split()

# Extraction of key_word
key_word = []
for i in range(len(user)):
    if ":" in user[i]:
        key_word.append(user[i])

# converting txt to emoji
emo_list = []
for j in range(len(key_word)):
    emo = emoji.emojize(key_word[j], language="alias")
    emo_list.append(emo)

# replacing txt with emoji
plus = 0
for i in range(len(user)):
    if user[i] == key_word[plus]:
        user[i] = emo_list[plus]
        plus += 1

# prompting the output
text = ""
for i in range(len(user)):
    if i == 0:
        text += user[i]
    else:
        text += " " + user[i]
print(text)
