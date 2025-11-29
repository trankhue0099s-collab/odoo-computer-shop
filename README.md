# 💻 Odoo 17 Computer Shop ERP System

Hệ thống Quản trị Nguồn lực Doanh nghiệp (ERP) chuyên dụng cho chuỗi bán lẻ máy tính. Hệ thống tích hợp toàn diện quy trình từ **Mua hàng (Purchase) ➔ Kho vận (Inventory) ➔ Bán hàng (Sales) ➔ Kế toán (Accounting)** trên nền tảng Odoo 17.

## 🌟 Điểm nhấn của Đồ án (Highlights)

Dự án không chỉ dừng lại ở việc quản lý thông tin đơn thuần mà tập trung giải quyết bài toán **"Luồng dữ liệu khép kín"** của doanh nghiệp:
1.  **Dữ liệu nhất quán:** Một đơn hàng bán ra sẽ tự động tạo phiếu xuất kho và hóa đơn kế toán.
2.  **Tự động hóa:** Robot tự động quét đơn hàng để gửi email chăm sóc khách hàng.
3.  **Báo cáo quản trị:** Phân tích doanh thu và tồn kho theo thời gian thực.

---

## 🚀 Tính năng chi tiết (Features)

### 1. Phân hệ Bán hàng & Sản phẩm (Sales & Product)
* **Cấu hình động:** Quản lý chi tiết CPU, RAM, HDD. Tự động sinh mã sản phẩm (Internal Reference) khi nhập liệu.
* **Giao diện Kanban:** Hiển thị trực quan thông số kỹ thuật (Icon chip/ram) ngay trên thẻ sản phẩm.
* **Website E-commerce:** Đồng bộ dữ liệu sản phẩm lên trang bán hàng trực tuyến.

### 2. Phân hệ Kho vận & Mua hàng (Inventory & Purchase)
* **Quản lý tồn kho thực tế:** Sản phẩm được định nghĩa là *Storable Product*. Hệ thống tự động trừ kho khi bán và cộng kho khi nhập mua.
* **Quy trình cung ứng:** Tự động đề xuất mua hàng khi tồn kho xuống thấp.
* **Truy vết:** Theo dõi lịch sử nhập/xuất chi tiết từng dòng sản phẩm.

### 3. Phân hệ Tài chính Kế toán (Invoicing/Accounting)
* **Tự động hóa đơn:** Tạo hóa đơn (Invoice) từ đơn bán hàng (Sale Order) chỉ với 1 click.
* **Ghi nhận thanh toán:** Quản lý trạng thái thanh toán (Paid/Not Paid), hỗ trợ thanh toán tiền mặt và chuyển khoản.
* **Hạch toán tự động:** Hệ thống tự động định khoản vào các tài khoản doanh thu (5111) và công nợ.

### 4. Tự động hóa & Tiện ích (Automation)
* **Robot Bảo hành (Cron Job):** Hệ thống tự động quét đơn hàng mỗi đêm (12:00 PM).
* **Email Marketing:** Tự động gửi email nhắc nhở khách hàng khi thiết bị hết hạn bảo hành.
* **Smart Buttons:** Liên kết nhanh giữa Phần mềm (Software) - Sản phẩm - Tồn kho - Hóa đơn.

---
## 🛠 Công nghệ sử dụng (Tech Stack)

* **Core Framework:** Odoo 17 (Community Edition).
* **Languages:** Python, XML, QWeb, PostgreSQL.
* **Modules:** Sales, Website, Inventory, Purchase, Invoicing, Mail.
* **Tools:** VS Code, Git/GitHub.

