### Câu 1 (tr. 43). Merge base là gì?
- Merge base là commit tổ tiên chung gần nhất của hai nhánh (xem bằng git merge-base A B).
- Merge ba chiều: Git so sánh base → nhánh A và base → nhánh B. Chỉ một bên đổi thì lấy bên đó; hai bên đổi cùng vùng theo cách khác nhau thì xung đột. Ở Phần C, merge base là commit master lúc Dev 1 và Dev 2 cùng rẽ nhánh; cả hai sửa cùng dòng print nên xung đột.
- GitHub cũng dùng merge base để hiện diff của PR (các commit trên nhánh kể từ điểm rẽ). Vì vậy PR chọn nhầm base sẽ hiện «nhiều commit lạ» (tr. 43), và bugfix từ feature phải chọn base là nhánh feature.
- Rebase «dời» nhánh sang gốc mới nên merge base thay đổi theo.

### Câu 2 (tr. 43). Vì sao master/release/* phải dùng revert?
- Đây là lịch sử dùng chung và là baseline: người khác đã pull, tag và release trỏ vào đó.
- reset/rebase/amend viết lại lịch sử → SHA đổi → phải force push (bị branch protection cấm), clone của người khác lệch, mất dấu vết kiểm toán «ai đã đổi gì».
- revert tạo commit mới đảo ngược thay đổi: lịch sử giữ nguyên (cả lỗi lẫn bản sửa), push bình thường, đi qua PR/review như mọi thay đổi, an toàn cho người khác.
- Lưu ý: revert một merge commit cần -m 1 (chọn parent số 1 làm mainline). Muốn đưa lại tính năng đã revert thì phải revert chính commit revert, không phải merge lại nhánh cũ.