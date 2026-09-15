"""Validate Blue Mosaic against local Omarchy templates without changing the theme."""
import json
from pathlib import Path
import re
import shlex
import shutil
import struct
import subprocess
import tempfile
import tomllib

ROOT = Path(__file__).resolve().parents[1]

def luminance(color):
    rgb = [int(color[i:i+2], 16) / 255 for i in (1, 3, 5)]
    return sum((v / 12.92 if v <= .04045 else ((v + .055) / 1.055) ** 2.4) * w
               for v, w in zip(rgb, (.2126, .7152, .0722)))

def contrast(a, b):
    low, high = sorted((luminance(a), luminance(b)))
    return (high + .05) / (low + .05)

def main():
    colors = tomllib.loads((ROOT / 'colors.toml').read_text())
    assert colors['mode'] == 'light'
    for key, color in colors.items():
        if key != 'mode':
            assert re.fullmatch(r'#[0-9a-fA-F]{6}', color), (key, color)
    text_keys = ['foreground', 'dark_foreground', 'light_foreground', 'bright_foreground', 'muted',
                 'accent', 'red', 'green', 'yellow', 'orange', 'blue', 'cyan', 'magenta', 'brown']
    text_keys += [key for key in colors if key.startswith('bright_') and key != 'bright_foreground']
    minimum = min(contrast(colors[key], colors['background']) for key in text_keys)
    assert minimum >= 4.5, minimum
    selected = contrast(colors['selection_foreground'], colors['selection_background'])
    assert selected >= 4.5
    wallpapers = sorted((ROOT / 'backgrounds').glob('*.png'))
    assert len(wallpapers) == 2
    for path in wallpapers:
        data = path.read_bytes()
        assert data[:8] == b'\x89PNG\r\n\x1a\n'
        assert struct.unpack('>II', data[16:24]) == (3840, 2160)

    executable = shutil.which('omarchy-theme-set-templates')
    assert executable, 'Omarchy theme renderer is required'
    with tempfile.TemporaryDirectory(prefix='blue-mosaic-validation-') as scratch:
        output = Path(scratch) / 'generated'
        output.mkdir()
        for source in ROOT.glob('*.toml'):
            shutil.copy2(source, output / source.name)
        renderer = Path(executable).read_text()
        assignment = 'NEXT_THEME_DIR="$HOME/.local/state/omarchy/current/next-theme"'
        assert assignment in renderer, 'Omarchy renderer path changed; update the validation adapter'
        # Redirect only this temporary copy's output; HOME and the installed script stay untouched.
        renderer = renderer.replace(assignment, 'NEXT_THEME_DIR=' + shlex.quote(str(output)), 1)
        subprocess.run(['bash', '-c', renderer], check=True)
        assert len(list(output.iterdir())) >= 20
        for path in output.iterdir():
            contents = path.read_text()
            assert '{{' not in contents, f'Unresolved template token in {path.name}'
            if path.suffix == '.toml':
                tomllib.loads(contents)
            if path.suffix == '.json':
                json.loads(contents)
        shell = tomllib.loads((output / 'shell.toml').read_text())
        assert shell['bar']['background'] == '#F5F6F7'
        assert shell['bar']['background-alpha'] == 0.0
        assert shell['menu']['background-alpha'] == 1.0
        assert shell['menu']['selected-background'] == colors['selection']
        assert shell['launcher']['background-alpha'] == 1.0
        editor = json.loads((output / 'vscode-theme.json').read_text())
        assert editor['type'] == 'light'
        terminal = tomllib.loads((output / 'alacritty.toml').read_text())
        assert terminal['colors']['primary']['background'] == colors['background']
        assert terminal['colors']['selection']['text'] == colors['selection_foreground']
        print(f'Omarchy templates: {len(list(output.iterdir()))} files generated and checked')
    print(f'Text contrast: minimum {minimum:.2f}:1; selection {selected:.2f}:1')
    print('Two 4K mosaic-floor wallpapers checked')

if __name__ == '__main__':
    main()
