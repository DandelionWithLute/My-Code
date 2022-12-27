fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
def reverse(word):
    return word[::-1]
print(reverse('testing'))
print(sorted(fruits))
print(sorted(fruits, key=reverse))
abc = ["add", "back", "chapter"]
print(sorted(abc))
print(sorted(abc, key=reverse))
abcs = ["adds", "back", "chapter"]
print(sorted(abcs))
print(sorted(abcs, key=reverse))
#我们只是把反向拼写当作排序条件，因此各种浆果（berry）都
#排在一起。
