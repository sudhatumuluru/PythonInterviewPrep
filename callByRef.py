def double_it(formal_arg):
   # print(formal_arg,id(formal_arg))
    doubled = formal_arg * 2
    #print doubled,id(doubled)
    return doubled,formal_arg
actual_arg=4
#print actual_arg,id(actual_arg)
doubled_value=double_it(actual_arg)
#print doubled_value,id(doubled_value)
print doubled_value

## For Python its all about Pass by Object Reference as Python has only immutable or mutable objects. So in Python, if u pass a value,
## that means you are passing an object reference
## For example, In the above code, 4 is the object and actual_arg is the name to the object, id(actual_arg) returns the address value
## of the object.