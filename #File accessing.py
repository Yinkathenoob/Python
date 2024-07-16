#File accessing
file_path = '/Users/YinkaTN/Developer/python/test'
file = open(file_path)
contents = file.read()
print(contents)


#OR
file_path = '/Users/YinkaTN/Developer/python/test'
with open(file_path, mode = 'w') as file:
    file.write('This is a new file')