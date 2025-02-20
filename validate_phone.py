import re

# Does a string contain a phone number?
def has_phone_number(input_string):
    pattern = r"\d{3}-\d{3}-\d{4}"
    if re.search(pattern, input_string):
        return True
    return False
    

# Get a phone number back from a string
def get_phone_number(input_string):
    phone_number = ""
    pattern = r"\d{3}-\d{3}-\d{4}"
    # Need the .group(0) to get the matched string for return. Could use match?
    try:
        phone_number = (re.search(pattern, input_string)).group(0)
    except: return None #Try/Except handles none case.
    return phone_number


# Gets and returns all phone numbers from an inputed string
def get_all_phone_numbers(input_string):
    phone_numbers = []
    pattern = r"\d{3}-\d{3}-\d{4}"
    phone_numbers += (re.findall(pattern, input_string))
    return(phone_numbers)

# Hide all numbers in a phone number except the last 4 digits. An example of this looks like: XXX-XXX-1234
def hide_phone_numbers(input_string):
    pattern = r"(\d{3})-(\d{3})-(\d{4})"
    replace_str = r"XXX-XXX-\g<3>"
    hidden_phones = ""
    hidden_phones += re.sub(pattern, replace_str, input_string)
    return hidden_phones


# Get the string of the phone number and format it for our pretend application. Ensure all of the phone numbers use dashes for delimiters.
# Example: 312-111-2222, 312.111.2222, (312) 111-2222 would all be 312-111-2222
def format_phone_number(input_string):
    pattern = r".?(\d{3}).?.?(\d{3}).?(\d{4})"
    replace_str = r"\g<1>-\g<2>-\g<3>"
    reformated_phones = ""
    # Right hand regex generates a str, but numbers are jammed right after comma.
    # Re-run regex and get "," into ", "...if it's stupid and it works...
    reformated_phones += re.sub(',', ', ', re.sub(pattern, replace_str, input_string))
    return reformated_phones

# The grossest Regex: (((\d{3})[\S?](\d{3})[\S?](\d{4}))|(\d{3}).?(\d{3}).?(\d{4}))
# .?(\d{3}).?.?(\d{3}).?(\d{4})
