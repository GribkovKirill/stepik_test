class limited_hash:
    def __init__(self, left: int, right: int, hash_function=hash):
        self.left = left
        self.right = right
        self.hash_function = hash_function

    def __call__(self, obj):
        hashed_obj: int = self.hash_function(obj)

        while hashed_obj not in range(self.left, self.right + 1):
            if hashed_obj > self.right:
                hashed_obj = self.left + (hashed_obj - self.right - 1)
            elif hashed_obj < self.left:
                hashed_obj = self.right - (self.left - hashed_obj - 1)
        return hashed_obj
