# "You Are My Sunshine" in Colors

# Week 2 HW
# Amy Kang
# 09/10/2022

#Resource:
    #Resources:
    # Code - https://learn.adafruit.com/adafruit-feather-m4-express-atsamd51/creating-and-editing-code
    # “You Are My Sunshine” Music Notes - https://musescore.com/user/13881501/scores/3028766
    # Synesthesia - https://en.wikipedia.org/wiki/Synesthesia
    # Chromesthesia - https://en.wikipedia.org/wiki/Chromesthesia#:~:text=Chromesthesia%20or%20sound%2Dto%2Dcolor,associations%2Fperceptions%20in%20daily%20life.
    # Scriabin Circle - https://en.wikipedia.org/wiki/Clavier_%C3%A0_lumi%C3%A8res

# Color and Music Note Coordination:
# C - Red (255, 0, 0)
# D - Yellow (255, 255, 0)
# E - Sky Blue (195, 242, 255)
# F - Deep Red (171, 0, 52)
# G - Orange (255, 127, 0)
# A - Green (51, 204, 51)
# B - Blue (142, 201, 255)

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


led.brightness = 0.0 #break
time.sleep(2.0)
led.brightness = 0.3

print("You Are My Sunshine")
led[0] = (255, 0, 0) # You (C)
time.sleep(0.5)
led.brightness = 0.0 #same note break
time.sleep(0.02)
led.brightness = 0.3
led[0] = (255, 0, 0) # are (C)
time.sleep(0.5)
led[0] = (255, 255, 0) # my (D)
time.sleep(0.5)

led[0] = (195, 242, 255) # sun (E)
time.sleep(1.0)
led.brightness = 0.0 #same note break
time.sleep(0.02)
led.brightness = 0.3
led[0] = (195, 242, 255) # shine (E)
time.sleep(1.0)

print("My only sunshine.")

led.brightness = 0.0 #break
time.sleep(0.5)
led.brightness = 0.3
led[0] = (195, 242, 255) # my (E)
time.sleep(0.5)
led[0] = (255, 255, 0) # on- (D)
time.sleep(0.5)
led[0] = (195, 242, 255) # ly (E)
time.sleep(0.5)

led[0] = (255, 0, 0) # sun (C)
time.sleep(1.0)
led.brightness = 0.0 #same note break
time.sleep(0.02)
led.brightness = 0.3
led[0] = (255, 0, 0) # shine (C)
time.sleep(1.0)

print("You make me happy,")

led.brightness = 0.0 #break
time.sleep(0.5)
led.brightness = 0.3
led[0] = (255, 0, 0) # you (C)
time.sleep(0.5)
led[0] = (255, 255, 0) # make (D)
time.sleep(0.5)
led[0] = (195, 242, 255) # me (E)
time.sleep(0.5)

led[0] = (171, 0, 52) # hap- (F)
time.sleep(1.0)
led[0] = (51, 204, 51) # py (A)
time.sleep(1.0)

print("when skies are gray")
led.brightness = 0.0 #break
time.sleep(0.5)
led.brightness = 0.3
led[0] = (51, 204, 51) # when (A)
time.sleep(0.5)
led[0] = (255, 127, 0) # skies (G)
time.sleep(0.5)
led[0] = (171, 0, 52) # are (F)
time.sleep(0.5)

led[0] = (195, 242, 255) # gray (E)
time.sleep(2.0)

print("You'll never know dear")
led.brightness = 0.0 #break
time.sleep(0.5)
led.brightness = 0.3
led[0] = (255, 0, 0) # you'll (C)
time.sleep(0.5)
led[0] = (255, 255, 0) # ne- (D)
time.sleep(0.5)
led[0] = (195, 242, 255) # ver (E)
time.sleep(0.5)

led[0] = (171, 0, 52) # know (F)
time.sleep(1.0)
led[0] = (51, 204, 51) # dear (A)
time.sleep(1.0)

print("how much I love you")
led.brightness = 0.0 #break
time.sleep(0.5)
led.brightness = 0.3
led[0] = (51, 204, 51) # how (A)
time.sleep(0.5)
led[0] = (255, 127, 0) # much (G)
time.sleep(0.5)
led[0] = (171, 0, 52) # I (F)
time.sleep(0.5)

led[0] = (195, 242, 255) # love (E)
time.sleep(1.0)
led[0] = (255, 0, 0) # you (C)
time.sleep(1.0)

print("Please don't take my sunshine away")
led.brightness = 0.0 #2 breaks
time.sleep(1.0)
led.brightness = 0.3
led[0] = (255, 0, 0) # please (C)
time.sleep(0.5)
led[0] = (255, 255, 0) # don't (D)
time.sleep(0.5)

led[0] = (195, 242, 255) # take (E)
time.sleep(1.5)
led[0] = (171, 0, 52) # my (F)
time.sleep(0.5)

led[0] = (255, 255, 0) # sun (D)
time.sleep(1.0)
led.brightness = 0.0 #same note break
time.sleep(0.02)
led.brightness = 0.3
led[0] = (255, 255, 0) # shine (D)
time.sleep(0.5)
led[0] = (195, 242, 255) # a- (E)
time.sleep(0.5)

led[0] = (255, 0, 0) # way... (C)
time.sleep(1.0)
led.brightness = 0.1 # fade out = lower brightness
time.sleep(1.0)

print("Music End")
