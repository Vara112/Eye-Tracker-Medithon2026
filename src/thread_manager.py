import cv2
import threading
import time
from video_stream import VideoStream
from inference_worker import InferenceWorker

class ThreadManager:
    """
        Connects Worker and Video Stream threads together simplifying the interface. 
        TODO finish

    """
    def __init__(self, src=0):
        '''
            src: index to select which camera to use on system (defaults to 0)

            Initalises the VideoStream and InferenceWorker objects (which run on their own threads)
        '''
        self.stream = VideoStream(src=src)
        self.worker = InferenceWorker(self.stream)

    def get_frame(self):
        '''
            Grabs and returns a copy of the current finished frame buffer from video stream
        '''
        return self.stream.read()

    def get_result(self):
        '''
            Grabs and returns some result computed by the worker (Very temp, more proof of concept then useful)
        '''
        return self.worker.get_result()

    def stop_all(self):
        #Kills the threads
        #We stop the consumer first (worker) then the producer (video stream) 
        self.worker.stop()
        self.stream.stop()