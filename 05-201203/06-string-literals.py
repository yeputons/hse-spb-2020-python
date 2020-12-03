s1 = "hello"
s2 = "hello'world"
s3 = 'hello"world'
s4 = "hello\"'world"
print(s1, repr(s1))
print(s2, repr(s2))
print(s3, repr(s3))
print(s4, repr(s4))

s5 = """hello
world
"""
print(repr(s5))
