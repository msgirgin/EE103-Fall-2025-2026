# 1. Aşama: Girdileri al (Lecture 2)
isim = input("Lütfen isminizi girin: ")
sayi_str = input("Lütfen bir sayı girin (örn: 12345): ")

# 2. Aşama: Çift rakamları topla (Lecture 3 - for, Lecture 1 - int, Lecture 2 - if)
cift_rakamlar_toplami = 0  # Döngü için bir "biriktirici" değişken (Lecture 3)

# 'sayi_str' string'indeki her bir karakteri 'harf' olarak gez
for harf in sayi_str:
    
    # Her harfi (string) bir tamsayıya (int) çevir (Lecture 1)
    rakam_int = int(harf)
    
    # Rakamın 2'ye bölümünden kalan 0 ise (çift ise) (Lecture 2 - if, Lecture 1 - %)
    if rakam_int % 2 == 0:
        
        # Toplamı güncelle
        cift_rakamlar_toplami = cift_rakamlar_toplami + rakam_int

# 3. Aşama: Toplamın son basamağını bul (Lecture 1 - %)
# Bir sayının 10'a bölümünden kalanı (mod) almak, son basamağı verir
tekrar_sayisi = cift_rakamlar_toplami % 10

# 4. Aşama: Son basamak kadar ismi yazdır (Lecture 3 - for...range)
print("---------------------------------")
# f-string'ler Lecture 2'de (slayt 27) işlendi [cite: 1235-1241]
print(f"Sayıdaki çift rakamların toplamı: {cift_rakamlar_toplami}")
print(f"Toplamın son basamağı (tekrar sayısı): {tekrar_sayisi}")
print("---------------------------------")

# range(tekrar_sayisi) kullanarak o sayı kadar dönen bir döngü
for i in range(tekrar_sayisi):
    print(isim)