# -*- coding: utf-8 -*-

from odoo import api, fields, models
from odoo.tools.translate import _


class StockScrapReason(models.Model):
    _description = "Scrap Reasons"
    _name = "stock.scrap.reason"

    name = fields.Char(string="Name", size=256, required=True)
    code = fields.Char(string="Code", size=64, required=True)

