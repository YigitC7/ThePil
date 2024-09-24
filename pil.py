# The pil
# Turkish program

try:
    import psutil
except:
    print("Hata: Modül sistemde yüklü değil!\n$ pip install psutil")

# Yiğit çıtak tarafından programlanmıştır
# acpi programının Yerli ve milli alternatifi
# Sürüm tutumayan tek seferde yazılmış bir programdır
# eğere bir hata varsa sürüm bilgisi girmeden düzeltirim

def program():
    batarya = psutil.sensors_battery()

    if batarya:
        if batarya.power_plugged:
            print(f"[Sarj: {int(batarya.percent)}% | Durum: Sarj oluyor]")
        else:
            print(f"[Sarj: {int(batarya.percent)}% | Durum: Sarj olmuyor]")
    else:
        print("Batarya bulunamadı :(")


if __name__ == "__main__":
    try:
        program()
    except:
        pass
