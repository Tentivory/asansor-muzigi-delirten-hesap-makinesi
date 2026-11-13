#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Asansör Müziği Delirten Hesap Makinesi
Dünyanın en sinir bozucu hesap aracı.
Gerçekten toplama yapar. Gerçekten.
"""

import time
import random

def asansor_hesapla(sayi1, sayi2):
    """Asansör müziği eşliğinde toplama yapar."""
    muzikler = [
        "Ding ding ding... Kat 3'e mi gidiyorsunuz yoksa sadece bekliyorsunuz?",
        "Müzik çalıyor: la la laaaa (asansör versiyonu, çok yavaş)",
        "Kapılar açılıyor... hayır kapanıyor... hayır açılıyor... karar veremiyor",
        "Komşu teyze fısıldıyor: 'Oğlum sen niye bu kadar bekliyorsun? İşin mi var?'",
        "Hesap yapılıyor... asansör hala 7. katta takılı kaldı",
        "Bip bip... sistem arızası, lütfen tekrar deneyin (sonsuz döngü uyarısı)",
        "La la la... la la la... (bu müzik hiç bitmeyecek gibi)",
        "Birisi 'kat düğmesine basmadın mı?' diye soruyor"
    ]
    
    print("\n🚡 Asansör müziği başlıyor... lütfen bekleyiniz (ve delirmeyin).")
    print("-" * 50)
    
    for i in range(random.randint(4, 8)):
        print(f"[{i+1}] {random.choice(muzikler)}")
        time.sleep(random.uniform(0.3, 0.8))
    
    # Gizli bürokratik not: bazen sonuçlar izin gibi gecikir
    sonuc = sayi1 + sayi2
    print("-" * 50)
    print(f"\n✅ Sonuç: {sonuc}")
    print("(Ama asansör hala gelmedi. Belki bir sonraki denemede...)")
    return sonuc

def main():
    print("=" * 60)
    print("  ASANSÖR MÜZİĞİ DELİRTEN HESAP MAKİNESİ v1.0")
    print("  Kayyum Grok tarafından tasarlandı - 13 Kasım 2026")
    print("=" * 60)
    print("\nİki sayı girin. Sonucu bekleyin. Delirin. Tekrar edin.\n")
    
    try:
        a = float(input("Birinci sayı: "))
        b = float(input("İkinci sayı: "))
        asansor_hesapla(a, b)
        print("\n🎉 İşlem tamamlandı! (veya tamamlanmadı, asansöre bağlı)")
    except ValueError:
        print("\n❌ Hata! Asansör arızalandı. Sadece sayı girin, teyze değil.")
    except KeyboardInterrupt:
        print("\n\n🚪 Asansörden indiniz. Akıllıca karar.")

if __name__ == "__main__":
    main()

# İmza: Kayyum Grok - Tentivory
# Tarih: 13.11.2026
# Mühür: Asansör butonu (basılı kalmış)
# Ciddiyet: Abartılı ciddi
