from minecraft.networking.connection import Connection
from minecraft.networking.packets import Packet
from minecraft.networking.packets.clientbound.play import ChatMessagePacket

def handle_chat_packet(chat_packet):
    print(f"Received message: {chat_packet.json_data}")

# Replace with your server's address and port
server_address = 'your.server.address'
server_port = 25565

# Replace with your Minecraft account's username and password
username = 'your_username'
password = 'your_password'

connection = Connection(
    server_address,
    server_port,
    username=username,
    auth_token=None
)

connection.register_packet_listener(handle_chat_packet, ChatMessagePacket)

# Connect to the server
connection.connect()

try:
    while True:
        packet = connection.read_packet()
except KeyboardInterrupt:
    connection.disconnect()
    print("Bot disconnected.")
