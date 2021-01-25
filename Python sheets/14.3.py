class Password_manager:
    old_passwords = ['12345', 'password']

    def get_password(self):
        return self.old_passwords[-1]

    def set_password(self, password):
        inList = False
        for i in self.old_passwords:
            if i == password:
                inList = True
                break
        if not inList:
            self.old_passwords.append(password)

    def is_correct(self, password):
        if password == self.old_passwords[-1]:
            return True
        else:
            return False


manager = Password_manager()

print(manager.is_correct('password'))
print(manager.is_correct('12345'))
print(manager.get_password())
print(manager.set_password('12345'))
print(manager.set_password('112233'))
print(manager.is_correct('112233'))
