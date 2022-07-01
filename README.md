# Graduation Project: Gesture Control RoboHand
Ngày tạo: 22/06/2022

# Mô tả 
Thực hiện được những yêu cầu sau:  
- Dùng 5 động cơ servo để điều khiển 5 ngón tay.
- Tay robot điều khiển được các ngón tay.
- Nhận diện bàn tay. Đưa ra các tín hiệu cử chỉ của ngón tay.
- Vi điều khiển xử lý dữ liệu nhận được dữ liệu, sau đó điều khiển motor tương ứng với ngón tay.
- Xử lý được package data của giao tiếp giữa máy tính với Vi điều khiển.
# Linh kiện sử dụng
- Arduino Uno R3
- Motor servo mg966r x5
- Mô hình cánh tay robot ( nguồn -> http://inmoov.fr/inmoov-stl-parts-viewer/?bodyparts=Right-Hand)
- Camera trên laptop hoặc camera rời.
# Công cụ và ngôn ngữ sử dụng.
**Công cụ:**  
    - pyCharm IDE hoặc Visual studio code  
    - Arduino IDE  
 **Ngôn Ngữ:**  
    - Python 3.10.5  
    - C++
    
# Nguyên lý hoạt động   
  ![Picture1](https://user-images.githubusercontent.com/67089995/176935110-3482d677-5c8b-4c41-91b6-e0ec622286ea.png)  
Nguyên lý hoạt động: Dữ liệu đầu vào là hình ảnh trực tiếp. Hình ảnh đưa vào sẽ được xử lý để nhận diện được bàn tay. 
Khi đã nhận diện được bàn tay sẽ kiểm tra trạng thái các ngón tay và trả về giá trị tương ứng(duỗi ra – 1, co vào – 0).
Trạng thái 5 ngón tay sẽ trả về dưới dạng mảng ký tự, sau đó sẽ được truyền qua Serial(cổng COM) được nối từ arduino đến máy tính.
Khi nhận được chuỗi ký tự thì arduino sẽ phải đọc và tách lấy từ ký tự tương ứng với từng ngón tay để điều khiển motor servo tương ứng với mỗi ngón.

# Demo

Click vào link để xem demo - >> https://youtu.be/YBay6AIpYGo  

[![Watch the video](https://user-images.githubusercontent.com/67089995/176939670-371df1e1-846d-4cc4-8650-efbc7e571a75.png)](https://youtu.be/YBay6AIpYGo)
