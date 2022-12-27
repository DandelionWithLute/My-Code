fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
print(sorted(fruits, key=lambda word: word[::-1]))
#word:: reprents reversing!
#Lambda 表达式，也可称为闭包，它是推动 Java 8 发布的最重要新特性。
#Lambda 允许把函数作为一个方法的参数（函数作为参数传递进方法中）。
#使用 Lambda 表达式可以使代码变的更加简洁紧凑。
#https://www.runoob.com/java/java8-lambda-expressions.html