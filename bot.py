import json
from khl import Bot, Cert, Message


def open_file(path: str):
    """打开path对应的json文件"""
    with open(path, 'r', encoding='utf-8') as f:
        tmp = json.load(f)
    return tmp


# 打开Token

config = open_file('./config/token.json')
bot = Bot(token=config['token'])
if not config['websocketMode']:  # webhook
    print(f"[BOT] using webhook at port {config['webhook_port']}")
    bot = Bot(cert=Cert(token=config['token'],
                        verify_token=config['verify_token'],
                        encrypt_key=config['encrypt_token']),
              port=config['webhook_port'])


if __name__ == '__main__':
    print('[Bot]启动成功')
    bot.run()
