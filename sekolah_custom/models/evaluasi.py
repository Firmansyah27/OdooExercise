from odoo import models, fields, api, _

class Evaluasi(models.Model):
	_name = "evaluasi"
	_description = "Data Evaluasi"

	ekstrakur_id = fields.Many2one("ekstrakul", required=True,)
	trainer_id = fields.Many2one("trainer", required=True,)
	evaluasi_det_ids = fields.One2many("evaluasi.det", "evaluasi_id", string="Daftar Nilai",)
	rata_rata = fields.Char(compute="_compute_rata_rata", store=True,)

	@api.multi
	@api.depends('evaluasi_det_ids')
	def _compute_rata_rata(self):
		for record in self:
			if len(record.evaluasi_det_ids) > 0:
				record.rata_rata = sum(e_det.nilai for e_det in record.evaluasi_det_ids) / len(record.evaluasi_det_ids)

	@api.multi
	def name_get(self):
		result = []
		for record in self:
			name = record.ekstrakur_id.name
			result.append((record.id, "%s" % (name)))
		return result