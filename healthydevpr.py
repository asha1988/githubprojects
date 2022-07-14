from time import time
from pygame import mixer
from datetime import datetime

print("\nHealthy Developer")

def music_on_loop(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    mixer.music.set_volume(0.7)
    while True:
        input1=input()
        if input1==stopper:
            mixer.music.stop()
            break
        else:
            exit()
def log_now(msg):
        with open("logactivity.txt", "a") as f:
           f.write(f"{msg}{datetime.now()} \n")

if __name__ == '__main__':
      water_init=time()
      eyes_init=time()
      exec_init=time()
      watersecs=4
      eyessecs=6
      phyexesecs=10
      while(True):
         if time() - water_init > watersecs:
             print("It is water drinking time,Enter stop to end the music or press quit to end the process\n")
             music_on_loop("water.mp3","stop")
             water_init = time()
             log_now("Drank water at:")
         if time() - eyes_init > eyessecs:
             print("It is Eyes exercise time,Enter eyesdone to stop the music or press quit to end the process\n")
             music_on_loop("eyes.mp3","eyesdone")
             eyes_init = time()
             log_now("Eyes Exercise done at:")
         if time() - exec_init >  phyexesecs:
             print("It is physical exercise time,Enter phydone to stop the music or press quit to end the process\n")
             music_on_loop("phyexec.mp3","phydone")
             exec_init = time()
             log_now("Physical Exercise done at:")
