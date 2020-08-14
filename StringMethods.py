course='python for beginners'
print(len(course))
print(course.upper())

#index of first occurance of the charcter provided is the output and find method is case sensitive and it returns -1 if the character is not present in the string
print(course.find('o'))
print(course.find('O'))
print(course.find('for beginners'))


print(course.replace('for beginners','learning for Newbies'))
print(course.replace('n','a'))

#to check whether given word is present in the string use in keyword
print('python or' in course)
print(course.title())