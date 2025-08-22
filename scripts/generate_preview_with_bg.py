#!/usr/bin/env python3
import os
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import yaml

def get_theme_colors(theme_path):
    """Load theme colors from YAML file"""
    with open(theme_path) as f:
        theme = yaml.safe_load(f)
    
    colors = {
        'foreground': theme['foreground'],
        'background': theme['background'],
        'accent': theme['accent'],
    }
    
    # Add terminal colors
    for color_name in theme['terminal_colors']['normal']:
        colors[color_name] = theme['terminal_colors']['normal'][color_name]
    
    for color_name in theme['terminal_colors']['bright']:
        colors[f'br{color_name}'] = theme['terminal_colors']['bright'][color_name]
    
    return colors

def create_text_overlay(colors, output_path, width=600, height=290):
    """Create transparent PNG with terminal text"""
    # Create transparent image
    img = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Use a larger font size and simpler approach
    font_size = 16
    
    # Try to load Monaco or Menlo font
    font = None
    font_paths = [
        '/System/Library/Fonts/Monaco.ttf',
        '/System/Library/Fonts/Menlo.ttc',
        '/Library/Fonts/Courier New.ttf',
        '/System/Library/Fonts/Courier.ttc',
    ]
    
    for font_path in font_paths:
        if Path(font_path).exists():
            try:
                font = ImageFont.truetype(font_path, font_size)
                break
            except:
                continue
    
    # Fallback to default if no font found
    if font is None:
        font = ImageFont.load_default()
        font_size = 11  # Default font is smaller
    
    # Draw terminal content with better spacing
    y_pos = 30
    line_height = 25
    
    # Line 1: ls command
    draw.text((30, y_pos), 'ls', fill=colors['foreground'], font=font)
    y_pos += line_height
    
    # Line 2: dir, executable, file
    draw.text((30, y_pos), 'dir', fill=colors['blue'], font=font)
    draw.text((100, y_pos), 'executable', fill=colors['red'], font=font)
    draw.text((250, y_pos), 'file', fill=colors['foreground'], font=font)
    y_pos += line_height + 10
    
    # Separator line
    draw.line([(0, y_pos), (width, y_pos)], fill=colors['foreground'], width=1)
    y_pos += 15
    
    # Colors display
    draw.text((30, y_pos), 'bash ~/colors.sh', fill=colors['foreground'], font=font)
    y_pos += line_height
    
    # Normal colors
    draw.text((30, y_pos), 'normal:', fill=colors['foreground'], font=font)
    x = 110
    for color in ['black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']:
        draw.text((x, y_pos), color[:5], fill=colors[color], font=font)
        x += 55
    y_pos += line_height
    
    # Bright colors
    draw.text((30, y_pos), 'bright:', fill=colors['foreground'], font=font)
    x = 110
    for color in ['black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']:
        draw.text((x, y_pos), color[:5], fill=colors[f'br{color}'], font=font)
        x += 55
    y_pos += line_height + 10
    
    # Separator line
    draw.line([(0, y_pos), (width, y_pos)], fill=colors['foreground'], width=1)
    y_pos += 15
    
    # Prompt
    draw.text((30, y_pos), '~/project', fill=colors['magenta'], font=font)
    draw.text((130, y_pos), 'git(', fill=colors['green'], font=font)
    draw.text((170, y_pos), 'main', fill=colors['yellow'], font=font)
    draw.text((220, y_pos), ')', fill=colors['green'], font=font)
    
    # Cursor
    draw.rectangle([(30, y_pos + 25), (35, y_pos + 45)], fill=colors['accent'])
    
    img.save(output_path)
    return img

def create_preview_with_background(theme_dir, theme_name):
    """Create preview image with actual background"""
    theme_path = Path(theme_dir) / f'{theme_name}.yaml'
    bg_path = Path(theme_dir) / f'{theme_name}.jpg'
    
    # Get colors from theme
    colors = get_theme_colors(theme_path)
    
    # Create text overlay
    overlay_path = Path(theme_dir) / 'previews' / f'{theme_name}_text.png'
    overlay_path.parent.mkdir(exist_ok=True)
    text_img = create_text_overlay(colors, overlay_path)
    
    # Load and resize background
    if bg_path.exists():
        bg = Image.open(bg_path)
        # Resize background to preview size
        bg = bg.resize((600, 290), Image.Resampling.LANCZOS)
        
        # Create a solid color background
        solid_bg = Image.new('RGBA', (600, 290), colors['background'])
        
        # Convert background to RGBA and apply opacity
        bg = bg.convert('RGBA')
        # Blend: 40% solid background + 60% image (0.6 opacity)
        bg_with_opacity = Image.blend(solid_bg, bg, 0.6)
        
        # Composite text over background
        final = Image.alpha_composite(bg_with_opacity.convert('RGBA'), text_img)
    else:
        # Just use solid background if no image
        final = Image.new('RGBA', (600, 290), colors['background'])
        final = Image.alpha_composite(final, text_img)
    
    # Convert to RGB for saving as PNG (removes transparency)
    final = final.convert('RGB')
    
    # Save final preview
    output_path = Path(theme_dir) / 'previews' / f'{theme_name}_preview.png'
    final.save(output_path, 'PNG', quality=95)
    print(f"Generated preview: {output_path}")
    
    return output_path

if __name__ == "__main__":
    # Generate previews for both themes
    create_preview_with_background('warp', 'warp')
    create_preview_with_background('warp_darker', 'warp_darker')