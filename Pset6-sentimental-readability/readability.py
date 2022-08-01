# TODO
# call user for input
n = str(input("Text: "))

# count letters
letters = 0
for i in n:
    if i.isalpha():
        letters += 1

# count words
word_count = 1
for i in n:
    if (i == " "):
        word_count += 1

# count sentences
sentence_count = 0
for i in n:
    if (i == "." or i == "!" or i == "?"):
        sentence_count += 1


# Coleman-Liau index
L = letters / (word_count / 100)
S = sentence_count / (word_count / 100)
cl_index = round(0.0588 * L - 0.296 * S - 15.8)


if (cl_index < 1):
    print("Before Grade 1")
elif (cl_index > 16):
    print("Grade 16+")
else:
    print("Grade", cl_index)