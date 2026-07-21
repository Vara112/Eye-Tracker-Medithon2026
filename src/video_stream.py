import cv2
import threading
import time
import math

class VideoStream:

    def __init__(self, src=0):
        """
        Initalises the video stream object. The Frame buffer is stored in self.frame, and is updated on a dedicated thread for video
        streaming. A mutex is also introduce to prevent conflicting access to this buffer

        Args:
            src (int, optional): Defaults to 0. defines which camera to use

        Raises:
            IOError: If camera cannot be index/issue connecting
        """
        self.cap = cv2.VideoCapture(src)
        if not self.cap.isOpened():
            raise IOError("Camera not working")
        
        self.lock = threading.Lock()
        self.frame = None
        self.stopped = False
        self.fps = 0

        frameSuccess, frame = self.cap.read()
        if frameSuccess:
            self.frame = frame

        self.thread = threading.Thread(target=self._update, daemon=True)
        #Creating a thread that the _update method will run on
        self.thread.start()


    def _update(self):
        
        while not self.stopped:
            startTime = time.perf_counter_ns()
            frameSuccess, frame = self.cap.read()
            if not frameSuccess:
                continue
            with self.lock: #Try to acquire the lock. If it cannot it will wait for the lock to be released
                self.frame = frame
            
            self.fps = math.floor(1_000_000_000 / (time.perf_counter_ns() - startTime))
            print("The FPS is: %d", self.fps)
            
    
    def read(self):

        with self.lock:
            return None if self.frame is None else self.frame.copy()    #Copys the frame when released (not being written to)
        

    def stop(self):
        self.stopped = True
        self.thread.join()  #Waits till update thread finishes before moving on (synchronization)
        self.cap.release()
        

    

def main():
    stream = VideoStream(src=0)

    try:
        while True:
            frame = stream.read()
            if frame is None:
                continue
            result = parallel_test()

            cv2.imshow("frame", frame)

            print("New Frame")

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    finally:
        stream.stop()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()





