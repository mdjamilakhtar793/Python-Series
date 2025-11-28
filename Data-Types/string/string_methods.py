name = "john doe"
print(name.capitalize())   # John doe

text = "Straße"
print(text.casefold())     # strasse


title = "MENU"
print(title.center(20, "-"))
# -------MENU--------


msg = "The rain in Spain"
print(msg.count("ain"))    # 2


msg = "hello ✓"
print(msg.encode("utf-8"))


filename = "report.pdf"
print(filename.endswith(".pdf"))   # True


text = "Name\tAge\tCity"
print(text.expandtabs(10))



email = "user@gmail.com"
print(email.find("@"))   # 4



msg = "Hello {}, your score is {}"
print(msg.format("Alice", 95))


data = {"name": "Bob", "age": 30}
print("{name} is {age} years old".format_map(data))


text = "hello"
print(text.index("e"))   # 1



username = "User123"
print(username.isalnum())   # True


name = "Paris"
print(name.isalpha())   # True


price = "250"
print(price.isdecimal())   # True


year = "2024"
print(year.isdigit())   # True


var = "my_variable"
print(var.isidentifier())   # True


text = "hello"
print(text.islower())   # True


num = "Ⅷ"
print(num.isnumeric())   # True


num = "Ⅷ"
print(num.isnumeric())   # True


s = "hello\n"
print(s.isprintable())   # False


s = "   "
print(s.isspace())   # True


title = "The Great Gatsby"
print(title.istitle())   # True


words = ["2025", "02", "15"]
print("-".join(words))  # 2025-02-15


item = "Apple"
print(item.ljust(10, "."))   # Apple.....


email = "USER@GMAIL.COM"
print(email.lower())


text = "   hello"
print(text.lstrip())   # "hello"


mapping = str.maketrans("aeiou", "12345")
print("hello world".translate(mapping))


email = "user@gmail.com"
print(email.partition("@"))
# ('user', '@', 'gmail.com')


text = "Hello World"
print(text.replace("World", "Python"))


text = "banana"
print(text.rindex("a"))   # 5


url = "example.com/index.html"
print(url.rpartition("/"))


sentence = "a,b,c,d"
print(sentence.rsplit(",", 1))   # ['a,b,c', 'd']


text = "hello!!!"
print(text.rstrip("!"))


csv = "apple,banana,orange"
print(csv.split(","))


msg = "Hello\nWorld\nPython"
print(msg.splitlines())


url = "https://google.com"
print(url.startswith("https"))


text = "   hello   "
print(text.strip())


msg = "Hello WORLD"
print(msg.swapcase())   # hELLO world


book = "war and peace"
print(book.title())   # War And Peace


trans = str.maketrans({"a": "@", "e": "3"})
print("apple".translate(trans))   # @ppl3

city = "london"
print(city.upper())


invoice = "45"
print(invoice.zfill(5))   # 00045
