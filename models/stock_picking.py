from odoo import models,api

class StockPickings(models.Model):
    _inherit='stock.picking'


    def button_copy(self):
        for picking in self:
            self.ensure_one()
            picking_copy=picking.copy({'origin': f"Copy of {picking.name}"})
            return{
                'type':'ir.actions.act_window',
                'res_model':'stock.picking',
                'res_id':picking_copy.id,
                'view_mode':'form',
                'target':'current',

            }
