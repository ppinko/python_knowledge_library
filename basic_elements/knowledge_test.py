""" 
Short script to generate 10 random topics to talk about
"""

import random

way_of_the_program = [
	'problem solving', 'low-level languages', 'high-level languages',
	'script', 'program', 'bug', 'debugging', 'syntax errors', 
	'runtime errors', 'semantic errors', 'parse', 'comment', 'source code'
]

variables_expressions_and_statements = [
    'keyword', 'assignment statement', 'concatenate', 'data type', 
    'modulus operator', 'operand', 'operator', 'rules of precedence',
    'state snapshot', 'variable', 'variable name', 'attribute', 
    'loop variable', 'instance', 'method', 'invoke', 'module', 'object',
    'terminating condition'
]

functions = [
    'function definition', 'argument', 'docstring', 'flow of execution',
    'function', 'function call', 'fruiful function', 'void function', 
    'import statement', 'local variable', 'parameter', 'refactor', 
    'stack diagram', 'traceback'
]

conditionals = [
	'comparison operatos', 'logical operators', 'chained conditionals',
	'nested conditionals', 'logical opposites', "de Morgan's laws", 'block',
	'Boolean expression', 'Boolean value', 'branch', 'conditional statement',
	'nesting', 'truth table'
]

all_topics = []
all_topics.append(way_of_the_program)
all_topics.append(variables_expressions_and_statements)
all_topics.append(functions)
all_topics.append(conditionals)

# list comprehension to flatten the list of topics
flatten_list = [ element for row in all_topics for element in row]

def quiz(ls, questions):
	""" 
	Ask randomly choosen questions from the list
	
	Parameters:
	list - list of questions
	questions - number of questions to be asked
	"""
	for number, question in enumerate(random.sample(ls, questions)):
		print("{0}    {1}".format(number, question))

quiz(functions, 10)
