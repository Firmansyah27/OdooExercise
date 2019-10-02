from odoo import models, fields, api, _

class Ujian(models.Model):
    _name = "t.ujian"
    _description = "Ujian"

    tgl_ujian = fields.Date(string="Tanggal Ujian", required=True,)
    siswa_id = fields.Many2one("siswa",string="Siswa", required=True)
    t_ujian_det_ids = fields.One2many("ujian.det", 'ujian_id',)
    rata_rata = fields.Char(compute="_compute_rata_rata", store=True)

    @api.multi
    @api.depends('t_ujian_det_ids')
    def _compute_rata_rata(self):
        for record in self:
        	if len(record.t_ujian_det_ids) > 0:
        		record.rata_rata = sum(u_det.nilai for u_det in record.t_ujian_det_ids)/len(record.t_ujian_det_ids)

    @api.multi
    def name_get(self):
    	result = []
    	for record in self:
    		name = record.siswa_id.name
    		result.append((record.id, "nilai %s" % (name)))
    	return result