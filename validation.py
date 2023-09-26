import re
def validate_age(age):
    try:
        age = int(age)
        if age >= 18:
            return age
        else:
            return None
    except ValueError:
        return None
    
def validate_ifsc_code(ifsc_code):
   
    if len(ifsc_code) != 11:
        return False
    
    
    if not ifsc_code[:4].isalpha() or not ifsc_code[:4].isupper():
        return False
    
     
    
    if not ifsc_code[5:11].isalnum():
        return False
    
    return True


def validate_gender(gender):
    if gender.lower() in ['male', 'female', 'other']:
        return gender
    else:
        return None
    
def validate_dob(dob):
   
    parts = dob.split('-')
    
    
    if len(parts) != 3:
        return False
    
    day, month, year = parts
    
    
    if not day.isdigit() or not month.isdigit() or not year.isdigit():
        return False
    
   
    day = int(day)
    month = int(month)
    year = int(year)
    
   
    if (day < 1 or day > 31) or (month < 1 or month > 12) or (year < 1900 or year > 2099):
        return False
    
    
    if (month == 2 and day > 29) or (month == 4 and day > 30) or (month == 6 and day > 30) or (month == 9 and day > 30) or (month == 11 and day > 30):
        return False
    
    
    if month == 2 and day > 28 and not (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
        return False
    
    return True


  
def validate_pan_card(pan_card_number):
    
    if len(pan_card_number) != 10:
        return False
    
    
    if not pan_card_number[:5].isalpha() or not pan_card_number[:5].isupper():
        return False
    
    
    if not pan_card_number[5].isdigit():
        return False
    
    
    if not pan_card_number[6:9].isdigit():
        return False
    
    
    if not pan_card_number[9].isalpha() or not pan_card_number[9].isupper():
        return False
    
    return True


  
def validate_aadhar_number(aadhar_number):
    
    if len(aadhar_number) != 12:
        return False
    
    
    if not aadhar_number.isdigit():
        return False
    
      
    return True
