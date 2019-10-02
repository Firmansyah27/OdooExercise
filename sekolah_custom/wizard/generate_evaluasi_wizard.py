from odoo import models, fields, api, _

class GenerateEvaluasi(models.TransientModel):
	_name = "generate.evaluasi"
	_description = "Data Generate Evaluasi"

	ekstrakul_id = fields.Many2one("ekstrakul", string="Ekstrakulikuler", readonly=True)
	trainer_id = fields.Many2one("trainer", required=True, ondelete="cascade")

	def _get_generate_evaluasi_det(self):
		res = []
		for siswa in self.env.context.get("siswa_ids", []):
			res.append([0,0,{"siswa_id":siswa, "nilai":0}])	

		return res

	generate_evaluasi_det_ids = fields.One2many("generate.evaluasi.det.wizard", "generate_evaluasi_id", default=_get_generate_evaluasi_det)
	def set_generate_evaluasi(self):

		evaluasi_det_ids = []
		exist_evaluasi = self.env['evaluasi'].search([
				("ekstrakur_id", "=", self.ekstrakul_id.id),
				("trainer_id", "=", self.trainer_id.id),
			], limit=1)
		if exist_evaluasi:
			evaluasi_det_ids.append([5])
		for i in self.generate_evaluasi_det_ids: 
			evaluasi_det_ids.append([0,0,{"siswa_id":i.siswa_id.id,"nilai":i.nilai}])
		if exist_evaluasi:
			exist_evaluasi.sudo().write({
				 "evaluasi_det_ids": evaluasi_det_ids
				})
			evaluasi = exist_evaluasi
		else:
			evaluasi = self.env['evaluasi'].sudo().create({'ekstrakur_id': self.ekstrakul_id.id, "trainer_id": self.trainer_id.id, "evaluasi_det_ids": evaluasi_det_ids})
		
		return {
            'name': _('Evaluasi'),
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'evaluasi',
            'view_id': False,
            'type': 'ir.actions.act_window',
            'target': 'current',
            'res_id': evaluasi.id,        
        }


class GenerateEvaluasiDet(models.TransientModel):
	_name= "generate.evaluasi.det.wizard"
	_description= "Generate Evaluasi Wizard"

	generate_evaluasi_id = fields.Many2one("generate.evaluasi",)
	siswa_id = fields.Many2one("siswa")
	nilai = fields.Integer(required=True, default=0)