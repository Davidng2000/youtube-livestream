import os
import time

stream_url = "rtmp://a.rtmp.youtube.com/live2/vure-evsf-mmbc-4y5d-1dht"

while True:
    os.system(
        "ffmpeg -re -loop 1 -i static/background.jpg -c:v libx264 -tune stillimage "
        "-preset veryfast -b:v 3000k -maxrate 3000k -bufsize 6000k "
        "-pix_fmt yuv420p -g 50 -r 25 -f flv " + stream_url
    )
    time.sleep(5)
  
