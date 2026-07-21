import threading
import time

class InferenceWorker:
    """
        Worker class which runs on its own thread. Currently doesnt do anything but sleep, but will be responsible for all calculations relating
        to pupil tracking
    """
    def __init__(self, stream):
        self.stream = stream            #Holds a reference to the VideoStream instance
        self.lock = threading.Lock()    #Mutex to prevent race conditions 
        self.result = None
        self.stopped = False
        #Thread
        self.thread = threading.Thread(target=self._run, daemon=True)
        self.thread.start()

    def _run(self):
        #Runs in the thread
        #Currently just takes a copy of a finished frame buffer and places in its result. Bit useless.
        #Again proof of concept
        while not self.stopped:
            frame = self.stream.read()   #Pulls from VideoStream
            if frame is None:
                continue
            result = self._infer(frame)
            with self.lock:
                self.result = result

    def _infer(self, frame):
        """
        TODO:CHANGE TO DO SOMETHING
        This is where logic code will go
        """
        time.sleep(1)
        return "dummy result"

    def get_result(self):
        #Returns the result frame
        with self.lock:
            return self.result

    def stop(self):
        self.stopped = True
        self.thread.join()