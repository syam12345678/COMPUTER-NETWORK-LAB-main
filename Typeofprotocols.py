import random

def send_data(data_chunks):
    for i, chunk in enumerate(data_chunks):
        print(f"Sending chunk {i}: {chunk}")
        if random.random() < 0.8:
            print(f"ACK received for chunk {i}")
        else:
            print(f"Timeout! Resending chunk {i}")
            print(f"Resending chunk {i}: {chunk}")
            print(f"ACK received for chunk {i}")

data = ['Hello', 'from', 'a', 'TCP-like', 'protocol']
send_data(data)
