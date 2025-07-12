# analisis_rumah.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("📦 Membaca data...")
df = pd.read_csv('train.csv')

print("✅ Data berhasil dimuat. Jumlah baris:", len(df))

# Korelasi Fitur Terhadap Harga
print("📊 Membuat heatmap korelasi...")
plt.figure(figsize=(10, 6))
sns.heatmap(df[['SalePrice', 'OverallQual', 'GrLivArea', 'YearBuilt', 'TotalBsmtSF']].corr(), annot=True)
plt.title('Korelasi Antar Fitur terhadap Harga Jual')
plt.tight_layout()
plt.savefig('korelasi_harga.png')
plt.close()

# Scatterplot Luas vs Harga
print("📊 Membuat scatterplot luas vs harga...")
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='GrLivArea', y='SalePrice', hue='OverallQual', palette='viridis')
plt.title('Hubungan Luas Rumah dengan Harga Jual')
plt.tight_layout()
plt.savefig('luas_vs_harga.png')
plt.close()

# Tren Harga per Tahun Bangun
print("📊 Membuat grafik tren harga per tahun...")
plt.figure(figsize=(12, 6))
mean_price_per_year = df.groupby('YearBuilt')['SalePrice'].mean().reset_index()
sns.lineplot(data=mean_price_per_year, x='YearBuilt', y='SalePrice')
plt.title('Tren Harga Rumah Rata-rata Berdasarkan Tahun Bangun')
plt.tight_layout()
plt.savefig('tren_tahun_vs_harga.png')
plt.close()

print("✅ Semua grafik berhasil dibuat dan disimpan:")
print("- korelasi_harga.png")
print("- luas_vs_harga.png")
print("- tren_tahun_vs_harga.png")
