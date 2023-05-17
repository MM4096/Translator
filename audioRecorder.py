import asyncio

import sounddevice as sd
from scipy.io.wavfile import write
from writeFiles import GetDataPath
from os import path, makedirs


def StopAudio():
    sd.stop()


async def RecordAudio(duration):
    fs = 44100
    seconds = 180
    recording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()
    if not path.exists(path.join(GetDataPath(), "recordings")):
        makedirs(path.join(GetDataPath(), "recordings"))
    savePath = path.join(GetDataPath(), "recordings", "output.wav")
    write(savePath, fs, recording)