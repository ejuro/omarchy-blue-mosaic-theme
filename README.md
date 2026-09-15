# Blue Mosaic

A light Omarchy theme with a pale mosaic floor, graphite-blue motifs, and matching interface colors.

![Blue Mosaic wordmark wallpaper](preview.png)

## Appearance

- Two 3840 × 2160 wallpapers: the Omarchy logo and wordmark set into a continuous tile grid.
- A transparent top bar lets the tiles continue behind its icons and clock.
- Solid, cool-white terminal, menu, and launcher backgrounds keep text clear.
- Blue accents, pale slate borders, and a coordinated graphite-blue terminal palette.
- Standard Adwaita icons.

| Role | Color |
| --- | --- |
| Main text / dark motif tiles | `#283545` |
| Accent / blue motif tiles | `#354B67` |
| Secondary text / muted tiles | `#62748A` |
| Inactive borders / pale tiles | `#A8B3C1` |
| App background | `#FAFBFC` |
| Selection background | `#E0E5EB` |

The terminal palette deliberately uses shades of graphite and blue for all ANSI colors. Programs that rely on red/green distinctions will therefore appear monochromatic. Apps with fixed colors or their own artwork may retain them.

## Install

Requires **Omarchy 4 with Omarchy Shell**. Validated against Omarchy 4.0.3.

From a local checkout:

```sh
mkdir -p "$HOME/.config/omarchy/themes"
ln -s "$PWD" "$HOME/.config/omarchy/themes/blue-mosaic"
omarchy theme set "Blue Mosaic"
```

Run these commands from the repository root. The destination must not already exist.

For a published repository, use `omarchy theme install <repository-url>`. The recommended GitHub repository name is **omarchy-blue-mosaic-theme**, which Omarchy installs as **blue-mosaic**.

Switch wallpapers through Omarchy's background picker or:

```sh
omarchy theme bg next
```

Omarchy generates terminal, editor, browser, and shell configurations from `colors.toml`. No runtime scripts, hooks, or extra services are required. The bundled GTK stylesheet applies where the current theme stylesheet is loaded by the application.

## Wallpapers

| Motif | Wallpaper | Editable source |
| --- | --- | --- |
| Logo | [4K PNG](backgrounds/01-blue-mosaic-logo-4k.png) | [SVG](source/logo.svg) |
| Wordmark | [4K PNG](backgrounds/02-blue-mosaic-wordmark-4k.png) | [SVG](source/wordmark.svg) |

The pale floor uses three near-white tile shades and fine blue-grey grout. Both motifs share the floor's grid, with no cast shadow or grain layer. The preview contains only wallpaper artwork.

## Optional workspace accent

The standard workspace widget uses the bar text color for every workspace. The optional adaptation in `extras/Workspaces.qml` reads `workspaces.focused-color` from the theme. It falls back to the normal bar color for themes without that token.

To use it, from this repository:

```sh
omarchy plugin clone omarchy.workspaces
cp extras/Workspaces.qml "$HOME/.config/omarchy/plugins/$USER.workspaces/Workspaces.qml"
omarchy restart shell
```

If you already customized a local workspace widget, merge the `foreground` binding instead of replacing your file. The theme works without this optional widget.

## Development

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

## License

[MIT](LICENSE). Omarchy artwork and the optional workspace widget retain their upstream attribution in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
