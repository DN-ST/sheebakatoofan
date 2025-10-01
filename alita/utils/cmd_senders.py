from alita.bot_class import Alita
from alita.utils.msg_types import Types
from alita import bot

async def send_cmd(client: Alita, msgtype: int):
    GET_FORMAT = {
        Types.TEXT.value: client.send_message,

    }
    return GET_FORMAT[msgtype]

