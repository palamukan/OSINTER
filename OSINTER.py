import requests
import threading
from threading import Thread
from requests import get
import time

def github(username):
    adres = "https://github.com/"
    response = requests.get(adres + username)
    if response.status_code == 200:
        print("[+]Github Hesabı bulundu, Adres: {}".format(adres + username))
    else:
        print("[-]Github hesabı bulunamadı.")

def twitter(username):
    adres = "https://twitter.com/"
    response = requests.get(adres + username)
    if response.status_code == 200:
        print("[+]Twitter hesabı bulundu, Adres: {}".format(adres + username))
    else:
        print("[-]Twitter hesabı bulunamadı.")

def facebook(username):
    adres = "https://facebook.com/"
    response = requests.get(adres + username)
    if response.status_code == 200:
        print("[+]Facebook hesabı bulundu, Adres: {}".format(adres + username))
    else:
        print("[-]Facebook hesabı bulunamadı.")

def youtube(username):
    adres = "https://youtube.com/"
    response = requests.get(adres + username)
    if response.status_code == 200:
        print("[+]Youtube hesabı bulundu, Adres: {}".format(adres + username))
    else:
        print("[-]Youtube hesabı bulunamadı.")

def googleplus(username):
    adres = "https://plus.google.com/"
    response = requests.get(adres + username)
    if response.status_code == 200:
        print("[+]Google+ bulundu, Adres: {}".format(adres + username))
    else:
        print("[-]Google Plus hesabı bulunamadı.")

def linkedin(username):
    adres = "https://linkedin.com/in/"
    response = requests.get(adres + username)
    if response.status_code == 200:
        print("[+]Linkedin hesabı bulundu, Adres: {}".format(adres + username))
    else:
        print("[-]Linkedin hesabı bulunamadı.")

def tumblr(username):
    adres = "https://" + username + ".tumblr.com"
    response = requests.get(adres)
    if response.status_code == 200:
        print("[+]Tumblr bulundu, Adres: {}".format(adres))
    else:
        print("[-]Tumblr hesabı bulunamadı.")

def steam(username):
    adres = "https://steamcommunity.com/id/"
    response = requests.get(adres + username)
    if response.status_code == 200:
        print("[+]Steam hesabı bulundu, Adres: {}".format(adres + username))
    else:
        print("[-]Steam hesabı bulunamadı.")

def medium(username):
    adres = "https://medium.com/@"
    response = requests.get(adres + username)
    if response.status_code == 200:
        print("[+]Medium hesabı bulundu, Adres: {}".format(adres + username))
    else:
        print("[-]Medium hesabı bulunamadı.")

def deviantart(username):
    adres = "https://" + username + ".deviantart.com"
    response = requests.get(adres)
    if response.status_code == 200:
        print("[+]Deviantart hesabı bulundu, Adres: {}".format(adres))
    else:
        print("[-]Deviantart hesabı bulunamadı.")

def vk(username):
    adres = "https://vk.com/"
    response = requests.get(adres + username)
    if response.status_code == 200:
        print("[+]vk hesabı bulundu, Adres: {}".format(adres + username))
    else:
        print("[-]vk hesabı bulunamadı.")


def vimeo(username):
    adres = "https://vimeo.com/"
    response = requests.get(adres + username)
    if response.status_code == 200:
        print("[+]Vimeo bulundu, Adres: {}".format(adres + username))
    else:
        print("[-]Vimeo hesabı bulunamadı.")

def reddit(username):
    adres = "https://www.reddit.com/r/" + username + "/"
    response = requests.get(adres)
    if response.status_code == 200:
        print("[+]Reddit hesabı bulundu, Adres: {}".format(adres))
    else:
        print("[-]Reddit hesabı bulunamadı.")

def instagram(username):
    adres = "https://instagram.com/"
    response = requests.get(adres + username)
    if response.status_code == 200:
        print("[+]İnstagram hesabı bulundu, Adres: {}".format(adres + username))
    else:
        print("[-]Vimeo hesabı bulunamadı.")


def blogger(username):
    adres = "https://" + username + ".blogspot.com"
    response = requests.get(adres)
    if response.status_code == 200:
        print("[+]Blogger hesabı bulundu, Adres: {}".format(adres))
    else:
        print("[-]Blogger hesabı bulunamadı.")

def wordpress(username):
    adres = "https://" + username + ".wordpress.com"
    response = requests.get(adres)
    if response.status_code == 200:
        print("[+]Wordpress hesabı bulundu, Adres: {}".format(adres))
    else:
        print("[-]Wordpress hesabı bulunamadı.")

def twitch(username):
    adres = "https://twitch.tv/"
    response = requests.get(adres + username)
    if response.status_code == 200:
        print("[+]Twitch hesabı bulundu, Adres: {}".format(adres + username))
    else:
        print("[-]Twitch hesabı bulunamadı.")





print("""""""""""""""""""""""""""""""""


   ___    ____    ___   _   _   _____   _____   ____                _   ____       _      _          _    
  / _ \  / ___|  |_ _| | \ | | |_   _| | ____| |  _ \              ( ) |  _ \     / \    | |        / \   
 | | | | \___ \   | |  |  \| |   | |   |  _|   | |_) |    _____    |/  | |_) |   / _ \   | |       / _ \  
 | |_| |  ___) |  | |  | |\  |   | |   | |___  |  _ <    |_____|       |  __/   / ___ \  | |___   / ___ \ 
  \___/  |____/  |___| |_| \_|   |_|   |_____| |_| \_\                 |_|     /_/   \_\ |_____| /_/   \_\
                                                                                                                                                    
  
          
1.Tarama yapmak için "osint" yazınız.
2.Programdan çıkış yapmak istiyorsanız "Çıkış" yazınız
                                                                                                                                                                                                                                                                                                         
""""")
while True:


    işlem = input("Ne yapmak istiyorsunuz: ")



    if (işlem == "Çıkış"):
        print("Programdan çıkış yapılıyor..")
        time.sleep(1)
        break

    elif (işlem == "osint"):
        username = input("Kullanıcı adı giriniz: ")
        Thread(target=github, args=(username,)).start()
        Thread(target=twitter, args=(username,)).start()
        Thread(target=facebook, args=(username,)).start()
        Thread(target=youtube, args=(username,)).start()
        Thread(target=googleplus, args=(username,)).start()
        Thread(target=linkedin, args=(username,)).start()
        Thread(target=tumblr, args=(username,)).start()
        Thread(target=steam, args=(username,)).start()
        Thread(target=medium, args=(username,)).start()
        Thread(target=deviantart, args=(username,)).start()
        Thread(target=vk, args=(username,)).start()
        Thread(target=vimeo, args=(username,)).start()
        Thread(target=reddit, args=(username,)).start()
        Thread(target=instagram, args=(username,)).start()
        Thread(target=blogger, args=(username,)).start()
        Thread(target=wordpress, args=(username,)).start()
        Thread(target=twitch, args=(username,)).start()

        time.sleep(5)


    else:
        print("Hatalı Tuşlama yaptınız, menüye geri döndürülüyorsunuz.")
        time.sleep(1)
