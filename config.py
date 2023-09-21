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
    STRING_SESSION = "BQFVwaUAOUjv3EhDAPBFfoYereCkg3XQqZDIxPUrNIpqRvHsctpuwlqZCh-iUHMICxnKvkgvkd-K0FJO8CbFFwVzzFLgsh2fzkuYTpg8dc1Bi4JuTKNEs46hljfG82MEuBJXknYf-BHHVybsNtaz6vnrp0f_l35AwRCDW1sJcqEAQfkvVKL_zUF2qyuuIFALjoE2cJnR-h6YwqHV5g4vs_L8x9htkuQIJOwNIMuI6eysoZkF1CU5K2J7VVKkhrpG01Geg0GvxJPpV6Bl_DZuYh2licVBRDr_080sBYpBOlvADVgpa37s1heYRUIAd9g1sBxKIVeehm4yE_nBbYSbyri6OfOxKQAAAAGB-BwCAA"
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
