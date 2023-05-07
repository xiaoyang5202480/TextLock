from cryptography.fernet import Fernet 
from tkinter import *
from tkinter import messagebox
# import os

version="v0.1.3"
ZuoZhe="xiaoyang5202480"

#语言文件
zh_cn={
    "input":"请输入你想要加密的文字",
    "done":"加密完成！\n加密后的文字在text.txt，\n秘钥在key.txt",
    "encryption_button":"加密",
    "tip":"提示",
    "decrypt_button":"解密",
    "decrypt":"请输入你想要解密的文字",
    "decrypt_done":"解密完成！\n加密后的文字在text.txt",
    "decrypt_key":"请输入这段文字的解密秘钥",
    "ZuoZhe":"作者：{}",
    "title":"文字加密器",
    "error_title":"错误",
    "error1":"解密失败！\n您可能没有输入正确的秘钥",
    "error2":"解密失败！\n您可能没有输入正确的加密文字！"
}

#自定义函数
def JiaMi():
    #秘钥
    key=Fernet.generate_key()
    f=Fernet(key)
    data=v1.get()
    bytes_data=data.encode()
    encrypted_data = f.encrypt(bytes_data)
    with open(r"text.txt","w") as t1:
        t1.write(encrypted_data.decode("utf-8"))
    with open(r"key.txt","w") as t2:
        t2.write(key.decode("utf-8"))
    messagebox.showinfo(zh_cn["tip"],zh_cn["done"])


def JieMi():    
    key2=v3.get()
    try:
        bytes_key2=key2.encode()
        f2=Fernet(bytes_key2)
    except:
        messagebox.showerror(zh_cn["error_title"],zh_cn["error1"])
    try:
        decrypt_data=v2.get()
        bytes_decrypt_data=decrypt_data.encode()
        decrypted_data = f2.decrypt(bytes_decrypt_data)
    except:
        messagebox.showerror(zh_cn["error_title"],zh_cn["error2"])
    with open(r"text.txt","w") as t3:
        t3.write(decrypted_data.decode("utf-8"))
    messagebox.showinfo(zh_cn["tip"],zh_cn["decrypt_done"])



#制作GUI
root=Tk()
root.geometry("500x400")
root.title(zh_cn["title"])
#root.iconphoto(file=r"") #设置窗口图标

label1=Label(root,text=zh_cn["input"])
label2=Label(root,text=zh_cn["decrypt"])
label3=Label(root,text=zh_cn["decrypt_key"])
label_ZuoZhe=Label(root,text=zh_cn["ZuoZhe"].format(ZuoZhe))

v1=StringVar()
v2=StringVar()
v3=StringVar()

entry1=Entry(root,textvariable=v1)
entry2=Entry(root,textvariable=v2)
entry3=Entry(root,textvariable=v3)

encryption_btn=Button(root,text=zh_cn["encryption_button"],command=JiaMi)
decrypt_btn=Button(root,text=zh_cn["decrypt_button"],command=JieMi)

label1.pack()
entry1.pack()
encryption_btn.pack()
label2.pack()
entry2.pack()
label3.pack()
entry3.pack()
decrypt_btn.pack()
label_ZuoZhe.pack(side="bottom")

root.mainloop() #进入事件循环