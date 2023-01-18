import sys
import time
import threading
from pypylon import pylon
from camera import Camera, CAMERA_SETTINGS
from logger import Logger


class Basler(Camera):
    def __init__(self, serial=None):
        super().__init__(self)
        try:
            if serial is not None:
                info = pylon.DeviceInfo()
                info.SetSerialNumber(serial)
                cam = pylon.TlFactory.GetInstance().CreateFirstDevice(info)
            else:
                cam = pylon.TlFactory.GetInstance().CreateFirstDevice()
            self.camera = pylon.IntanceCamera(cam)
            self.converter = pylon.ImageFormatConverter()
            self.converter.OutputBitAlignment = pylon.OutputBitAlignment_MsbAligned

            self.frame = None
            self.grab_thread = None
        except Exception as e:
            Logger.get_logger().error(f'Please check if basler camera is connected\n{e}')
            sys.exit()

    def camera_setting(self, target, value):
        """set camera"""
        if not self.is_open():
            self.camera.Open()

        if target is CAMERA_SETTINGS.GAIN:
            self.camera.Gain.SetValue(value)
        elif target is CAMERA_SETTINGS.GAIN_AUTO:
            self.camera.GainAuto.SetValue(value)
        elif target is CAMERA_SETTINGS.GAMMA:
            self.camera.Gamma.SetValue(value)
        elif target is CAMERA_SETTINGS.WIDTH:
            self.camera.Width.SetValue(value)
        elif target is CAMERA_SETTINGS.HEIGHT:
            self.camera.Height.SetValue(value)
        elif target is CAMERA_SETTINGS.OFFSET_X:
            self.camera.OffsetX.SetValue(value)
        elif target is CAMERA_SETTINGS.OFFSET_Y:
            self.camera.OffsetY.SetValue(value)
        elif target is CAMERA_SETTINGS.CENTER_X:
            self.camera.CenterX.SetValue(value)
        elif target is CAMERA_SETTINGS.CENTER_Y:
            self.camera.CenterY.SetValue(value)
        elif target is CAMERA_SETTINGS.BALANCE_WHITE_AUTO:
            self.camera.BalanceWhiteAuto.SetValue(value)
        elif target is CAMERA_SETTINGS.BALANCE_RATIO_SELECTOR:
            self.camera.BalanceRatioSelector.SetValue(value)
        elif target is CAMERA_SETTINGS.BALANCE_RATIO:
            self.camera.BalanceRatio.SetValue(value)
        elif target is CAMERA_SETTINGS.COLOR_ADJUSTMENT_SELECTOR:
            self.camera.ColorAdjustmentSelector.SetValue(value)
        elif target is CAMERA_SETTINGS.COLOR_ADJUSTMENT_HUE:
            self.camera.ColorAdjustmentHue.SetValue(value)
        elif target is CAMERA_SETTINGS.COLOR_ADJUSTMENT_SATURATION:
            self.camera.ColorAdjustmentSaturation.SetValue(value)
        elif target is CAMERA_SETTINGS.COLOR_TRANSFORMATION_VALUE:
            self.camera.ColorTransformationValue.SetValue(value)
        elif target is CAMERA_SETTINGS.EXPOSURE_AUTO:
            self.camera.ExposureAuto.SetValue(value)
        elif target is CAMERA_SETTINGS.EXPOSURE_TIME:
            self.camera.ExposureTime.SetValue(value)
        elif target is CAMERA_SETTINGS.ACQUISITION_FRAME_RATE_ENABLE:
            self.camera.AcquisitionFrameRateEnable.SetValue(value)
        elif target is CAMERA_SETTINGS.ACQUISITION_FRAME_RATE:
            self.camera.AcquisitionFrameRate.SetValue(value)
        elif target is CAMERA_SETTINGS.MAX_NUM_BUFFER:
            self.camera.MaxNumBuffer = value
        elif target is CAMERA_SETTINGS.DEVICE_LINK_THROUGHPUT_LIMIT:
            self.camera.DeviceLinkThroughputLimit = value

    def get_serial_number(self):
        return self.camera.GetDeviceInfo().GetSerialNumber()

    def open(self):
        """open camera"""
        try:
            if not self.is_open():
                self.camera.Open()
            self.grab_thread = threading.Thread(target=self.__grab, daemon=True)
            self.camera.StartGrabbing(pylon.GrabStrategy_LatestImageOnly)
            time.sleep(1)
            self.grab_thread.start()
        except Exception as e:
            Logger.get_logger().error(f'Cannot open basler camera. \n{e}')
            sys.exit()

    def __grab(self):
        while self.camera.IsGrabbing():
            grab_result = self.camera.RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)
            if self.camera.IsGrabbing() and grab_result.GrabSucceeded():
                image = self.converter.Convert(grab_result)
                self.frame = image.GetArray()
            grab_result.Release()

    def close(self):
        """stop getting frame"""
        try:
            if self.camera.IsGrabbing():
                self.camera.StopGrabbing()
                self.grab_thread.join()
                self.grab_thread = None
            self.camera.Close()
        except Exception as e:
            Logger.get_logger().error(f'Cannot close basler camera. \n{e}')

    def is_open(self):
        """check if basler camera is open"""
        return self.camera.IsOpen()

    def read(self):
        """read frame"""
        return self.frame

    def release(self):
        """release camera"""
        self.close()
        self.camera.DestroyDevice()
