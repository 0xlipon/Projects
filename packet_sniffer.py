from scapy.all import sniff, IP
import tkinter as tk
from tkinter import scrolledtext

class NetworkSnifferGUI:
    def __init__(self, master):
        self.master = master
        master.title("Network Sniffer")

        self.text_area = scrolledtext.ScrolledText(master, wrap=tk.WORD, width=50, height=20)
        self.text_area.pack(padx=10, pady=10)

        self.start_button = tk.Button(master, text="Start Sniffing", command=self.start_sniffing)
        self.start_button.pack(pady=10)

    def packet_callback(self, packet):
        # Check if the packet has an IP layer
        if IP in packet:
            # Print source and destination IP addresses
            src_ip = packet[IP].src
            dst_ip = packet[IP].dst
            info = f"IP Packet: Source IP - {src_ip}, Destination IP - {dst_ip}\n"
            self.text_area.insert(tk.END, info)

    def start_sniffing(self):
        # Clear the text area before starting a new sniffing session
        self.text_area.delete(1.0, tk.END)

        # Sniffing function with a filter for IP packets
        sniff(prn=self.packet_callback, count=10)

# Create the main Tkinter window
root = tk.Tk()

# Create an instance of the NetworkSnifferGUI class
app = NetworkSnifferGUI(root)

# Run the Tkinter event loop
root.mainloop()
