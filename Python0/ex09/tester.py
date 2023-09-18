from ft_package import say_hello, add, sub, mul, div, mod, count_in_list

# python setup.py sdist bdist_wheel
say_hello()
print(add(1, 2))
print(sub(1, 2))
print(mul(1, 2))
print(div(1, 2))
print(mod(1, 2))

print(count_in_list(["toto", "tata", "toto"], "toto"))
print(count_in_list(["toto", "tata", "toto"], "tutu"))
