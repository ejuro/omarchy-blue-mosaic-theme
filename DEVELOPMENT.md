# Development

## Local checkout

From the repository root:

```sh
mkdir -p "$HOME/.config/omarchy/themes"
ln -s "$PWD" "$HOME/.config/omarchy/themes/blue-mosaic"
omarchy theme set "Blue Mosaic"
```

The destination must not already exist. For publication, the repository name `omarchy-blue-mosaic-theme` installs as `blue-mosaic` through Omarchy's theme installer.

## Tools

Rebuild the PNG wallpapers and preview from the bundled SVGs:

```sh
python tools/render_wallpapers.py
```

Requires Python 3 and `rsvg-convert` from librsvg. The installed theme needs neither tool.

Validate colors, wallpaper dimensions, and generated configurations:

```sh
python tools/validate.py
```

Requires Python 3.11+ and a local Omarchy installation. Validation renders configurations in a temporary directory without changing the active theme. See [VALIDATION.md](VALIDATION.md) for the release checks.

