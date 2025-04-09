import re

def validate_first_and_last_name(First_Name):
    """
    Function to validate the first and last name
    :param First_Name:
    :return: bool value based on the condition matches
    """
    pattern = r"^[A-Z][a-z]{2,}$"
    return bool(re.fullmatch(pattern, First_Name))


<<<<<<< HEAD
def validate_email_id(mail):
    """
    Function to check the given mail id is correct or false
    :param mail:
    :return: bool value based on the condition matches
    """
    pattern = r"^[a-z]+(\.[a-z0-9]+)?@[a-z]+\.[a-z]{2,3}(\.[a-z]{2})?$"

    return bool(re.fullmatch(pattern, mail))


=======
>>>>>>> 1b6bcb3 (Implemented the test file for user registration problem)
def validate_mobile_number(mobile_number):
    """
    Validate the given mobile number is valid or not
    :param mobile_number:
    :return: bool value based on the condition matches
    """
    pattern = r"^91\s[6-9]\d{9}"

    return bool(re.fullmatch(pattern, mobile_number))


def validate_password(password):

    """
    Function validates the given password and checks whether the password is following the rules
    :param password:
    :return: bool value based on the condition matches
    """

    #usecase-5
    if len(password)<8:
        return False

    #usecase-6
    if not re.search(r"[A-Z]", password):
        return False

    #usecase-7
    if not re.search(r"\d", password):
        return False

    # usecase-8
    if len(re.findall(r"[!@#$%^&*()_+=\-{}\[\]:;\"'<>,.?/]", password)) != 1:
        return False

    return True


def validate_email_samples(email):
    pattern = r"^[a-zA-Z0-9]+([._+-]?[a-zA-Z0-9]+)*@[a-zA-Z0-9-]+(\.[a-zA-Z]{2,}){1,2}$"
    return re.match(pattern, email) is not None

if __name__ == '__main__':

    First_Name = input("Enter your first name :")
    print(validate_first_and_last_name(First_Name))

    last_name = input("Enter your last name :")
    print(validate_first_and_last_name(last_name))

<<<<<<< HEAD
    mail_id = input("Enter your mail id: ")
    print(validate_email_id(mail_id))

=======
>>>>>>> 1b6bcb3 (Implemented the test file for user registration problem)
    mobile_number = input("Enter your mobile number: ")
    print(validate_mobile_number(mobile_number))

    password = input("Enter your password :")
    print(validate_password(password))

    email_sample = input("Enter the email sample : ")
    print(validate_email_samples(email_sample))










