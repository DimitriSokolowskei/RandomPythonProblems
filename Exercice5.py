def PigLatin(word):
    if word[0] in 'aeiou':
        print(word + 'way')
    else:
        print(word[1:] + '' + word[0] + 'ay')

print(PigLatin('python'))
