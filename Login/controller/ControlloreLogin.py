from Login.model.loginModel import loginModel


class ControlloreLogin():

    def __init__(self):
        super(ControlloreLogin, self).__init__()
        self.model = loginModel()

    def hide_or_show_pw(self, vista):
        self.model.hide_or_show_pw(vista)

    def login(self, pw):
        return self.model.login(pw)
