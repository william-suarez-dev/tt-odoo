# -*- coding: utf-8 -*-

from odoo import api, fields, models
from odoo.tools.translate import _


class StockScrap(models.Model):
    _inherit = 'stock.scrap'

    scrap_reason_id = fields.Many2one('stock.scrap.reason', string='Scrap reason')
    reason_note = fields.Text(string='Note')

