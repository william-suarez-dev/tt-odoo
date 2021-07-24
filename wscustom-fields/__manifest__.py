# coding: utf-8

{
    'name': 'Custom Fields',
    'version' : '1.0',
    'author' : 'CIEXPRO',
    'category' : 'Uncategorized',
    'description' : """

    - Add new fields in the modules
    - Add new scrap reason model to mp modules
 
    """,

    'depends': [
        'base','stock','mrp','sale','crm','website_sale',
    ],
    'data': [
        'security/ir.model.access.csv',

        'views/stock_scrap_reason_view.xml',
        'views/stock_scrap_view.xml',
        'views/res_partner_view.xml',
        'views/product_family_view.xml',
        'views/product_template_view.xml',
    ],
    'installable': True,
}

