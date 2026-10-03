import re

with open('README.en.md', 'r', encoding='utf-8') as f:
    content = f.read()

intro_target_proper = r'Midas-Printer-Control is a local-first printer fleet manager for Nova3D resin printers and SDCP 3.0 compatible resin printers. It provides a polished Windows desktop app and an Android companion app for monitoring printers, browsing printer storage, and managing local print jobs on the same LAN.'

new_intro = """Midas-Printer-Control is a modern fleet manager to track and control multiple Nova3D and SDCP 3.0 compatible resin printers from a single Windows or Android application.

## Key Features

- **Dual Protocol Support**: Seamlessly controls legacy Nova3D HTTP (Port 8081) printers alongside next-generation **SDCP 3.0** (Port 3030) compatible resin printers.
- **Live Camera Streaming**: View real-time RTSP video streams from the internal cameras of SDCP 3.0 supported printers directly on your desktop via built-in FFMPEG integration.
- **Android & Desktop Sync**: Unified experience for Desktop (Windows) and Mobile (Android). Use the dedicated applications or scan the local QR code to manage your farm directly via the PWA.
- **Multi-Device Tracking**: Monitor dozens of printers in a single dashboard. Track print progress, time remaining, and current status in real-time.
- **Modern UI**: Polished, responsive interface with full Light and Dark mode support and perfect typography readability."""

content = content.replace(intro_target_proper, new_intro)

# also add logo
if 'logo.png' not in content:
    content = '<img src="public/logo.png" height="80" align="right" />\n\n' + content

with open('README.en.md', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated EN README")
