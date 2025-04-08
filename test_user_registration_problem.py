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



