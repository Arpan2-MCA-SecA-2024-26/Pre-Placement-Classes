//14. Create an acronym or an abbreviation for the name ‘Python For Everyone’.

phrase = "Python For Everyone"
acronym = ''.join(word[0].upper() for word in phrase.split())
print(f"Acronym: {acronym}")