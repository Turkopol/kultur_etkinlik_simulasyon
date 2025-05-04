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

# Grup oluşturma
st.header("1. Rol Seçimi")
selected_roller = {}
for rol in roller:
    selected_roller[rol] = st.text_input(f"{rol} adı:", key=rol)

if all(selected_roller.values()):
    st.success("Tüm roller atandı.")

    st.header("2. Kriz Senaryosu")
    if st.button("🎲 Kriz Senaryosu Oluştur"):
        senaryo = random.choice(kriz_senaryolari)
        st.warning(f"🚨 Kriz: {senaryo}")

    st.header("3. Krize Çözüm Geliştirme")
    for rol, kisi in selected_roller.items():
        st.text_area(f"{kisi} ({rol}) çözüm önerisi:", key=f"cozum_{rol}")

    st.header("4. Performans Değerlendirmesi")
    st.radio("Plana ne kadar sadık kalındı?", ["%100", "%75", "%50", "Daha az"])
    st.radio("Zamanında tamamlandı mı?", ["Evet", "Hayır"])
    st.radio("Maliyet kontrol altında mıydı?", ["Evet", "Hayır"])
    st.radio("Kalite korundu mu?", ["Evet", "Hayır"])

    st.header("5. Değişiklik Yönetimi")
    if st.button("📣 Değişiklik Senaryosu Göster"):
        st.info(f"📌 Yeni Durum: {degisiklik_senaryosu}")
        st.text_area("Yeni duruma karşı grup olarak nasıl bir aksiyon alırsınız?", key="degisiklik_cozumu")

    st.header("6. Sunum Notları ve Geri Bildirim")
    st.text_area("Grubunuzun genel stratejisini ve öğrendiklerinizi buraya yazınız:", key="sunum")

    st.button("📤 Simülasyonu Tamamla ve Geri Bildirim Al")

else:
    st.info("Lütfen önce tüm rolleri atayınız.")

