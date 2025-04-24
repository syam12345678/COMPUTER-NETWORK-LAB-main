import time

class TokenBucket:
    def __init__(self, rate, capacity):
        self.rate = rate
        self.capacity = capacity
        self.tokens = capacity
        self.last_time = time.time()

    def allow_request(self, tokens_needed):
        current_time = time.time()
        elapsed = current_time - self.last_time
        self.tokens += elapsed * self.rate
        self.tokens = min(self.tokens, self.capacity)
        self.last_time = current_time

        if self.tokens >= tokens_needed:
            self.tokens -= tokens_needed
            return True
        else:
            return False

bucket = TokenBucket(rate=1, capacity=5)

for i in range(10):
    if bucket.allow_request(1):
        print(f"Request {i+1}: Allowed")
    else:
        print(f"Request {i+1}: Denied (Too fast)")
    time.sleep(0.5)
