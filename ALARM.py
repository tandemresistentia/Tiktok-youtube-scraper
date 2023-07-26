import os
import easygui
import subprocess

if os.path.isfile(r'C:\Users\Death\Desktop\Main Uploader\TwitchDownloader\0.mp4') or os.path.isfile(r'C:\Users\Death\Desktop\Main Uploader\TwitchDownloader\1.mp4')or os.path.isfile(r'C:\Users\Death\Desktop\Main Uploader\TwitchDownloader\2.mp4'):
    easygui.msgbox("Twitch Channel has a problem", title="ALERT")
if os.path.isfile(r'C:\Users\Death\Desktop\Main Uploader\DogChannel\0.mp4'):
    easygui.msgbox("Dog Channel has a problem", title="ALERT")
if os.path.isfile(r'C:\Users\Death\Desktop\Main Uploader\CatChannel\0.mp4'):
    easygui.msgbox("Cat Channel has a problem", title="ALERT")
if os.path.isfile(r'C:\Users\Death\Desktop\Main Uploader\NBAChannel\0.mp4'):
    easygui.msgbox("NBA Channel has a problem", title="ALERT")
if os.path.isfile(r'C:\Users\Death\Desktop\Main Uploader\EuropeanFootballChannel\0.mp4'):
    easygui.msgbox("EuropeanFootballChannel has a problem", title="ALERT")
if os.path.isfile(r'C:\Users\Death\Desktop\Main Uploader\NFLChannel\0.mp4'):
    easygui.msgbox("NFLChannel has a problem", title="ALERT")
if os.path.isfile(r'C:\Users\Death\Desktop\Main Uploader\PaintingsChannel\0.mp4'):
    easygui.msgbox("PaintingsChannel has a problem", title="ALERT")
else:
    easygui.msgbox("HAVE A GOOD DAY! :)", title="ALL CLEAR")