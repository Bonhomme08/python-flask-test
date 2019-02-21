from misc.custom_print import custom_print

# v1
#print_temp = print
#print = custom_print.print


def print_line(the_func):
    def wrapper():
        print('')
        print('=' * 50)

        the_func()
    return wrapper


# v2
# def print_line(the_whole_string):
#     def wrap(f):
#         def wrapped_f(*args):
#             if the_whole_string is None:
#                 print('')
#                 print('=' * 50)
#             else:
#                 #the_whole_string = the_whole_string + ""
#             # if arg1 is None:
#             #     print('')
#             #     print('=' * 50)
#             # else:
#             #     arg1 += "\n"
#             #     arg1 += "=" * 50
#
#             f(*args)
#
#         return wrapped_f
#     return wrap
#
#
# # PythonDecorators/decorator_function_with_arguments.py
# def decorator_function_with_arguments(arg1, arg2, arg3):
#     def wrap(f):
#         print("Inside wrap()")
#
#         def wrapped_f(*args):
#             print("Inside wrapped_f()")
#             print("Decorator arguments:", arg1, arg2, arg3)
#             f(*args)
#             print("After f(*args)")
#         return wrapped_f
#     return wrap
