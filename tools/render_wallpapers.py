"""Render the two Blue Mosaic wallpapers and a wallpaper-only README preview."""
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]

def main():
    for number, kind in ((1, 'logo'), (2, 'wordmark')):
        source = ROOT / 'source' / f'{kind}.svg'
        output = ROOT / 'backgrounds' / f'{number:02}-blue-mosaic-{kind}-4k.png'
        subprocess.run(['rsvg-convert', str(source), '-o', str(output)], check=True)
        print(output.name)
    subprocess.run(['rsvg-convert', '-w', '1920', str(ROOT / 'source/wordmark.svg'),
                    '-o', str(ROOT / 'preview.png')], check=True)

if __name__ == '__main__':
    main()
