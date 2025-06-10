import board
import busio
import adafruit_ssd1306
from PIL import Image, ImageDraw, ImageFont

# Initialize I2C
i2c = busio.I2C(board.SCL, board.SDA)
oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3C)

# Clear display
oled.fill(0)
oled.show()

# Draw text
image = Image.new("1", (128, 64))
draw = ImageDraw.Draw(image)
draw.text((10, 30), "Hello, Pi Zero!", fill=255)

# Display
oled.image(image)
oled.show()