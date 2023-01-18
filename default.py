import cv2
from camera import Camera, CAMERA_SETTINGS


class Default(Camera):
    def __init__(self, address):
        super().__init__(self)
        self.address = address
        self.camera = cv2.VideoCapture(address, cv2.CAP_DSHOW)

    def camera_setting(self, target, value):
        """set camera"""
        if target is CAMERA_SETTINGS.GAIN:
            self.camera.set(cv2.CAP_PROP_GAIN, value)
        elif target is CAMERA_SETTINGS.GAMMA:
            self.camera.set(cv2.CAP_PROP_GAMMA, value)
        elif target is CAMERA_SETTINGS.WIDTH:
            self.camera.set(cv2.CAP_PROP_FRAME_WIDTH, value)
        elif target is CAMERA_SETTINGS.HEIGHT:
            self.camera.set(cv2.CAP_PROP_FRAME_HEIGHT, value)
        elif target is CAMERA_SETTINGS.BALANCE_WHITE_AUTO:
            self.camera.set(cv2.CAP_PROP_AUTO_WB, value)
        elif target is CAMERA_SETTINGS.EXPOSURE_AUTO:
            self.camera.set(cv2.CAP_PROP_AUTO_EXPOSURE, value)
        elif target is CAMERA_SETTINGS.EXPOSURE_TIME:
            self.camera.set(cv2.CAP_PROP_EXPOSURE, value)

    def get_serial_number(self):
        return self.address

    def open(self):
        """open camera"""
        pass

    def close(self):
        """close camera"""
        pass

    def is_open(self):
        """check if camera is open"""
        return self.camera.isOpend()

    def read(self):
        if self.camera.isOpend():
            ret, frame = self.camera.read()
        return frame

    def release(self):
        self.camera.release()