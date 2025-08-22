# Warp Theme (No Logo)

The official Warp terminal theme with its signature blue accent and dark background, but with the Warp logo removed from the background image for a cleaner look.

## Available Variants

- **warp** - Original theme with logo removed
- **warp_darker** - Darker variant with enhanced contrast

## Installation

### Option 1: Clone and Copy
```bash
# Clone the repository
git clone https://github.com/silouanwright/warp-default-no-logo.git
cd warp-default-no-logo

# Copy themes to Warp directory
cp warp.yaml ~/.warp/themes/
cp warp.jpg ~/.warp/themes/

# For the darker variant
cp warp_darker.yaml ~/.warp/themes/
cp darker.jpg ~/.warp/themes/
```

### Option 2: Clone and Symlink
```bash
# Clone the repository
git clone https://github.com/silouanwright/warp-default-no-logo.git
cd warp-default-no-logo

# Symlink themes (automatically updates when you pull changes)
ln -s $(pwd)/warp.yaml ~/.warp/themes/warp_no_logo.yaml
ln -s $(pwd)/warp.jpg ~/.warp/themes/warp_no_logo.jpg

# For the darker variant
ln -s $(pwd)/warp_darker.yaml ~/.warp/themes/warp_darker.yaml
ln -s $(pwd)/darker.jpg ~/.warp/themes/darker.jpg
```

### Using the Theme
1. Open Warp settings (⌘+,)
2. Go to Appearance → Themes
3. Select "Warp No Logo" or "Warp Darker" from the theme list

## Theme Colors

- **Accent**: `#5299bf` (Blue)
- **Background**: `#061229` (Dark Navy)
- **Foreground**: `#b8bbc2` (Light Gray)

## Features

- Original Warp theme colors and settings
- Custom background image with 60% opacity (Warp logo removed)
- Dark theme optimized for long coding sessions
- Carefully selected terminal colors for optimal readability

## Differences from Original

This theme is based on the official [Warp theme](https://github.com/warpdotdev/themes/tree/main/warp_bundled) that comes bundled with Warp Terminal.

This variant is identical to the official Warp theme except:
- The Warp logo has been masked out from the background image for a cleaner, distraction-free appearance
- All color values and settings remain exactly the same as the original

Original theme location: `~/.warp/themes/warp_bundled/warp.yaml`