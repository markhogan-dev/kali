import datetime as dt
quantity = 14
unit_price = 2.25
calcd_price = quantity * unit_price
print(unit_price)
print(quantity)
print(calcd_price)
x = 1.123456789
y = round(x,3)
print(x)
print(y)

x = -4
y = abs(x)
print(x)
print(y)

s1 = ""
s2 = " "
s3 = "A B C"
print(len(s1))
print(len(s2))
print(len(s3))

s = "Abracadabra Hocus Pocus you're a turtle dove"
#Is there a lower case 't' in the string above?
print("t" in s)
#Is there an upper case 'T' in the string above?
print("T" in s)
#Is there no upper case 'T' in the string above?
print("T" not in s)
#Print 15 hyphens in a row
print("-" * 15)
#What is first character in the string above?
print(s[0])
#Print chars 33-39 from above?
print(s[33:39])
#Print every third char from string above?
print(s[0:44:3]) 
#Print lowest character is s
print(min(s))
#Print max character is s
print(max(s))
#Where is the first uppercase P
print(s.index("P"))
#Where is lowercase 'o' in latter half of string?
print(s.index("o"),22,44)
#How many lower case 'a's
print(s.count("a"))

s1 = "There is no such word as schmeedledorp"
s2 = " a b c"
s3 = "ABC"
s4 = "hogan"
# Capatilize only first letter
print(s3.capitalize())
# Count the number of spaces in s1
print(s1.count(" "))
# Find the '.' in s4
print(s4.find("."))
# Is s2 all lowercase letters
print(s2.islower())
# Convert all s3 to lowercase
print(s3.lower())
# String leading characters from s2
print(s2.lstrip())
# String leading and trailing characters from s2
print(s2.strip())
# Swap the case of letters in s1
print(s1.swapcase())
# Show s1 in title case
print(s1.title())
# Show s1 uppercase
print(s1.upper())
# Define new class member
class Member:
    def __init__(self, username, fullname):
      self.username = username
      self.fullname = fullname
      self.date_joined = dt.date.today()
      self.is_active = True

    def show_datejoined(self):
        return f"{self.fullname} joined on {self.date_joined:%m/%d/%y}"

new_guy = Member('Hogan', 'Asher Hogan')
print(new_guy.show_datejoined())


