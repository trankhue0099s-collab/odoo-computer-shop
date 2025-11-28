from odoo import models, fields, api
from odoo.exceptions import ValidationError # <--- Thư viện để báo lỗi chặn người dùng

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    pro_cpu = fields.Char(string="Vi xử lý (CPU)")
    pro_ram = fields.Selection([
        ('4gb', '4 GB'),
        ('8gb', '8 GB'),
        ('16gb', '16 GB'),
        ('32gb', '32 GB'),
    ], string="Bộ nhớ (RAM)")
    pro_hdd = fields.Char(string="Ổ cứng (HDD/SSD)")
    software_ids = fields.Many2many('computer.software', string="Phần mềm cài sẵn")

    # ---------------------------------------------------------
    # 1. TỰ ĐỘNG ĐIỀN MÃ (ONCHANGE)
    # Sự kiện: Khi người dùng thay đổi CPU hoặc RAM -> Chạy hàm này
    # ---------------------------------------------------------
    @api.onchange('pro_cpu', 'pro_ram')
    def _onchange_auto_gen_code(self):
        # Nếu đã có cả CPU và RAM
        if self.pro_cpu and self.pro_ram:
            # Xử lý text: Ví dụ CPU "Core i5" -> Lấy chữ "i5" (Tách dấu cách, lấy phần tử cuối)
            cpu_clean = self.pro_cpu.split(' ')[-1] 
            # Xử lý RAM: "16gb" -> "16GB" (Viết hoa lên)
            ram_clean = self.pro_ram.upper()
            
            # Gán vào ô Mã nội bộ (default_code)
            self.default_code = f"PC-{cpu_clean}-{ram_clean}"

    # ---------------------------------------------------------
    # 2. CHẶN NHẬP SAI (CONSTRAINS)
    # Sự kiện: Khi bấm nút LƯU -> Chạy hàm này để kiểm tra
    # ---------------------------------------------------------
    @api.constrains('list_price')
    def _check_price_not_negative(self):
        for record in self:
            if record.list_price < 0:
                raise ValidationError("Giá bán không được phép âm tiền! 😡")