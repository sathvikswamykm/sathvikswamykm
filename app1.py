#importing flask module in the project is mandatory
#an object of flask class is our WSGI application.

from flask import Flask

#Flask construct takes the name of
#current module(_name_)as argument,

app=Flask(__name__)

@app.route('/')

def hello_world():
              return 'hello world'

if __name__=='__main__':
      app.run()

