
import random

def generatePassword(pwlength):
    """
    Generate a list of random passwords with specified lengths.

    Parameters:
        pwlength (list): A list containing the desired lengths of passwords.

    Returns:
        list: A list of randomly generated passwords.
    """
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    passwords = []

    for i in pwlength:
        password = ""
        for j in range(i):
            next_letter_index = random.randrange(len(alphabet))
            password = password + alphabet[next_letter_index]

        password = replaceWithNumber(password)
        password = replaceWithUppercaseLetter(password)

        passwords.append(password)

    return passwords


def replaceWithNumber(pword):
    """
    Replace one or two random characters in the password with a random digit.

    Parameters:
        pword (str): The input password.

    Returns:
        str: The password with one or two random characters replaced by a digit.
    """
    for i in range(random.randrange(1, 3)):
        replace_index = random.randrange(len(pword) // 2)
        pword = pword[0:replace_index] + str(random.randrange(10)) + pword[replace_index + 1:]
    return pword


def replaceWithUppercaseLetter(pword):
    """
    Replace one or two random characters in the password with a random uppercase letter.

    Parameters:
        pword (str): The input password.

    Returns:
        str: The password with one or two random characters replaced by an uppercase letter.
    """
    for i in range(random.randrange(1, 3)):
        replace_index = random.randrange(len(pword) // 2, len(pword))
        pword = pword[0:replace_index] + pword[replace_index].upper() + pword[replace_index + 1:]
    return pword


def main():
    """
    Main function to generate passwords based on user input.

    This function asks the user for the number of passwords to generate and their desired lengths.
    It then generates random passwords and displays them.
    """
    numPasswords = int(input("How many passwords do you want to generate? "))
    print("Generating " + str(numPasswords) + " passwords")

    passwordLengths = []
    print("Minimum length of password should be 3")

    for i in range(numPasswords):
        length = int(input("Enter the length of Password #" + str(i + 1) + " "))
        if length < 3:
            length = 3
        passwordLengths.append(length)

    Password = generatePassword(passwordLengths)

    for i in range(numPasswords):
        print("Password #" + str(i + 1) + " = " + Password[i])

if __name__ == "__main__":
    main()
