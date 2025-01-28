//16. Slice out the phrase ‘because because because’ in the following sentence: ‘You cannot end a sentence with because because because is a conjunction’.

sentence = "You cannot end a sentence with because because because is a conjunction"
start = sentence.find("because because because")
result = sentence[:start] + sentence[start + len("because because because"):]
print(f"Modified sentence: {result}")