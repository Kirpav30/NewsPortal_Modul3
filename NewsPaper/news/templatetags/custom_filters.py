import posts as posts
from django import template


register = template.Library()

bad_words = ['корова', 'козел', 'лягушка']

@register.filter()
def censor(sentence):
    text = sentence.split()
    for i, word in enumerate(text):
        if word in bad_words:
            text[i] = word[0] + '*' * (len(word) - 1)
    return ' '.join(text)




