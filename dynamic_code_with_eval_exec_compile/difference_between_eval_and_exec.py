"""
eval - is used to evaluate a single dynamically generated Python expression.
exec - is used to execute dynamically generated Python code only for its side effects.


1) eval accepts only a single expression, exec can take a code block that has Python
statements: loops, try: except:, class and function/method definitions and so on.

    a_variable = (anything you can put within these parentheses is an expression)

2) eval returns the value of the given expression, whereas exec ignores the return
value from its code, and always returns None.
"""


a = 5
print(eval('37 + a'))   # it is an expression
# out: 42

print(exec('37 + a'))   # it is an expression statement; value is ignored (None is returned)
# out: None

exec('a = 47')   # modify a global variable as a side effect
print(a)
# out: 47

''' This would raise SyntaxError '''
# eval('a = 47')  # you cannot evaluate a statement
