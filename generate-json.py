#!/usr/bin/env python3
"""
Script per generare albums.json dalla struttura cartelle
Esegui dopo aver aggiunto nuove foto: python3 generate-json.py
"""

import os
import json
from pathlib import Path

def generate_albums_json():
    albums_dir = Path('albums')
    albums = []
    
    # Verifica che la cartella albums esista
    if not albums_dir.exists():
        print("❌ Cartella 'albums' non trovata!")
        print("💡 Crea la cartella: mkdir albums")
        return
    
    # Estensioni immagini supportate
    image_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.webp', '.JPG', '.JPEG', '.PNG'}
    
    # Scansiona le sottocartelle
    subdirs = [d for d in albums_dir.iterdir() if d.is_dir()]
    
    if not subdirs:
        print("⚠️  Nessuna sottocartella trovata in 'albums/'")
        print("💡 Crea sottocartelle per ogni album:")
        print("   mkdir 'albums/Partita vs Padova'")
        return
    
    for subdir in sorted(subdirs):
        photos = []
        
        # Trova tutte le immagini nella cartella
        for file in sorted(subdir.iterdir()):
            if file.suffix.lower() in image_extensions:
                photos.append(file.name)
        
        if photos:
            albums.append({
                'name': subdir.name,
                'folder': subdir.name,
                'photos': photos,
                'count': len(photos)
            })
            print(f"✅ {subdir.name}: {len(photos)} foto")
    
    if not albums:
        print("⚠️  Nessuna foto trovata!")
        print("💡 Aggiungi foto nelle sottocartelle di 'albums/'")
        return
    
    # Salva JSON
    with open('albums.json', 'w', encoding='utf-8') as f:
        json.dump(albums, f, indent=2, ensure_ascii=False)
    
    total_photos = sum(a['count'] for a in albums)
    print(f"\n🎉 Generato albums.json:")
    print(f"   📁 {len(albums)} album")
    print(f"   📸 {total_photos} foto totali")
    print(f"\n✨ Pronto per il commit su GitHub!")

if __name__ == '__main__':
    generate_albums_json()