from odoo import models, fields, api

class ComputerSoftware(models.Model):
    _name = 'computer.software'
    _description = 'Phần mềm Máy tính'
    # Kế thừa Mixin để có tính năng Chat và Theo dõi lịch sử
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Tên phần mềm", required=True, tracking=True) # tracking=True: Để ghi lại lịch sử khi sửa tên
    price = fields.Float(string="Giá bản quyền", tracking=True) # Ghi lại lịch sử khi sửa giá

    # ... (Các phần code cũ giữ nguyên: product_count, compute, action...)
    product_count = fields.Integer(string="Số lượng máy", compute='_compute_product_count')

    def _compute_product_count(self):
        for record in self:
            record.product_count = self.env['product.template'].search_count([
                ('software_ids', 'in', record.id)
            ])

    def action_view_products(self):
        return {
            'name': 'Sản phẩm cài ' + self.name,
            'type': 'ir.actions.act_window',
            'res_model': 'product.template',
            'view_mode': 'tree,form',
            'domain': [('software_ids', 'in', self.id)],
            'context': {'default_software_ids': [self.id]},
        }