import secrets
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

def save_password_to_file(password, filename):
    with open(filename, 'a') as file:
        file.write(password + '\n')

def main():
    num_passwords = int(input("Enter the number of passwords to generate: "))
    password_length = int(input("Enter the length of each password: "))
    save_to_file = input("Do you want to save passwords to pass.txt? (y/n): ").lower() == 'y'

    if save_to_file:
        file_name = 'pass.txt'
    else:
        file_name = None

    for _ in range(num_passwords):
        password = generate_password(password_length)
        print(f"Generated Password: {password}")

        if save_to_file:
            save_password_to_file(password, file_name)

if __name__ == "__main__":
    main()
