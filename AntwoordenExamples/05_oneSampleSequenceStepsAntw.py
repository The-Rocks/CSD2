import simpleaudio as sa
import time
import random

"""
An example project in which a sequence (one measure, one sample) is played.
  - One meassure, time signature: 3 / 4
  - 3 * 4 sixteenth notes per measure = 12 'steps'

------ HANDS-ON TIPS ------
- Run the code, read the code and answer the following question:
  This script does not use a list with time intervals, but does play a rhythm
  with one sample. Explain how.
  --> It has a list with the places where the samples must play. It checks
      every place periodicly if there has to play a sample. Line 39.

- Alter the code:
  Fix the bug that occurs: "IndexError: pop from empty list"
"""

#load 1 audioFile and store it into a list
#note: using a list taking the next step into account: using multiple samples
samples = [sa.WaveObject.from_wave_file("audioFiles/Pop.wav")]

#set bpm
bpm = 120
#calculate beatDuration with bpm
beatDuration = 60 / bpm
#number of beats per sequence (time signature: 3 / 4 = 3 beats per sequence)
beatsPerSequence = 3
#number of steps per beat (4 steps per beat -> using sixteenth notes)
stepsPerBeat = 4
#calculate stepDuration
stepDuration = beatDuration / stepsPerBeat
#calculate number of steps per sequence
stepsPerSequence = stepsPerBeat * beatsPerSequence

#create a list with a rhythm: the steps at which the sample will be played
sequence = [0, 2, 4, 8, 11]
#retrieve first event of sequence
#NOTE: pop(0) returns and removes the element at index 0
event = sequence.pop(0)
#play the sequence
while True:
    for step in range(int(stepsPerSequence)):
      print("Current step: ", step)
      if(step == event):
        samples[0].play()
        if step == 11:
            quit()
        #retrieve the next event
        event = sequence.pop(0)

      #wait!
      time.sleep(stepDuration)
