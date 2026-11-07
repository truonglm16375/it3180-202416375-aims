### Câu 1 (tr. 19). Cấu hình --global được lưu ở đâu? Khác gì so với --local?
- --global lưu trong file cấu hình của người dùng: ~/.gitconfig (Windows: C:\Users\<tên>\.gitconfig). Áp dụng cho mọi repo của người dùng đó trên máy.
- --local (mặc định khi không ghi cờ, phải đứng trong repo) lưu ở <repo>/.git/config, chỉ áp dụng cho repo đó.
- Ưu tiên: local > global > system (--system, nằm trong thư mục cài Git). Cùng một khóa thì mức hẹp hơn thắng – vd. đặt email trường ở global nhưng repo khác dùng --local user.email riêng.
- Kiểm chứng: git config --list --show-origin in từng dòng cấu hình kèm file nguồn.

### Câu 2 (tr. 26). Vì sao dùng git mv?
- git mv a b đổi tên/di chuyển file và đưa thay đổi vào staging trong một lệnh (tương đương mv + git rm + git add), nên git status thấy ngay renamed.
- Git không lưu thao tác «đổi tên» mà nhận ra rename bằng cách so độ giống nội dung giữa file bị xóa và file mới. Vì vậy PDF tách commit «move» (nội dung không đổi, giống 100%) khỏi commit «update imports».
- Kết quả: tab Files changed của PR hiện renamed (không phải xóa + thêm) và git log --follow -- aims/cart.py vẫn lần được lịch sử trước khi chuyển; review dễ, blame không bị đứt.
- Nếu tự xóa + thêm file kèm sửa nhiều nội dung trong cùng commit, độ giống thấp có thể khiến Git coi là hai file khác nhau và mất liên kết lịch sử.

### Câu 3 (tr. 26). release/lab01 có phải baseline không?
- Có, về khái niệm: baseline là phiên bản đã thống nhất, chỉ thay đổi qua quy trình (tr. 6). release/lab01 được cắt từ master sau khi PR #1 merge và kiểm tra (hai mã băm giống master), là phiên bản giao nộp; từ đó muốn đổi nó chỉ qua hotfix + PR.
- Tuy nhiên ở Lab 01 nó mới là baseline «mềm»: chưa có branch protection và chưa có tag. Đến Lab 04 nó mới được đóng băng hẳn (rule release/*) và được định danh bằng tag v0.1.0.

### Câu 4 (tr. 26). Vì sao không commit thẳng master dù làm một mình?
- Truy vết & kiểm soát thay đổi: mỗi thay đổi gắn với một nhánh + PR (+ Issue), nên biết ai đổi gì, vì sao, ai duyệt. PR đóng vai Change Request, reviewer là CCB thu nhỏ.
- master luôn ổn định: master là nguồn để cắt release; thay đổi dở dang chỉ nằm trên nhánh riêng cho đến khi được kiểm thử/duyệt.
- Dễ hoàn tác: một PR là một đơn vị có thể revert gọn (Lab 03).
- Rèn quy trình: làm một mình vẫn viết mô tả PR theo template, chạy test/CI để sẵn sàng khi làm nhóm; branch protection (Lab 02) ép điều này bằng kỹ thuật.
- Ghi chú: các commit khởi tạo ở Phần A–C đi thẳng master vì repo mới tinh và chưa có protection; từ Phần D mọi thay đổi đều qua PR.