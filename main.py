import string


class PasswordValidator:
    def __init__(self, min_length=12, min_sets=3):
        self.min_length = min_length
        self.min_sets = min_sets
        self.char_sets = [
            set(string.digits),
            set(string.ascii_uppercase),
            set(string.ascii_lowercase),
            set('#@(?$0')
        ]

    def validate_password(self, password):
        if len(password) < self.min_length:
            return False

        num_sets = sum(1 for char_set in self.char_sets if any(char in char_set for char in password))
        if num_sets < self.min_sets:
            return False

        return True
