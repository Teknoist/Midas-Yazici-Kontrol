import re

with open('README.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the intro
intro_target = r'Midas YazÄ±cÄ± Kontrol, birden fazla Nova3D reÃ§ine yazÄ±cÄ±yÄ± aynÄ± Windows uygulamasÄ±ndan izlemek ve yÃ¶netmek iÃ§in geliÅŸtirilmiÅŸ modern bir masaÃ¼stÃ¼ uygulamasÄ±dÄ±r\.'
# Wait, reading with utf-8 will give proper characters:
intro_target_proper = r'Midas Yazıcı Kontrol, birden fazla Nova3D reçine yazıcıyı aynı Windows uygulamasından izlemek ve yönetmek için geliştirilmiş modern bir masaüstü uygulamasıdır.'

new_intro = """Midas Yazıcı Kontrol, birden fazla Nova3D ve SDCP 3.0 destekli reçine yazıcıyı aynı Windows ve Android uygulamasından izlemek ve yönetmek için geliştirilmiş modern bir araçtır.

## Öne Çıkan Özellikler

- **Çift Protokol Desteği**: Eski nesil Nova3D HTTP (Port 8081) yazıcıların yanında, yeni nesil **SDCP 3.0** (Port 3030) destekli tüm reçine yazıcıları tam uyumlulukla kontrol eder.
- **Canlı Kamera Akışı**: SDCP 3.0 destekli yazıcılarınızın (örn: Nova3D vb.) iç kameralarından gelen canlı RTSP video akışını, entegre FFMPEG teknolojisi sayesinde masaüstünden gecikmesiz olarak izleyin.
- **Android & Masaüstü Uygulaması**: Masaüstü (Windows) ve Mobil (Android) için ortak deneyim. İster masaüstü uygulamasını kullanın, ister yerleşik karekod üzerinden PWA arayüzü ile telefonunuzdan yönetin.
- **Çoklu Cihaz Takibi**: Onlarca yazıcıyı tek bir havuzda listeleyin, yazdırma yüzdelerini, kalan sürelerini ve çalışma durumlarını canlı takip edin.
- **Modern Arayüz**: Açık / Koyu tema destekli şık ve pürüzsüz arayüz. Özel renk tonları ve kusursuz okunabilirlik."""

content = content.replace(intro_target_proper, new_intro)

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated TR README")
