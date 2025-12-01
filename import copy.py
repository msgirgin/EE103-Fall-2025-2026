import copy

# Senaryo Verisi: [ID, [Vize, Final]]
# Bazı veriler hatalı (Notu -1 olanlar veya boş listeler)
raw_student_data = [
    [101, [50, 60]], 
    [102, [-1, 40]],   # Hatalı Veri (Vize -1)
    [103, [80, 90]], 
    [104, []],         # Hatalı Veri (Not girilmemiş)
    [105, [45, 50]]
]

# ---------------------------------------------------------
# PART 1: HELPER FUNCTIONS (YARDIMCI FONKSİYONLAR)
# ---------------------------------------------------------

def calculate_averages(data):
    """
    Öğrencilerin ortalamasını (Vize*0.4 + Final*0.6) hesaplar.
    Geriye sadece ortalamaların olduğu bir liste döndürür.
    """
    # TODO 1: List Comprehension kullanarak ortalamaları hesapla.
    # İpucu: [ (student[1][0]*0.4 + student[1][1]*0.6) for student in data ]
    calculated_average = [(student[1][0]*0.4 + student[1][1]*0.6) for student in data]
    return calculated_average

def get_high_achievers(data, threshold=70):
    """
    Belirli bir notun üzerindeki öğrencilerin ID'lerini döndürür.
    """
    # TODO 2: List Comprehension ve 'if' kullanarak filtreleme yap.
    high_achievers = [student[0] for student in data if (student[1][0]*0.4 + student[1][1]*0.6) > threshold]
    return high_achievers

def remove_invalid_entries(data):
    """
    Not listesi boş olan veya notu 0'dan küçük olan öğrencileri 
    listeden SİLER (Mutate eder).
    """
    # TODO 3: Listenin kopyası üzerinde gezerek (iterate over copy)
    # hatalı olanları orijinal listeden (data) sil (remove/pop).
    # İPUCU: for student in data[:]: ...
    
    # DOĞRU: data[:] kullanarak kopyada geziyorsun. Harika!
    for student in data[:]:
        notlar = student[1]
        
        # Hata 1 Düzeltildi: Parantez ve Mantık
        if len(notlar) == 0:
            data.remove(student) # [] yerine () kullandık
            
        # Hata 2 Düzeltildi: Listeyi sayıyla kıyaslamak yerine min() kullandık
        # Listenin en küçüğü 0'dan küçükse, negatif not var demektir.
        elif min(notlar) < 0:
            data.remove(student) # [] yerine () kullandık

# ---------------------------------------------------------
# PART 2: MAIN SCENARIO (GÜVENLİ VERİ İŞLEME)
# ---------------------------------------------------------

def apply_curve_safe(data, bonus_points):
    """
    Orijinal veriyi BOZMADAN notlara bonus puan ekler.
    """
    
    # TODO 4: Verinin 'Deep Copy'sini oluştur (safe_data değişkenine).
    # İpucu: copy.deepcopy(...) kullan.
    safe_data = copy.deepcopy(data) 
    
    # TODO 5: Oluşturduğun kopyadaki (safe_data) her notu güncelle.
    # Not: List comprehension yerine açık döngü (nested loop) daha güvenlidir.
    
    for student in safe_data:       # 1. Döngü: Öğrencileri gezer
        notlar = student[1]         # Öğrencinin not listesini (örn: [50, 60]) al
        
        # 2. Döngü: O not listesinin içindeki notları (indeksle) gez
        for i in range(len(notlar)):
            notlar[i] += bonus_points  # Her nota bonus ekle
            
    return safe_data

def main():
    print("--- Orijinal Veri ---")
    print(raw_student_data)

    # Adım 1: Veriyi Temizle
    remove_invalid_entries(raw_student_data)
    print("--- Temizlenmiş Veri (Hatalılar Silindi) ---")
    print(raw_student_data) 
    
    # TODO 6: get_high_achievers fonksiyonunu çağır ve yazdır.

    # Fonksiyonu çağırıyoruz (Veriyi ve baraj notunu gönderiyoruz)
    basarili_ogrenciler = get_high_achievers(raw_student_data, 80)

    # Sonucu ekrana basıyoruz
    print(f"80 Barajını Geçen Öğrenciler: {basarili_ogrenciler}")

    # Adım 2: Çan Eğrisi Uygula (Güvenli Mod)
    curved_data = apply_curve_safe(raw_student_data, 10)
    
    print("--- Çan Uygulanmış Veri (Yeni Liste) ---")
    print(curved_data)
    
    print("--- Orijinal Veri Kontrolü (Değişmemiş Olmalı) ---")
    print(raw_student_data)

    # TODO 7: Orijinal veri ile yeni verinin bellek adreslerini (id) 
    # veya içeriklerini karşılaştırarak kopyalamanın başarılı olduğunu doğrula.
    
    # 1. İçerik Kontrolü: Orijinal veri hala eski notlarda mı?
    print("Kontrol 1 - İçerik Farkı:")
    print(f"Orijinaldeki İlk Öğrenci Notu: {raw_student_data[0][1]}") # Örn: [50, 60] çıkmalı
    print(f"Yenideki İlk Öğrenci Notu:     {curved_data[0][1]}")      # Örn: [60, 70] çıkmalı

    # 2. Bellek (Memory) Kontrolü: Adresler farklı mı?
    # Eğer Shallow Copy yapsaydın bu adresler AYNI çıkardı.
    # Deep Copy yaptığın için FARKLI çıkmalı.
    print("\nKontrol 2 - Bellek Adresi:")
    print(f"Orijinal Not Listesi ID: {id(raw_student_data[0][1])}")
    print(f"Yeni Not Listesi ID:     {id(curved_data[0][1])}")

    if id(raw_student_data[0][1]) != id(curved_data[0][1]):
        print("SONUÇ: Deep Copy Başarılı! Orijinal veri korunmuş.")
    else:
        print("SONUÇ: HATA! Veriler hala birbirine bağlı (Aliasing var).")

if __name__ == "__main__":
    main()
