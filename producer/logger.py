
import os
import sys

class FileLogger:
    def __init__(self, file_path, write_buffer):
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        self.file = open(file_path, 'a')
        self.write_buffer = write_buffer

    def write(self, message):
        self.file.write(message)
        self.file.flush()
        self.write_buffer.write(message)
        self.write_buffer.flush()

    def flush(self):
        self.file.flush()
        self.write_buffer.flush()

    def isatty(self):
        return False

class StdFileLogger(FileLogger):
    def __init__(self, module_name):
        super().__init__("./logs/" + module_name + ".log", sys.__stdout__)