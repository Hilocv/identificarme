from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hey {}

BIENVENIDO to {}

Bot programado para saber cuál es tu id de Telegram o algún grupo

🤖
By @nautaii
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton(text="💚 PRINCIPAL💚", callback_data="home")],
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("🤖CAMBIOS🤖", url="https://t.me/stikerino")],
        [
            InlineKeyboardButton("👁️HELP👁️", callback_data="help"),
            InlineKeyboardButton("✋ INFO✋", callback_data="about")
        ],
        [InlineKeyboardButton("♥ DESARROLLADOR♥", url="https://t.me/nautaii")],
        [InlineKeyboardButton("SOPORTE", url="https://t.me/stikerino")],
    ]

    # Help Message
    HELP = """
**Help & Features**

1)Envíe cualquier mensaje para obtener su identificación.
2) Reenvíe cualquier mensaje de cualquier usuario/bot/canal o administradores anónimos para obtener ID.
3) Envíe cualquier pegatina para obtener ID de etiqueta.
4) Use el modo en línea para enviar su identificación en cualquier chat.
5) Agregue el grupo / canal para obtener ID.
6) Comando de uso /id:
- En privado: para obtener identificación a través del nombre de usuario
- En grupo/canal: para obtener la identificación de ese chat.

✨ COMANDOS ✨

/id - Obtener (ID)
/about - Información
/help - Mensaje de ayuda
/start - Inicia el bot
    """

    # About Message
    ABOUT = """
**About This Bot** 

BOT PROGRAMADO PARA SABER EL ID. by @nautaii

Programandor : @nautaii
    """
