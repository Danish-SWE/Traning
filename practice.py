# print('Hello world!') # printing through python
# print('Be kind.' * 3) # this is an expression that shows the string 3 or (n) times
# print('Thank you.')

# Variables in python
studentName = 'Danish'
studentAge = 24
studentGPA = 3.03
isActive = True
# studentProgram = 'MSc in Software Engineering'
# print("presenting student data:")
# print('Student Name :' + studentName)
# print('Student Age :',studentAge)
# print('Is Student Active :',studentGPA)
# print('Student Program : ' + studentProgram)

# input through python
# fav_subject = input('What is student favorite subject in Software Engineering? ')
# print(studentName + ' favorite subject is : ', fav_subject)
# graduation_year = input('Enter the student graduation year? ')
# education_gap = 2026 - int(graduation_year)
# print(studentName + ' graduation gap is : ' , education_gap , ' year/years.')

# Multiple lines string
# student_message = '''Hello Professor
#
# I am interested in the research that you working on.
#
# Thank you sir!'''
# print(student_message)
# print(student_message[0:5])
# print(student_message[16:])
# print(student_message[1:-1])

# formating strings
# skill_1 = 'Software Engineer'
# skill_2 = 'Software Developer'
# print(f'{skill_2} is a part of {skill_1}')

# some built-in functions and methods in python
statement = 'Python is a powerful programming language for Machine learning and Data analytics operations.'
# print(len(statement)) # this is function
# print(statement.upper()) # this is a method
# print(statement.lower())
# print(statement.capitalize())
# print(statement.title())
# print(statement.find('z')) # if the method the given character or sub-string its return index number, otherwise its return the -1
# print('powerful' in statement) # this is an expression which checks for a character or sub-string and returns boolean value as a result.
# print(statement.replace('operations', 'works'))


# some arithmatic operations
x = 3
# print(3+1) #Addition
# print(3-2) #substraction
# print(3*2) #multiplication
# print(3/2) #division
# print(3 // 2) #division and gives us integer value
# print(3 % 2) #modules
# print(3 ** 4) #power
# x +=3
# print(x)
# x -=3
# print(x)
# x *=3
# print(x)

# mathematical expressions
# 1- first prirorty to brackets
# 2- second prirorty to division
# 3- third prirorty to multiplication
# 4- fourth prirority to substraction
# 5- fifth prirorty to the addition
# x = (3*4) -10 + 3*2 - 5/5
# print(x)


# some math methods and functions
# import math
# z = 99.98
# print(z)
# print(abs(-99.98))
# print(math.floor(z))
# print(math.ceil(z))

# if, elif, and else conditions
# is_research_proposal_accepted = False
# is_research_proposal_rejected = False
#
# if is_research_proposal_accepted:
#     print('congratulations, great work!')
# elif is_research_proposal_rejected:
#     print("don't worry, try again.")
# else:
#     print('the research approving is in pending.')

# logical(and,or) and comparison(>,<,>=,<=,==) operators
# knowledge_eligibility = True
# research_eligibility = True
# has_ethically_weakness = False
# if knowledge_eligibility and research_eligibility and not has_ethically_weakness:
#     print('You are eligible for conducting this research.')
# else:
#     print('Sorry, you are not eligible for conducting this research.')
#
# knowledge_eligibility = True
# research_eligibility = False
# if knowledge_eligibility or research_eligibility:
#     print('You are eligible for conducting this research.')
# else:
#     print('Sorry, you are not eligible for conducting this research.')
#

# research_evaluation_marks = 78
# if research_evaluation_marks >= 85:
#     print('Conducted research approved successfully!')
# else:
#     print('Sorry, you should to conduct research again.')


# loops(while,do-while,for,forelse)
is_research_approved = False
while  is_research_approved == False:
    print('Sorry, try again.')
    print('''
    .
    .
    .
    ''')
    response = input('Is research approved now, answer with True/False only? ')
    if response == 'True' or response == 'true':
        is_research_approved = True

print('finally, research approved successfully.')