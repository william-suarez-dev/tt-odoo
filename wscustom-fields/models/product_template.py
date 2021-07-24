# -*- coding: utf-8 -*-

from odoo import api, fields, models
from odoo.tools.translate import _


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    product_family_id = fields.Many2one('product.family', string='Product family')
