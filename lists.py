basket = ['a', 'x', 'b', 'c', 'd', 'e', 'd']
basket.sort()
basket.reverse()
print(basket[::-1])
print(list(range(0, 101)))
sentence = '!'
new_sentence = sentence.join(['Hi', 'my', 'name', 'is', 'Andrew'])
print(new_sentence)

# list unpacking

a, b, c, * other, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(a)
print(b)
print(c)
print(other)
print(d)


