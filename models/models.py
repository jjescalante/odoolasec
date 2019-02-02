# -*- coding: utf-8 -*-


from odoo import models, fields, api


class Invoice(models.Model):
    _name = 'lasec.invoice'

    name = fields.Char(string="Report", required=True)
    description = fields.Text()
    invoice_ids = fields.One2many('lasec.report', 'report_id')
    debts_pay = fields.One2many('lasec.accounts', 'report2_id')
    accounts = fields.One2many('lasec.account', 'report3_id')

class Report(models.Model):
    _name = 'lasec.report'

    accounting_account = fields.Char(required=True)
    warehouse = fields.Char(required=True)
    location = fields.Char(required=True)
    item = fields.Char(required=True)
    description_item = fields.Text()
    posting_date = fields.Date()
    invoice_date = fields.Date()
    antiquity = fields.Float(digits=(6, 2), help="Duration in days")
    unit_measure = fields.Char(required=True)
    unit = fields.Integer()
    unit_cost = fields.Float(digits=(7, 2))
    value = fields.Float(digits=(12, 2), compute='_value', store=True)
    type = fields.Char(required=True)
    area = fields.Char(required=True)
    report_id = fields.Many2one('lasec.invoice',
								 ondelete='cascade',
                                 required=True)

    @api.depends('unit', 'unit_cost')
    def _value(self):
        for record in self.filtered(lambda r: r.unit):
            record.value = record.unit_cost * record.unit


class Accounts(models.Model):
    _name = 'lasec.accounts'

    company = fields.Char(requires=True)
    invoice_date = fields.Date()
    invoice = fields.Char(required=True)
    description = fields.Text()
    amount = fields.Float(digits=(12, 2))
    currency = fields.Char(required=True)
    total = fields.Float(digits=(12, 2))
    not_expired = fields.Float(digits=(12, 2))
    zero = fields.Float(digits=(12, 2))
    thirty = fields.Float(digits=(12, 2))
    sixty = fields.Float(digits=(12, 2))
    ninety = fields.Float(digits=(12, 2))
    more_one_hundred = fields.Float(digits=(12, 2))
    report2_id = fields.Many2one('lasec.invoice',
								  ondelete='cascade',
								  required=True)


class Account(models.Model):
    _name = 'lasec.account'

    company = fields.Char(requires=True)
    invoice_date = fields.Date()
    invoice = fields.Char(required=True)
    description = fields.Text()
    amount = fields.Float(digits=(12, 2))
    currency = fields.Char(required=True)
    total = fields.Float(digits=(12, 2))
    not_expired = fields.Float(digits=(12, 2))
    zero = fields.Float(digits=(12, 2))
    thirty = fields.Float(digits=(12, 2))
    sixty = fields.Float(digits=(12, 2))
    ninety = fields.Float(digits=(12, 2))
    more_one_hundred = fields.Float(digits=(12, 2))
    report3_id = fields.Many2one('lasec.invoice',
								  ondelete='cascade',
								  required=True)
