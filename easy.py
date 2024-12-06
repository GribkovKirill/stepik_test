class WriteSpy:
    def __init__(self, file1, file2, to_close=False):
        self.file1 = file1
        self.file2 = file2
        self.to_close = to_close

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.to_close:
            self.close()
        return True

    def write(self, text: str):
        print(self.closed())
        if (
            self.writable() and
            not self.file1.closed
            and not self.file2.closed
        ):
            self.file1.write(text)
            self.file2.write(text)
        else:
            raise ValueError('Файл закрыт или недоступен для записи')

    def close(self):
        self.file1.close()
        self.file2.close()

    def writable(self) -> bool:
        return self.file1.writable() and self.file2.writable()

    def closed(self) -> bool:
        return self.file1.closed and self.file2.closed
