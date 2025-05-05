from minecraft.networking.connection import Connection
from minecraft.networking.packets import ChatPacket
import time

# ➤ Ayarları buradan değiştir
host = "sunucu_ip_adresi"    # Örn: "2b2t.org.tr"
port = 25565
username = "BotNick"         # Botun görünen ismi
password = "gizliSifre123"   # /login ya da /register şifresi

# Minecraft bağlantısı oluştur
conn = Connection(host=host, port=port, username=username)

def handle_join(packet):
    print("✔ Sunucuya bağlanıldı!")
    login_command = f"/login {password}"
    conn.write_packet(ChatPacket(chat=login_command))

conn.register_packet_listener(handle_join, "minecraft:join_game")

conn.connect()
print("⏳ Bağlantı kuruluyor...")

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    conn.disconnect()
