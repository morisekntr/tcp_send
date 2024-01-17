from scapy.all import IP, TCP, send
from scapy.layers.http import HTTPRequest  # HTTPリクエスト用
from scapy.layers.mqtt import MQTTConnect  # MQTT用

# 送信先の設定
dst_ip = "192.168.1.100"  # 送信先のIPアドレス
dst_port = 80             # 送信先のポート

# TCPパケットの基本設定
tcp_packet = IP(dst=dst_ip) / TCP(dport=dst_port)

# HTTPリクエストの例
http_packet = tcp_packet / HTTPRequest(
    Method="GET",
    Path="/",
    Http_Version="HTTP/1.1",
    Host="example.com"
)

# MQTT接続リクエストの例
mqtt_packet = tcp_packet / MQTTConnect(
    ClientId="client_id"
)

# 送信するパケットを選択
packet_to_send = http_packet  # HTTPリクエストを送信する場合
# packet_to_send = mqtt_packet  # MQTT接続を送信する場合

# パケットの送信
send(packet_to_send)

# 送信したパケットの監視（オプション）
# sniff(filter="tcp and host " + dst_ip, count=10)  # 送信先のIPアドレスに関連するTCPパケットをキャプチャ
