from hyphenate import hyphenate_word
import csv
'''
#print(hyphenate_word('picture'))
def createHyphenation(fname):
    with open(fname) as file: 
        # Passing the TSV file to 
        # reader() function
        # with tab delimiter
        # This function will
        # read data from file
        tsv_file = csv.reader(file, delimiter="\t")
        for line in tsv_file:
        # hyphenating data line by line
            (hyphenate_word(line[0]))
        
createHyphenation("EnglishWords.tsv")
'''

vowels = 'AEIOU'
consts = 'BCDFGHJKLMNPQRSTVWXYZ'
consts = consts + consts.lower()
vowels = vowels + vowels.lower()
def is_vowel(letter):
    return letter in vowels 
def is_const(letter):
    return letter in consts
#return list of vowel to consonant ratios
def createRatioList(fname):
    worldLen = 0
    vowelCount = 0
    consCount = 0
    ratioList = []
    with open(fname) as file: 
        # Passing the TSV file to 
        # reader() function
        # with tab delimiter
        # This function will
        # read data from file
        tsv_file = csv.reader(file, delimiter="\t")
        for line in tsv_file:
        # hyphenating data line by line
            wordLen = len(line[0])
            vowelCount = 0
            consCount = 0
            for i in line[0]:
                if is_vowel(i):
                    vowelCount += 1
                if is_const(i):
                    consCount += 1
            if consCount == 0:
                consCount = 1
            ratioList.append(vowelCount / consCount)
    return ratioList

print(createRatioList('EnglishWords.tsv'))


            
                