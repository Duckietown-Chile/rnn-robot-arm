# -*- coding: utf-8 -*

import serial, time
import struct
from array import array
from io import BytesIO

class RobotCmd(object):

    _struct = struct.Struct('<hhh')

    def __init__(self):
        self.t1 = 0
        self.t2 = 0
        self.t3 = 0

    def serialize(self, buff):
        #try
        buff.write(RobotCmd._struct.pack(self.t1, self.t2, self.t3))
        #except struct.error as se:
        #    raise SerializationError('Error in serialization %s' % (self.__str__))


def to_hex(data):
    return ":".join("{:02x}".format(c) for c in data)


if __name__ == '__main__':

    arduino = serial.Serial('COM6', 9600)
    cmd = RobotCmd()
    buff = BytesIO()
    cmd.t1 = int(input("th1: "))
    cmd.t2 = int(input("th2: "))
    cmd.t3 = int(input("th3: "))

    cmd.serialize(buff)

    #print(to_hex(buff.getvalue()))
    #print(buff.getvalue())

    base_cmd = bytearray(buff.getvalue())
    arduino.write(base_cmd) # envia bytes a arduino

    while True:

        try:
            ser_bytes = arduino.readline() # lee una linea del puerto serial
            decoded_bytes = float(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
            print(decoded_bytes)
        except:
            print("Keyboard Interrupt")
            break
