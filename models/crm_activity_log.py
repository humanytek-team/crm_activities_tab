from odoo import api, fields, models


class CRMActivityLog(models.TransientModel):
    _inherit = 'crm.activity.log'

    @api.multi
    def action_log(self):
        super(CRMActivityLog, self).action_log()
        for log in self:
            self.env['crm.activity.log_persistent'].create({
                'date_deadline': log.date_deadline,
                'lead_id': log.lead_id.id,
                'next_activity_id': log.next_activity_id.id,
                'note': log.note,
                'planned_revenue': log.planned_revenue,
                'title_action': log.title_action,
            })
        return True
