from gtts import gTTS
import os

tts = gTTS(text='Car behind you is approaching', lang='en')
tts.save("test.mp3")
os.system("mpg321 good.mp3")