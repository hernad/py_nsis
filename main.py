import sys
from flask import Flask, render_template
from waitress import serve
import webbrowser
from threading import Thread
import socket
from time import sleep

app = Flask(__name__)
already_open = False

#@app.route('/greeting')
#def greeting():
#    msg = "Hello from flask"
#    return render_template("app.html", greeting=msg)

@app.route('/hello')
def hello():
    return "hello"


def isOpen(ip,port):
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   try:
      s.connect((ip, int(port)))
      s.shutdown(2)
      return True
   except:
      return False

def web_open():
    print("otvaram")
    webbrowser.open_new_tab("http://localhost:5000/hello")


def web_open_pdf():
    print("otvaram pdf")
    #webbrowser.open("file:///C:/Users/ernad.husremovic.SA/Downloads/9781801070119-PYTHON_FOR_GEEKS.pdf")
    webbrowser.open_new_tab("file:///C:/Users/ernad.husremovic.SA/Downloads/9781801070119-PYTHON_FOR_GEEKS.pdf")




def serve_app():
    global already_open
    if isOpen('127.0.0.1', 5000):
        print("port 5000 je vec otvoren!?")
        already_open = True
        exit()
    print("serviram v7")
    serve(app, host='127.0.0.1', port=5000)


if __name__ == '__main__':
    #app.run()
    #serve(app, host='127.0.0.1', port=5000)
    print(sys.version)
    threads = Thread( target= serve_app)
    thread = Thread(target = web_open)
    thread2 = Thread(target = web_open_pdf)
    threads.start()

    sleep(1)
    if not already_open:
        thread2.start()
        thread.start()
        

     
    