from http.server import BaseHTTPRequestHandler
from minecraft.networking.connection import Connection
from minecraft.networking.packets.clientbound.play import ChatMessagePacket

class MinecraftBot:
    def __init__(self, server_address, server_port, username, password):
        self.server_address = server_address
        self.server_port = server_port
        self.username = username
        self.password = password
        self.connection = None

    def connect(self):
        self.connection = Connection(
            self.server_address,
            self.server_port,
            username=self.username,
            auth_token=None
        )
        self.connection.register_packet_listener(self.handle_chat_packet, ChatMessagePacket)
        self.connection.connect()

    def handle_chat_packet(self, chat_packet):
        print(f"Received message: {chat_packet.json_data}")

    def disconnect(self):
        if self.connection:
            self.connection.disconnect()

# Replace with your Minecraft server details
SERVER_ADDRESS = 'kaboom.pw'
SERVER_PORT = 25565
USERNAME = 'your_bot_username'

bot = MinecraftBot(SERVER_ADDRESS, SERVER_PORT, USERNAME)

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        global bot
        bot.connect()
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write('Bot started'.encode('utf-8'))
