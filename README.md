# Warp Theme (No Logo)

![Warp Theme Preview](example.png)

The official Warp terminal theme with its signature blue accent and dark background, but with the Warp logo removed from the background image for a cleaner look.

## Available Variants

- **warp** - Original theme with logo removed
- **warp_darker** - Same theme with a darker background image for reduced eye strain

## Installation

```bash
# Clone the repository
git clone https://github.com/silouanwright/warp-default-no-logo.git
cd warp-default-no-logo

# For the standard theme
cp warp/* ~/.warp/themes/

# For the darker variant
cp warp_darker/* ~/.warp/themes/
```

## Using the Theme
1. Open Warp settings (⌘+,)
2. Go to Appearance → Themes
3. Select "Warp No Logo" or "Warp Darker" from the theme list

## Theme Colors

- **Accent**: `#5299bf` (Blue)
- **Background**: `#061229` (Dark Navy)
- **Foreground**: `#d8dbe2` (Soft White - slightly adjusted for better readability)

## Features

- Original Warp theme colors and settings
- Custom background image with 60% opacity (Warp logo removed)
- Dark theme optimized for long coding sessions
- Carefully selected terminal colors for optimal readability

## Differences from Original

This theme is based on the official [Warp theme](https://github.com/warpdotdev/themes/tree/main/warp_bundled) that comes bundled with Warp Terminal.

This variant is based on the official Warp theme with these adjustments:
- The Warp logo has been masked out from the background image for a cleaner, distraction-free appearance
- Foreground text color slightly brightened from `#b8bbc2` to `#d8dbe2` for improved readability
- All other color values and settings remain the same as the original

Original theme location: `~/.warp/themes/warp_bundled/warp.yaml`