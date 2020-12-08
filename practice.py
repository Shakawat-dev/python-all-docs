# Find out the given Bangla words meaning #
myWordsList = {
  'patil':'container',
  'mog':'jar',
  'baksho':'box'
}
print('Options are :',myWordsList.keys())
a = input('Enter your Bangla words: ')
print('your given word meaning is :', myWordsList[a])

# program of unique number #
num1 = int(input('Enter your number 1\n'))
num2 = int(input('Enter your number 2\n'))
num3 = int(input('Enter your number 3\n'))
num4 = int(input('Enter your number 4\n'))
num5 = int(input('Enter your number 5\n'))
num6 = int(input('Enter your number 6\n'))
num7 = int(input('Enter your number 7\n'))
num8 = int(input('Enter your number 8\n'))

uniqueNum = {num1, num2, num3, num4, num5, num6, num7, num8}
print('The list of your entered number are:',uniqueNum)

# add user input into a emty string #
favLang = {}
a = input('Enter your favorite language sonali\n')
b = input('Enter your favorite language ropali\n')
c = input('Enter your favorite language masum\n')
d = input('Enter your favorite language khan\n')
favLang['sonali'] = a
favLang['ropali'] = b
favLang['khan'] = c
favLang['khan'] = d
print(favLang)

# check the set's value #
s = {6, 6, 12, 'Harry', tuple([1, 3])}
print(type(s))
