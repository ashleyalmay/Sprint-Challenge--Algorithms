'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    start = word.find('th')
    if start != -1:
        return 1 + count_th(word[start+2:])
    else:
        return 0

#set a base to find 'th'
#if the start is not the end 
#it will push thur and check every 2 of the word and then get it
#if not return 0