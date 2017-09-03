from odoo import api, fields, models


class CRMLead(models.Model):
    _inherit = 'crm.lead'

    logs = fields.One2many(
        comodel_name="crm.activity.log_persistent",
        inverse_name="lead_id",
    )
