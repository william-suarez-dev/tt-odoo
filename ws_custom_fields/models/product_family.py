# -*- coding: utf-8 -*-

from odoo import api, fields, models
from odoo.tools.translate import _


class ProductFamily(models.Model):
    _description = "Product Family"
    _name = "product.family"

    name = fields.Char(string="Name", size=256, required=True)
    code = fields.Char(string="Code", size=64, required=True)

