# initialize variables
name, title = 'Monty', 'Python'

# Code starts here

# full name
full_name = name + ' ' + title
print('Full name : ', full_name)

# first name
first_name = full_name[:5]
print('First name : ', first_name)

# length of full name
len_name = len(full_name) - 1
print('Length of full name : ', len_name)

print(type(len_name))

# Is "f" in full name?
is_f = 'f' in full_name
print('Is \'f\' in full name : ', is_f)

# Split into first name and title
split = full_name.split()
print(split)
