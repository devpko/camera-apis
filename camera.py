import enum
from abc import *


class CAMERA_SETTINGS(enum.Enum):
    GAIN = enum.auto()
    GAIN_AUTO = enum.auto()
    GAMMA = enum.auto()
    WIDTH = enum.auto()
    HEIGHT = enum.auto()
    OFFSET_X = enum.auto()
    OFFSET_Y = enum.auto()
    CENTER_X = enum.auto()
    CENTER_Y = enum.auto()
    BALANCE_WHITE_AUTO = enum.auto()
    BALANCE_RATIO_SELECTOR = enum.auto()
    BALANCE_RATIO = enum.auto()
    COLOR_ADJUSTMENT_SELECTOR = enum.auto()
    COLOR_ADJUSTMENT_HUE = enum.auto()
    COLOR_ADJUSTMENT_SATURATION = enum.auto()
    COLOR_TRANSFORMATION_VALUE = enum.auto()
    EXPOSURE_AUTO = enum.auto()
    EXPOSURE_TIME = enum.auto()
    ACQUISITION_FRAME_RATE_ENABLE = enum.auto()
    ACQUISITION_FRAME_RATE = enum.auto()
    DEVICE_LINK_THROUGHPUT_LIMIT = enum.auto()
    MAX_NUM_BUFFER = enum.auto()


class Camera(metaclass=ABCMeta):
    def __init__(self, cam) -> None:
        self.camera = cam

    @abstractmethod
    def camera_setting(self, target, value):
        pass

    @abstractmethod
    def get_serial_number(self):
        pass

    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def close(self):
        pass

    @abstractmethod
    def is_open(self):
        pass

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def release(self):
        pass
