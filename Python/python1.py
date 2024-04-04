
def generate_random_char(sets):
   chosen_set = random.choice(sets)
   return random.choic(chosen_set) 

def generate_strong_password(length, include_lower, include_upper, include_digits, include_symbols):
   character_sets = []
   if include_lower:
       character_sets.append("abcdefghijklmnopqrstuvwxyz")
   if include_upper:
       character_sets.append("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
   if include_digits:
       character_sets.append("0123456789")
   if include_symbols:
       character_sets.append("!@#$%^&*()_+-=[]{}|;':\",.<>/?")

   password = ""
   for _ in range(length):
       password += generate_random_char(character_sets)

   return password

desired_length = int(input("Enter the desired password length: "))
include_lowercase = True if input("Include lowercase letters? (y/n): ") == "y" els False  
include_uppercase = True if input("Include uppercase letters? (y/n): ") == "y" else False
include_numbers = True if input("Include numbers? (y/n): ") == "y" else False
include_symbols = True if input("Include symbols? (y/n): ") == "y" else False

password = generate_strong_password(desired_length, include_lowercase, include_uppercase, include_numbers, include_symbols)
print("\nGenerated password:", password)
