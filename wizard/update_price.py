from odoo import models, fields, api

class UpdatePriceWizard(models.TransientModel):
    _name = 'computer.update.price.wizard'
    _description = 'Cập nhật giá hàng loạt'

    percent = fields.Integer(string="Phần trăm tăng giá (%)", default=5)

    def action_update_price(self):
        # Lấy tất cả sản phẩm
        products = self.env['product.template'].search([])
        for p in products:
            # Tính giá mới
            p.list_price = p.list_price * (1 + self.percent / 100)

        # Đóng cửa sổ sau khi chạy xong
        return {'type': 'ir.actions.act_window_close'}