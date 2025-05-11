# Simple X (Twitter) Crypto Sentiment Analyzer with Twikit and Gemini

Aplikasi Python ini menganalisis sentimen cryptocurrency di platform X (Twitter) menggunakan Gemini API, mengumpulkan tweet berdasarkan kata kunci pencarian, kemudian menganalisis sentimen dan tren.

## ✨ Fitur Utama

-   🔍 Pencarian tweet berdasarkan kata kunci atau hashtag (contoh: #BTC, #ETH)
-   📊 Pengumpulan tweet dari berbagai halaman dengan penanganan rate limiting
-   🤖 Analisis sentimen menggunakan Google Gemini AI
-   📈 Laporan sentimen termasuk:
    -   Breakdown sentimen (positif, negatif, netral)
    -   Analisis momentum
    -   Narasi utama yang sedang trending
    -   Aktivitas influencer
    -   Tweet dengan engagement tertinggi

## 🔧 Prasyarat

-   Python 3.10+
-   Akun X (Twitter)
-   API Key Google Gemini

## 📦 Instalasi

1. Clone repositori ini:

    ```bash
    git clone https://github.com/gafarybyh/crypto_x_sentiment.git
    cd twikit_gemini
    ```

2. Buat dan aktifkan virtual environment:

    ```bash
    python -m venv my_env

    # Windows
    my_env\Scripts\activate

    # Linux/Mac
    source my_env/bin/activate
    ```

3. Install dependensi:
    ```bash
    pip install -r requirements.txt
    ```

## ⚙️ Konfigurasi

1. Salin file `env.example` menjadi `.env`:

    ```bash
    cp env.example .env
    ```

2. Edit file `.env` dan isi dengan kredensial Anda:

    ```
    # X Account
    USERNAME = your_x_username
    EMAIL = your_x_email
    PASSWORD = your_x_password

    # Gemini API Key
    GEMINI_API_KEY = your_gemini_api_key
    ```

## 🚀 Cara Penggunaan

Jalankan aplikasi dengan perintah:

```bash
python main.py
```

Aplikasi akan meminta Anda untuk memasukkan kata kunci pencarian (misalnya `#btc`). Setelah itu, aplikasi akan:

1. Login ke akun X Anda (atau menggunakan cookies yang tersimpan)
2. Mengumpulkan minimal 30 tweet terkait kata kunci
3. Menganalisis tweet menggunakan Gemini AI
4. Menampilkan laporan sentimen yang komprehensif

## 📋 Contoh Output

```
🔥 #BTC X SENTIMENT 🔥

📊 Total tweets: 35

✅ Positive: 22 (avg score: 0.78)
❌ Negative: 8 (avg score: 0.65)
⚪ Neutral: 5

🏆 Dominant sentiment: positive

Momentum analysis:
Sentiment is building up with increasing engagement on positive tweets about Bitcoin's price recovery above $60K.

Key emerging narratives:
• ETF inflows accelerating after recent market correction
• Technical analysis suggesting strong support at $58K level
• Institutional buying pressure increasing
• Reduced selling from miners
• Positive regulatory signals from SEC commissioner statements

Notable influencer activity:
@michaelsaylor and @CryptoCred tweets showing bullish sentiment are receiving high engagement

Top tweets:
- @bitcoinmagazine: "BREAKING: BlackRock's #BTC ETF sees $250M inflows today as Bitcoin reclaims $60K" (RT: 1245, ❤️: 3782)
- @CryptoCred: "The $BTC chart is showing a classic accumulation pattern. Expecting a move to $65K within the week." (RT: 876, ❤️: 2103)
```

## 📄 Lisensi

Proyek ini dilisensikan di bawah [MIT License](LICENSE).
