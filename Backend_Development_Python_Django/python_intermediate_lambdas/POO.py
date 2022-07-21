
class User:

    def __init__(self, name, last_name, email):
        self.name = name
        self.last_name = last_name
        self.email = email

def run():
    pablo = User("Pablo", "Calderon", "asdfdasf")


if __name__ == '__main__':
    run()