from PIL import Image, ImageDraw
import cv2
import numpy as np
import random
import math

#=================================
# SETTINGS
#=================================

WIDTH = 1000
HEIGHT = 700

FPS = 30
TOTAL_FRAMES = 1000

#==================================
# VIDEO WRIITER
#==================================

fourcc = cv2.VideoWriter_fourcc(*"mp4v")

video = cv2.VideoWriter("campfire_scene.mp4", fourcc, FPS, (WIDTH, HEIGHT))

#===================================
# STARS
#===================================

stars = []

for i in range(250):
    stars.append((random.randint(0, WIDTH), random.randint(0, HEIGHT//2)))

#====================================
# FIREFLIES
#====================================
fireflies = []

for i in range(20):
    fireflies.append(
        [random.randint(100, WIDTH-100), random.randint(300, HEIGHT - 150)]
    )

for frame in range(TOTAL_FRAMES):
    img = Image.new("RGB", (WIDTH, HEIGHT), (10, 10, 35))
    draw = Image.ddraw.Draw(img)

#=====================================
# STARS
#=====================================

for x, y in stars:
    brightness = random.randint(150, 255)
    draw.ellipse(
        (x-1, y-1, x+1, y+1), fill=(brightness, brightness, brightness)
    )

#======================================
# MOON
#======================================

draw.ellipse((750, 60, 830, 140), fill=(240, 240, 220))

#======================================
# CLOUDS
#======================================
coud_x = WIDTH - (frame*2)%(WIDTH + 300)
for offset in [0, 80, 160]:
    cx = coud_x + offset
    draw.ellipse((cx, 100, cx+80, 150), fill=(90, 90, 110))
    draw.ellipse((cx+40, 80, cx+120, 150), fill=(90, 90, 110))
    draw.ellipse((cx+80, 100, cx+160, 150), fill=(90, 90, 110))

#=======================================
# GROUND
#=======================================

draw.rectangle((0, 500, WIDTH, HEIGHT), fill=(20, 80, 20))

#=======================================
# TREES
#=======================================

tree_positions = [120, 220, 850, 930]

for tx in tree_positions:
    draw.rectangle((tx, 380, tx+20, 500), fill=(90, 50, 20))
    draw.polygon([(tx-40, 420), (tx+10, 300), (tx+60, 420)], fill=(0, 120, 0))
    draw.polygon([(tx-35, 370), (tx+10, 250), (tx+55, 370)], fill=(0, 140, 0))

#========================================
# HUT
#========================================

draw.rectangle((350, 320, 550, 500), fill=(139, 69, 19))
draw.polygon([(320, 320), (450, 220), (580, 320)], fill=(100, 40, 10))
draw.rectangle((430, 410, 480, 500), fill=(60, 30, 10))
draw.rectangle((380, 360, 420, 400), fill=(255, 255, 120))
draw.rectangle((500, 360, 540, 400), fill=(255, 255, 120))

#=========================================
# FENCE
#=========================================

for  x in range(20, WIDTH, 35):
    draw.rectangle((x, 460, x+10, 500), fill=(170, 120, 70))
draw.rectangle((0, 470, WIDTH, 475), fill=(170, 120, 70))
draw.rectangle((0, 490, WIDTH, 495), fill=(170, 120, 70))

#==========================================
# CAMPFIRE
#==========================================

fire_x = 700
fire_y = 480

#==========================================
# LOGS
#==========================================
draw.line(
    (fire_x-20, fire_y+10, fire_x+20, fire_y - 10),
    fill=(120, 70, 30),
    width=6,
)

flame_height = random.randint(40, 70)

draw.polygon([(fire_x, fire_y - flame_height), (fire_x - 20, fire_y), (fire_x+20, fire_y)], fill=(255, 120, 0))

draw.polyon(
    [
        (fire_x, fire_y - flame_height +15),
        (fire_x - 12, fire_y),
        (fire_x + 12, fire_y),
    ],
    fill=(255, 255, 0),
)