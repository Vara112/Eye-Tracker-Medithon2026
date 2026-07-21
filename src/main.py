from thread_manager import ThreadManager
import cv2

def main():
    manager = ThreadManager(src=0)

    try:
        while True:
            frame = manager.get_frame()
            if frame is None:
                continue

            result = manager.get_result()

            cv2.imshow("frame", frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    finally:
        manager.stop_all()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()