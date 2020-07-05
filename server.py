

from flask import Flask, request
app = Flask(__name__)

import pymysql
def insert_data(hi1, hi2):
     connection = pymysql.connect(host="localhost", user="root", passwd="password", database="hamus")
     cursor = connection.cursor()
     sql = "INSERT INTO users2 (name, ip) VALUES (%s, %s)"
     val = (hi1, hi2) 
     cursor.execute(sql, val)
     connection.commit() 
     connection.close()


@app.route('/')
def hello():
    return "\nHello World!"
@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

@app.route('/', methods=['POST'])
def hamus_turkey():
    to_echo = request.args.get("echo", "")
    ipu = request.remote_addr
    file1 = open("myfile.txt", "a")  # write mode
    file1.write(to_echo + ": " + ipu + '\n')
    insert_data(to_echo, ipu) 
    file1.close()
    return "very good"

if __name__ == '__main__':
    app.run()


