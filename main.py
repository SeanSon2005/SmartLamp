from multiprocessing import Process, Queue, Event
from audio.ASR import ASR, VAD, Microphone, StartEndMonitor

if __name__ == "__main__":

    SAMPLE_RATE = 48000
    NUM_CHANNELS = 1
    SPEECH_THRESHOLD = 0.25

    audio_chunks = Queue()
    speech_segments = Queue()
    vad_ready = Event()
    asr_ready = Event()
    speech_start = Event()
    speech_end = Event()


    asr = ASR("base.en", "whisper_trt", speech_segments, ready_flag=asr_ready)

    vad = VAD(audio_chunks, speech_segments, max_filter_window=5, ready_flag=vad_ready, speech_start_flag=speech_start, speech_end_flag=speech_end, sample_rate=SAMPLE_RATE, speech_threshold=SPEECH_THRESHOLD)

    mic = Microphone(audio_chunks, num_channels=NUM_CHANNELS, sample_rate=SAMPLE_RATE)
    mon = StartEndMonitor(speech_start, speech_end)

    vad.start()
    asr.start()
    mon.start()

    vad_ready.wait()
    asr_ready.wait()

    mic.start()

    mic.join()
    vad.join()
    asr.join()
    mon.join()