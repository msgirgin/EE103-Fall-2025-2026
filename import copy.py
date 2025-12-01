import copy

# Senaryo Verisi: [ID, [Vize, Final]]
raw_student_data = [
    [101, [50, 60]], 
    [102, [-1, 40]],   # Hatalı Veri (Vize -1)
    [103, [80, 90]], 
    [104, []],         # Hatalı Veri (Not girilmemiş)
    [105, [45, 50]]
]

# ---------------------------------------------------------
# PART 1: HELPER FUNCTIONS
# ---------------------------------------------------------

def calculate_averages(data):
    """
    Öğrencilerin ortalamasını hesaplar.
    """
    # DÜZELTME 1: Sonucu 'return' ile döndürmeyi unutma!
    calculated_average = [(student[1][0]*0.4 + student[1][1]*0.6) for student in data]
    return calculated_average

def get_high_achievers(data, threshold=70):
    """
    Belirli bir notun üzerindeki öğrencilerin ID'lerini döndürür.
    """
    # DÜZELTME 2: Burada da 'return' ekledik.
    high_achievers = [student[0] for student in data if (student[1][0]*0.4 + student[1][1]*0.6) > threshold]
    return high_achievers

def remove_invalid_entries(data):
    """
    Not listesi boş olan veya notu 0'dan küçük olanları siler.
    """
    # DÜZELTME 3: İç içe 'def' silindi, girintiler düzeltildi.
    for student in data[:]: # Kopya üzerinde gez
        notlar = student[1]
        
        if len(notlar) == 0:
            data.remove(student)
        elif min(notlar) < 0:
            data.remove(student)

# ---------------------------------------------------------
# PART 2: MAIN SCENARIO
# ---------------------------------------------------------

def apply_curve_safe(data, bonus_points):
    """
    Orijinal veriyi BOZMADAN notlara bonus puan ekler.
    """
    safe_data = copy.deepcopy(data) 
    
    for student in safe_data:
        notlar = student[1]
        for i in range(len(notlar)):
            notlar[i] += bonus_points
            
    return safe_data

def main():
    print("--- Orijinal Veri ---")
    print(raw_student_data)

    # Adım 1: Veriyi Temizle
    remove_invalid_entries(raw_student_data)
    print("--- Temizlenmiş Veri (Hatalılar Silindi) ---")
    print(raw_student_data) 
    
    # Adım 2: Başarılıları Bul
    basarili_ogrenciler = get_high_achievers(raw_student_data, 80)
    
    # DÜZELTME 4: 'rint' -> 'print' yapıldı.
    print(f"80 Barajını Geçen Öğrenciler: {basarili_ogrenciler}")

    # Adım 3: Çan Eğrisi Uygula (Güvenli Mod)
    curved_data = apply_curve_safe(raw_student_data, 10)
    
    print("--- Çan Uygulanmış Veri (Yeni Liste) ---")
    print(curved_data)
    
    print("--- Orijinal Veri Kontrolü (Değişmemiş Olmalı) ---")
    print(raw_student_data)

    # DÜZELTME 5: Bu blok main fonksiyonunun içine alındı (Girinti düzeltildi).
    # 1. İçerik Kontrolü
    print("\nKontrol 1 - İçerik Farkı:")
    print(f"Orijinaldeki İlk Öğrenci Notu: {raw_student_data[0][1]}") 
    print(f"Yenideki İlk Öğrenci Notu:     {curved_data[0][1]}")

    # 2. Bellek (Memory) Kontrolü
    print("\nKontrol 2 - Bellek Adresi:")
    print(f"Orijinal Not Listesi ID: {id(raw_student_data[0][1])}")
    print(f"Yeni Not Listesi ID:     {id(curved_data[0][1])}")

    if id(raw_student_data[0][1]) != id(curved_data[0][1]):
        print("SONUÇ: Deep Copy Başarılı! Orijinal veri korunmuş.")
    else:
        print("SONUÇ: HATA! Veriler hala birbirine bağlı (Aliasing var).")

if __name__ == "__main__":
    main()