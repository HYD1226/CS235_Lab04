from flask import Flask

main = Flask(__name__)


@main.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    main.run()
