from odoo import models, fields, api, _
from datetime import datetime
from odoo.exceptions import  ValidationError

class Ujian(models.Model):
    _inherit="t.ujian"
    _description="Ujian Inherit"


    @api.multi
    @api.constrains("tgl_ujian")
    def date_constrains(self):
        for rec in self:
            if rec.tgl_ujian > datetime.now().date():
                raise ValidationError(_('Tanggal ujian harus sebelum ' + str(datetime.now().date()) ))