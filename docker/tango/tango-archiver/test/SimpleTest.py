import tango
import time

def test_cm_device_is_ON():
    tango_test = tango.DeviceProxy("archiving/hdbpp/confmanager01")
    time.sleep(2)
    assert tango_test.state() == tango.DevState.ON

def test_es_device_is_ON():
    tango_test = tango.DeviceProxy("archiving/hdbpp/eventsubscriber01")
    time.sleep(2)
    assert tango_test.state() == tango.DevState.ON