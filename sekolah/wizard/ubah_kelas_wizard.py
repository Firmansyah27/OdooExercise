from odoo import models, fields, api, _

class UbahKelas(models.TransientModel):
	_name = "ubah.kelas"
	_description = "Ubah Data Kelas"

	def _get_default_siswa(self):
		return self.env["siswa"].browse(self.env.context.get("active_ids"))

	siswa_ids = fields.Many2many("siswa", string="siswa", default=_get_default_siswa)
	kelas = fields.Selection([
		("i","I"),
		("ii","II"),
		("iii","III"),
		], default="i", required=True)

	@api.multi
	def set_siswa_kelas(self):
		for record in self:
			if record.siswa_ids:
				for siswa in record.siswa_ids:
					siswa.kelas = self.kelas