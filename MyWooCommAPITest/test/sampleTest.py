

print("Program to demonstrate **kwargs for variable number of keywords:")
print("\n")
def concatenate(**kwargs):
    r = ""
    for arg in kwargs.values():
        r += arg
    return r
print("The concatenated value is displayed as follows:")
print(concatenate(a="Educba", b="Training", c="Institue"))