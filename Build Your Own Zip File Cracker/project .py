import zipfile
import itertools
import string
def brute_force_zip(zip_file, max_length):
    characters = string.ascii_letters + string.digits
    for length in range(1, max_length + 1):
        for password in itertools.product(characters, repeat=length):
            password = ''.join(password)
            if attempt_extract(zip_file, password):
                print(f"Password found: {password}")
                return password
    print("Password not found.")
    return None
def dictionary_attack(zip_file, dictionary_file):
    with open(dictionary_file, 'r') as f:
        for line in f:
            password = line.strip()
            if attempt_extract(zip_file, password):
                print(f"Password found: {password}")
                return password
    print("Password not found.")
    return None
def attempt_extract(zip_file, password):
    try:
        zip_file.extractall(pwd=password.encode())
        return True
    except:
        return False
def main(zip_path, dictionary_file=None, max_length=5):
    zip_file = zipfile.ZipFile(zip_path)
    if dictionary_file:
        print("Starting dictionary attack...")
        password = dictionary_attack(zip_file, dictionary_file)
    else:
        print("Starting brute-force attack...")
        password = brute_force_zip(zip_file, max_length)
    if password:
        print(f"Cracked! The password is: {password}")
    else:
        print("Failed to crack the zip file.")
if __name__ == "__main__":
    zip_path = "protected.zip"  # Path to your zip file
    dictionary_file = "wordlist.txt"  # Optional path to dictionary file
    max_length = 4  # Maximum length of password for brute-force
    main(zip_path, dictionary_file, max_length)
