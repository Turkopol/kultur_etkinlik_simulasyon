import streamlit as st
import random

st.set_page_config(page_title="Proje Simülasyonu", layout="wide")

st.title("🎭 Proje Uygulama Simülasyonu: Kampüste Kültürel Etkinlik")

# Roller ve senaryolar
roller = {
    "Proje Yöneticisi": "Tüm ekiplerin koordinasyonundan sorumludur.",
    "Pazarlama Sorumlusu": "Davetiye, duyuru, sosyal medya çalışmalarını yapar.",
    "Teknik Ekip Üyesi": "Ses, görüntü, teknik ekipmanlardan sorumludur.",
    "Lojistik Koordinatörü": "Mekan, masa-sandalye düzeni, güvenlik gibi konulara bakar.",
    "Finans Sorumlusu": "Bütçe ve maliyetleri kontrol eder."
}

kriz_senaryolari = [
    "Mekan son anda iptal edildi.",
    "Davetiye basımı gecikecek.",
    "Ses sistemi arızalandı.",
    "Katılımcı sayısı beklenenden fazla geldi."
]

degisiklik_senaryosu = "Etkinliğe iki konuk konuşmacı daha eklendi."

# 1. ROL SEÇİMİ
st.header("1. Rol Seçimi")
selected_roller = {}
for rol in roller:
    selected_roller[rol] = st.text_input(f"{rol} adı:", key=rol)

# Tüm roller atandıysa devam et
if all(selected_roller.values()):
    st.success("✅ Tüm roller başarıyla atandı.")

    # 2. KRİZ SENARYOSU
    st.header("2. Kriz Senaryosu")
    if "senaryo" not in st.session_state:
        if st.button("🎲 Kriz Senaryosu Oluştur"):
            st.session_state.senaryo = random.choice(kriz_senaryolari)
    if "senaryo" in st.session_state:
        st.warning(f"🚨 Kriz: {st.session_state.senaryo}")

    # 3. ÇÖZÜM ÖNERİLERİ
    st.header("3. Krize Çözüm Geliştirme")
    for rol, kisi in selected_roller.items():
        st.text_area(f"{kisi} ({rol}) çözüm önerisi:", key=f"cozum_{rol}")

    # 4. PERFORMANS DEĞERLENDİRMESİ
    st.header("4. Performans Değerlendirmesi")
    st.radio("Plana ne kadar sadık kalındı?", ["%100", "%75", "%50", "Daha az"], key="plan_sadakat")
    st.radio("Zamanında tamamlandı mı?", ["Evet", "Hayır"], key="zaman")
    st.radio("Maliyet kontrol altında mıydı?", ["Evet", "Hayır"], key="maliyet")
    st.radio("Kalite korundu mu?", ["Evet", "Hayır"], key="kalite")

    # 5. DEĞİŞİKLİK YÖNETİMİ
    st.header("5. Değişiklik Yönetimi")
    if "degisiklik_gosterildi" not in st.session_state:
        if st.button("📣 Değişiklik Senaryosu Göster"):
            st.session_state.degisiklik_gosterildi = True
    if "degisiklik_gosterildi" in st.session_state:
        st.info(f"📌 Yeni Durum: {degisiklik_senaryosu}")
        st.text_area("Yeni duruma karşı grup olarak nasıl bir aksiyon alırsınız?", key="degisiklik_cozumu")

    # 6. SUNUM & GERİ BİLDİRİM
    st.header("6. Sunum ve Öğrenilenler")
    st.text_area("Grubunuzun genel stratejisini ve öğrendiklerinizi buraya yazınız:", key="sunum")

    # GERİ BİLDİRİM DÜĞMESİ
    if st.button("📤 Simülasyonu Tamamla ve Geri Bildirim Al"):
        st.subheader("📝 Geri Bildirim ve Özet")

        st.write("### 🎯 Rol Dağılımı:")
        for rol, kisi in selected_roller.items():
            st.write(f"• **{rol}**: {kisi}")

        st.write("### 🧩 Kriz Senaryosu:")
        st.write(f"• {st.session_state.get('senaryo', 'Belirtilmedi.')}")

        st.write("### 🛠️ Çözüm Önerileri:")
        for rol in roller:
            cozum = st.session_state.get(f"cozum_{rol}", "")
            st.write(f"- **{rol} ({selected_roller[rol]})**: {cozum}")

        st.write("### 📊 Performans Değerlendirmesi:")
        st.write(f"• Plana Uyma: {st.session_state.plan_sadakat}")
        st.write(f"• Zamanında Tamamlandı mı?: {st.session_state.zaman}")
        st.write(f"• Maliyet Durumu: {st.session_state.maliyet}")
        st.write(f"• Kalite Korundu mu?: {st.session_state.kalite}")

        st.write("### 🔄 Değişiklik Karşısındaki Strateji:")
        st.write(st.session_state.get("degisiklik_cozumu", "Belirtilmemiş."))

        st.write("### 🎤 Genel Sunum ve Öğrenilenler:")
        st.success(st.session_state.get("sunum", "Sunum bölümü boş bırakılmış."))

        st.balloons()
        st.info("🎉 Tebrikler! Simülasyonu başarıyla tamamladınız. Geri bildirimlerinizi gözden geçirin ve öğretmeninizle paylaşın.")

else:
    st.info("👉 Lütfen önce tüm rolleri atayınız.")
