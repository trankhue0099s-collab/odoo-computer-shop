{
    'name': "Cửa hàng Máy tính (Computer Shop)",
    'summary': "Bán máy tính, Laptop (Sửa đổi từ Sale)",
    'description': """
        Module quản lý cửa hàng máy tính:
        - Thêm cấu hình CPU, RAM vào sản phẩm.
        - Chỉnh sửa quy trình bán hàng.
    """,
    'author': "Ten Cua Ban",
    'category': 'Sales',
    'version': '1.0',
    
    # QUAN TRỌNG: Khai báo phụ thuộc vào module Bán hàng & Sản phẩm
    'depends': ['base', 'sale', 'website_sale', 'mail'],
    
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/product_view.xml',
        'views/sale_order_view.xml',
        'views/website_product_view.xml',
        'views/software_view.xml',
        'wizard/update_price_view.xml',
        'report/sale_report_inherit.xml',
        'data/cron_job.xml',
        'data/mail_template.xml',
        # Tạm thời để trống
    ],
    'application': True,
    'installable': True,
}