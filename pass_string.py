from colorama import Fore, Style, init
import string

# Initialize Colorama
init(autoreset=True)


# Load common password dataset
def load_password(file_path):
    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as file:
            return set(line.strip().lower() for line in file)

    except FileNotFoundError:
        print(Fore.RED + "[!] Password dataset not found!")
        exit()


common_passwords = load_password("Arabic_common-password-list-top-487.txt")

# User Input
password = input(Fore.CYAN + "Enter your password: ")

print("\n" + Fore.YELLOW + "Password Analysis")
print("-" * 30)

# Check against common password list
if password.lower() in common_passwords:
    print(Fore.RED + "[!] This password exists in a common password dataset!")
    print(Fore.RED + "[!] Estimated crack time: Instantly")
    exit()

# Variables
score = 0
charset_size = 0

lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
digits = string.digits
symbols = string.punctuation

# Length Check
if len(password) >= 8:
    score += 1
    print(Fore.GREEN + "[+] Good password length")
else:
    print(Fore.RED + "[-] Password should be at least 8 characters long")

# Lowercase Check
if any(c.islower() for c in password):
    charset_size += len(lowercase)
    print(Fore.GREEN + "[+] Contains lowercase letters")

# Uppercase Check
if any(c.isupper() for c in password):
    charset_size += len(uppercase)
    score += 1
    print(Fore.GREEN + "[+] Contains uppercase letters")

# Number Check
if any(c.isdigit() for c in password):
    charset_size += len(digits)
    score += 1
    print(Fore.GREEN + "[+] Contains numbers")

# Symbol Check
if any(c in symbols for c in password):
    charset_size += len(symbols)
    score += 1
    print(Fore.GREEN + "[+] Contains special characters")

# Fallback
if charset_size == 0:
    charset_size = 26

# Calculate combinations
combinations = charset_size ** len(password)

# Assume 1 billion guesses/sec
guesses_per_second = 1_000_000_000

seconds = combinations / guesses_per_second


# Convert seconds into readable format
def convert_time(seconds):
    minutes = seconds / 60
    hours = minutes / 60
    days = hours / 24
    years = days / 365

    if seconds < 60:
        return f"{seconds:.2f} seconds"

    elif minutes < 60:
        return f"{minutes:.2f} minutes"

    elif hours < 24:
        return f"{hours:.2f} hours"

    elif days < 365:
        return f"{days:.2f} days"

    else:
        return f"{years:.2f} years"


# Strength Result
print("\n" + Fore.YELLOW + "Strength Result")
print("-" * 30)

if score <= 1:
    print(Fore.RED + "TOO WEAK")

elif score == 2:
    print(Fore.YELLOW + "MEDIUM PASSWORD")

elif score == 3:
    print(Fore.BLUE + "STRONG PASSWORD")

else:
    print(Fore.GREEN + "VERY STRONG PASSWORD")

print(
    Fore.MAGENTA
    + f"Estimated time to crack the password: {convert_time(seconds)}"
)