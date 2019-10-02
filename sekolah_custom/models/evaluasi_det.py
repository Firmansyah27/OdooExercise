from odoo import models, fields, api, _

class Evaluasi(models.Model):
	_name = "evaluasi.det"
	_description = "Data Evaluasi"

	evaluasi_id = fields.Many2one("evaluasi", ondelete="cascade")
	siswa_id = fields.Many2one("siswa", string="Siswa")
	nilai = fields.Integer(required=True, default=0)