password = "Pyth0n@School2025!"

# ----------------------------------
# 1. First 4 and Last 4 Characters
# ----------------------------------

first_four = password[:4]
last_four = password[-4:]

first_has_upper = False
first_has_digit = False

for ch in first_four:
    if ch.isupper():
        first_has_upper = True
    if ch.isdigit():
        first_has_digit = True

last_has_upper = False
last_has_digit = False

for ch in last_four:
    if ch.isupper():
        last_has_upper = True
    if ch.isdigit():
        last_has_digit = True

print("First 4:", first_four)
print("Has uppercase:", "Yes" if first_has_upper else "No")
print("Has digit:", "Yes" if first_has_digit else "No")

print()

print("Last 4:", last_four)
print("Has uppercase:", "Yes" if last_has_upper else "No")
print("Has digit:", "Yes" if last_has_digit else "No")


# ----------------------------------
# 2. Count Character Types
# ----------------------------------

uppercase = 0
lowercase = 0
digits = 0
special = 0

for ch in password:

    if ch.isupper():
        uppercase += 1

    elif ch.islower():
        lowercase += 1

    elif ch.isdigit():
        digits += 1

    else:
        special += 1

print("\nCharacter Counts")
print("Uppercase:", uppercase)
print("Lowercase:", lowercase)
print("Digits:", digits)
print("Special:", special)


# ----------------------------------
# 3. Detect Repeated Patterns
#    Using find(), index(),
#    replace(), count()
# ----------------------------------

weak_pattern_found = False

for i in range(len(password) - 1):

    if password[i] == password[i + 1]:

        pattern = password[i] * 2

        print("\nRepeated Pattern Found:", pattern)

        print("find():", password.find(pattern))
        print("index():", password.index(pattern))
        print("count():", password.count(password[i]))

        modified = password.replace(pattern, "**")
        print("replace():", modified)

        weak_pattern_found = True

if not weak_pattern_found:
    print("\nNo consecutive repeated patterns found")


# ----------------------------------
# 4. Reverse String and
#    Check 3-Character Palindromes
# ----------------------------------

reversed_password = password[::-1]

print("\nReversed Password:")
print(reversed_password)

palindromes = []

for i in range(len(password) - 2):

    sub = password[i:i+3]

    if sub == sub[::-1]:
        palindromes.append(sub)

if palindromes:
    print("Palindrome substrings:", palindromes)
else:
    print("Palindrome substrings: None found")


# ----------------------------------
# 5. Mask Password
# ----------------------------------

middle_stars = "*" * (len(password) - 4)

masked_password = (
    password[:2]
    + middle_stars
    + password[-2:]
)

print("\nMasked Password:")
print(masked_password)


# ----------------------------------
# 6. Password Rating
# ----------------------------------

score = 0

# Length check
if len(password) >= 12:
    score += 1

# Character diversity
if uppercase >= 1:
    score += 1

if lowercase >= 1:
    score += 1

if digits >= 1:
    score += 1

if special >= 1:
    score += 1

# First and Last section checks
if first_has_upper and last_has_digit:
    score += 1

# No repeated pattern
if not weak_pattern_found:
    score += 1

# No palindrome patterns
if len(palindromes) == 0:
    score += 1

if score >= 7:
    rating = "Strong"
elif score >= 5:
    rating = "Medium"
else:
    rating = "Weak"

print("\nRating:", rating)
