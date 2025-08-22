#!/bin/bash

echo "Converting transparent SVGs to PNGs with rsvg-convert..."

# Convert transparent SVGs to PNGs with proper text rendering
rsvg-convert -w 600 -h 290 --background-color=transparent \
  warp/previews/warp_transparent.svg \
  -o warp/previews/warp_text_rsvg.png

rsvg-convert -w 600 -h 290 --background-color=transparent \
  warp_darker/previews/warp_darker_transparent.svg \
  -o warp_darker/previews/warp_darker_text_rsvg.png

echo "Creating backgrounds with 60% opacity..."

# Create background layers: solid color + 60% image
magick -size 600x290 xc:'#061229' \
  \( warp/warp.jpg -resize 600x290^ -gravity center -extent 600x290 \) \
  -compose over -define compose:args=60 -composite \
  warp/previews/warp_bg.png

magick -size 600x290 xc:'#061229' \
  \( warp_darker/warp_darker.jpg -resize 600x290^ -gravity center -extent 600x290 \) \
  -compose over -define compose:args=60 -composite \
  warp_darker/previews/warp_darker_bg.png

echo "Compositing text over backgrounds..."

# Composite the clean text over the backgrounds
magick warp/previews/warp_bg.png \
  warp/previews/warp_text_rsvg.png \
  -composite \
  warp/previews/warp_with_bg.png

magick warp_darker/previews/warp_darker_bg.png \
  warp_darker/previews/warp_darker_text_rsvg.png \
  -composite \
  warp_darker/previews/warp_darker_with_bg.png

echo "Complete!"
echo "Generated: warp/previews/warp_with_bg.png"
echo "Generated: warp_darker/previews/warp_darker_with_bg.png"