

def WordValueConversion(word):
    value = 0
    for i in range(len(word)):
        value += ord(word[i]) - 64
    return value
#print(WordValueConversion("SKY"))

def isTriangleNum(num):
    n = ((-1 + (1 + (8 * num))**0.5)/2)
    if n % 1 == 0:
        return True
    return False

def TriangleWord(word):
    return isTriangleNum(WordValueConversion(word))

f = open('p042_words.txt','r')
content = f.read().replace('"', '')
lst = content.split(',')
 
counter = 0           
for words in lst:
    if TriangleWord(words):
        counter += 1
print(counter)
