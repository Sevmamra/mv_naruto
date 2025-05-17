import os

class Config(object):
    # Telegram Bot ka token
    BOT_TOKEN = "7734880223:AAGnNR-dX9tnPWH2gU3xKdCtAhd_zCRghy8"
    # Telegram API ki ID
    API_ID = 26797881
    # Telegram API ki hash key
    API_HASH = "9699262c708c2e45ba18bfce925ed5ed"
    # Admin users ki IDs (comma se separate ki hui)
    ADMIN = '6567162029'.split(',')
    # Admin IDs ko integer list mein convert karna
    ADMIN_ID = [int(id) for id in ADMIN]
    # MongoDB database ka URL
    DB_URL = "mongodb+srv://sevmamra01:<db_password>@cluster0.ff29e.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    # Database ka naam
    DB_NAME = "MY_BOT_DB"
    # Text log channel ki ID
    TXT_LOG = -1002303981738
    # Authentication log channel ki ID
    AUTH_LOG = -1002303981738
    # Hit log channel ki ID
    HIT_LOG = -1002303981738
    # DRM dump channel ki ID
    DRM_DUMP = -1002303981738
    # Main channel ki ID
    CHANNEL = -1002303981738
    # Channel ka link
    CH_URL = "https://t.me/+sYOgy9ZgCZRhYTNl"
    # Bot ke owner ka Telegram link
    OWNER = "https://t.me/Ganshyamv"
    # Thumbnail image ka URL
    THUMB_URL = "https://telegra.ph/file/example-thumb-image.jpg" #Replace by with your Thumb URL
    # API host ka URL
    HOST = "https://www.masterapi.tech/"

