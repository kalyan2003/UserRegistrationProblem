<<<<<<< HEAD
from user_registration_problem import validate_first_and_last_name
from user_registration_problem import validate_email_samples
from user_registration_problem import validate_password
from user_registration_problem import validate_email_id
from user_registration_problem import validate_mobile_number
import pytest


@pytest.mark.parametrize("name, output",[("Pava", True), ("Pa", False), ("pava", False), ("Pav", True)])
def test_validate_first_and_last_name(name,output):
    assert validate_first_and_last_name(name) == output


@pytest.mark.parametrize("mail,output", [
    ("pavan@gmail.co.in",True),
    ("Pavan@gmail.com",False),
    ("pavan.1996@gmail.co.in",True),
    ("pavan.@gmail.com",False)
    ])
def test_validate_email_id(mail,output):
    assert validate_email_id(mail) == output


@pytest.mark.parametrize("mobile_Number,output",[
    ("91 9939930322", True),
    ("919939930322", False),
    ("91 993993",False),
    ("9 9939930322",False),
    ("72 9989980344", False),
    ("91 1234567891",False)
])
def test_validate_mobile_number(mobile_Number,output):
    assert validate_mobile_number(mobile_Number) == output


@pytest.mark.parametrize("password,output",[
    ("Pavan@2003",True),
    ("Pavan",False),
    ("Pavan2003",False),
    ("Pavan@",False),
    ("PAVAN@2003",True),
    ("pava",False)
])
def test_validate_password(password,output):
    assert validate_password(password) == output


@pytest.mark.parametrize("email_sample, expected", [
    ("abc@yahoo.com", True),
    ("abc-100@yahoo.com", True),
    ("abc.100@yahoo.com", True),
    ("abc111@abc.com", True),
    ("abc-100@abc.net", True),
    ("abc.100@abc.com.au", True),
    ("abc@1.com", True),
    ("abc@gmail.com.com", True),
    ("abc+100@gmail.com", True),
    ("abc", False),
    ("abc@.com.my", False),
    ("abc123@gmail.a", False),
    ("abc123@.com", False),
    ("abc123@.com.com", False),
    (".abc@abc.com", False),
    ("abc()*@gmail.com", False),
    ("abc@%*.com", False),
    ("abc..2002@gmail.com", False),
    ("abc.@gmail.com", False),
    ("abc@abc@gmail.com", False),
    ("abc@gmail.com.1a", False),
    ("abc@gmail.com.aa.au", False)
])
def test_valid_email_samples(email_sample, expected):
    assert validate_email_id(email_sample) == expected



=======
import json
import pytest
from loguru import logger
from user_registration_problem import (
    validate_first_and_last_name,
    validate_email_samples,
    validate_password,
    validate_mobile_number
)

# Setup logger to log only errors
logger.add("test_validation_errors.log", rotation="1 MB", retention="10 days", level="ERROR")

# Load test data from JSON file
def load_test_data():
    with open('test_data.json', 'r') as f:
        return json.load(f)

# Extract test data
test_data = load_test_data()
valid_tuples = test_data.get('True', [])
invalid_tuples = test_data.get('False', [])

@pytest.mark.parametrize("test_tuple", valid_tuples)
def test_individual_valid_tuples(test_tuple):
    name, mobile, password, email = test_tuple

    try:
        assert validate_first_and_last_name(name), f"Valid name failed: {name}"
        assert validate_mobile_number(mobile), f"Valid mobile failed: {mobile}"
        assert validate_password(password), f"Valid password failed: {password}"
        assert validate_email_samples(email), f"Valid email failed: {email}"

    except AssertionError as e:
        logger.error(f" Validation failed for valid tuple: {test_tuple} | Reason: {str(e)}")
        raise

@pytest.mark.parametrize("test_tuple", invalid_tuples)
def test_individual_invalid_tuples(test_tuple):
    name, mobile, password, email = test_tuple

    is_name_valid = validate_first_and_last_name(name)
    is_mobile_valid = validate_mobile_number(mobile)
    is_password_valid = validate_password(password)
    is_email_valid = validate_email_samples(email)

    validation_results = [is_name_valid, is_mobile_valid, is_password_valid, is_email_valid]

    if all(validation_results):
        logger.error(f" Invalid tuple unexpectedly passed all validations: {test_tuple}")
    assert False in validation_results, f"Invalid tuple unexpectedly passed all validations: {test_tuple}"
>>>>>>> 1b6bcb3 (Implemented the test file for user registration problem)
