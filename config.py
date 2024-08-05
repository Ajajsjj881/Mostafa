import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
que = {}
SESSION_NAME = getenv("SESSION_NAME", "BACIVfMAheVGXoxKbeKvdtqc49XawSSrpmcRr2RBHOnpz2wHV57q_GtGfBaJWi15Dbrh9oUqtLl7LEYiDKJEtBT7Iks8FM5SZnT-9uXNueTRQ4ZhgrJ9wNo7ZfEXaNtLcCdc9tc73_FH2Xz5mOYrZR2mMfEoSfMlBIJ_HVBVAnQK6nZqVahEOknnFrsfvrKfr4h7oq4JjUfUoYHf_kV02WEIhBvCrZqeog8al_WwrNR0XS4W-dHaPESVjay4L4DFfNtxyzg2QsoEVxC-Li1YxlqLWfbSAFdoFB-aBWkX3I6cg9GsV3xjMr6vtQ9RBhdtL2vbpAja84OhBICgaahp0FoTbLKzqgAAAAG5Qi-yAA")
BOT_TOKEN = getenv("BOT_TOKEN", "7132844561:AAGn1sXPuM0cS1-fNidqypDKGsgelgMn0DY")
BOT_NAME = getenv("BOT_NAME", "ميوزك هليام")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/6d31d6b18722ce94521cb.jpg")
THUMB_IMG = getenv("THUMB_IMG", "https://telegra.ph/file/6d31d6b18722ce94521cb.jpg")
AUD_IMG = getenv("AUD_IMG", "https://telegra.ph/file/6d31d6b18722ce94521cb.jpg")
QUE_IMG = getenv("QUE_IMG", "https://telegra.ph/file/6d31d6b18722ce94521cb.jpg")
admins = {}
API_ID = int(getenv("API_ID", "25207641"))
API_HASH = getenv("API_HASH", "1fbb9045e33f79412ee946213bb30eff")
BOT_USERNAME = getenv("BOT_USERNAME", "Muic_2003BOT")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "JS7SS")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "xv00v")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "xv00v")
OWNER_NAME = getenv("OWNER_NAME", "JS7SS") 
DEV_NAME = getenv("DEV_NAME", "JS7SS")
PMPERMIT = getenv("PMPERMIT", None)

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "250"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6552505459").split()))
