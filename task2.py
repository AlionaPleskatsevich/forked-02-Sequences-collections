text = """
Вчера Анна и Артем гуляли в парке. Анна заметила слово level на
старом плакате. Рядом кто-то написал radar, а чуть дальше было
нарисовано слово kayak. На скамейке сидел человек с книгой civic,
а возле фонтана дети мелом написали refer. Остальные слова в тексте
палиндромами не являются.
"""
palindroms = []
text = text.lower()
words = text.split()
for ind in range(len(words)):
    words[ind] = words[ind].strip(",.\n")
for word in words:
    if len(word)>2:
      if word[::-1] == word:
        if word not in palindroms:
         palindroms.append(word)
print(palindroms)
