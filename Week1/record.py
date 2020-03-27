import sounddevice as sd
import soundfile as sf
import time 


def sync_record(filename, duration, fs, channels):
    print('recording')
    myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=channels)
    sd.wait()
    sf.write(filename, myrecording, fs)
    print('done recording')
    
def record(data):
    f = wave.open('/.wav', 'wb')
    f.setframerate(8000)
    f.setsampwidth(2)
    f.setnchannels(1)
    f.writeframes(data)
    f.close()
    #return r.recognize_google(audio, language='vi-VN')



# change text as necessary
# e.g. 'the weather is currently 90 degrees outside.'
#text=input('type text to speak here: \n')
# speak output text 
#spoken_time=speak_text(text)

# playback file 
#sync_record(fileNameRecord, 10, 16000, 1)

f = open('Data/thegioi.txt','r', encoding='utf8')
sentences = f.readlines()

for sentence in sentences:
    print(sentence)
    fileNameRecord = 'fileWav/thegioi/' + str(sentences.index(sentence)) + '.wav'
    sync_record(fileNameRecord, 10, 16000, 1)





