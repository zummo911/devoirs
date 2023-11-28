def jacc(x, y):
  x = set(x.split())
  y = set(y.split())
  z = x.intersection(y)
  union = len(x) + len(y) - len(z)
  sim = len(z) / union
  return round(sim, 2)

sentence_1 = input()
sentence_2 = input()
print(jacc(sentence_1, sentence_2))