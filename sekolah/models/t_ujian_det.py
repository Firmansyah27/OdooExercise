from odoo import models, fields, api, _

class UjianDet(models.Model):
    _name = "ujian.det"
    _description = "Ujian Det"

    ujian_id = fields.Many2one("t.ujian", ondelete="cascade")
    mata_pelajaran_id = fields.Many2one("mata.pelajaran",  string="Mata Pelajaran", required=True)
    nilai = fields.Integer(required=True, default=0)