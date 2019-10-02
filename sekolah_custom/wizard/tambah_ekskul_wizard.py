from odoo import models, fields, api, _

class TambahEkskul(models.TransientModel):
	_name = "tambah.ekskul"
	_description = "Data Tambah Ekskul"

	def _get_default_siswa(self):
			return self.env["siswa"].browse(self.env.context.get("active_ids"))

	siswa_ids = fields.Many2many("siswa", string="siswa", default=_get_default_siswa)
	ekstrakul_ids = fields.Many2one("ekstrakul", required=True)

	@api.multi
	def set_tambah_ekskul(self):
		for record in self:
			if record.siswa_ids:
				for siswa in record.siswa_ids:
					siswa.ekstrakul_ids = self.ekstrakul_ids + siswa.ekstrakul_ids
