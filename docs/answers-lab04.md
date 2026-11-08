### Câu 1 (tr. 47). Vì sao chuẩn bị phát hành (version, CHANGELOG) trên master trước, không sửa trên nhánh release?
- `release/*` là baseline bị đóng băng: không commit trực tiếp, mọi thay đổi phải qua PR. `release/*` không bao giờ merge ngược vào `master`, mọi thứ sửa trực tiếp trên `release` sẽ không có trong `master` → hai dòng lệch nhau; bản sau (1.1.0…) mất số phiên bản và CHANGELOG của bản trước.
- Chuẩn bị trên `master` cho phép review/kiểm thử như mọi thay đổi khác; sau đó cắt `release` thì baseline chính là thứ đã duyệt.
- CHANGELOG là tài liệu liên tục ([Unreleased] → [1.0.0] → …) nên phải nằm trong lịch sử `master`.

### Câu 2 (tr. 52). Vì sao release/* không merge vào master? So sánh với GitFlow.
- `release/*` là dòng bảo trì của một bản đã phát hành: chỉ nhận hotfix. Nó chứa những thứ đặc thù của bản đó (số phiên bản, bản vá đã `cherry-pick`). Merge nó vào `master` sẽ kéo các thay đổi này (vd. 1.0.1) về `master`, gây xung đột và làm lịch sử `master` lộn xộn.
- Nhánh `master` đóng vai trò là nhánh gốc chuẩn (Single Source of Truth). Các bản sửa lỗi được chuyển sang master bằng lệnh `cherry-pick -x` để giữ vết thay vì merge cả nhánh.

**So sánh Release Flow và GitFlow**
- Trong mô hình Release Flow của học phần, hệ thống chỉ sử dụng một nhánh gốc duy nhất là `master`, khác với GitFlow khi duy trì song song hai nhánh gốc chính là `main` và `develop`.
- Đối với nhánh `release`, Release Flow cắt nhánh này từ `master` và giữ lại làm dòng bảo trì độc lập mà không merge ngược về. Trong khi đó, GitFlow cắt `release` từ `develop` và khi hoàn thành sẽ merge đồng thời vào cả `main` lẫn `develop`.
- Khi xử lý lỗi khẩn cấp (hotfix), Release Flow tạo hotfix từ `release/*` rồi áp dụng thay đổi sang cả `release` lẫn `master` bằng thao tác cherry-pick. Ngược lại, GitFlow lại tạo hotfix từ `main` rồi thực hiện merge vào hai nhánh `main` và `develop`.
- Chính cơ chế cherry-pick này giúp Release Flow giữ cho lịch sử của nhánh `master` luôn gọn gàng, loại bỏ các commit đặc thù của bản `release` và tránh được tình trạng xuất hiện quá nhiều commit merge hai chiều như trên GitFlow. Mô hình Release Flow này rất tối ưu cho các bài toán nộp bài theo tuần hoặc khi cần quản lý nhiều bản chạy song song.