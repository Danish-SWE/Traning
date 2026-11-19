# import utilities.grade_converter
# from utilities.grade_converter import converter
# from utilities import grade_converter
#
# value = 0.0
# grade_format = input(str('Enter what you want to get [percentage/gpa]: '))
# grade_format.lower()
# if grade_format == 'percentage':
#     value = input('Enter the GPA:')
# elif grade_format == 'gpa':
#     value = input('Enter the Percentage: ')
# else:
#     print('invalid formated entered, try again.')
#
# # result = utilities.grade_converter.converter(grade_format, float(value))
# # result = converter(grade_format, float(value))
# result = grade_converter.converter(grade_format, float(value))
#
# print(f'Result is :{result[0]}' )
# print(f'Result message :{result[1]}')


# working with python built-in modules
import random

print(random.random()) # it gives us result between 0 and 1
print(random.randint(0, 10)) # it gives us a random between the identified interval
