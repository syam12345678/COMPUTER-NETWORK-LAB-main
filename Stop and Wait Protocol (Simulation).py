import time
import random
def stop_and_wait():
    frames = ["Frame1", "Frame2", "Frame3"]
    for i, frame in enumerate(frames):
        print(f"Sender: Sending {frame}")
        time.sleep(1)
        ack = random.choice([True, False])
        if ack:
            print(f"Receiver: Received {frame}")
            print(f"Sender: ACK received\n")
        else:
            print(f"Receiver: Lost {frame}")
            print("Sender: Timeout! Resending...\n")
            time.sleep(1)
            print(f"Sender: Sending {frame} again")
            print(f"Receiver: Received {frame}")
            print("Sender: ACK received\n")

stop_and_wait()
