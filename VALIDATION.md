# Release validation

Validated with Omarchy 4.0.3 and Python 3.11+.

## Theme and artwork

- 29 generated configuration and override files checked with the installed Omarchy renderer; TOML and JSON parse successfully and contain no unresolved template tokens.
- Two native 3840 × 2160 PNG wallpapers, reproduced from the bundled SVGs and matched against the approved artwork.
- The 1920 × 1080 README preview contains wallpaper artwork only.
- Minimum palette text contrast is 4.62:1; selected text contrast is 9.84:1.
- Transparent top bar; solid terminal, menu, and launcher surfaces.
- Optional workspace widget is separate from the theme and requires explicit local installation.

## Repository review

- Only the final theme, two wallpapers, their SVG sources, preview, optional widget, documentation, and development tools are included.
- No desktop captures, experimental variants, personal shell layout, hooks, terminal histories, or machine-specific configuration are included.
- Text files checked for credential patterns, private keys, personal paths, local usernames, and email addresses; no matches found.
- PNGs contain no EXIF or text metadata. SVGs have no external asset references.
- MIT copyright attribution is retained in LICENSE and THIRD_PARTY_NOTICES.md.

Checks describe this release snapshot. Future changes should be reviewed before publication. Individual third-party applications with cached or fixed colors have not all been tested.
