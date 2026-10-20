"""Ekstraksi dan ringkasan fasilitas publik dari OpenStreetMap menggunakan OSMnx."""
import pandas as pd
import osmnx as ox

def main():
    place = input("Masukkan wilayah (contoh: Bengkulu City, Indonesia): ").strip()
    if not place:
        place = "Bengkulu City, Indonesia"
    tags = {
        "amenity": ["hospital", "clinic", "school", "pharmacy"],
    }
    print(f"Mengambil fasilitas OpenStreetMap untuk: {place}")
    gdf = ox.features_from_place(place, tags)
    if gdf.empty:
        print("Tidak ada fitur yang ditemukan untuk tag tersebut di wilayah ini.")
        return
    gdf = gdf.reset_index()
    # Fitur dapat berupa point atau polygon; centroid dipakai untuk ringkasan titik.
    gdf["geometry"] = gdf.geometry.to_crs("EPSG:3857")
    centroids = gdf.geometry.centroid.to_crs("EPSG:4326")
    gdf["longitude"] = centroids.x
    gdf["latitude"] = centroids.y
    keep = [c for c in ["element", "id", "name", "amenity", "healthcare", "geometry",
                        "latitude", "longitude"] if c in gdf.columns]
    result = gdf[keep].copy()
    result = result.drop(columns=["geometry"], errors="ignore")
    result.to_csv("osm_public_facilities.csv", index=False)
    print(f"Jumlah fitur: {len(result)}")
    print("\nRingkasan menurut jenis:")
    type_col = "amenity" if "amenity" in result else "healthcare"
    print(result[type_col].value_counts(dropna=False))
    print("\nSampel:")
    print(result.head(10).to_string(index=False))
    print("\nTersimpan: osm_public_facilities.csv")
    print("Data OSM tidak selalu lengkap. Verifikasi lapangan diperlukan.")
if __name__ == "__main__":
    main()
