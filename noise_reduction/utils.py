import wave

import pyaudio


def listen(filename, chunk=1024):
    """Play a wave file.

    Parameters
    ----------
    filename : str
        Path to wave file to play.
    chunk : int
        Number of frames to read at a time. Default is 1024.

    Returns
    -------
    None

    """
    with wave.open(filename, 'rb') as wf:
        p = pyaudio.PyAudio()
        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output=True)

        while len(data := wf.readframes(chunk)):
            stream.write(data)
        stream.close()
        p.terminate()

def record(filename, chunk=1024, rate=44100, seconds=5):
    """Record a wave file.

    Parameters
    ----------
    filename : str
        Path to wave file to play.
    chunk : int
        Number of frames to read at a time. Default is 1024.
    rate : int
        Sampling rate. Default is 44100.
    seconds : int
        Number of seconds to record. Default is 5.

    Returns
    -------
    None

    """
    with wave.open(filename, 'wb') as wf:
        p = pyaudio.PyAudio()
        wf.setnchannels(1)
        wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
        wf.setframerate(rate)
        
        stream = p.open(format=pyaudio.paInt16, channels=1, rate=rate, input=True)

        print('Recording...')
        for _ in range(0, rate // chunk * seconds):
            wf.writeframes(stream.read(chunk))
        print('Done')
        stream.close()
        p.terminate()