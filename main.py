from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

WIB = ZoneInfo("Asia/Jakarta")

def main():
    besok = datetime.now(WIB) + timedelta(days=1)

    print("SISTEM ANALISIS BOLA OTOMATIS")
    print("Tanggal analisis:", besok.strftime("%d-%m-%Y"))
    print("Zona waktu: WIB")
    print("Status: Program berhasil dijalankan.")

if __name__ == "__main__":
    main()
