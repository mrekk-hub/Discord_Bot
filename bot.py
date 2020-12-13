import io

import aiohttp
import discord
from PIL import Image, ImageDraw, ImageFont

import pass_gen


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.startswith('Hello'):
            await message.channel.send('Hello! \nUse prefix "$" before commands')

        if message.content.startswith('$password'):
            await message.channel.send('Choose password type: regular, with special symbols(special) or verbal')

        if message.content.startswith('$regular'):
            await message.channel.send("Send password's length")
            f = False
            while f is False:
                try:
                    n = await self.wait_for('message')
                    f = True
                    await message.channel.send(f'Your password: {pass_gen.code(int(n.content))}')
                except ValueError:
                    f = False
                    await message.channel.send('Length must be a number. Try again.')

        if message.content.startswith('$verbal'):
            await message.channel.send("Send password's length")
            f = False
            while f is False:
                try:
                    n = await self.wait_for('message')
                    f = True
                    await message.channel.send(f'Your password: {pass_gen.verbal(int(n.content))}')
                except ValueError:
                    f = False
                    await message.channel.send('Length must be a number. Try again.')

        if message.content.startswith('$special'):
            await message.channel.send("Send password's length")
            f = False
            while f is False:
                try:
                    n = await self.wait_for('message')
                    f = True
                    await message.channel.send(f'Your password: {pass_gen.code_s(int(n.content))}')
                except ValueError:
                    f = False
                    await message.channel.send('Length must be a number. Try again.')

        if message.content.startswith('$url'):
            await message.channel.send(
                "Send your text's color(red, black, white, blue or grey),\n your text and url")

            m = await self.wait_for('message')
            a = await self.wait_for('message')
            b = await self.wait_for('message')
            c = await self.wait_for('message')
            async with aiohttp.ClientSession() as session:
                async with session.get(c.content) as resp:
                    if resp.status != 200:
                        return await message.channel.send('Could not download file...')
                    image_file = io.BytesIO(await resp.read())
                    im, txt_up, txt_down, pallet = Image.open(image_file), a.content, b.content, {'red': '#FF0000',
                                                                                                  'black': '#000000',
                                                                                                  'white': '#FFFFFF',
                                                                                                  'blue': '#0000FF',
                                                                                                  'grey': '#C0C0C0'}
                    font = ImageFont.truetype(r'C:\Users\MAX-Ryzen\Desktop\Roboto\Font.ttf', size=75)
                    draw_text = ImageDraw.Draw(im)
                    # lower text
                    width, height = draw_text.textsize(txt_down, font=font)
                    position_down: tuple = ((im.width - width) / 2, im.height - 100)
                    draw_text.text(position_down, txt_down, font=font, fill=pallet[m.content])
                    # upper text
                    position_up: tuple = ((im.width - width) / 2, im.height - 1070)
                    draw_text.text(position_up, txt_up, font=font, fill=pallet[m.content])
                    # converting to bytes
                    image_content = io.BytesIO()
                    im.seek(0)
                    im.save(image_content, format='JPEG')
                    image_content.seek(0)
                    await message.channel.send(file=discord.File(image_content, 'cool_image.png'))

        if message.content.startswith('$file'):
            await message.channel.send(
                "Send your text's color(red, black, white, blue or grey),\n text and path to your image file")

            m = await self.wait_for('message')
            cont = m.content.split()
            color, pallet = cont[0], {'red': '#FF0000', 'black': '#000000', 'white': '#FFFFFF', 'blue': '#0000FF',
                                      'grey': '#C0C0C0'}
            im, txt = Image.open(cont[-1]), ' '.join(cont[1:len(cont) - 1])
            font = ImageFont.truetype(r'C:\Users\MAX-Ryzen\Desktop\Roboto\Font.ttf', size=75)
            draw_text = ImageDraw.Draw(im)
            width, height = draw_text.textsize(txt, font=font)
            position: tuple = ((im.width - width) / 2, im.height - 100)
            draw_text.text(position, txt, font=font, fill=pallet[color])
            image_content = io.BytesIO()
            im.seek(0)
            im.save(image_content, format='JPEG')
            image_content.seek(0)
            await message.channel.send(file=discord.File(image_content, 'cool_image.png'))


client = MyClient()
client.run('Token here')
