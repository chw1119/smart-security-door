
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer
import threading
import random
import cv2
import sqlite3
import socket
import struct
import pickle
import numpy as np
from PIL import Image, ImageTk
from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
import tkinter as tk 
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

standard_password = 1234
is_open = False
is_send_image = False

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"./assets/frame2")



def update_video():
    global canvas
    global image_image_6
    global client_socket
    global is_send_image
    
    cap = cv2.VideoCapture(1)  # 1번 카메라를 엽니다.

    while True:
        ret, frame = cap.read()
        if not ret:
            print(123)
            break
        print(143)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)



        image = Image.fromarray(frame)
        image_tk = ImageTk.PhotoImage(image=image)
        
        if is_send_image and client_socket:
            send_image(client_socket, frame)

        canvas.itemconfig(image_6, image=image_tk)
        canvas.image = image_tk  # Keep a reference to avoid garbage collection


    cap.release()


def socket_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 9999))
    server_socket.listen(5)
    print('Server listening on port 9999')

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr}")

        threading.Thread(target=handle_client, args=(client_socket,)).start()

def handle_client(client_socket):
    while True:
        message_type = receive_control_message(client_socket)
        print(message_type)
        if message_type == "%OPEN":
            print("Connection opened")
        elif message_type == "%CLOS":
            print("Connection closed")

            #client_socket.close()
            #return
        elif message_type == "%RAND":
            print("Random message received")
        elif message_type == "%QQQQ":
            print("%OPEN" if is_open == True else "%CLOS")
            send_control_message(client_socket, "%OPEN" if is_open == True else "%CLOS")
        elif message_type == "%IMAG":
            frame = receive_image(client_socket)
            if frame is not None:
                show_image(frame)

def show_image(frame):
    image = Image.fromarray(frame)
    image_tk = ImageTk.PhotoImage(image=image)
    canvas.create_image(0, 0, anchor=tk.NW, image=image_tk)
    canvas.image = image_tk  # Keep a reference to avoid garbage collection


def send_image(socket_connection, frame):
    data = pickle.dumps(frame)
    message_size = struct.pack("L", len(data))
    socket_connection.sendall(b"%IMAG" + message_size + data)

def receive_video(socket_connection):
    data = b""
    payload_size = struct.calcsize("L")

    while True:
        while len(data) < payload_size:
            packet = socket_connection.recv(4096)
            if not packet:
                return
            data += packet

        packed_msg_size = data[:payload_size]
        data = data[payload_size:]
        msg_size = struct.unpack("L", packed_msg_size)[0]

        while len(data) < msg_size:
            data += socket_connection.recv(4096)

        frame_data = data[:msg_size]
        data = data[msg_size:]

        frame = pickle.loads(frame_data)
        cv2.imshow('Received', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    socket_connection.close()
    cv2.destroyAllWindows()


def receive_image(socket_connection):
    payload_size = struct.calcsize("L")

    packed_msg_size = socket_connection.recv(payload_size)
    if not packed_msg_size:
        return None

    msg_size = struct.unpack("L", packed_msg_size)[0]

    data = b""
    while len(data) < msg_size:
        packet = socket_connection.recv(4096)
        if not packet:
            return None
        data += packet

    frame_data = data[:msg_size]
    frame = pickle.loads(frame_data)
    return frame

def send_control_message(socket_connection, message):
    if message in ["%OPEN", "%CLOS", "%RAND"]:
        socket_connection.sendall(message.encode())
    else:
        raise ValueError("Invalid control message. Use '%OPEN', '%CLOSE', or '%RAND'")

def receive_control_message(socket_connection):
    message_type = socket_connection.recv(6)
    print("raw :", message_type)
    if message_type in [b"%OPEN", b"%CLOS", b"%RAND", b"%QQQQ"]:
        return message_type.decode()
    elif message_type == b"%IMAG":
        return "%IMAG"
    else:
        return None
    
def clear_all():
    global window

    for child in window.winfo_children():
        print(child.winfo_id)
        child.destroy()


def open():
    global is_open
    is_open = True
    global canvas, image_image_1, image_1, button_image_1, button_1, button_image_2, button_2
    global button_image_3, button_3, button_image_4, button_4, button_image_5, button_5
    global button_image_6, button_6, button_image_7, button_7, button_image_8, button_8
    global button_image_9, button_9, button_image_10, button_10, button_image_11, button_11
    global button_image_12, button_12, image_image_2, image_2, image_image_3, image_3
    global image_image_4, image_4, image_image_5, image_5, image_image_6, image_6
    global entry_image_1, entry_bg_1, entry_1, OUTPUT_PATH, ASSETS_PATH
    print("open")
    clear_all()
        
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"./assets/frame3")


    canvas = Canvas(
        window,
        bg = "#181A20",
        height = 852,
        width = 393,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        196.0,
        514.0,
        image=image_image_1
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_1 clicked"),
        relief="flat"
    )
    button_1.place(
        x=97.0,
        y=365.0,
        width=60.0,
        height=60.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_2 clicked"),
        relief="flat"
    )
    button_2.place(
        x=166.0,
        y=364.0,
        width=60.0,
        height=60.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_3 clicked"),
        relief="flat"
    )
    button_3.place(
        x=235.0,
        y=363.0,
        width=60.0,
        height=60.0
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_4 clicked"),
        relief="flat"
    )
    button_4.place(
        x=95.0,
        y=430.0,
        width=60.0,
        height=60.0
    )

    button_image_5 = PhotoImage(
        file=relative_to_assets("button_5.png"))
    button_5 = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_5 clicked"),
        relief="flat"
    )
    button_5.place(
        x=166.0,
        y=429.0,
        width=60.0,
        height=60.0
    )

    button_image_6 = PhotoImage(
        file=relative_to_assets("button_6.png"))
    button_6 = Button(
        image=button_image_6,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_6 clicked"),
        relief="flat"
    )
    button_6.place(
        x=235.0,
        y=430.0,
        width=60.0,
        height=60.0
    )

    button_image_7 = PhotoImage(
        file=relative_to_assets("button_7.png"))
    button_7 = Button(
        image=button_image_7,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_7 clicked"),
        relief="flat"
    )
    button_7.place(
        x=96.0,
        y=496.0,
        width=60.0,
        height=60.0
    )

    button_image_8 = PhotoImage(
        file=relative_to_assets("button_8.png"))
    button_8 = Button(
        image=button_image_8,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_8 clicked"),
        relief="flat"
    )
    button_8.place(
        x=166.0,
        y=495.0,
        width=60.0,
        height=60.0
    )

    button_image_9 = PhotoImage(
        file=relative_to_assets("button_9.png"))
    button_9 = Button(
        image=button_image_9,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_9 clicked"),
        relief="flat"
    )
    button_9.place(
        x=235.0,
        y=495.0,
        width=60.0,
        height=60.0
    )

    button_image_10 = PhotoImage(
        file=relative_to_assets("button_10.png"))
    button_10 = Button(
        image=button_image_10,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_10 clicked"),
        relief="flat"
    )
    button_10.place(
        x=96.0,
        y=562.0,
        width=60.0,
        height=60.0
    )

    button_image_11 = PhotoImage(
        file=relative_to_assets("button_11.png"))
    button_11 = Button(
        image=button_image_11,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_11 clicked"),
        relief="flat"
    )
    button_11.place(
        x=166.0,
        y=562.0,
        width=60.0,
        height=60.0
    )

    button_image_12 = PhotoImage(
        file=relative_to_assets("button_12.png"))
    button_12 = Button(
        image=button_image_12,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_12 clicked"),
        relief="flat"
    )
    button_12.place(
        x=236.0,
        y=562.0,
        width=60.0,
        height=60.0
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        195.0,
        653.0,
        image=image_image_2
    )

    image_image_3 = PhotoImage(
        file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(
        305.0,
        588.0,
        image=image_image_3
    )

    image_image_4 = PhotoImage(
        file=relative_to_assets("image_4.png"))
    image_4 = canvas.create_image(
        195.0,
        695.0,
        image=image_image_4
    )

    canvas.create_rectangle(
        134.0,
        71.0,
        257.0,
        228.0,
        fill="#FFFFFF",
        outline="")

    image_image_5 = PhotoImage(
        file=relative_to_assets("image_5.png"))
    image_5 = canvas.create_image(
        200.0,
        338.0,
        image=image_image_5
    )

    image_image_6 = PhotoImage(
        file=relative_to_assets("image_6.png"))
    image_6 = canvas.create_image(
        197.0,
        143.0,
        image=image_image_6
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        196.0,
        284.5,
        image=entry_image_1
    )
    entry_1 = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=91.5,
        y=270.0,
        width=209.0,
        height=27.0
    )

def close():
    
    global is_open
    is_open = False
    global canvas, image_image_1, image_1, button_image_1, button_1, button_image_2, button_2
    global button_image_3, button_3, button_image_4, button_4, button_image_5, button_5
    global button_image_6, button_6, button_image_7, button_7, button_image_8, button_8
    global button_image_9, button_9, button_image_10, button_10, button_image_11, button_11
    global button_image_12, button_12, image_image_2, image_2, image_image_3, image_3
    global image_image_4, image_4, image_image_5, image_5, image_image_6, image_6
    global entry_image_1, entry_bg_1, entry_1, OUTPUT_PATH, ASSETS_PATH
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"./assets/frame2")

    print("close")
    clear_all()
    canvas = Canvas(
        window,
        bg = "#181A20",
        height = 852,
        width = 393,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        196.0,
        514.0,
        image=image_image_1
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        195.0,
        653.0,
        image=image_image_2
    )

    image_image_3 = PhotoImage(
        file=relative_to_assets("image_3.png"))
    image_3 = canvas.create_image(
        305.0,
        588.0,
        image=image_image_3
    )

    canvas.create_text(
        156.0,
        677.0,
        anchor="nw",
        text="Batt .  9V /  Reset",
        fill="#D9D9D9",
        font=("Inter Bold", 6 * -1)
    )

    image_image_4 = PhotoImage(
        file=relative_to_assets("image_4.png"))
    image_4 = canvas.create_image(
        195.0,
        700.0,
        image=image_image_4
    )

    canvas.create_rectangle(
        134.0,
        71.0,
        257.0,
        228.0,
        fill="#FFFFFF",
        outline="")

    image_image_5 = PhotoImage(
        file=relative_to_assets("image_5.png"))
    image_5 = canvas.create_image(
        200.0,
        338.0,
        image=image_image_5
    )

    image_6 = canvas.create_image(
        197.0,
        143.0
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        196.0,
        284.5,
        image=entry_image_1
    )
    entry_1 = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=91.5,
        y=270.0,
        width=209.0,
        height=27.0
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: on_click(1),
        relief="flat"
    )
    button_1.place(
        x=98.0,
        y=365.0,
        width=60.0,
        height=60.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: on_click(2),
        relief="flat"
    )
    button_2.place(
        x=167.0,
        y=364.0,
        width=60.0,
        height=60.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: on_click(3),
        relief="flat"
    )
    button_3.place(
        x=236.0,
        y=363.0,
        width=60.0,
        height=60.0
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: on_click(4),
        relief="flat"
    )
    button_4.place(
        x=96.0,
        y=430.0,
        width=60.0,
        height=60.0
    )

    button_image_5 = PhotoImage(
        file=relative_to_assets("button_5.png"))
    button_5 = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: on_click(5),
        relief="flat"
    )
    button_5.place(
        x=167.0,
        y=429.0,
        width=60.0,
        height=60.0
    )

    button_image_6 = PhotoImage(
        file=relative_to_assets("button_6.png"))
    button_6 = Button(
        image=button_image_6,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: on_click(6),
        relief="flat"
    )
    button_6.place(
        x=236.0,
        y=430.0,
        width=60.0,
        height=60.0
    )

    button_image_7 = PhotoImage(
        file=relative_to_assets("button_7.png"))
    button_7 = Button(
        image=button_image_7,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: on_click(7),
        relief="flat"
    )
    button_7.place(
        x=97.0,
        y=496.0,
        width=60.0,
        height=60.0
    )

    button_image_8 = PhotoImage(
        file=relative_to_assets("button_8.png"))
    button_8 = Button(
        image=button_image_8,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: on_click(8),
        relief="flat"
    )
    button_8.place(
        x=167.0,
        y=495.0,
        width=60.0,
        height=60.0
    )

    button_image_9 = PhotoImage(
        file=relative_to_assets("button_9.png"))
    button_9 = Button(
        image=button_image_9,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: on_click(9),
        relief="flat"
    )
    button_9.place(
        x=236.0,
        y=495.0,
        width=60.0,
        height=60.0
    )

    button_image_10 = PhotoImage(
        file=relative_to_assets("button_10.png"))
    button_10 = Button(
        image=button_image_10,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: on_click(10),
        relief="flat"
    )
    button_10.place(
        x=97.0,
        y=562.0,
        width=60.0,
        height=60.0
    )

    button_image_11 = PhotoImage(
        file=relative_to_assets("button_11.png"))
    button_11 = Button(
        image=button_image_11,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: on_click(11),
        relief="flat"
    )
    button_11.place(
        x=167.0,
        y=562.0,
        width=60.0,
        height=60.0
    )

    button_image_12 = PhotoImage(
        file=relative_to_assets("button_12.png"))
    button_12 = Button(
        image=button_image_12,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: on_click(12),
        relief="flat"
    )
    button_12.place(
        x=237.0,
        y=562.0,
        width=60.0,
        height=60.0
    )
    
    pass


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def on_click(num):
    global canvas, image_image_1, image_1, button_image_1, button_1, button_image_2, button_2
    global button_image_3, button_3, button_image_4, button_4, button_image_5, button_5
    global button_image_6, button_6, button_image_7, button_7, button_image_8, button_8
    global button_image_9, button_9, button_image_10, button_10, button_image_11, button_11
    global button_image_12, button_12, image_image_2, image_2, image_image_3, image_3
    global image_image_4, image_4, image_image_5, image_5, image_image_6, image_6
    global entry_image_1, entry_bg_1, entry_1, OUTPUT_PATH, ASSETS_PATH
    temp = entry_1.get()
    if num == 10:
        entry_1.delete(0,tk.END)
        entry_1.insert(0,"")
    if num == 12:
        if temp == str(standard_password):
            entry_1.delete(0,tk.END)
            open()
        
    if num == 1:
        entry_1.delete(0,tk.END)
        entry_1.insert(0,temp + "1")
    if num == 2:
        
        entry_1.delete(0,tk.END)
        entry_1.insert(0,temp + "2")
    if num == 3:
        entry_1.delete(0,tk.END)
        entry_1.insert(0,temp + "3")
    if num == 4:
        entry_1.delete(0,tk.END)
        entry_1.insert(0,temp + "4")
    if num == 5:
        entry_1.delete(0,tk.END)
        entry_1.insert(0,temp + "5")
    if num == 6:
        entry_1.delete(0,tk.END)
        entry_1.insert(0,temp + "6")
    if num == 7:
        entry_1.delete(0,tk.END)
        entry_1.insert(0,temp + "7")
    if num == 8:
        entry_1.delete(0,tk.END)
        entry_1.insert(0,temp + "8")
    if num == 9:
        entry_1.delete(0,tk.END)
        entry_1.insert(0,temp + "9")
    if num == 11:
        entry_1.delete(0,tk.END)
        entry_1.insert(0,temp + "0")

window = Tk()

window.geometry("393x852")
window.configure(bg = "#181A20")

close()

threading.Thread(target=socket_server, daemon=True).start()
window.resizable(False, False)
threading.Thread(target=update_video, daemon=True).start()
window.mainloop()
