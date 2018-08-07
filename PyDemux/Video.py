from PyDemux import _demux
from PIL import Image

class RawImage(object):
    width = 0
    height = 0
    channel = 3 # RGB format
    data = None # bytes
    pts = 0
    ms = 0

    def __init__(self, w, h, c, data, pts, ms):
        self.width = w
        self.height = h
        self.channel = c
        self.data = data
        self.pts = pts
        self.ms = ms


class Demux(object):
    def __init__(self, filename):
        self.ctx = _demux.open(filename)


    def get_frame(self):
        result = _demux.get_frame(self.ctx)
        if result is None:
            return None

        frame, w, h, pts, ms, = result
        return Image.frombytes("RGB", (w, h), frame)


    def get_raw_frame(self):
        result = _demux.get_frame(self.ctx)
        if result is None:
            return None
        frame, w, h, pts, ms, = result
        return RawImage(w, h, 3, frame, pts, ms)


    def seek(self, ms, stream_type=0, seek_type=0):
        return _demux.seek(self.ctx, ms, stream_type, seek_type);


    def __del__(self):
        if self.ctx is not None:
            _demux.close(self.ctx)


def open(filename):
    """
    Opens video file
    """
    return Demux(filename)
