### Câu 1 (tr. 35). Vì sao phải đồng bộ master trước khi gửi PR?
- Nhánh được tạo từ master cũ; trong lúc bạn làm, master đã đi tiếp (vd. đã có print_cart). Đồng bộ (git fetch + git merge origin/master) để mã của bạn được tích hợp và kiểm thử cùng mã mới nhất (python main.py).
- Xung đột hoặc lỗi tích hợp được phát hiện và sửa trên nhánh của tác giả, trước khi vào master – không đẩy gánh nặng đó cho reviewer hay người bấm merge.
- Diff và kết quả kiểm thử của PR phản ánh đúng thứ sẽ được tích hợp (thứ được duyệt = thứ được tích hợp); master luôn chạy được.
- Phù hợp quy tắc «nhánh sống ngắn, gần master» (tr. 9), tránh «merge hell».

### Câu 2 (tr. 35). Khi nào không được rebase?
- Khi commit đã chia sẻ (đã push, người khác có thể đã lấy về hoặc dựa vào): rebase viết lại lịch sử, tạo SHA mới → lịch sử của người khác bị lệch và phải force push (quy tắc 5, tr. 9).
- Trên master và release/*: nhánh dùng chung/baseline, bị bảo vệ và cấm force push.
- Khi PR đang được review: rebase + force push làm comment/approval gắn với commit cũ mất ngữ cảnh. Trong bài, feature/search-by-title đã push và có PR nên dùng git merge origin/master, không rebase.
- Rebase chỉ hợp với nhánh riêng chưa ai dùng (như Cách 2 ở Lab 03, kèm --force-with-lease).

### Câu 3 (tr. 35). feature/* khác topic/* ra sao?
- feature/*: thêm tính năng cho sản phẩm, người dùng thấy được hành vi mới (cart-print, search-by-title, sort-cart) → vào mục Added của CHANGELOG.
- topic/*: công việc theo chủ đề không phải tính năng sản phẩm: tài liệu, cấu hình, template, chuẩn bị release, CI (topic/pr-template, topic/use-case-diagram, topic/prepare-release-1.0.0, topic/ci-unit-tests).
- Giống nhau: đều tạo từ master, merge vào master, qua PR, sống ngắn. Khác ở mục đích – tên nhánh phải nói lên loại công việc (quy tắc 2).