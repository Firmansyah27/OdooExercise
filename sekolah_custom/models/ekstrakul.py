from odoo import models, fields, api, _

class Ekstrakul(models.Model):
	_name = "ekstrakul"
	_description = "Data Ekstrakulikuler"

	# def _get_default_siswa(self):
	# 	return self.env["siswa"].browse(self.env.context.get("active_ids"))

	name = fields.Char(required=True, string="Nama Ekstrakulikuler")
	siswa_ids = fields.Many2many("siswa","siswa_ekstrakul_rel", string="Siswa", )

	@api.multi
	def call_generate_evaluasi_wizard(self):
		wizard_form = self.env.ref(
			'sekolah_custom.view_generate_evaluasi_wizard_form', False)

		return {
			'name': _('Generate Evaluasi'),
			'type': 'ir.actions.act_window',
			'res_model': 'generate.evaluasi',
			# 'res_id': new.id,
			'view_id': wizard_form.id,
			'view_type': 'form',
			'view_mode' : 'form',
			'target': 'new',
			'context': {"default_ekstrakul_id": self.id, "siswa_ids": self.siswa_ids.ids}
		}

class Siswa(models.Model):
	_inherit = "siswa"

	ekstrakul_ids = fields.Many2many("ekstrakul", "siswa_ekstrakul_rel", string="Ekstrakulikuler")
