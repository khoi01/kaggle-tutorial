
class UserRepository(object):
    @staticmethod
    def listUsers():
        return [
            {"username":"admin",
             "password":"password",
             "token":"AdminD#$$FIDIU"},
                  {"username":"user",
             "password":"user",
             "token":"User#$FFFEF"}
        ]
    