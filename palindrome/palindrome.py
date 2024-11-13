def is_palindrome(str_to_check):
    filtered_chars = [char.lower() for char in str_to_check if char.isalnum()]
    return filtered_chars == filtered_chars[::-1]


