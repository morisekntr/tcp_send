from scapy.all import IP, TCP, send

# 送信先のIPアドレスとポートを指定
destination_ip = "192.168.1.100"  # ここに送信先のIPアドレスを入力
destination_port = 80            # ここに送信先のポートを入力

# 16進数で表されたTCPペイロードをユーザーに入力してもらう
hex_payload = input("Enter the hexadecimal payload: ")

# 16進数文字列をバイナリデータに変換
binary_payload = bytes.fromhex(hex_payload)

# IPレイヤーとTCPレイヤーを構築
ip_layer = IP(dst=destination_ip)
tcp_layer = TCP(dport=destination_port)

# パケットを作成し、バイナリペイロードを追加
packet = ip_layer / tcp_layer / binary_payload

# パケットを送信
send(packet)
