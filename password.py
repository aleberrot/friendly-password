import sys
import random

class PasswordGenerator:
    def generate_password(self):
        """
        This method is called after the password is validated and return your new password
        """
        args = sys.argv[1:]
        if len(args) > 0:
            if len(args[0]) < 8:
                print("Provide at least 8 characters")
                return 1
            PASSWORD = ""
            while len(PASSWORD) != len(sys.argv[1]):
                PASSWORD += random.choice(sys.argv[1])
            return PASSWORD
        print("No command line argumments provided, ERROR")

new_password: PasswordGenerator = PasswordGenerator()
psw = new_password.generate_password()
print(psw)
