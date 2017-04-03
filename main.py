#!/usr/bin/env python

from __future__ import unicode_literals
from flask import Flask, jsonify, request
import youtube_dl

VIDEO_PREFIX = 'https://youtube.com/watch?v='

app = Flask(__name__)

ydl_opts = {
  'format': 'bestaudio/best',
  'outtmpl': '/music/%(title)s-%(id)s.%(ext)s',
}

def get_video(video_url, download=False):
  with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(video_url, force_generic_extractor=False, download=download)
    info['url'] = ydl.prepare_filename(info)
    return info

@app.route("/")
def hello():
  return "Hello World!"

@app.route("/info")
def video_info():
  video_id = request.args.get('v', '')
  return jsonify(get_video(video_id, download=False))

@app.route("/download")
def video_download():
  video_id = request.args.get('v', '')
  return jsonify(get_video(video_id, download=True))

if __name__ == "__main__":
  app.run()

