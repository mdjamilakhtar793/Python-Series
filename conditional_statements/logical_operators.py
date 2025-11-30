# and - Returns True if both statements are true
# or - Returns True if one of the statements is true
# not - Reverses the result, returns False if the result is true
a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both conditions are True")
a = 200
b = 33
c = 500
if a > b or a > c:
    print("At least one of the conditions is True")
a = 33
b = 200
if not a > b:
    print("a is NOT greater than b")
age = 25
is_student = False
has_discount_code = True

if (age < 18 or age > 65) and not is_student or has_discount_code:
    print("Discount applies!")
username = "Tobias"
password = "secret123"
is_verified = True

if username and password and is_verified:
    print("Login successful")
else:
    print("Login failed")
