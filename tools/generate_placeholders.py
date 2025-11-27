#!/usr/bin/env python3
"""
Generate solid-color PNG placeholders without external dependencies.
Writes 128x128 PNGs to `assets/images/` for the names used in the project atlas.
"""
import os
import zlib
import struct

OUT_DIR = os.path.join(os.path.dirname(__file__), '..', 'assets', 'images')
os.makedirs(OUT_DIR, exist_ok=True)

IMAGES = {
    'lantern_red.png': (255, 60, 60),
    'lantern_blue.png': (60, 120, 255),
    'lantern_yellow.png': (255, 210, 60),
    'luma_idle.png': (200, 230, 255),
    'heart.png': (255, 80, 90),
    'background.png': (18, 24, 48),
}

W = 128
H = 128

def png_chunk(chunk_type, data):
    chunk = struct.pack('>I', len(data)) + chunk_type + data
    crc = zlib.crc32(chunk_type + data) & 0xffffffff
    chunk += struct.pack('>I', crc)
    return chunk

def write_png(path, width, height, rgb):
    r, g, b = rgb
    sig = b'\x89PNG\r\n\x1a\n'
    # IHDR: width(4) height(4) bitdepth(1) colorType(1) compression(1) filter(1) interlace(1)
    ihdr = struct.pack('>IIBBBBB', width, height, 8, 2, 0, 0, 0)
    raw = bytearray()
    for y in range(height):
        raw.append(0)  # no filter for this scanline
        raw.extend([r, g, b] * width)
    compressed = zlib.compress(bytes(raw), level=9)

    png = bytearray()
    png.extend(sig)
    png.extend(png_chunk(b'IHDR', ihdr))
    png.extend(png_chunk(b'IDAT', compressed))
    png.extend(png_chunk(b'IEND', b''))

    with open(path, 'wb') as f:
        f.write(png)

def main():
    created = []
    for name, color in IMAGES.items():
        path = os.path.join(OUT_DIR, name)
        write_png(path, W, H, color)
        created.append(path)
    print('Created images:')
    for p in created:
        print(' -', p)

if __name__ == '__main__':
    main()
