import pandas as pd #pip3 install pandas
import covid #pip3 install covid
import tkinter as tk #Varsayılan kütüphane
import matplotlib.pyplot as plt #pip3 install matplotlib


def yazilari_temizle(): #entry'leri temizlemek için bir fonksiyon
    ulke_girisi.delete(0, 'end')
    aktif_vaka_girisi.delete(0, 'end')
    olum_sayi_girisi.delete(0, 'end')
    toplam_vaka_girisi.delete(0, 'end')
    iyilesen_vaka_girisi.delete(0, 'end')

def verileri_getir(): #Entry'e girilien ülkenin verilerini getirmesini sağlayan fonksiyon.
    data = covid.Covid()
    ulke_adi = ulke_girisi.get() #Ülke adının kullanıcıdan alınması
    status = data.get_status_by_country_name(ulke_adi) #Covid kütüphanesinin "get_status_by_country_name" methodu ile ülkenin verilerinin alınması
    aktif_vaka = status['active'] #Aktif vaka sayısı
    aktif_vaka_girisi.insert(0,aktif_vaka) #Aktif Vaka'nın entry'e bastırıyoruz.
    vefat_vaka = status['deaths'] #Vefat eden kişi sayısı
    olum_sayi_girisi.insert(0, vefat_vaka) #Vefat Eden Kişi sayısı'nın entry'e bastırıyoruz.
    toplam_vaka = status['confirmed'] #Toplam Vaka Sayısı
    toplam_vaka_girisi.insert(0, toplam_vaka) #Toplam Vaka Sayısını entry'e bastırıyoruz.
    iyilesen_vaka = status['recovered'] #İyileşen Vaka Sayısı
    iyilesen_vaka_girisi.insert(0, iyilesen_vaka) #İyileşen Vaka Sayısı'nı entry'e bastırıyoruz.

    veri = {
        key:status[key]
        for key in status.keys() & {"confirmed","active","deaths","recovered"}
    }
    veri_keys = list(veri.keys())
    veri_values = list(veri.values())
    plt.title(ulke_adi) #Grafiğin başlığını belirliyoruz.
    plt.bar(range(len(veri)),veri_values,tick_label=veri_keys) #Grafiğin çubuklarını ayarlıyoruz.
    plt.plot(range(len(veri)))
    plt.show() #Grafiği ekrana veriyoruz.

#Tkinter
root = tk.Tk()
root.title('Covid-19') #Pencere Başlığı
root.geometry('500x250') #Pencere boyutu
root.maxsize(500,250) #Pencerenin max boyutu
root.minsize(500,250) #Pencerenin min boyutu
root.configure(bg="green") #Pencerenin arkaplan rengi


baslik = tk.Label(root, text="Covid-19", font=('Helvetica',12,'bold'), bg="green", fg="white") #"Covid-19" başlığı
baslik.place(x=210,y=10) #Konumu

#Ülke Girişi(Entry)
ulke_girisi_text = tk.Label(root, text="Ülke Adı:", bg="green", fg="white", font=('verdana',10,'bold')) #"Ülke Adı:" yazısı
ulke_girisi_text.place(x=8,y=50) #"Ülke Adı:" konumu
ulke_girisi = tk.Entry(root, text="", width="20") #Ülke Adı'nın girişi(entry)
ulke_girisi.place(x=120,y=50) #Entry'nin konumu

ayrac = tk.Label(root, text="-------------------------------------------------------", fg="white", bg="green") #Ayraç
ayrac.place(x=8,y=74) #Ayraç konumu

#Aktif Vaka verisi
aktif_vaka_text = tk.Label(root, text="Aktif Vaka:", bg="green", fg="white", font=('verdana',10,'bold')) #"Aktif Vaka" yazısı
aktif_vaka_text.place(x=8,y=94) #Konumlama
aktif_vaka_girisi = tk.Entry(root) #Aktif Vaka girişi -Buraya kullanıcı tarafından herhangi bir bilgi yazılmayacak.
aktif_vaka_girisi.place(x=120,y=94)#Konumlama

#Vefat Sayısı verisi
olum_text = tk.Label(root, text="Vefat Sayısı:", bg="green", fg="white", font=('verdana', 10, 'bold')) #"Vefat Sayısı:" yazısı
olum_text.place(x=8, y=130) #Konumlama
olum_sayi_girisi = tk.Entry(root) #Vefat Sayısı girişi -Buraya kullanıcı tarafından herhangi bir bilgi yazılmayacak
olum_sayi_girisi.place(x=120, y=130) #Konumlama

#Toplam Vaka verisi
toplam_vaka_text = tk.Label(root, text="Toplam Vaka:", bg="green", fg="white", font=('verdana',10,'bold')) #"Toplam Vaka:" yazısı
toplam_vaka_text.place(x=8,y=168) #Konumlama
toplam_vaka_girisi = tk.Entry(root) #Toplam Vaka Sayısı girişi -Buraya kullanıcı tarafından herhangi bir bilgi yazılmayacak
toplam_vaka_girisi.place(x=120, y=168) #Konumlama

#İyileşen kişi verisi
iyilesen_vaka_text = tk.Label(root, text="İyileşen Kişi:", bg="green", fg="white", font=('verdana',10,'bold')) #"İyileşen Kişi:" yazısı
iyilesen_vaka_text.place(x=8, y=200) #Konumlama
iyilesen_vaka_girisi = tk.Entry(root) #İyileşen Vaka Sayısı girişi -Buraya kullanıcı tarafından herhangi bir bilgi yazılmayacak
iyilesen_vaka_girisi.place(x=120, y=200) #Konumlama

#verilerin getirilmesini sağlayan buton.
goster = tk.Button(root, text='Göster', command=verileri_getir)
goster.place(x=400, y=100)

#Ekrandaki verilerin silinmesini sağlayan buton
temizle = tk.Button(root, text="Temizle", command=yazilari_temizle)
temizle.place(x=400, y=150)

root.mainloop()

#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html
#https://www.w3schools.com/python/ref_func_list.asp
#https://www.w3schools.com/python/ref_dictionary_keys.asp
#https://www.w3schools.com/python/ref_dictionary_values.asp
#https://ahmednafies.github.io/covid/
#https://docs.python.org/3/library/tk.html
#https://matplotlib.org/3.3.1/api/_as_gen/matplotlib.pyplot.plot.html
#https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.bar.html
