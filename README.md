LỖ HỔNG BẢO MẬT IDOR TRÊN WEBSITE AZOTA
Mô tả: lỗi bảo mật có thể khiến cho người dùng với quyền giáo viên sẽ xem được đáp án của các câu hỏi không thuộc về mình.

Quá trình thực hiện:

Bước 1: Tạo tài khoản giáo viên

Bước 2: Tạo một đề thi thử và vào phần chỉnh sửa nội dung câu hỏi


![668a5136-43d9-404e-8ebf-3a7bf5054ec8](https://github.com/Ngoducvan/Report_Bug/assets/88313289/7e8932b3-6259-498a-96fb-3fb4d8e7a8cd)

Chú ý: Url trên có chứa ID của câu hỏi


![5ca7ce02652acb74923b](https://github.com/Ngoducvan/Report_Bug/assets/88313289/c787b394-4de8-40b7-8e45-e15bfabdd382)

* ID của câu hỏi trên là 169688459
* Vậy muốn xem nội dung và đáp án của câu hỏi nào thì chỉ cần thay ID của câu hỏi đó là sẽ xem được
  
Buớc 3: Lấy ID của câu hỏi trong đề thi ( 2 cách )
  
  Cách 1: Có thể lấy được bằng cách inspect câu hỏi trực tiếp trong đề thi
  
  
  ![b7f1be90-adec-472f-98e2-6d1335920def](https://github.com/Ngoducvan/Report_Bug/assets/88313289/72f82c6f-ac63-40f1-b319-8915591e2471)
  
  Cách 2: Có thể lấy được bằng cách bắt request của đề thi trước khi làm bài
  
  
  ![6c73006b-8da7-4bcc-b1e8-1e28e17dd8c5](https://github.com/Ngoducvan/Report_Bug/assets/88313289/09de1129-2405-4a87-b7ce-796017c9581c)


Bước 4: Dán ID câu hỏi vừa lấy được vào URL ở bước 2 thì sẽ xem được đáp án của câu hỏi


![f7e9b4aa-77ce-4c63-8157-8dcc9eaa2a47](https://github.com/Ngoducvan/Report_Bug/assets/88313289/ea548345-e017-4f88-b47b-3fbcbd57e683)
  
Dưới đây là đường link dẫn đến video quá trình thực hiện
* Mình có viết 1 tool Python để dán link vào và tool sẽ tự động lấy đáp án
  
  [VIDEO THỰC HIỆN TRÊN MÁY TÍNH](https://drive.google.com/drive/folders/1qQiC8_f9JNI91FMHwWliaVpLkHy59n2g?usp=drive_link)

Cảm ơn bạn đã đọc báo cáo.
  
  






















