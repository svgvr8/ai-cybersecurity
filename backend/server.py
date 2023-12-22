from flask import Flask, jsonify
from scapy.all import sniff, Ether, IP, TCP, UDP
from threading import Thread
from flask_cors import CORS  # Import CORS

app = Flask(__name__)
CORS(app)
# Store the packets
packets = []


def extract_packet_info(packet):
    packet_info = {}

    # Function to serialize complex Scapy objects
    def scapy_default(obj):
        if isinstance(obj, bytes):
            return obj.decode("utf-8", "ignore")  # Decode bytes to string
        return str(obj)  # Convert other types to string

    # Extract information from the Ethernet layer
    if Ether in packet:
        packet_info["ethernet"] = {
            "source": scapy_default(packet[Ether].src),
            "destination": scapy_default(packet[Ether].dst),
            "type": scapy_default(packet[Ether].type),
        }

    # Extract information from the IP layer
    if IP in packet:
        packet_info["ip"] = {
            "version": packet[IP].version,
            "ihl": packet[IP].ihl,
            "tos": packet[IP].tos,
            "length": packet[IP].len,
            "id": packet[IP].id,
            "flags": scapy_default(packet[IP].flags),
            "frag": packet[IP].frag,
            "ttl": packet[IP].ttl,
            "proto": packet[IP].proto,
            "checksum": packet[IP].chksum,
            "source": packet[IP].src,
            "destination": packet[IP].dst,
        }

    # Similarly, process other layers like TCP, UDP, etc., using scapy_default when necessary

    return packet_info


# Function to capture packets
def capture_packets():
    def packet_callback(packet):
        packets.append(extract_packet_info(packet))

    sniff(prn=packet_callback, count=10)  # Capturing first 10 packets


# Start packet capturing in a separate thread
Thread(target=capture_packets).start()


@app.route("/api/packets", methods=["GET"])
def get_packets():
    return jsonify(packets)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
