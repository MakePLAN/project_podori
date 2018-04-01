from gtts import gTTS
import os

# tts = gTTS(text='Good morning', lang='en')
# tts.save("good.mp3")
# os.system("mpg321 good.mp3")

# tts = gTTS(text='Please step on the right pedal to move forward', lang='en')
# tts.save("move_forward.mp3")
# os.system("mpg321 move_forward.mp3")

# tts = gTTS(text='Warning: approaching speed limit', lang='en')
# tts.save("approach_limit.mp3")
# os.system("mpg321 approach_limit.mp3")

# tts = gTTS(text='Alert: you\'re over the speed limit', lang='en')
# tts.save("over_limit.mp3")
# os.system("mpg321 over_limit.mp3")

# tts = gTTS(text='Good job! You\'re doing great', lang='en')
# tts.save("good_job.mp3")
# os.system("mpg321 good_job.mp3")

# tts = gTTS(text='Step on the left pedal to brake!', lang='en')
# tts.save("brake_inst.mp3")
# os.system("mpg321 brake_inst.mp3")

# tts = gTTS(text='Heads up! A car is approaching from the left', lang='en')
# tts.save("car_on_left.mp3")
# os.system("mpg321 car_on_left.mp3")

# tts = gTTS(text='Heads up! A car is approaching from the right', lang='en')
# tts.save("car_on_right.mp3")
# os.system("mpg321 car_on_right.mp3")

# tts = gTTS(text='Turn left at by turning the steering at around 45 degrees to switch lanes', lang='en')
# tts.save("turn_left.mp3")
# os.system("mpg321 turn_left.mp3")

# tts = gTTS(text='Turn right at by turning the steering at around 45 degrees to switch lanes', lang='en')
# tts.save("turn_right.mp3")
# os.system("mpg321 turn_right.mp3")

# tts = gTTS(text='Try to stop the car completely by  pressing the left pedal', lang='en')
# tts.save("brake_inst.mp3")
# os.system("mpg321 over_limit.mp3")

# tts = gTTS(text='You\'re over the speed limit. You should brake by stepping on the left pedal!', lang='en')
# tts.save("brake_warning.mp3")

tts = gTTS(text='Pull up the left bar to signal lane changing to the left. Watch out for the car coming from left side.', lang='en')
tts.save("signal_left.mp3")

tts = gTTS(text='Pull up the right bar to signal lane changing to the right. Watch out for the car coming from right side.', lang='en')
tts.save("signal_right.mp3")