import speech_recognition as sr 
import moviepy.editor as mp
import uuid 
sourcrName = str(uuid.uuid1())
fullSource = sourcrName+".wav"
clip = mp.VideoFileClip(r"Alan.mp4") 
clip.audio.write_audiofile(fullSource)
r = sr.Recognizer()
audio = sr.AudioFile(sourcrName+".wav")
with audio as source:
	audio_file = r.record(source)
	result = r.recognize_google(audio_file)
# exporting the result 
with open(sourcrName+'.txt',mode ='w') as file: 
   file.write(result) 
   print("Extraction Complete")