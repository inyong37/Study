#! /usr/bin/python3
#-*- coding: utf-8 -*-
# Author: In-Yong Hwang
# Date: 2023-10-18-Wednesday
# To Install pytube: pip install pytube
# Reference: https://pytube.io/en/latest/user/streams.html#downloading-streams


def download_youtube_video(
  video_url: str='https://youtu.be/jNQXAC9IVRw?si=FyW2QN9hnnrEQeee',
  output_path: str='downloads/'
) -> None:
  from pytube import YouTube
  video = YouTube(video_url)
  stream = video.streams.get_highest_resolution()
  stream.download(output_path)
  print(f'Downloaded: {video.title} to {output_path}')
  return None


def search_and_download_youtube_video(
  query: str='cat',
  output_path: str='downloads/'
) -> None:
  from pytube import YouTube
  search_results = YouTube(f'https://www.youtube.com/results?search_query={query}')
  video_url = f'https://www.youtube.com{search_results.find_all("a", {"class": "yt-uix-tile-link"})[0]["href"]}'
  video = YouTube(video_url)
  stream = video.streams.get_highest_resolution()
  stream.download(output_path)
  print(f'Downloaded: {video.title} to {output_path}')
  return None
