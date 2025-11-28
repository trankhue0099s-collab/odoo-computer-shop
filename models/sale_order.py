from odoo import models, fields, api
from dateutil.relativedelta import relativedelta
from datetime import date # <--- Mới thêm để lấy ngày hôm nay

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    bao_hanh = fields.Integer(string="Bảo hành (Tháng)", default=12)
    han_bao_hanh = fields.Date(string="Hết hạn BH", compute="_tinh_han_bao_hanh", store=True)
    
    # 1. Thêm cột Trạng thái bảo hành
    warranty_status = fields.Selection([
        ('valid', 'Còn bảo hành'),
        ('expired', 'Hết hạn'),
    ], string="Trạng thái", default='valid')

    @api.depends('bao_hanh', 'order_id.date_order')
    def _tinh_han_bao_hanh(self):
        for r in self:
            if r.order_id.date_order and r.bao_hanh:
                r.han_bao_hanh = r.order_id.date_order + relativedelta(months=r.bao_hanh)
            else:
                r.han_bao_hanh = False

    # 2. Hàm cho Robot chạy (Quét và cập nhật trạng thái)
    # 2. Hàm Robot: Quét đơn hết hạn VÀ Gửi Email
    def cron_check_warranty_expiration(self):
        today = date.today()
        # Tìm các dòng đơn hàng đang "Còn bảo hành" nhưng thực tế ngày đã qua
        # (Để tránh gửi lại email cho những đơn đã Hết hạn từ lâu rồi)
        lines = self.search([
            ('han_bao_hanh', '!=', False),
            ('han_bao_hanh', '<', today),
            ('warranty_status', '=', 'valid') # Chỉ quét những cái chưa đổi trạng thái
        ])
        
        # Lấy mẫu email ra sẵn
        template = self.env.ref('computer_shop.email_template_warranty_expired')

        for line in lines:
            # 1. Đổi trạng thái sang Hết hạn
            line.warranty_status = 'expired'
            
            # 2. Gửi Email (Gửi cho khách hàng của Đơn hàng đó)
            # Lưu ý: line là dòng chi tiết, line.order_id là Đơn hàng tổng
            if line.order_id.partner_id.email:
                template.send_mail(line.order_id.id, force_send=True)