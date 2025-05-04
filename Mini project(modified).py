from tkinter import *
from tkinter import filedialog, messagebox
import base64
import os
import random
import string

def generate_key():
    key = ''.join(random.choices(string.ascii_letters + string.digits, k=12))
    code.set(key)

def encrypt_text(text):
    return base64.b64encode(text.encode("ascii")).decode("ascii")

def decrypt_text(text):
    try:
        return base64.b64decode(text.encode("ascii")).decode("ascii")
    except Exception:
        messagebox.showerror("Decryption", "Invalid encrypted text!")
        return None

def encrypt_file():
    file_path = filedialog.askopenfilename()
    if not file_path:
        return
    
    password = code.get()
    if not password:
        messagebox.showerror("Encryption", "Please enter the secret key!")
        return
    
    with open(file_path, "r") as file:
        content = file.read()
    
    encrypted_content = encrypt_text(content)
    encrypted_file = file_path + ".enc"
    with open(encrypted_file, "w") as file:
        file.write(encrypted_content)
    
    messagebox.showinfo("Success", f"File encrypted successfully!\nSaved as: {encrypted_file}")

def decrypt_file():
    file_path = filedialog.askopenfilename()
    if not file_path:
        return
    
    password = code.get()
    if not password:
        messagebox.showerror("Decryption", "Please enter the secret key!")
        return
    
    with open(file_path, "r") as file:
        content = file.read()
    
    decrypted_content = decrypt_text(content)
    if decrypted_content is None:
        return
    
    decrypted_file = file_path.replace(".enc", "_decrypted.txt")
    with open(decrypted_file, "w") as file:
        file.write(decrypted_content)
    
    messagebox.showinfo("Success", f"File decrypted successfully!\nSaved as: {decrypted_file}")

def main_screen():
    global screen, code
    
    screen = Tk()
    screen.geometry("500x500")
    screen.title("Secure File Encryptor & Decryptor")
    screen.configure(bg="#1e272e")
    
    Label(screen, text="🔒 Secure File Encryption & Decryption 🔓", fg="white", font=("Helvetica", 16, "bold"), bg="#1e272e").pack(pady=15)
    
    Label(screen, text="Enter Secret Key", fg="white", font=("Calibri", 12, "bold"), bg="#1e272e").pack(pady=5)
    
    code = StringVar()
    Entry(screen, textvariable=code, width=22, font=("Arial", 14), show="*", bd=3, relief=GROOVE, bg="#dcdde1", fg="black").pack(pady=5)
    Button(screen, text="Generate Key 🔑", height=2, width=20, bg="#f39c12", fg="white", bd=0, font=("Arial", 10, "bold"), command=generate_key).pack(pady=5)
    
    Button(screen, text="Encrypt File 📂", height=2, width=20, bg="#e74c3c", fg="white", bd=0, font=("Arial", 10, "bold"), command=encrypt_file).pack(pady=10)
    Button(screen, text="Decrypt File 🔓", height=2, width=20, bg="#2ecc71", fg="white", bd=0, font=("Arial", 10, "bold"), command=decrypt_file).pack(pady=5)
    
    Label(screen, text="© 2024 Secure Encryption App", fg="gray", font=("Arial", 10, "italic"), bg="#1e272e").pack(side=BOTTOM, pady=10)
    
    screen.mainloop()

main_screen()
from tkinter import *
from tkinter import filedialog, messagebox
import base64
import os
import random
import string

def generate_key():
    key = ''.join(random.choices(string.ascii_letters + string.digits, k=12))
    code.set(key)

def encrypt_text(text):
    return base64.b64encode(text.encode("ascii")).decode("ascii")

def decrypt_text(text):
    try:
        return base64.b64decode(text.encode("ascii")).decode("ascii")
    except Exception:
        messagebox.showerror("Decryption", "Invalid encrypted text!")
        return None

def encrypt_file():
    file_path = filedialog.askopenfilename()
    if not file_path:
        return
    
    password = code.get()
    if not password:
        messagebox.showerror("Encryption", "Please enter the secret key!")
        return
    
    with open(file_path, "r") as file:
        content = file.read()
    
    encrypted_content = encrypt_text(content)
    encrypted_file = file_path + ".enc"
    with open(encrypted_file, "w") as file:
        file.write(encrypted_content)
    
    messagebox.showinfo("Success", f"File encrypted successfully!\nSaved as: {encrypted_file}")

def decrypt_file():
    file_path = filedialog.askopenfilename()
    if not file_path:
        return
    
    password = code.get()
    if not password:
        messagebox.showerror("Decryption", "Please enter the secret key!")
        return
    
    with open(file_path, "r") as file:
        content = file.read()
    
    decrypted_content = decrypt_text(content)
    if decrypted_content is None:
        return
    
    decrypted_file = file_path.replace(".enc", "_decrypted.txt")
    with open(decrypted_file, "w") as file:
        file.write(decrypted_content)
    
    messagebox.showinfo("Success", f"File decrypted successfully!\nSaved as: {decrypted_file}")

def main_screen():
    global screen, code
    
    screen = Tk()
    screen.geometry("500x500")
    screen.title("Secure File Encryptor & Decryptor")
    screen.configure(bg="#1e272e")
    
    Label(screen, text="🔒 Secure File Encryption & Decryption 🔓", fg="white", font=("Helvetica", 16, "bold"), bg="#1e272e").pack(pady=15)
    
    Label(screen, text="Enter Secret Key", fg="white", font=("Calibri", 12, "bold"), bg="#1e272e").pack(pady=5)
    
    code = StringVar()
    Entry(screen, textvariable=code, width=22, font=("Arial", 14), show="*", bd=3, relief=GROOVE, bg="#dcdde1", fg="black").pack(pady=5)
    Button(screen, text="Generate Key 🔑", height=2, width=20, bg="#f39c12", fg="white", bd=0, font=("Arial", 10, "bold"), command=generate_key).pack(pady=5)
    
    Button(screen, text="Encrypt File 📂", height=2, width=20, bg="#e74c3c", fg="white", bd=0, font=("Arial", 10, "bold"), command=encrypt_file).pack(pady=10)
    Button(screen, text="Decrypt File 🔓", height=2, width=20, bg="#2ecc71", fg="white", bd=0, font=("Arial", 10, "bold"), command=decrypt_file).pack(pady=5)
    
    Label(screen, text="© 2024 Secure Encryption App", fg="gray", font=("Arial", 10, "italic"), bg="#1e272e").pack(side=BOTTOM, pady=10)
    
    screen.mainloop()

main_screen()
