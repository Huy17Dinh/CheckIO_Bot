import json



def read_credentials():
    secrets = 'secrets.json'
    with open(secrets) as f:
        keys = json.loads(f.read())
        return keys


class CheckIOSolver:

    def __init__(self, login, password):
        # init function is a special function in python when we created a class. 
        # init function will executed everytime a new object is created
        self.login = login
        self.password = password


if __name__ == '__main__':
    credentials = read_credentials()
    bot = CheckIOSolver(credentials['username'], credentials['password'])
    # at this stage, we can created our objects
    print(bot.password)