#Desc: This web application serves a motion JPEG stream
# main.py
# import the necessary packages
from flask import Flask, render_template, Response, request
from camera import VideoCamera
import webbrowser
import socket

pi_camera = VideoCamera(flip=False) # flip pi camera if upside down.

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def gen(camera):
    #get camera frame
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(pi_camera),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    #webbrowser.open('http://127.0.0.1:3000', new=2)
    app.run(host='0.0.0.0', port=3000, debug=False)
    


