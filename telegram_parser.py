from telethon import TelegramClient, events



def telegram_parser(send_message_func=None, loop=None):

    # Параметры из my.telegram.org
    #Я сначла случайно свои слил((
    api_id = 'your_api_id by kolya'
    api_hash = 'your_api id by kolya'

    # Канал источник новостей @prime1
    channel_source = 'https://t.me/prime1'

    # Сессия клиента telethon
    session = 'gazp'

    client = TelegramClient(session, api_id, api_hash, loop=loop)
    client.start()

    @client.on(events.NewMessage(chats=channel_source))
    async def handler(event):
        '''Забирает посты из телеграмм каналов и посылает их в наш канал'''

        if send_message_func is None:
            print(event.raw_text, '\n')
        else:
            await send_message_func(f'@prime1\n{event.raw_text}')

    return client


if __name__ == "__main__":

    client = telegram_parser()

    client.run_until_disconnected()
