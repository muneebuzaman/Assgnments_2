def longest_word(words):
    longest=''
    for word in words:
        if len(word)> len(longest):
            longest=word
    return longest,len(longest)
words=['Srinagar','Hyderabad','Delhi','Kanpur']
longest,length=(longest_word(words))
print(f'the longest word is {longest} and \nlength={length}')


