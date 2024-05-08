import emoji
import string

def getEmojiBase(c):
    e = ''.join(sorted(emoji.EMOJI_DATA, key=lambda e: (emoji.EMOJI_DATA[e] != 'Smileys & Emotion', e))); return (e[9562:] + e[:9562])[:c]

def toEmojiBase(n, b=16769):
    b = 16769 if b < 2 else b
    c = getEmojiBase(b)
    return '' if n == 0 else toEmojiBase(n // b, b) + c[n % b]

def fromEmojiBase(s, b):
    b = 16769 if b < 2 else b
    c = getEmojiBase(b)
    return sum(c.index(d) * b**i for i, d in enumerate(reversed(s)))

# NOTES:
# pip install emoji is required
# not stable
# emoji modifiers are an issue
# code does not group properly for conversion
