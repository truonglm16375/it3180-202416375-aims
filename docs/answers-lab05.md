### Câu 1 (tr. 60): Vì sao ở Phần A chưa gắn tag `v1.1.0` ngay khi tạo nhánh `release/lab05`?

* **Quy tắc bất biến của Tag:** Tag được sử dụng để định danh chính xác một *baseline* phát hành. Theo nguyên tắc SCM, một tag đã được chia sẻ/push lên remote thì tuyệt đối **không được di chuyển hoặc xóa bỏ**.

* **Trạng thái nhánh chưa hoàn chỉnh:** Tại Phần A, nhánh `release/lab05` được cắt từ `master` nhưng vẫn mang lỗi phân biệt hoa/thường trong hàm `search_by_title` (lỗi tồn tại từ Lab 02 và chưa được vá). Nếu đánh tag `v1.1.0` ngay lúc này, tag sẽ bị khóa cố định vào một mốc mã nguồn chứa lỗi.

* **Chi phí xử lý khi trót gắn tag:** Nếu lỡ gắn tag `v1.1.0` trước khi sửa lỗi, sau khi `cherry-pick` bản vá hotfix vào `release/lab05`, ta bắt buộc phải nâng phiên bản PATCH lên `v1.1.1` chứ không thể dời tag `v1.1.0` sang commit mới. Do đó, việc trì hoãn gắn tag cho đến khi hoàn tất `cherry-pick` giúp đảm bảo mốc phát hành `v1.1.0` đại diện cho một baseline hoàn chỉnh và ổn định nhất.

---

### Câu 2 (tr. 64): Ưu và nhược điểm của chiến lược Upstream First so với Release First?

Bản chất của mô hình **Release First** (được sử dụng trong học phần) là thực hiện sửa lỗi trực tiếp trên dòng `release/*` đã phát hành trước, sau đó dùng lệnh `cherry-pick` để lan truyền bản vá về `master`. Trái lại, mô hình **Upstream First** (được áp dụng trong Release Flow của Microsoft) làm ngược lại: ưu tiên sửa lỗi và hoàn tất kiểm thử trên nhánh gốc `master` trước, sau đó mới `cherry-pick` xuống các nhánh `release/*` bị ảnh hưởng.

Về **chiến lược Upstream First**, ưu điểm lớn nhất là khả năng **chống tái lỗi (anti-regression)** tuyệt đối. Do bản vá được đưa vào nhánh `master` đầu tiên, mọi phiên bản phát hành trong tương lai chắc chắn sẽ thừa hưởng bản sửa này. Bên cạnh đó, mã nguồn sửa lỗi được kiểm thử và review đồng bộ trên môi trường phát triển chính với đầy đủ quy trình CI. Tuy nhiên, nhược điểm của Upstream First là **tốc độ phát hành bản vá chậm** hơn do phải vượt qua các bước kiểm duyệt trên `master`. Đồng thời, khi `cherry-pick` bản sửa từ `master` về các nhánh `release/*` cũ, nguy cơ **xung đột mã nguồn (conflict)** rất cao do `master` đã tiến xa và khác biệt nhiều so với các bản release trước đó.

Về **chiến lược Release First**, ưu điểm vượt trội là khả năng **vá lỗi khẩn cấp và tức thì** cho người dùng. Lập trình viên có thể tái hiện và xác nhận lỗi chính xác trên đúng môi trường baseline đã phát hành mà không làm ảnh hưởng đến tiến độ tính năng mới trên `master`. Mặc dù vậy, nhược điểm quan trọng của Release First là **rủi ro bỏ sót bản vá** khi quên `cherry-pick` ngược về `master` hoặc các nhánh release khác, khiến lỗi có nguy cơ xuất hiện lại ở các bản phát hành sau. Ngoài ra, mô hình này đòi hỏi đội ngũ phải **tốn thêm chi phí kiểm toán** đa phiên bản thủ công ở Phần F để xác minh bản vá đã được lan truyền đầy đủ.

Trong bài thực hành, quy trình **Release First** được chọn vì phản ánh chính xác kịch bản "sửa bài đã nộp" — nơi yêu cầu quan trọng nhất là khắc phục lỗi nhanh nhất trên bài làm đã giao cho khách hàng.

---

### Câu 3 (tr. 64): Nếu quên lan truyền bản sửa sang `release/lab05`, các lệnh ở Phần F sẽ phát hiện ra sao?

1. **`git log --all --oneline --grep "cherry picked from commit <FIX_SHA>"`**:
* *Kỳ vọng:* Xuất hiện **2 commit** (một trên `master` và một trên `release/lab05`).
* *Nếu quên:* Chỉ hiển thị **1 commit** (trên `master`).


2. **`git cherry -v origin/release/lab05 origin/release/lab04`**:
* *Kỳ vọng:* Hiển thị dấu `-` trước commit sửa lỗi (báo hiệu `release/lab05` đã sở hữu commit tương đương).
* *Nếu quên:* Hiển thị dấu `+` (báo hiệu commit sửa lỗi từ `release/lab04` **chưa có** bản tương ứng trên `release/lab05`).


3. **Vòng lặp kiểm tra hành vi tự động (`for ref in v1.0.1 v1.1.0 master...`)**:
* *Kỳ vọng:* Cả 3 mốc (`v1.0.1`, `v1.1.0`, `master`) đều trả về kết quả `1`.
* *Nếu quên:* Mốc `v1.1.0` sẽ trả về `0` do chưa có logic xử lý không phân biệt hoa/thường. Đây là phương pháp kiểm toán đáng tin cậy nhất vì nó xác minh trực tiếp hành vi chạy thực tế của mã nguồn.


(Lưu ý: Lệnh `git tag --contains <FIX_SHA>` không thể phát hiện thiếu sót này do nó chỉ truy vết đúng mã SHA gốc trên `release/lab04`. Khi `cherry-pick` sang nhánh khác, Git tạo ra commit mới với mã SHA mới nên lệnh này sẽ luôn chỉ liệt kê tag `v1.0.1`).

---

### Câu bổ sung (tr. 59): Vì sao không merge cả nhánh hotfix vào `master`?

* **Xung đột thông tin phiên bản:** Nhánh `hotfix` chứa 2 commit riêng biệt:

1. *Commit 1 (`FIX_SHA`):* Mã nguồn sửa lỗi và unit test tái hiện (dùng chung cho mọi dòng phiên bản).
2. *Commit 2:* Nâng số phiên bản lên `1.0.1` và cập nhật mục `[1.0.1]` trong `CHANGELOG.md`.
Commit 2 mang thông tin dành riêng cho dòng bảo trì `1.0.x`. Nếu merge cả nhánh `hotfix` vào `master` (vốn đang chuẩn bị cho `1.1.0`), GitHub sẽ báo `Can't automatically merge` do xung đột số phiên bản giữa `1.0.1` và `1.1.0`.

* **Đảm bảo tính độc lập của lịch sử (Separation of Concerns):** Việc sử dụng `git cherry-pick -x <FIX_SHA>` cho phép chỉ trích xuất duy nhất phần mã sửa lỗi nguyên bản đưa sang `master`. Sau đó, `master` sẽ tự bổ sung ghi chú vào `CHANGELOG.md` của riêng mình mà không làm sai lệch luồng đánh số phiên bản.
