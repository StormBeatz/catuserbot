from sample_config import Config


class Development(Config):
    # get this values from the my.telegram.org
    APP_ID = 22397349
    API_HASH = "5073fa415c2c34cbebf0401c25fe3ce1"
    # the name to display in your alive message
    ALIVE_NAME = "𝐍ɪᴋʜɪʟ ᥫ᭡"
    # create any PostgreSQL database (i recommend to use elephantsql) and paste that link here
    DB_URI = "postgres://jfgubssg:5cLUNg8lS-WdM3CIMI4ca6bO9819zBLs@berry.db.elephantsql.com/jfgubssg"
    # After cloning the repo and installing requirements do python3 stringsetup.py an fill that value with this
    STRING_SESSION = "1BVtsOLgBux95RaY4xJCeY-t3JlSZwpuI5YNyEe-_ulmUm_va_n5ak3EqbeS-skvweb5bfke_Jvh1Dpwt6Yd117ti8tVxa5kAKy_5Z7v3NfhDCB7ZF8e592KMxwZlt07iglflFVz18EaZ1Ft3OTxM57rhP0COV9GlHvFueKrjaM7-kOdt7iHBNAqAzCP1X4jY7lTGjh4Et2E03Xkecm_Zv07xELerMYBuXOU4F1lzWx2szYLBQAtb0Ff1nCfp-kIGIAzKps-YiB3DEPy0cMAHHdp-6-CuBzTecw2cQ5YKQV8csjpQxwySIhd0prrZ-VW7Yq2_bxB4YlRMu8PTGGp8NtheW6rhTqI="
    # create a new bot in @botfather and fill the following vales with bottoken
    TG_BOT_TOKEN = "6660105397:AAG0FGSX6GUaMiOm4a0OSC10fKIhR_0AnJY"
    # create a private group and a rose bot to it and type /id and paste that id here (replace that -100 with that group id)
    PRIVATE_GROUP_BOT_API_ID = -1001960397203
    # command handler
    COMMAND_HAND_LER = "."
    # command hanler for sudo
    SUDO_COMMAND_HAND_LER = "."
    # External plugins repo
    EXTERNAL_REPO = "https://github.com/TgCatUB/CatPlugins"
    # if you need badcat plugins set "True"
    BADCAT = "False"
