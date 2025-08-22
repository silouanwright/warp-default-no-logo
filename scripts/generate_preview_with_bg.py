#!/usr/bin/env python3
import os
import subprocess
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter
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
    
    # Try to use a monospace font
    try:
        # Try different font options
        font_size = 14
        font = ImageFont.truetype('/System/Library/Fonts/Monaco.dfont', font_size)
    except:
        try:
            font = ImageFont.truetype('/System/Library/Fonts/Menlo.ttc', 14)
        except:
            font = ImageFont.load_default()
    
    # Draw terminal content
    y_pos = 20
    line_height = 20
    
    # Line 1: ls command
    draw.text((20, y_pos), 'ls', fill=colors['foreground'], font=font)
    y_pos += line_height
    
    # Line 2: dir, executable, file
    draw.text((20, y_pos), 'dir', fill=colors['blue'], font=font)
    draw.text((80, y_pos), 'executable', fill=colors['red'], font=font)
    draw.text((200, y_pos), 'file', fill=colors['foreground'], font=font)
    y_pos += line_height + 5
    
    # Separator line
    draw.line([(0, y_pos), (width, y_pos)], fill=colors['foreground'], width=1)
    y_pos += 10
    
    # Colors display
    draw.text((20, y_pos), 'bash ~/colors.sh', fill=colors['foreground'], font=font)
    y_pos += line_height
    
    # Normal colors
    draw.text((20, y_pos), 'normal:', fill=colors['foreground'], font=font)
    x = 80
    for color in ['black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']:
        draw.text((x, y_pos), color[:3], fill=colors[color], font=font)
        x += 40
    y_pos += line_height
    
    # Bright colors
    draw.text((20, y_pos), 'bright:', fill=colors['foreground'], font=font)
    x = 80
    for color in ['black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']:
        draw.text((x, y_pos), color[:3], fill=colors[f'br{color}'], font=font)
        x += 40
    y_pos += line_height + 5
    
    # Separator line
    draw.line([(0, y_pos), (width, y_pos)], fill=colors['foreground'], width=1)
    y_pos += 10
    
    # Prompt
    draw.text((20, y_pos), '~/project', fill=colors['magenta'], font=font)
    draw.text((100, y_pos), 'git(', fill=colors['green'], font=font)
    draw.text((130, y_pos), 'main', fill=colors['yellow'], font=font)
    draw.text((170, y_pos), ')', fill=colors['green'], font=font)
    
    # Cursor
    draw.rectangle([(20, y_pos + 20), (22, y_pos + 35)], fill=colors['accent'])
    
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
        
        # Apply opacity (60% as specified in theme)
        # Create a solid color background
        solid_bg = Image.new('RGBA', (600, 290), colors['background'])
        
        # Convert background to RGBA and apply opacity
        bg = bg.convert('RGBA')
        bg_with_opacity = Image.blend(solid_bg, bg, 0.6)
        
        # Composite text over background
        final = Image.alpha_composite(bg_with_opacity.convert('RGBA'), text_img)
    else:
        # Just use solid background if no image
        final = Image.new('RGBA', (600, 290), colors['background'])
        final = Image.alpha_composite(final, text_img)
    
    # Save final preview
    output_path = Path(theme_dir) / 'previews' / f'{theme_name}_preview.png'
    final.save(output_path)
    print(f"Generated preview: {output_path}")
    
    return output_path

if __name__ == "__main__":
    # Generate previews for both themes
    create_preview_with_background('warp', 'warp')
    create_preview_with_background('warp_darker', 'warp_darker')