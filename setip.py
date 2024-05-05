import tkinter as tk
import os

from tkinter import messagebox

root = tk.Tk()

root.title("Ipv4 Settings")
root.geometry('500x650')


def setip():
    if interface_entry.get() or ip_entry.get() or subnet_entry.get() or gateway_entry.get() or dns_entry.get() or dns_alternate_entry.get() != "":
        os.system(f'netsh interface ipv4 set address name="{interface_entry.get()}" static {
                  ip_entry.get()} {subnet_entry.get()} {gateway_entry.get()}')
        os.system(f'netsh interface ipv4 add dnsserver name="{
                  interface_entry.get()}" address={dns_entry.get()} index=1')
        os.system(f'netsh interface ipv4 add dnsserver name="{
                  interface_entry.get()}" address={dns_alternate_entry.get()} index=2')
        messagebox.showinfo(title="Info", message="Check your IP")
    else:
        messagebox.showerror(title="Alert", message="Field Can't be blank")


# info label
info_label = tk.Label(
    root, text="This app need administrator privilage", font=("Gill Sans MT", 12))
info_label.pack(pady=10)

# interface label
interface_label = tk.Label(
    root, text="Enter interface: \n (exmpl: Ethernet or Ethernet2 or Wi-Fi etc)", font=("Gill Sans MT", 10))
interface_label.pack(pady=10)

# ip entry
interface_entry = tk.Entry(root, width=20, font=("Gill Sans MT", 10))
interface_entry.pack()


# ip label
ip_label = tk.Label(
    root, text="Enter ip: \n (exmpl: 192.168.1.11)", font=("Gill Sans MT", 10))
ip_label.pack(pady=10)

# ip entry
ip_entry = tk.Entry(root, width=20, font=("Gill Sans MT", 10))
ip_entry.pack()

# subnet label
subnet_label = tk.Label(
    root, text="Enter subnet: \n (exmpl: 255.255.255.0)", font=("Gill Sans MT", 10))
subnet_label.pack(pady=10)

# subnet entry
subnet_entry = tk.Entry(root, width=20, font=("Gill Sans MT", 10))
subnet_entry.pack()

# gateway label
gateway_label = tk.Label(root, text="Enter gateway: \n (exmpl: 192.168.1.1)",
                         font=("Gill Sans MT", 10))
gateway_label.pack(pady=10)

# gateway entry
gateway_entry = tk.Entry(root, width=20, font=("Gill Sans MT", 10))
gateway_entry.pack()

# dns label
dns_label = tk.Label(
    root, text="Enter dns: \n (exmpl: 8.8.8.8)", font=("Gill Sans MT", 10))
dns_label.pack(pady=10)

# dns entry
dns_entry = tk.Entry(root, width=20, font=("Gill Sans MT", 10))
dns_entry.pack()

# dns_alternate label
dns_alternate_label = tk.Label(
    root, text="Enter alternate dns: \n (exmpl: 8.8.4.4)", font=("Gill Sans MT", 10))
dns_alternate_label.pack(pady=10)

# dns entry
dns_alternate_entry = tk.Entry(root, width=20, font=("Gill Sans MT", 10))
dns_alternate_entry.pack()


# button
my_button = tk.Button(root, text="Submit", command=setip)
my_button.pack(pady=20)


root.mainloop()
