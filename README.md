# Simple X (Twitter) Crypto Sentiment Analyzer with Twikit and Gemini

Aplikasi python ini menganalisis sentimen cryptocurrency di platform X (Twitter) menggunakan Gemini API, mengumpulkan tweet berdasarkan kata kunci pencarian, kemudian menganalisis sentimen dan tren.

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
-   Akun X (Twitter) (recommended to use second account)
-   API Key Google Gemini

## 📦 Instalasi

1. Clone repositori ini:

    ```bash
    git clone https://github.com/gafarybyh/crypto_x_sentiment.git
    cd crypto_x_sentiment
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

    # Gemini Model
    # [gemini-2.5-flash-preview-04-17, gemini-2.0-flash]
    GEMINI_MODEL = gemini-2.5-flash-preview-04-17

    # Max Retry (if errors getting tweets)
    MAX_RETRY = 2
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
🔥 #BTC X Sentiment 🔥

📊 Total tweets: 38
✅ Positive: 18 (avg score: 0.79)
❌ Negative: 3 (avg score: -0.63)
⚪ Neutral: 17
🏆 Dominant sentiment: Positive

**Momentum analysis:**
Sentiment around #BTC appears to be building up strongly, driven by key technical indicators turning bullish and anticipation of price breakouts towards new highs. High engagement on positive tweets indicates growing conviction.

**Key emerging narratives:**
*   Anticipation of breaking $100K and setting new All-Time Highs.
*   Technical indicators flashing bullish signals (MACD, Buy signals).
*   Focus on liquidation levels for short positions.
*   Discussion around BTC Dominance and its potential impact on Altcoins.
*   Comparisons to previous market cycles and Halving related price analysis.

**Notable influencer activity:**
Several accounts show high engagement with bullish calls, including @Titan of Crypto, @Thomas Lauder ⚖️, and @Kevin Svenson, boosting pos
itive sentiment with technical analysis and price targets.

**Top tweets:**
- @Thomas Lauder ⚖️: “Good morning! #BTC around 100k https://t.co/hopdhpMmml” (RT: 275, ❤️: 1660)
- @Titan of Crypto: “#Bitcoin Bullish Crossover is Happening! 🔥\n\nThe MACD is flipping bullish on the weekly chart.\n\n#BTC momentum is shifting and this could be the start of a bigger move. 🚀 https://t.co/smSikCtF84” (RT: 275, ❤️: 1076)
```

## 📄 Lisensi

Proyek ini dilisensikan di bawah [MIT License](LICENSE).
