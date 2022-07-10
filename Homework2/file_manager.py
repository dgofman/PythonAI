import logging
import os

class FileManager:
    def __init__(self, filename, debugLevel = logging.DEBUG):
        self._filename = filename
        self._f = None
        logging.basicConfig(
            level = debugLevel,
            format='%(asctime)s.%(msecs)03d %(levelname)s: %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S',
        )

    def write(self, context: str):
        self.open("w")
        logging.debug("Write: %s", context)
        self._f.write(context)
        self.close()
    
    def read(self):
        context = None
        try:
            self.open("r")
            logging.debug("Read Context")
            context = self._f.read()
            self.close()
        except FileNotFoundError as e:
            print(f"\033[91m  Error: {e}\033[00m")
        return context

    def append(self, context: str):
        if self._f == None:
            self.open("a")
        self._f.write(context)

    def open(self, mode):
        logging.debug("Open file: %s", self._filename)
        self._f = open(self._filename, mode)

    def close(self):
        if self._f != None:
            logging.debug("Close file: %s", self._filename)
            self._f.close()
        self._f = None

    def delete(self):
        if os.path.exists(self._filename):
            logging.debug("Delete file: %s", self._filename)
            os.remove(self._filename)