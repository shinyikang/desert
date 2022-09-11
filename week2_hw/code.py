# "You Are My Sunshine" in Colors

# Week 2 HW
# Amy Kang
# 09/10/2022

#Resource:
    # Code - https://learn.adafruit.com/adafruit-feather-m4-express-atsamd51/creating-and-editing-code
    # “You Are My Sunshine” Music Notes - https://musescore.com/user/13881501/scores/3028766
    # Synesthesia - https://en.wikipedia.org/wiki/Synesthesia
    # Chromesthesia - https://en.wikipedia.org/wiki/Chromesthesia#:~:text=Chromesthesia%20or%20sound%2Dto%2Dcolor,associations%2Fperceptions%20in%20daily%20life.
    # Scriabin Circle - https://en.wikipedia.org/wiki/Clavier_%C3%A0_lumi%C3%A8res

# Create Variables Connecting Color and Music Note Coordination:
# C - Red (255, 0, 0)
c = (255, 0, 0)
# D - Yellow (255, 255, 0)
d = (255, 255, 0)
# E - Sky Blue (195, 242, 255)
e = (195, 242, 255)
# F - Deep Red (171, 0, 52)
f = (171, 0, 52)
# G - Orange (255, 127, 0)
g = (255, 127, 0)
# A - Green (51, 204, 51)
a = (51, 204, 51)
# B - Blue (142, 201, 255)
b = (142, 201, 255)

import time
import board

if hasattr(board, "APA102_SCK"):
    import adafruit_dotstar
    led = adafruit_dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1)
else:
    import neopixel
    led = neopixel.NeoPixel(board.NEOPIXEL, 1)

# Animation Features

    # 0.5 seconds = 1 beat
    # Quarter note receives one beat
    # 4 beats per measure

    # Lyrics are printed as the music goes on
    # Color fades out at the end of the song

print("Music Start!")

#break before beginning of the song
led.brightness = 0.0 #break
time.sleep(2.0)
led.brightness = 0.3

#print lyrics alongside the song
print("You Are My Sunshine")
led[0] = c # You (C)
time.sleep(0.5)
led.brightness = 0.0 #same note break
time.sleep(0.02)
led.brightness = 0.3
led[0] = c # are (C)
time.sleep(0.5)
led[0] = d # my (D)
time.sleep(0.5)

led[0] = e # sun (E)
time.sleep(1.0)
led.brightness = 0.0 #same note break
time.sleep(0.02)
led.brightness = 0.3
led[0] = e # shine (E)
time.sleep(1.0)

print("My only sunshine.")

led.brightness = 0.0 #break
time.sleep(0.5)
led.brightness = 0.3
led[0] = e # my (E)
time.sleep(0.5)
led[0] = d # on- (D)
time.sleep(0.5)
led[0] = e # ly (E)
time.sleep(0.5)

led[0] = c # sun (C)
time.sleep(1.0)
led.brightness = 0.0 #same note break
time.sleep(0.02)
led.brightness = 0.3
led[0] = c # shine (C)
time.sleep(1.0)

print("You make me happy,")

led.brightness = 0.0 #break
time.sleep(0.5)
led.brightness = 0.3
led[0] = c # you (C)
time.sleep(0.5)
led[0] = d # make (D)
time.sleep(0.5)
led[0] = e # me (E)
time.sleep(0.5)

led[0] = f # hap- (F)
time.sleep(1.0)
led[0] = a # py (A)
time.sleep(1.0)

print("when skies are gray")
led.brightness = 0.0 #break
time.sleep(0.5)
led.brightness = 0.3
led[0] = a # when (A)
time.sleep(0.5)
led[0] = g # skies (G)
time.sleep(0.5)
led[0] = f # are (F)
time.sleep(0.5)

led[0] = e # gray (E)
time.sleep(2.0)

print("You'll never know dear")
led.brightness = 0.0 #break
time.sleep(0.5)
led.brightness = 0.3
led[0] = c # you'll (C)
time.sleep(0.5)
led[0] = d # ne- (D)
time.sleep(0.5)
led[0] = e # ver (E)
time.sleep(0.5)

led[0] = f # know (F)
time.sleep(1.0)
led[0] = a # dear (A)
time.sleep(1.0)

print("how much I love you")
led.brightness = 0.0 #break
time.sleep(0.5)
led.brightness = 0.3
led[0] = a # how (A)
time.sleep(0.5)
led[0] = g # much (G)
time.sleep(0.5)
led[0] = f # I (F)
time.sleep(0.5)

led[0] = e # love (E)
time.sleep(1.0)
led[0] = c # you (C)
time.sleep(1.0)

print("Please don't take my sunshine away")
led.brightness = 0.0 #2 breaks
time.sleep(1.0)
led.brightness = 0.3
led[0] = c # please (C)
time.sleep(0.5)
led[0] = d # don't (D)
time.sleep(0.5)

led[0] = e # take (E)
time.sleep(1.5)
led[0] = f # my (F)
time.sleep(0.5)

led[0] = d # sun (D)
time.sleep(1.0)
led.brightness = 0.0 #same note break
time.sleep(0.02)
led.brightness = 0.3
led[0] = d # shine (D)
time.sleep(0.5)
led[0] = e # a- (E)
time.sleep(0.5)

led[0] = c # way... (C)
time.sleep(1.0)
led.brightness = 0.1 # fade out = lower brightness
time.sleep(1.0)

print("Music End")
