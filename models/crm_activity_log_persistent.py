from odoo import api, fields, models


class CRMActivityLog(models.Model):
    _inherit = 'crm.activity.log'
    _name = 'crm.activity.log_persistent'

    state = fields.Selection(
        required=True,
        selection=[
                ('new', 'New'),
                ('to_close', 'To Close'),
                ('closed', 'Closed'),
                ('canceled', 'Canceled'),
        ],
        default='new',
    )
