name = 'Andrew'
age = 33

print(f'Hi {name}. You are {age} years old')

print('Hi {}. You are {} years old'.format(name, age))

print('Hi {1}. You are {0} years old'.format(name, age))

print('Hi {new_name}. You are {age} years old'.format(new_name='Sally', age=100))

# [start at incext: stop at index: stepover increment, negative numbers start at end of string]

print(name[1:1:2])

