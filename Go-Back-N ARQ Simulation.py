import random  # Add this at the top

def go_back_n(frames, window_size):
    i = 0
    while i < len(frames):
        print(f"Sender: Sending frames {frames[i:i+window_size]}")
        success = all(random.choice([True, True, False]) for _ in range(window_size))

        if success:
            print(f"Receiver: All frames received successfully\n")
            i += window_size
        else:
            print("Receiver: Error in receiving! Resending current window...\n")
            # i remains the same (Go-Back-N logic)

# Example usage
frames = ["F1", "F2", "F3", "F4", "F5"]
go_back_n(frames, 3)
