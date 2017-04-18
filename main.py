#!/usr/bin/env python

from __future__ import unicode_literals
from flask import Flask, jsonify, request
import youtube_dl

app = Flask(__name__)

ydl_opts = {
  'format': 'bestaudio/best',
  'outtmpl': '/music/%(title)s-%(id)s.%(ext)s',
  'ignoreerrors': True,
}

def prepare_filename(ydl, info):
  info['url'] = ydl.prepare_filename(info)
  return info

def add_filename(ydl, info):
  if '_type' in info and info['_type'] is "playlist":
    info['entries'] = [prepare_filename(ydl, entry) for entry in info['entries'] if entry != None]
  else:
    info['url'] = ydl.prepare_filename(info)

def get_video(video_url, download=False, filename=False):
  with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(video_url, force_generic_extractor=False, download=download)

    if download or filename:
      add_filename(ydl, info)

    return info

@app.route("/")
def hello():
  return "Hello World!"

@app.route("/info")
def video_info():
  video_id = request.args.get('v', '')
  hasFilename = bool(request.args.get('filename', ''))
  return jsonify(get_video(video_id, download=False, filename=hasFilename))

@app.route("/download")
def video_download():
  video_id = request.args.get('v', '')
  return jsonify(get_video(video_id, download=True))

if __name__ == "__main__":
  app.run()
