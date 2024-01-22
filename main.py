import argparse
from googlesearch import search

class Color:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    END = '\033[0m'

banner = Color.BLUE + r"""
 _____ _   _ _____  _____  _____ _____ _____ 
/  ___| | | /  __ \/  __ \|  ___/  ___/  ___|
\ `--.| | | | /  \/| /  \/| |__ \ `--.\ `--. 
 `--. \ | | | |    | |    |  __| `--. \`--. \
/\__/ / |_| | \__/\| \__/\| |___/\__/ /\__/ /
\____/ \___/ \____/ \____/\____/\____/\____/ 
""" + Color.END

def google_arama(file_path, ulke_kodu, site_sayisi):
    print(banner)
    try:

        with open(file_path, 'r') as file:
            dorks = [line.strip() for line in file]

        for dork in dorks:
            dork_sorgu = f"inurl:{dork} site:{ulke_kodu}"
            sonuclar = search(dork_sorgu, num_results=site_sayisi)

            index = 0
            for sonuc in sonuclar:
                index += 1
                print(f"{index}: {sonuc}")
                with open("sonuclar.txt", "a") as dosya:
                    dosya.write(sonuc + "\n")
                if index >= site_sayisi:
                    break
    except Exception as hata:
        print(f"Hata: {hata}")

def main():
    parser = argparse.ArgumentParser(description="Google araması yapma scripti.")
    parser.add_argument("-f", "--file", required=True, help="Dork'ları içeren metin dosyasının yolu (her satıra bir tane)")
    parser.add_argument("-u", "--ulke", required=True, help="Ülke kodu (Ör: us, za)")
    parser.add_argument("-s", "--site", type=int, required=True, help="Kaç tane site sıralaması istediğiniz (Ör: 12)")
    args = parser.parse_args()

    google_arama(args.file, args.ulke, args.site)

if __name__ == "__main__":
    main()