#for loop
# number = 0
# for number in range(50):
#    number += number
#    print(number)
# students ={'Y243':'Ahmad', 'Y244':'Mahmood', 'Y245':'Wali', 'Y246':'Noor'}
# count = 1
# print('The class students are listed below :')
# print('#:     ID:         Name:          ' )
# print('=======================================================')
# for id,name in students.items():
#    print(count ,'     '+ id + '        ' + name)
#    print('-----------------------------------------------------')
#    count += 1

# List in python
# names= ['Ahmad', 'Mahmood', 'Noor', 'Naqib']
# print(names)
# print(names[2])
# print(names[1:])
# print(names[-1])
# list_count = 1
# names.append('Ahsan')
# names.insert(1, 'Ali')
# names.pop()
# names[-1] = "Atiq"
# for name in names:
#    print(list_count,'.' + name)
#    list_count +=1

# 2D list
# classes =[
#    ['Ahmad', 'Mahmood'],
#    ['Noor', 'Naqib'],
#    ['Ahsan', 'Ali', 'Atiq']
# ]
# alphabets=['A', 'B', 'C', 'D']
# print(classes)
# print(classes[0])
# print(classes[1][1])
# for alphabet,row in zip(alphabets,classes):
#    print(f'Class {alphabet} students' )
#    for student in row:
#       print(f' ->{student}')

#Exercise: write a program that removes duplicates from a list.
# initially_list=[10, 24, 12, 10, 15, 28, 12, 24, 25, 26, 11, 14, 16, 17, 11]
# organized_list=[]
# for number in initially_list:
#    if organized_list.__contains__(number):
#       continue
#    else:
#       organized_list.append(number)
# print('organized list is :' , organized_list )

# Tuple: tuple in python a special type of container like list but it is not immutable(unchangeable)
# coordinates = (5, 10, 15)
# print(coordinates)
# print(coordinates[0])
# x, y, z = coordinates # this is the python beauty that we can assign value and make variables like this.
# print(z)

# dictionary in python
# digits_mapping={
#     0 : 'zero',
#     1: 'one',
#     2: 'two',
#     3: 'three',
#     4: 'four',
#     5: 'five',
#     6: 'six',
#     7: 'seven',
#     8: 'eight',
#     9: 'nine',
# }
# output = ""
# user_input = input('Enter a digits to convert it to the words? ')
# for digit in user_input:
#     output += digits_mapping.get(int(digit), '!') + ' '
# print(output)

# functions in python
# def greeting_msg(name):
#     print(f'hello {name}!')
#     print('This is sakarya University Software Engineering Department.')
#
# greeting_msg('Danish') #positional argument
# greeting_msg(name='Danish') #keyword argument

# exceptions handling in python
# try:
#     days = int(input('Enter days : '))
#     salary_per_day = 4500 / days
#
#     print(f'Given days are {days}')
#     print(f'per day salary equal to {salary_per_day}$.')
# except ValueError:
#     print('invalid value entered!')
# except ZeroDivisionError:
#     print('days should be greater than zero!')

# classes in python
class Research:
    def greeting(self):
        print('welcome to research center.')


obj = Research()
obj.greeting()

# class with a constructor method

class ResearchProposal:
    def __init__(self, title, author, duration = '1 year'):
        # self.research_title = 'Review to backlog'
        # self.research_duration = '11 - 12 weeks'
        # self.research_author = 'Beyza Ekan'
        self.research_title = title
        self.research_author = author
        self.research_duration = duration


    def previewResearchInfo(self):
        print(f'''
Research informations are listed below
    - Research Title : {self.research_title}
    - Research Author : {self.research_author}
    - Research Duration : {self.research_duration}
    
''')


# Research1 = ResearchProposal()
# Research1.previewResearchInfo()

Research2 = ResearchProposal(title='Future of AI', author='Beyza Ekan', duration= '2 months')
Research2.previewResearchInfo()