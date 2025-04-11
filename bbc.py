import requests
from bs4 import BeautifulSoup

base_url = 'https://www.bbc.com/indonesia/topics/cjgn7k8yx4gt?page='
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
}

all_links = []

for page in range(1, 41):
    url = base_url + str(page)
    print(f'📄 Mengambil dari halaman {page}...')

    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Ambil semua tag <a> yang sesuai dengan class
        links = soup.find_all('a', class_='bbc-1i4ie53 e1d658bg0')

        for link in links:
            href = link.get('href')
            if href and href.startswith('https://www.bbc.com/indonesia/articles/'):
                all_links.append(href)

    except Exception as e:
        print(f'❌ Gagal mengambil halaman {page}: {e}')

# Hapus duplikat jika ada
unique_links = list(set(all_links))

# Simpan ke file
with open('links.txt', 'w', encoding='utf-8') as f:
    for link in unique_links:
        f.write(link + '\n')

print(f'✅ Selesai! Total {len(unique_links)} link disimpan ke links.txt')
