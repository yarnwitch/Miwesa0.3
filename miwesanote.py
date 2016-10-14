import socket
import time
from utils import translate
from beauty import get, get_card


class Bot(object):

    def __init__(self, host, port, chan, nick, ident, realname):
        self.host = host
        self.port = port
        self.chan = chan
        self.nick = nick
        self.ident = ident
        self.realname = realname
        self.recv_buffer = ''
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        self.socket.connect((self.host, self.port))
        self.send('NICK {}\r\n'.format(self.nick))
        self.send('USER {} {} bla :{}\r\n'.format(self.ident, self.host, self.realname))
        time.sleep(3)
        self.send('JOIN {}\r\n'.format(self.chan))
        self.send('JOIN {}\r\n'.format('#teahouse'))
        self.message('NickServ', 'IDENTIFY regvl4t1on')

    def send(self, msg):
        self.socket.send(bytes('{}\r\n'.format(msg), 'UTF-8'))
        print('send: ' + msg)

    def recv(self):
        self.recv_buffer = self.socket.recv(1024).decode('UTF-8')
        temp = str.split(self.recv_buffer, '\n')

        for line in temp:
            try:
                line = str.rstrip(line)
                line = str.split(line)

                if (line[0] == 'PING'):
                    self.send('PONG {}'.format(line[1]))
            except:
                pass
        print('recv: ' + self.recv_buffer)

    def message(self, chan, msg):
        self.send('PRIVMSG {} : {}'.format(chan, msg))

    def main(self):
        msg = translate(self.recv_buffer)

        if msg['command'] == 'PRIVMSG':
            time.sleep(0.5)
            sender = msg['nick']
            channel = msg['params'][0].lower()
            message = msg['params'][1].lower()

            if self.nick.lower() in message:

                if 'hello' in message or 'hey' in message or 'hi' in message or 'sup' in message or 'howdy' in message or 'greeting' in message:
                    output = 'hello!'

                elif 'help' in message or '!help' in message:
                    output = ['Right now I\'m learning to take notes for people who aren\'t online! I can also read various information from a haindl deck for you! I\'m working on doing many spreads, but right now I can only do 3spread, 5spread, and lovespread! I can also read one card if you just say haindl after my name. I don\'t want to compete with the other bots, so I will only answer you if you address me directly, okay? You can ask me for more details on haindl and spreads by typing "help haindl" to me or "help spread" to me.']
                
                elif 'spread' in message:
                    if '5' in message or 'five' in message:
                        if 'haindl+v' in message:
                            output = get('haindl+v', '5spread')
                        elif 'haindl++' in message:
                            output = get_card('haindl++', '5spread')
                        elif 'haindl+' in message:
                            output = get_card('haindl+', '5spread')
                        else:
                            output = get_card('haindl', '5spread')
                    elif '10' in message or 'ten' in message:
                        output = get_card('haindl', '10spread')
                    elif 'love' in message or 'boyfriend' in message or 'girlfriend' in message or 'bf' in message or 'gf' in message:
                        output = get_card('haindl', 'lovespread')
                    elif 'hagall' in message:
                        output = get_card('haindl', 'hagall')
                    elif 'spirit' in message:
                        output = get_card('haindl', 'spiritual')
                    elif 'direction' in message:
                        output = get_card('haindl', 'wind')
                    else:
                        output = get_card('haindl', '3spread')

                    
                    

                elif 'quote' in message:
                    output = get('quote')

                elif 'book' in message:
                    output = get('book')
                    
                elif '3ndu5t' in message:
                    output = msg['params'][1].rsplit(' ', 1)[0]  + '\r\n'

                else:
                    output = get_card('haindl', 'single')
                    
                    if sender.lower() == 'soduvvengahaw':
                        output != '79287'
                        
                    elif 'fuck y' in message or 'fuck off' in message or 'fuck thy' in message or 'fuck thee' in message or 'fuck thine' in message or 'fuck Deltabot' in message:
                        output = 'I-i-i-i\'m really sorry...'

                self.message(channel, '{}: {}'.format(sender, output))

        print('msg: ' + str(msg))

bot = Bot(host='irc.sorcery.net', port=9000, chan='#teahouse',
          nick='miwesa', ident='miwesa', realname='miwesa')
bot.connect()

while 1:
    bot.recv()
    bot.main()