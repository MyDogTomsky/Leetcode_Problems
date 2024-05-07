# Leecode 1768 categorised by Array/strings
# The order: 1 in 75
# Two strings word1 and word2
# Merge the strings by adding letters in alternating order
# starting with word1 until both strings are ended.


import time


def merger(word1,word2):
    m = min(len(word1),len(word2))
    merged = []
    for i in range(m):
        merged.append(word1[i])
        merged.append(word2[i])
    
    merged.extend(word1[m:])    
    merged.extend(word2[m:])

    return ''.join(merged)

def main():

    start_time = time.time()

    wordset = []
    one = ('abc','pqr')
    two = ('ab','pqrs')
    three = ('abcd','pq') 
    wordset.append(one)
    wordset.append(two)
    wordset.append(three)
    for each in wordset:
        wordone = each[0]
        wordtwo = each[1]
        result = merger(wordone,wordtwo)    
        print(f'\nThe given two words are {wordone} and {wordtwo}\n')
        print(f'\nThe merged string is ===> {result}\n')
    end_time = time.time()
    print(f'\n\nTotal time: {end_time-start_time:.3f} seconds\n')


if __name__=='__main__':
    main()