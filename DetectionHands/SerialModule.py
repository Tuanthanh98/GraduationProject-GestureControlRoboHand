import serial
import time
import logging


class SerialObject:
    """
   Cho phép truyền dữ liệu đến Thiết bị nối tiếp như Arduino.
     Ví dụ gửi $ 255255000
    """

    def __init__(self, portNo, baudRate, digits):
        """
       Khởi tạo đối tượng nối tiếp.
         : cổng thông sốNo: Số cổng.
         : param baudRate: Tốc độ truyền.
         : chữ số tham số: Số chữ số trên mỗi giá trị để gửi
        """
        self.portNo = portNo
        self.baudRate = baudRate
        self.digits = digits
        try:
            self.ser = serial.Serial(self.portNo, self.baudRate)
            print("Đã kết nối thiết bị")
        except:
            logging.warning("Thiết bị ngắt kết nối")

    def sendData(self, data):
        """
        Gửi dữ liệu đến thiết bị nối tiếp
         : tham số data: danh sách các giá trị cần gửi
        """
        myString = "$"
        for d in data:
            myString += str(int(d)).zfill(self.digits)
        try:
            self.ser.write(myString.encode())
            print(myString)
            return True
        except:
            return False


def main():
    mySerial = SerialObject("COM2", 9600, 1)
    while True:
        mySerial.sendData([1, 1, 1, 1, 1])
        time.sleep(2)
        mySerial.sendData([0, 0, 0, 0, 0])
        time.sleep(2)


if __name__ == "__main__":
    main()
