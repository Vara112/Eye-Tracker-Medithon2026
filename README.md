# Eye-Tracker-Medithon2026


## Overview
Low-cost eye-tracking glasses using a basic camera to detect pupil movement, letting users control a computer hands-free. Built for Medithon 2026 to make assistive tech more accessible for people with limited mobility.

## How it works
The app runs the camera and the (future) eye-tracking inference on separate threads so frame capture isn't blocked while a frame is being processed:

- **`video_stream.py`** — `VideoStream` object continuously reads frames from the camera on a background thread and exposes the latest frame via a lock-protected (mutex) `read()`.
- **`inference_worker.py`** — `InferenceWorker` pulls frames from `VideoStream` on its own thread and runs inference on them (currently just sleeps for test, but later logic will be in `_infer`).
- **`thread_manager.py`** — `ThreadManager` wires the stream and worker together and exposes a simple `get_frame()` / `get_result()` / `stop_all()` interface which is accessed via the main function.
- **`main.py`** — entry point; opens a window showing the live feed and prints/uses inference results. Press `q` to quit <-- This doesnt work atm.
- **`record.py`** — standalone script for recording/previewing a grayscale camera feed (used for collecting sample footage, see `data/`).

# Multi-Threading Structure

main.py:
    Calls ThreadManager object



---

## DRAFT (below this line — feel free to edit/cut before committing)

## Overview
Low-cost eye-tracking glasses that use a basic camera to detect pupil movement, letting users control a computer hands-free. Built for Medithon 2026 to make assistive tech more accessible for people with limited mobility.

## Status
Early prototype. Video capture and a threaded pipeline are working; pupil-tracking inference is not yet implemented (`InferenceWorker._infer` currently returns a placeholder value).

## How it works
The app runs the camera and the (future) eye-tracking inference on separate threads so frame capture isn't blocked while a frame is being processed:

- **`video_stream.py`** — `VideoStream` continuously reads frames from the camera on a background thread and exposes the latest frame via a lock-protected `read()`.
- **`inference_worker.py`** — `InferenceWorker` pulls frames from `VideoStream` on its own thread and runs inference on them (currently a stub — pupil-tracking logic goes in `_infer`).
- **`thread_manager.py`** — `ThreadManager` wires the stream and worker together and exposes a simple `get_frame()` / `get_result()` / `stop_all()` interface.
- **`main.py`** — entry point; opens a window showing the live feed and prints/uses inference results. Press `q` to quit.
- **`record.py`** — standalone script for recording/previewing a grayscale camera feed (used for collecting sample footage, see `data/`).

## Requirements
- Python 3.x
- OpenCV (`opencv-python`)

## Team / Acknowledgements
Built for Medithon 2026.

