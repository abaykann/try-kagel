# 🏡 Analisis Harga Rumah – Ames Housing Dataset (Kaggle)

Proyek ini bertujuan untuk menganalisis harga rumah berdasarkan fitur-fitur seperti kualitas bangunan, luas rumah, dan tahun pembangunan. Hasil analisis divisualisasikan ke dalam grafik menggunakan Python.

Dataset: [House Prices - Advanced Regression Techniques](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques)

---

## 🔧 Cara Install Python dan Menjalankan Proyek (Windows & Mac)

### ✅ 1. Install Python

**Windows**
- Buka: https://www.python.org/downloads/
- Download dan install Python terbaru
- CENTANG “Add Python to PATH” saat install
- Setelah selesai, buka Command Prompt dan ketik:
  ```
  python --version
  pip --version
  ```

**Mac**
- Buka Terminal
- Jalankan:
  ```
  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
  brew install python
  ```
- Cek versi:
  ```
  python3 --version
  pip3 --version
  ```

---

### ✅ 2. Install Library Python

Jalankan salah satu:
```
pip install pandas matplotlib seaborn
```
> atau `pip3` jika pakai Mac

---

### ✅ 3. Download Dataset Kaggle

1. Buka: https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques/data  
2. Login dan download file `train.csv`  
3. Simpan file tersebut dalam folder yang sama dengan `analisis_rumah.py`

---

### ✅ 4. Struktur Folder

```
house-price-analysis/
├── README.md
├── analisis_rumah.py
├── train.csv
```

---

### ✅ 5. Jalankan Project

**Windows:**
```bash
cd path\ke\folder\house-price-analysis
python analisis_rumah.py
```

**Mac:**
```bash
cd /path/ke/folder/house-price-analysis
python3 analisis_rumah.py
```

---

### ✅ 6. Output

Script akan menghasilkan:
- `korelasi_harga.png`
- `luas_vs_harga.png`
- `tren_tahun_vs_harga.png`

Semua file ini akan muncul otomatis setelah script dijalankan.

---

## 📈 Insight

- Harga rumah sangat dipengaruhi oleh kualitas bangunan dan luas tempat tinggal.
- Harga rumah terus naik sejak tahun 1990-an.
- Analisis dilakukan dengan `pandas`, `seaborn`, dan `matplotlib`.

---

## ✍️ Author

Made with ❤️
