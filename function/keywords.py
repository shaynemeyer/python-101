def keyword_function(a=1, b=2):
    return a + b

print(keyword_function())
print(keyword_function(b=4, a=5))
print(keyword_function(5))


def many(*args, **kwargs):
    print(args)
    print(kwargs)

many(1, 2, 3, name="Mike", job="programmer")
