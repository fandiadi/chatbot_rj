def findDecision(obj): #obj[0]: jk, obj[1]: usia, obj[2]: keluhan_1, obj[3]: keluhan_2, obj[4]: keluhan_3
	# {"feature": "keluhan_1", "instances": 3292, "metric_value": 3.1767, "depth": 1}
	if obj[2] == 'BATUK':
		# {"feature": "usia", "instances": 194, "metric_value": 1.0679, "depth": 2}
		if obj[1] == 'anak':
			# {"feature": "keluhan_2", "instances": 162, "metric_value": 0.096, "depth": 3}
			if obj[3] == 'TIDAK ADA':
				# {"feature": "jk", "instances": 83, "metric_value": 0.0941, "depth": 4}
				if obj[0] == 'Laki-laki':
					# {"feature": "keluhan_3", "instances": 49, "metric_value": 0.1437, "depth": 5}
					if obj[4] == 'TIDAK ADA':
						return 'Kesehatan Anak'
					else: return 'Kesehatan Anak'
				elif obj[0] == 'Perempuan':
					return 'Kesehatan Anak'
				else: return 'Kesehatan Anak'
			elif obj[3] == 'PILEK':
				# {"feature": "jk", "instances": 50, "metric_value": 0.1414, "depth": 4}
				if obj[0] == 'Laki-laki':
					return 'Kesehatan Anak'
				elif obj[0] == 'Perempuan':
					# {"feature": "keluhan_3", "instances": 21, "metric_value": 0.2762, "depth": 5}
					if obj[4] == 'TIDAK ADA':
						return 'Kesehatan Anak'
					elif obj[4] == 'DEMAM':
						return 'Kesehatan Anak'
					elif obj[4] == 'HIDUNG TERSUMBAT':
						return 'Kesehatan Anak'
					elif obj[4] == 'PANAS':
						return 'Kesehatan Anak'
					elif obj[4] == 'SESAK':
						return 'Kesehatan Anak'
					else: return 'Kesehatan Anak'
				else: return 'Kesehatan Anak'
			elif obj[3] == 'DEMAM':
				return 'Kesehatan Anak'
			elif obj[3] == 'MUNTAH':
				return 'Kesehatan Anak'
			elif obj[3] == 'PANAS':
				return 'Kesehatan Anak'
			elif obj[3] == 'PUSING':
				return 'Kesehatan Anak'
			elif obj[3] == 'KERINGAT DINGIN':
				return 'Kesehatan Anak'
			elif obj[3] == 'MAAG':
				return 'Kesehatan Anak'
			elif obj[3] == 'ALERGI':
				return 'Kesehatan Anak'
			elif obj[3] == 'ASMA':
				return 'Kesehatan Anak'
			elif obj[3] == 'DIARE':
				return 'Kesehatan Anak'
			elif obj[3] == 'SARIAWAN':
				return 'Kesehatan Anak'
			elif obj[3] == 'MIMISAN':
				return 'Kesehatan Anak'
			else: return 'Kesehatan Anak'
		elif obj[1] == 'dewasa':
			# {"feature": "keluhan_2", "instances": 32, "metric_value": 2.244, "depth": 3}
			if obj[3] == 'TIDAK ADA':
				# {"feature": "jk", "instances": 23, "metric_value": 2.0329, "depth": 4}
				if obj[0] == 'Perempuan':
					# {"feature": "keluhan_3", "instances": 16, "metric_value": 2.0079, "depth": 5}
					if obj[4] == 'TIDAK ADA':
						return 'Penyakit Dalam'
					else: return 'Penyakit Dalam'
				elif obj[0] == 'Laki-laki':
					# {"feature": "keluhan_3", "instances": 7, "metric_value": 1.4488, "depth": 5}
					if obj[4] == 'TIDAK ADA':
						return 'Paru-paru'
					else: return 'Paru-paru'
				else: return 'Paru-paru'
			elif obj[3] == 'DEMAM':
				# {"feature": "jk", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[0] == 'Perempuan':
					return 'Rehabilitasi Medik'
				elif obj[0] == 'Laki-laki':
					return 'Paru-paru'
				else: return 'Paru-paru'
			elif obj[3] == 'FLU':
				# {"feature": "jk", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[0] == 'Laki-laki':
					# {"feature": "keluhan_3", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[4] == 'TIDAK ADA':
						return 'THT'
					else: return 'THT'
				else: return 'THT'
			elif obj[3] == 'SESAK':
				# {"feature": "jk", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[0] == 'Perempuan':
					return 'Paru-paru'
				elif obj[0] == 'Laki-laki':
					return 'Kardiologi atau Jantung'
				else: return 'Kardiologi atau Jantung'
			elif obj[3] == 'TELINGA GATAL':
				return 'THT'
			elif obj[3] == 'PUSING':
				return 'Paru-paru'
			elif obj[3] == 'RADANG':
				return 'THT'
			else: return 'THT'
		else: return 'Paru-paru'
	elif obj[2] == 'BAPIL':
		# {"feature": "usia", "instances": 172, "metric_value": 0.0515, "depth": 2}
		if obj[1] == 'anak':
			return 'Kesehatan Anak'
		elif obj[1] == 'dewasa':
			return 'Kebidanan dan Kandungan'
		else: return 'Kebidanan dan Kandungan'
	elif obj[2] == 'DEMAM':
		# {"feature": "usia", "instances": 159, "metric_value": 0.3696, "depth": 2}
		if obj[1] == 'anak':
			# {"feature": "jk", "instances": 151, "metric_value": 0.0575, "depth": 3}
			if obj[0] == 'Laki-laki':
				# {"feature": "keluhan_2", "instances": 79, "metric_value": 0.0979, "depth": 4}
				if obj[3] == 'TIDAK ADA':
					# {"feature": "keluhan_3", "instances": 52, "metric_value": 0.1371, "depth": 5}
					if obj[4] == 'TIDAK ADA':
						return 'Kesehatan Anak'
					else: return 'Kesehatan Anak'
				elif obj[3] == 'BATUK':
					return 'Kesehatan Anak'
				elif obj[3] == 'PILEK':
					return 'Kesehatan Anak'
				elif obj[3] == 'BAPIL':
					return 'Kesehatan Anak'
				elif obj[3] == 'FLU':
					return 'Kesehatan Anak'
				elif obj[3] == 'BINTIK BINTIK':
					return 'Kesehatan Anak'
				elif obj[3] == 'MUAL':
					return 'Kesehatan Anak'
				elif obj[3] == 'BATUK BERDAHAK':
					return 'Kesehatan Anak'
				elif obj[3] == 'BINTIK MERAH':
					return 'Kesehatan Anak'
				elif obj[3] == 'MUNTAH':
					return 'Kesehatan Anak'
				elif obj[3] == 'PERUT KEMBUNG':
					return 'Kesehatan Anak'
				elif obj[3] == 'DIARE':
					return 'Kesehatan Anak'
				elif obj[3] == 'KUPING SAKIT':
					return 'Kesehatan Anak'
				else: return 'Kesehatan Anak'
			elif obj[0] == 'Perempuan':
				return 'Kesehatan Anak'
			else: return 'Kesehatan Anak'
		elif obj[1] == 'dewasa':
			# {"feature": "jk", "instances": 8, "metric_value": 0.5436, "depth": 3}
			if obj[0] == 'Laki-laki':
				# {"feature": "keluhan_2", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[3] == 'TIDAK ADA':
					# {"feature": "keluhan_3", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[4] == 'TIDAK ADA':
						return 'Penyakit Dalam'
					else: return 'Penyakit Dalam'
				elif obj[3] == 'LEMAS':
					return 'Penyakit Dalam'
				elif obj[3] == 'MUNTAH':
					return 'Penyakit Dalam'
				else: return 'Penyakit Dalam'
			elif obj[0] == 'Perempuan':
				return 'Penyakit Dalam'
			else: return 'Penyakit Dalam'
		else: return 'Penyakit Dalam'
	elif obj[2] == 'KONTROL KESEHATAN':
		return 'Kesehatan Anak'
	elif obj[2] == 'KONTROL HAMIL':
		return 'Kebidanan dan Kandungan'
	elif obj[2] == 'VAKSIN':
		# {"feature": "usia", "instances": 54, "metric_value": 0.3095, "depth": 2}
		if obj[1] == 'anak':
			return 'Kesehatan Anak'
		elif obj[1] == 'dewasa':
			return 'Kebidanan dan Kandungan'
		else: return 'Kebidanan dan Kandungan'
	elif obj[2] == 'IMM':
		return 'Kesehatan Anak'
	elif obj[2] == 'IMUNISASI':
		return 'Kesehatan Anak'
	elif obj[2] == 'DIARE':
		# {"feature": "usia", "instances": 46, "metric_value": 0.6153, "depth": 2}
		if obj[1] == 'anak':
			return 'Kesehatan Anak'
		elif obj[1] == 'dewasa':
			return 'Penyakit Dalam'
		else: return 'Penyakit Dalam'
	elif obj[2] == 'KONTROL KULIT & KELAMIN':
		return 'Kulit dan Kelamin'
	elif obj[2] == 'GATAL GATAL':
		# {"feature": "usia", "instances": 42, "metric_value": 0.9046, "depth": 2}
		if obj[1] == 'dewasa':
			# {"feature": "jk", "instances": 27, "metric_value": 0.455, "depth": 3}
			if obj[0] == 'Laki-laki':
				# {"feature": "keluhan_2", "instances": 14, "metric_value": 0.3712, "depth": 4}
				if obj[3] == 'TIDAK ADA':
					# {"feature": "keluhan_3", "instances": 13, "metric_value": 0.3912, "depth": 5}
					if obj[4] == 'TIDAK ADA':
						return 'Kulit dan Kelamin'
					else: return 'Kulit dan Kelamin'
				elif obj[3] == 'PANU':
					return 'Kulit dan Kelamin'
				else: return 'Kulit dan Kelamin'
			elif obj[0] == 'Perempuan':
				# {"feature": "keluhan_2", "instances": 13, "metric_value": 0.3912, "depth": 4}
				if obj[3] == 'TIDAK ADA':
					# {"feature": "keluhan_3", "instances": 13, "metric_value": 0.3912, "depth": 5}
					if obj[4] == 'TIDAK ADA':
						return 'Kulit dan Kelamin'
					else: return 'Kulit dan Kelamin'
				else: return 'Kulit dan Kelamin'
			else: return 'Kulit dan Kelamin'
		elif obj[1] == 'anak':
			# {"feature": "jk", "instances": 15, "metric_value": 0.971, "depth": 3}
			if obj[0] == 'Perempuan':
				# {"feature": "keluhan_2", "instances": 10, "metric_value": 0.8813, "depth": 4}
				if obj[3] == 'TIDAK ADA':
					# {"feature": "keluhan_3", "instances": 10, "metric_value": 0.8813, "depth": 5}
					if obj[4] == 'TIDAK ADA':
						return 'Kulit dan Kelamin'
					else: return 'Kulit dan Kelamin'
				else: return 'Kulit dan Kelamin'
			elif obj[0] == 'Laki-laki':
				# {"feature": "keluhan_2", "instances": 5, "metric_value": 0.971, "depth": 4}
				if obj[3] == 'TIDAK ADA':
					# {"feature": "keluhan_3", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[4] == 'TIDAK ADA':
						return 'Kesehatan Anak'
					else: return 'Kesehatan Anak'
				else: return 'Kesehatan Anak'
			else: return 'Kesehatan Anak'
		else: return 'Kulit dan Kelamin'
	elif obj[2] == 'MATA':
		return 'Mata'
	elif obj[2] == 'PANAS':
		return 'Kesehatan Anak'
	elif obj[2] == 'KONTROL GIGI DAN MULUT':
		return 'Kesehatan Gigi dan Mulut Anak'
	elif obj[2] == 'DEMAM ':
		return 'Kesehatan Anak'
	elif obj[2] == 'BATUK PILEK':
		# {"feature": "jk", "instances": 30, "metric_value": 0.2108, "depth": 2}
		if obj[0] == 'Laki-laki':
			# {"feature": "keluhan_2", "instances": 16, "metric_value": 0.3373, "depth": 3}
			if obj[3] == 'TIDAK ADA':
				# {"feature": "usia", "instances": 14, "metric_value": 0.3712, "depth": 4}
				if obj[1] == 'anak':
					# {"feature": "keluhan_3", "instances": 14, "metric_value": 0.3712, "depth": 5}
					if obj[4] == 'TIDAK ADA':
						return 'Kesehatan Anak'
					else: return 'Kesehatan Anak'
				else: return 'Kesehatan Anak'
			elif obj[3] == 'PANAS':
				return 'Kesehatan Anak'
			else: return 'Kesehatan Anak'
		elif obj[0] == 'Perempuan':
			return 'Kesehatan Anak'
		else: return 'Kesehatan Anak'
	elif obj[2] == 'KONTROL BEDAH':
		return 'Bedah'
	elif obj[2] == 'SAKIT GIGI':
		# {"feature": "usia", "instances": 27, "metric_value": 1.4216, "depth": 2}
		if obj[1] == 'dewasa':
			# {"feature": "keluhan_2", "instances": 18, "metric_value": 0.5033, "depth": 3}
			if obj[3] == 'TIDAK ADA':
				# {"feature": "jk", "instances": 16, "metric_value": 0.5436, "depth": 4}
				if obj[0] == 'Perempuan':
					# {"feature": "keluhan_3", "instances": 11, "metric_value": 0.4395, "depth": 5}
					if obj[4] == 'TIDAK ADA':
						return 'Gigi dan Mulut'
					else: return 'Gigi dan Mulut'
				elif obj[0] == 'Laki-laki':
					# {"feature": "keluhan_3", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[4] == 'TIDAK ADA':
						return 'Gigi dan Mulut'
					else: return 'Gigi dan Mulut'
				else: return 'Gigi dan Mulut'
			elif obj[3] == 'BENGKAK':
				return 'Gigi dan Mulut'
			elif obj[3] == 'GUSI BENGKAK':
				return 'Gigi dan Mulut'
			else: return 'Gigi dan Mulut'
		elif obj[1] == 'anak':
			# {"feature": "jk", "instances": 9, "metric_value": 0.5033, "depth": 3}
			if obj[0] == 'Perempuan':
				# {"feature": "keluhan_2", "instances": 6, "metric_value": 0.65, "depth": 4}
				if obj[3] == 'TIDAK ADA':
					# {"feature": "keluhan_3", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[4] == 'TIDAK ADA':
						return 'Kesehatan Gigi dan Mulut Anak'
					else: return 'Kesehatan Gigi dan Mulut Anak'
				else: return 'Kesehatan Gigi dan Mulut Anak'
			elif obj[0] == 'Laki-laki':
				return 'Kesehatan Gigi dan Mulut Anak'
			else: return 'Kesehatan Gigi dan Mulut Anak'
		else: return 'Kesehatan Gigi dan Mulut Anak'
	elif obj[2] == 'HAMIL':
		return 'Kebidanan dan Kandungan'
	elif obj[2] == 'GATAL':
		# {"feature": "usia", "instances": 25, "metric_value": 1.3215, "depth": 2}
		if obj[1] == 'dewasa':
			# {"feature": "jk", "instances": 17, "metric_value": 0.952, "depth": 3}
			if obj[0] == 'Perempuan':
				# {"feature": "keluhan_2", "instances": 10, "metric_value": 0.9219, "depth": 4}
				if obj[3] == 'TIDAK ADA':
					# {"feature": "keluhan_3", "instances": 10, "metric_value": 0.9219, "depth": 5}
					if obj[4] == 'TIDAK ADA':
						return 'Kulit dan Kelamin'
					else: return 'Kulit dan Kelamin'
				else: return 'Kulit dan Kelamin'
			elif obj[0] == 'Laki-laki':
				# {"feature": "keluhan_2", "instances": 7, "metric_value": 0.5917, "depth": 4}
				if obj[3] == 'TIDAK ADA':
					# {"feature": "keluhan_3", "instances": 7, "metric_value": 0.5917, "depth": 5}
					if obj[4] == 'TIDAK ADA':
						return 'Kulit dan Kelamin'
					else: return 'Kulit dan Kelamin'
				else: return 'Kulit dan Kelamin'
			else: return 'Kulit dan Kelamin'
		elif obj[1] == 'anak':
			# {"feature": "jk", "instances": 8, "metric_value": 1.0, "depth": 3}
			if obj[0] == 'Laki-laki':
				# {"feature": "keluhan_2", "instances": 4, "metric_value": 1.0, "depth": 4}
				if obj[3] == 'TIDAK ADA':
					# {"feature": "keluhan_3", "instances": 4, "metric_value": 1.0, "depth": 5}
					if obj[4] == 'TIDAK ADA':
						return 'Kesehatan Anak'
					else: return 'Kesehatan Anak'
				else: return 'Kesehatan Anak'
			elif obj[0] == 'Perempuan':
				# {"feature": "keluhan_2", "instances": 4, "metric_value": 1.0, "depth": 4}
				if obj[3] == 'TIDAK ADA':
					# {"feature": "keluhan_3", "instances": 4, "metric_value": 1.0, "depth": 5}
					if obj[4] == 'TIDAK ADA':
						return 'Kesehatan Anak'
					else: return 'Kesehatan Anak'
				else: return 'Kesehatan Anak'
			else: return 'Kesehatan Anak'
		else: return 'Kesehatan Anak'
	elif obj[2] == 'KONSULTASI KEBIDANAN & KANDUNGAN':
		return 'Kebidanan dan Kandungan'
	elif obj[2] == 'TAMBAL GIGI':
		# {"feature": "usia", "instances": 24, "metric_value": 0.7383, "depth": 2}
		if obj[1] == 'dewasa':
			return 'Gigi dan Mulut'
		elif obj[1] == 'anak':
			# {"feature": "jk", "instances": 6, "metric_value": 0.65, "depth": 3}
			if obj[0] == 'Laki-laki':
				return 'Kesehatan Gigi dan Mulut Anak'
			elif obj[0] == 'Perempuan':
				# {"feature": "keluhan_2", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[3] == 'TIDAK ADA':
					# {"feature": "keluhan_3", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[4] == 'TIDAK ADA':
						return 'Kesehatan Gigi dan Mulut Anak'
					else: return 'Kesehatan Gigi dan Mulut Anak'
				else: return 'Kesehatan Gigi dan Mulut Anak'
			else: return 'Kesehatan Gigi dan Mulut Anak'
		else: return 'Kesehatan Gigi dan Mulut Anak'
	elif obj[2] == 'MUAL':
		# {"feature": "usia", "instances": 24, "metric_value": 0.4138, "depth": 2}
		if obj[1] == 'anak':
			return 'Kesehatan Anak'
		elif obj[1] == 'dewasa':
			return 'Penyakit Dalam'
		else: return 'Penyakit Dalam'
	elif obj[2] == 'MUNTAH':
		# {"feature": "usia", "instances": 22, "metric_value": 0.2668, "depth": 2}
		if obj[1] == 'anak':
			return 'Kesehatan Anak'
		elif obj[1] == 'dewasa':
			return 'Penyakit Dalam'
		else: return 'Penyakit Dalam'
	elif obj[2] == 'PUSING':
		# {"feature": "keluhan_2", "instances": 22, "metric_value": 2.4697, "depth": 2}
		if obj[3] == 'TIDAK ADA':
			# {"feature": "usia", "instances": 14, "metric_value": 2.156, "depth": 3}
			if obj[1] == 'dewasa':
				# {"feature": "jk", "instances": 10, "metric_value": 1.4855, "depth": 4}
				if obj[0] == 'Perempuan':
					# {"feature": "keluhan_3", "instances": 8, "metric_value": 1.5, "depth": 5}
					if obj[4] == 'TIDAK ADA':
						return 'Syaraf'
					else: return 'Syaraf'
				elif obj[0] == 'Laki-laki':
					# {"feature": "keluhan_3", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[4] == 'TIDAK ADA':
						return 'Penyakit Dalam'
					else: return 'Penyakit Dalam'
				else: return 'Penyakit Dalam'
			elif obj[1] == 'anak':
				# {"feature": "jk", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[0] == 'Laki-laki':
					# {"feature": "keluhan_3", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[4] == 'TIDAK ADA':
						return 'THT'
					else: return 'THT'
				elif obj[0] == 'Perempuan':
					return 'Kesehatan Anak'
				else: return 'Kesehatan Anak'
			else: return 'Kesehatan Anak'
		elif obj[3] == 'BURAM':
			return 'Mata'
		elif obj[3] == 'SEDANG HAMIL':
			return 'Kebidanan dan Kandungan'
		elif obj[3] == 'PILEK':
			return 'Kesehatan Anak'
		elif obj[3] == 'BINTIK DI KULIT':
			return 'Kesehatan Anak'
		elif obj[3] == 'DADA NYERI':
			return 'Kardiologi atau Jantung'
		elif obj[3] == 'DEMAM':
			return 'Penyakit Dalam'
		elif obj[3] == 'WAJAH KAKU ':
			return 'Syaraf'
		elif obj[3] == 'MUAL':
			return 'Kesehatan Anak'
		else: return 'Kesehatan Anak'
	elif obj[2] == 'BENJOLAN':
		# {"feature": "keluhan_2", "instances": 21, "metric_value": 1.7588, "depth": 2}
		if obj[3] == 'TIDAK ADA':
			# {"feature": "usia", "instances": 5, "metric_value": 1.9219, "depth": 3}
			if obj[1] == 'dewasa':
				# {"feature": "jk", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[0] == 'Perempuan':
					# {"feature": "keluhan_3", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[4] == 'TIDAK ADA':
						return 'Kulit dan Kelamin'
					else: return 'Kulit dan Kelamin'
				elif obj[0] == 'Laki-laki':
					return 'Bedah'
				else: return 'Bedah'
			elif obj[1] == 'anak':
				# {"feature": "jk", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[0] == 'Laki-laki':
					# {"feature": "keluhan_3", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[4] == 'TIDAK ADA':
						return 'Sub Spesialis Bedah Anak'
					else: return 'Sub Spesialis Bedah Anak'
				else: return 'Sub Spesialis Bedah Anak'
			else: return 'Sub Spesialis Bedah Anak'
		elif obj[3] == 'PAYUDARA':
			return 'Bedah'
		elif obj[3] == 'TANGAN':
			return 'Bedah'
		elif obj[3] == 'BAHU':
			# {"feature": "jk", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[0] == 'Perempuan':
				# {"feature": "usia", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[1] == 'dewasa':
					# {"feature": "keluhan_3", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[4] == 'TIDAK ADA':
						return 'Penyakit Dalam'
					else: return 'Penyakit Dalam'
				else: return 'Penyakit Dalam'
			else: return 'Penyakit Dalam'
		elif obj[3] == 'KEPALA':
			return 'Kesehatan Anak'
		elif obj[3] == 'GUSI':
			return 'Bedah Mulut'
		elif obj[3] == 'PUNGGUNG':
			return 'Bedah'
		elif obj[3] == 'BENGKAK':
			return 'Bedah Syaraf'
		elif obj[3] == 'KAKI':
			return 'Bedah'
		elif obj[3] == 'KELENJAR':
			return 'Bedah'
		elif obj[3] == 'PINGGANG':
			return 'Bedah'
		elif obj[3] == 'PINGGUL':
			return 'Bedah'
		else: return 'Bedah'
	elif obj[2] == 'SAKIT PERUT':
		# {"feature": "usia", "instances": 20, "metric_value": 0.2864, "depth": 2}
		if obj[1] == 'anak':
			return 'Kesehatan Anak'
		elif obj[1] == 'dewasa':
			return 'Kebidanan dan Kandungan'
		else: return 'Kebidanan dan Kandungan'
	elif obj[2] == 'CABUT GIGI':
		# {"feature": "usia", "instances": 20, "metric_value": 1.5589, "depth": 2}
		if obj[1] == 'dewasa':
			# {"feature": "jk", "instances": 11, "metric_value": 0.9457, "depth": 3}
			if obj[0] == 'Perempuan':
				# {"feature": "keluhan_2", "instances": 10, "metric_value": 0.8813, "depth": 4}
				if obj[3] == 'TIDAK ADA':
					# {"feature": "keluhan_3", "instances": 10, "metric_value": 0.8813, "depth": 5}
					if obj[4] == 'TIDAK ADA':
						return 'Bedah Mulut'
					else: return 'Bedah Mulut'
				else: return 'Bedah Mulut'
			elif obj[0] == 'Laki-laki':
				return 'Gigi dan Mulut'
			else: return 'Gigi dan Mulut'
		elif obj[1] == 'anak':
			# {"feature": "jk", "instances": 9, "metric_value": 1.3516, "depth": 3}
			if obj[0] == 'Laki-laki':
				# {"feature": "keluhan_2", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[3] == 'TIDAK ADA':
					# {"feature": "keluhan_3", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[4] == 'TIDAK ADA':
						return 'Kesehatan Gigi dan Mulut Anak'
					else: return 'Kesehatan Gigi dan Mulut Anak'
				else: return 'Kesehatan Gigi dan Mulut Anak'
			elif obj[0] == 'Perempuan':
				# {"feature": "keluhan_2", "instances": 4, "metric_value": 1.5, "depth": 4}
				if obj[3] == 'TIDAK ADA':
					# {"feature": "keluhan_3", "instances": 4, "metric_value": 1.5, "depth": 5}
					if obj[4] == 'TIDAK ADA':
						return 'Gigi dan Mulut'
					else: return 'Gigi dan Mulut'
				else: return 'Gigi dan Mulut'
			else: return 'Gigi dan Mulut'
		else: return 'Kesehatan Gigi dan Mulut Anak'
	elif obj[2] == 'SESAK':
		# {"feature": "usia", "instances": 19, "metric_value": 1.8968, "depth": 2}
		if obj[1] == 'dewasa':
			# {"feature": "keluhan_2", "instances": 13, "metric_value": 1.4573, "depth": 3}
			if obj[3] == 'TIDAK ADA':
				# {"feature": "jk", "instances": 7, "metric_value": 0.8631, "depth": 4}
				if obj[0] == 'Perempuan':
					# {"feature": "keluhan_3", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[4] == 'TIDAK ADA':
						return 'Kardiologi atau Jantung'
					else: return 'Kardiologi atau Jantung'
				elif obj[0] == 'Laki-laki':
					return 'Kardiologi atau Jantung'
				else: return 'Kardiologi atau Jantung'
			elif obj[3] == 'PUSING':
				# {"feature": "jk", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[0] == 'Laki-laki':
					return 'Paru-paru'
				elif obj[0] == 'Perempuan':
					return 'Kardiologi atau Jantung'
				else: return 'Kardiologi atau Jantung'
			elif obj[3] == 'PUNGGUNG':
				return 'Penyakit Dalam'
			elif obj[3] == 'BATUK':
				return 'Penyakit Dalam'
			elif obj[3] == 'FLU':
				return 'Penyakit Dalam'
			elif obj[3] == 'MUAL':
				return 'Kardiologi atau Jantung'
			else: return 'Kardiologi atau Jantung'
		elif obj[1] == 'anak':
			return 'Kesehatan Anak'
		else: return 'Kesehatan Anak'
	elif obj[2] == 'ALERGI':
		# {"feature": "usia", "instances": 19, "metric_value": 1.2364, "depth": 2}
		if obj[1] == 'anak':
			# {"feature": "jk", "instances": 14, "metric_value": 0.8631, "depth": 3}
			if obj[0] == 'Laki-laki':
				return 'Kesehatan Anak'
			elif obj[0] == 'Perempuan':
				# {"feature": "keluhan_2", "instances": 7, "metric_value": 0.9852, "depth": 4}
				if obj[3] == 'TIDAK ADA':
					# {"feature": "keluhan_3", "instances": 7, "metric_value": 0.9852, "depth": 5}
					if obj[4] == 'TIDAK ADA':
						return 'Kulit dan Kelamin'
					else: return 'Kulit dan Kelamin'
				else: return 'Kulit dan Kelamin'
			else: return 'Kulit dan Kelamin'
		elif obj[1] == 'dewasa':
			# {"feature": "keluhan_2", "instances": 5, "metric_value": 0.7219, "depth": 3}
			if obj[3] == 'TIDAK ADA':
				return 'Kulit dan Kelamin'
			elif obj[3] == 'HIDUNG TERSUMBAT':
				return 'THT'
			else: return 'THT'
		else: return 'Kulit dan Kelamin'
	elif obj[2] == 'KONSULTASI KESEHATAN':
		return 'Kesehatan Anak'
	elif obj[2] == 'KONSUL KESEHATAN':
		return 'Kesehatan Anak'
	elif obj[2] == 'BATUK ':
		# {"feature": "usia", "instances": 17, "metric_value": 1.4021, "depth": 2}
		if obj[1] == 'dewasa':
			# {"feature": "keluhan_2", "instances": 10, "metric_value": 0.7219, "depth": 3}
			if obj[3] == 'TIDAK ADA':
				# {"feature": "jk", "instances": 6, "metric_value": 0.9183, "depth": 4}
				if obj[0] == 'Laki-laki':
					# {"feature": "keluhan_3", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[4] == 'TIDAK ADA':
						return 'Penyakit Dalam'
					else: return 'Penyakit Dalam'
				elif obj[0] == 'Perempuan':
					# {"feature": "keluhan_3", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[4] == 'TIDAK ADA':
						return 'Paru-paru'
					else: return 'Paru-paru'
				else: return 'Paru-paru'
			elif obj[3] == 'BADAN SAKIT':
				return 'Penyakit Dalam'
			elif obj[3] == 'DEMAM':
				return 'Penyakit Dalam'
			elif obj[3] == 'PILEK':
				return 'Penyakit Dalam'
			elif obj[3] == 'SESAK NAFAS':
				return 'Penyakit Dalam'
			else: return 'Penyakit Dalam'
		elif obj[1] == 'anak':
			return 'Kesehatan Anak'
		else: return 'Kesehatan Anak'
	elif obj[2] == 'PILEK':
		# {"feature": "usia", "instances": 16, "metric_value": 0.8113, "depth": 2}
		if obj[1] == 'anak':
			return 'Kesehatan Anak'
		elif obj[1] == 'dewasa':
			return 'THT'
		else: return 'THT'
	elif obj[2] == 'SAKIT MATA':
		# {"feature": "usia", "instances": 15, "metric_value": 0.971, "depth": 2}
		if obj[1] == 'anak':
			# {"feature": "keluhan_2", "instances": 11, "metric_value": 0.684, "depth": 3}
			if obj[3] == 'TIDAK ADA':
				# {"feature": "jk", "instances": 8, "metric_value": 0.8113, "depth": 4}
				if obj[0] == 'Laki-laki':
					# {"feature": "keluhan_3", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[4] == 'TIDAK ADA':
						return 'Kesehatan Anak'
					else: return 'Kesehatan Anak'
				elif obj[0] == 'Perempuan':
					# {"feature": "keluhan_3", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[4] == 'TIDAK ADA':
						return 'Kesehatan Anak'
					else: return 'Kesehatan Anak'
				else: return 'Kesehatan Anak'
			elif obj[3] == 'LEHER IRITASI':
				return 'Kesehatan Anak'
			elif obj[3] == 'DEMAM':
				return 'Kesehatan Anak'
			elif obj[3] == 'PILEK':
				return 'Kesehatan Anak'
			else: return 'Kesehatan Anak'
		elif obj[1] == 'dewasa':
			return 'Mata'
		else: return 'Mata'
	elif obj[2] == 'KONSUL KANDUNGAN':
		return 'Kebidanan dan Kandungan'
	elif obj[2] == 'GUSI BENGKAK':
		# {"feature": "usia", "instances": 15, "metric_value": 1.4716, "depth": 2}
		if obj[1] == 'dewasa':
			# {"feature": "jk", "instances": 8, "metric_value": 0.5436, "depth": 3}
			if obj[0] == 'Perempuan':
				# {"feature": "keluhan_2", "instances": 6, "metric_value": 0.65, "depth": 4}
				if obj[3] == 'TIDAK ADA':
					# {"feature": "keluhan_3", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[4] == 'TIDAK ADA':
						return 'Gigi dan Mulut'
					else: return 'Gigi dan Mulut'
				else: return 'Gigi dan Mulut'
			elif obj[0] == 'Laki-laki':
				return 'Gigi dan Mulut'
			else: return 'Gigi dan Mulut'
		elif obj[1] == 'anak':
			# {"feature": "jk", "instances": 7, "metric_value": 1.3788, "depth": 3}
			if obj[0] == 'Perempuan':
				# {"feature": "keluhan_2", "instances": 6, "metric_value": 1.2516, "depth": 4}
				if obj[3] == 'TIDAK ADA':
					# {"feature": "keluhan_3", "instances": 5, "metric_value": 1.371, "depth": 5}
					if obj[4] == 'TIDAK ADA':
						return 'Kesehatan Gigi dan Mulut Anak'
					else: return 'Kesehatan Gigi dan Mulut Anak'
				elif obj[3] == 'TAMBAL GIGI':
					return 'Kesehatan Gigi dan Mulut Anak'
				else: return 'Kesehatan Gigi dan Mulut Anak'
			elif obj[0] == 'Laki-laki':
				return 'Gigi dan Mulut'
			else: return 'Gigi dan Mulut'
		else: return 'Kesehatan Gigi dan Mulut Anak'
	elif obj[2] == 'RADANG':
		# {"feature": "usia", "instances": 15, "metric_value": 0.9056, "depth": 2}
		if obj[1] == 'anak':
			return 'Kesehatan Anak'
		elif obj[1] == 'dewasa':
			# {"feature": "keluhan_2", "instances": 3, "metric_value": 0.9183, "depth": 3}
			if obj[3] == 'TIDAK ADA':
				return 'THT'
			elif obj[3] == 'PUSING':
				return 'Penyakit Dalam'
			elif obj[3] == 'DEMAM':
				return 'THT'
			else: return 'THT'
		else: return 'THT'
	elif obj[2] == 'FLU':
		# {"feature": "usia", "instances": 15, "metric_value": 1.3753, "depth": 2}
		if obj[1] == 'anak':
			# {"feature": "keluhan_2", "instances": 11, "metric_value": 0.4395, "depth": 3}
			if obj[3] == 'TIDAK ADA':
				# {"feature": "jk", "instances": 8, "metric_value": 0.5436, "depth": 4}
				if obj[0] == 'Perempuan':
					# {"feature": "keluhan_3", "instances": 7, "metric_value": 0.5917, "depth": 5}
					if obj[4] == 'TIDAK ADA':
						return 'Kesehatan Anak'
					else: return 'Kesehatan Anak'
				elif obj[0] == 'Laki-laki':
					return 'Kesehatan Anak'
				else: return 'Kesehatan Anak'
			elif obj[3] == 'BATUK':
				return 'Kesehatan Anak'
			elif obj[3] == 'DEMAM':
				return 'Kesehatan Anak'
			else: return 'Kesehatan Anak'
		elif obj[1] == 'dewasa':
			# {"feature": "keluhan_2", "instances": 4, "metric_value": 0.8113, "depth": 3}
			if obj[3] == 'TIDAK ADA':
				# {"feature": "jk", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[0] == 'Perempuan':
					# {"feature": "keluhan_3", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[4] == 'TIDAK ADA':
						return 'Penyakit Dalam'
					else: return 'Penyakit Dalam'
				else: return 'Penyakit Dalam'
			elif obj[3] == 'DEMAM':
				return 'THT'
			elif obj[3] == 'TELINGA KADANG TETUTUP':
				return 'THT'
			else: return 'THT'
		else: return 'THT'
	elif obj[2] == 'DM':
		return 'Penyakit Dalam'
	elif obj[2] == 'TB':
		# {"feature": "usia", "instances": 14, "metric_value": 1.2638, "depth": 2}
		if obj[1] == 'anak':
			return 'Kesehatan Anak'
		elif obj[1] == 'dewasa':
			# {"feature": "jk", "instances": 6, "metric_value": 0.65, "depth": 3}
			if obj[0] == 'Perempuan':
				# {"feature": "keluhan_2", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[3] == 'TIDAK ADA':
					# {"feature": "keluhan_3", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[4] == 'TIDAK ADA':
						return 'Paru-paru'
					else: return 'Paru-paru'
				else: return 'Paru-paru'
			elif obj[0] == 'Laki-laki':
				return 'Paru-paru'
			else: return 'Paru-paru'
		else: return 'Paru-paru'
	elif obj[2] == 'SAKIT TELINGA':
		# {"feature": "keluhan_2", "instances": 14, "metric_value": 0.3712, "depth": 2}
		if obj[3] == 'TIDAK ADA':
			return 'THT'
		elif obj[3] == 'HIDUNG TERSUMBAT':
			return 'THT'
		elif obj[3] == 'PILEK':
			return 'THT'
		elif obj[3] == 'PUSING':
			return 'Kesehatan Anak'
		else: return 'Kesehatan Anak'
	elif obj[2] == 'KONTROL UROLOGI':
		return 'Bedah Urologi'
	elif obj[2] == 'SAKIT PINGGANG':
		# {"feature": "keluhan_2", "instances": 14, "metric_value": 2.067, "depth": 2}
		if obj[3] == 'TIDAK ADA':
			# {"feature": "jk", "instances": 12, "metric_value": 1.825, "depth": 3}
			if obj[0] == 'Perempuan':
				# {"feature": "usia", "instances": 8, "metric_value": 1.4056, "depth": 4}
				if obj[1] == 'dewasa':
					# {"feature": "keluhan_3", "instances": 8, "metric_value": 1.4056, "depth": 5}
					if obj[4] == 'TIDAK ADA':
						return 'Syaraf'
					else: return 'Syaraf'
				else: return 'Syaraf'
			elif obj[0] == 'Laki-laki':
				# {"feature": "usia", "instances": 4, "metric_value": 1.5, "depth": 4}
				if obj[1] == 'dewasa':
					# {"feature": "keluhan_3", "instances": 4, "metric_value": 1.5, "depth": 5}
					if obj[4] == 'TIDAK ADA':
						return 'Rehabilitasi Medik'
					else: return 'Rehabilitasi Medik'
				else: return 'Rehabilitasi Medik'
			else: return 'Rehabilitasi Medik'
		elif obj[3] == 'PUSING':
			return 'Kesehatan Anak'
		elif obj[3] == 'MENGGIGIL':
			return 'Penyakit Dalam'
		else: return 'Penyakit Dalam'
	elif obj[2] == 'BEDAH TUMOR':
		return 'Sub Spesialis Bedah Tumor ( Onkologi )'
	elif obj[2] == 'KONSUL':
		# {"feature": "keluhan_2", "instances": 12, "metric_value": 1.4183, "depth": 2}
		if obj[3] == 'TIDAK ADA':
			# {"feature": "usia", "instances": 9, "metric_value": 1.2244, "depth": 3}
			if obj[1] == 'anak':
				# {"feature": "jk", "instances": 8, "metric_value": 1.0613, "depth": 4}
				if obj[0] == 'Laki-laki':
					# {"feature": "keluhan_3", "instances": 6, "metric_value": 1.2516, "depth": 5}
					if obj[4] == 'TIDAK ADA':
						return 'Tumbuh Kembang Anak (REMEDIA)'
					else: return 'Tumbuh Kembang Anak (REMEDIA)'
				elif obj[0] == 'Perempuan':
					return 'Tumbuh Kembang Anak (REMEDIA)'
				else: return 'Tumbuh Kembang Anak (REMEDIA)'
			elif obj[1] == 'dewasa':
				return 'THT'
			else: return 'THT'
		elif obj[3] == 'EVALUASI':
			return 'Tumbuh Kembang Anak (REMEDIA)'
		elif obj[3] == 'TERAPI':
			return 'Tumbuh Kembang Anak (REMEDIA)'
		elif obj[3] == 'SDH AGAK ENAKAN':
			return 'Kardiologi atau Jantung'
		else: return 'Kardiologi atau Jantung'
	elif obj[2] == 'BATUK PILEK ':
		# {"feature": "usia", "instances": 11, "metric_value": 0.4395, "depth": 2}
		if obj[1] == 'anak':
			return 'Kesehatan Anak'
		elif obj[1] == 'dewasa':
			return 'THT'
		else: return 'THT'
	elif obj[2] == 'KONSUL KEBIDANAN':
		return 'Kebidanan dan Kandungan'
	elif obj[2] == 'SARIAWAN':
		# {"feature": "usia", "instances": 11, "metric_value": 0.4395, "depth": 2}
		if obj[1] == 'anak':
			return 'Kesehatan Anak'
		elif obj[1] == 'dewasa':
			return 'THT'
		else: return 'THT'
	elif obj[2] == 'CACAR':
		# {"feature": "usia", "instances": 11, "metric_value": 0.9457, "depth": 2}
		if obj[1] == 'anak':
			# {"feature": "keluhan_2", "instances": 8, "metric_value": 0.5436, "depth": 3}
			if obj[3] == 'TIDAK ADA':
				return 'Kesehatan Anak'
			elif obj[3] == 'SARIAWAN':
				return 'Kulit dan Kelamin'
			else: return 'Kulit dan Kelamin'
		elif obj[1] == 'dewasa':
			return 'Kulit dan Kelamin'
		else: return 'Kulit dan Kelamin'
	elif obj[2] == 'GIGI BERLUBANG':
		# {"feature": "usia", "instances": 11, "metric_value": 0.994, "depth": 2}
		if obj[1] == 'anak':
			# {"feature": "jk", "instances": 6, "metric_value": 0.65, "depth": 3}
			if obj[0] == 'Laki-laki':
				# {"feature": "keluhan_2", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[3] == 'TIDAK ADA':
					# {"feature": "keluhan_3", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[4] == 'TIDAK ADA':
						return 'Kesehatan Gigi dan Mulut Anak'
					else: return 'Kesehatan Gigi dan Mulut Anak'
				else: return 'Kesehatan Gigi dan Mulut Anak'
			elif obj[0] == 'Perempuan':
				return 'Kesehatan Gigi dan Mulut Anak'
			else: return 'Kesehatan Gigi dan Mulut Anak'
		elif obj[1] == 'dewasa':
			return 'Gigi dan Mulut'
		else: return 'Gigi dan Mulut'
	elif obj[2] == 'KONSUL KULIT & KELAMIN':
		return 'Kulit dan Kelamin'
	elif obj[2] == 'CEK HAMIL':
		return 'Kebidanan dan Kandungan'
	elif obj[2] == 'IMUN':
		return 'Kesehatan Anak'
	elif obj[2] == 'KONTROL REHAB':
		return 'Rehabilitasi Medik'
	elif obj[2] == 'CEK KANDUNGAN':
		return 'Kebidanan dan Kandungan'
	elif obj[2] == 'KANDUNGAN':
		return 'Kebidanan dan Kandungan'
	elif obj[2] == 'PERAWATAN GIGI DAN MULUT':
		return 'Kesehatan Gigi dan Mulut Anak'
	elif obj[2] == 'KONTROL KANDUNGAN':
		return 'Kebidanan dan Kandungan'
	elif obj[2] == 'SAKIT KEPALA':
		# {"feature": "jk", "instances": 9, "metric_value": 1.4466, "depth": 2}
		if obj[0] == 'Perempuan':
			# {"feature": "usia", "instances": 8, "metric_value": 1.0613, "depth": 3}
			if obj[1] == 'dewasa':
				# {"feature": "keluhan_2", "instances": 7, "metric_value": 0.5917, "depth": 4}
				if obj[3] == 'TIDAK ADA':
					# {"feature": "keluhan_3", "instances": 7, "metric_value": 0.5917, "depth": 5}
					if obj[4] == 'TIDAK ADA':
						return 'Syaraf'
					else: return 'Syaraf'
				else: return 'Syaraf'
			elif obj[1] == 'anak':
				return 'Kesehatan Anak'
			else: return 'Kesehatan Anak'
		elif obj[0] == 'Laki-laki':
			return 'Penyakit Dalam'
		else: return 'Penyakit Dalam'
	elif obj[2] == 'KONSULTASI KULIT & KELAMIN':
		# {"feature": "usia", "instances": 9, "metric_value": 0.9183, "depth": 2}
		if obj[1] == 'dewasa':
			# {"feature": "jk", "instances": 6, "metric_value": 1.0, "depth": 3}
			if obj[0] == 'Perempuan':
				# {"feature": "keluhan_2", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[3] == 'TIDAK ADA':
					# {"feature": "keluhan_3", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[4] == 'TIDAK ADA':
						return 'Kulit dan Kelamin'
					else: return 'Kulit dan Kelamin'
				else: return 'Kulit dan Kelamin'
			elif obj[0] == 'Laki-laki':
				# {"feature": "keluhan_2", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[3] == 'TIDAK ADA':
					# {"feature": "keluhan_3", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[4] == 'TIDAK ADA':
						return 'Kesehatan Jiwa'
					else: return 'Kesehatan Jiwa'
				else: return 'Kesehatan Jiwa'
			else: return 'Kesehatan Jiwa'
		elif obj[1] == 'anak':
			return 'Kulit dan Kelamin'
		else: return 'Kulit dan Kelamin'
	elif obj[2] == 'FLEK':
		# {"feature": "usia", "instances": 9, "metric_value": 0.9183, "depth": 2}
		if obj[1] == 'dewasa':
			return 'Kebidanan dan Kandungan'
		elif obj[1] == 'anak':
			return 'Kesehatan Anak'
		else: return 'Kesehatan Anak'
	elif obj[2] == 'GIGI':
		# {"feature": "usia", "instances": 9, "metric_value": 1.2244, "depth": 2}
		if obj[1] == 'dewasa':
			# {"feature": "jk", "instances": 6, "metric_value": 0.65, "depth": 3}
			if obj[0] == 'Perempuan':
				# {"feature": "keluhan_2", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[3] == 'TIDAK ADA':
					# {"feature": "keluhan_3", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[4] == 'TIDAK ADA':
						return 'Gigi dan Mulut'
					else: return 'Gigi dan Mulut'
				else: return 'Gigi dan Mulut'
			elif obj[0] == 'Laki-laki':
				return 'Gigi dan Mulut'
			else: return 'Gigi dan Mulut'
		elif obj[1] == 'anak':
			# {"feature": "jk", "instances": 3, "metric_value": 0.9183, "depth": 3}
			if obj[0] == 'Laki-laki':
				return 'Kesehatan Gigi dan Mulut Anak'
			elif obj[0] == 'Perempuan':
				return 'Gigi dan Mulut'
			else: return 'Gigi dan Mulut'
		else: return 'Kesehatan Gigi dan Mulut Anak'
	elif obj[2] == 'USG':
		# {"feature": "jk", "instances": 9, "metric_value": 0.5033, "depth": 2}
		if obj[0] == 'Perempuan':
			# {"feature": "usia", "instances": 9, "metric_value": 0.5033, "depth": 3}
			if obj[1] == 'dewasa':
				# {"feature": "keluhan_2", "instances": 9, "metric_value": 0.5033, "depth": 4}
				if obj[3] == 'TIDAK ADA':
					# {"feature": "keluhan_3", "instances": 9, "metric_value": 0.5033, "depth": 5}
					if obj[4] == 'TIDAK ADA':
						return 'Kebidanan dan Kandungan'
					else: return 'Kebidanan dan Kandungan'
				else: return 'Kebidanan dan Kandungan'
			else: return 'Kebidanan dan Kandungan'
		else: return 'Kebidanan dan Kandungan'
	elif obj[2] == 'GIGI BERLUBANG ':
		return 'Gigi dan Mulut'
	elif obj[2] == 'BATUK BERDAHAK':
		# {"feature": "usia", "instances": 9, "metric_value": 0.9864, "depth": 2}
		if obj[1] == 'anak':
			return 'Kesehatan Anak'
		elif obj[1] == 'dewasa':
			# {"feature": "jk", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[0] == 'Laki-laki':
				return 'THT'
			elif obj[0] == 'Perempuan':
				return 'Paru-paru'
			else: return 'Paru-paru'
		else: return 'THT'
	elif obj[2] == 'JERAWAT':
		return 'Kulit dan Kelamin'
	elif obj[2] == 'KONSUL REHAB':
		return 'Rehabilitasi Medik'
	elif obj[2] == 'GATAL GATAL ':
		return 'Kulit dan Kelamin'
	elif obj[2] == 'PILEK ':
		# {"feature": "usia", "instances": 8, "metric_value": 0.5436, "depth": 2}
		if obj[1] == 'anak':
			return 'Kesehatan Anak'
		elif obj[1] == 'dewasa':
			return 'THT'
		else: return 'THT'
	elif obj[2] == 'MUNTAH MUNTAH':
		return 'Kesehatan Anak'
	elif obj[2] == 'SESAK NAFAS':
		# {"feature": "keluhan_2", "instances": 8, "metric_value": 2.25, "depth": 2}
		if obj[3] == 'TIDAK ADA':
			# {"feature": "jk", "instances": 5, "metric_value": 1.9219, "depth": 3}
			if obj[0] == 'Perempuan':
				# {"feature": "usia", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[1] == 'anak':
					return 'Kesehatan Anak'
				elif obj[1] == 'dewasa':
					return 'Kebidanan dan Kandungan'
				else: return 'Kebidanan dan Kandungan'
			elif obj[0] == 'Laki-laki':
				# {"feature": "usia", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[1] == 'dewasa':
					# {"feature": "keluhan_3", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[4] == 'TIDAK ADA':
						return 'Penyakit Dalam'
					else: return 'Penyakit Dalam'
				else: return 'Penyakit Dalam'
			else: return 'Penyakit Dalam'
		elif obj[3] == 'ASMA':
			return 'Paru-paru'
		elif obj[3] == 'GAMPANG CAPEK':
			return 'Kardiologi atau Jantung'
		elif obj[3] == 'SAKIT DADA':
			return 'Penyakit Dalam'
		else: return 'Penyakit Dalam'
	elif obj[2] == 'IMUNISASI ':
		return 'Kesehatan Anak'
	elif obj[2] == 'LUKA':
		# {"feature": "keluhan_2", "instances": 7, "metric_value": 1.5567, "depth": 2}
		if obj[3] == 'TIDAK ADA':
			# {"feature": "usia", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[1] == 'anak':
				return 'Kulit dan Kelamin'
			elif obj[1] == 'dewasa':
				return 'Bedah'
			else: return 'Bedah'
		elif obj[3] == 'DADA':
			return 'Kulit dan Kelamin'
		elif obj[3] == 'HIDUNG':
			return 'Kesehatan Anak'
		elif obj[3] == 'MUKA':
			return 'Kesehatan Anak'
		elif obj[3] == 'KETIAK':
			return 'Kulit dan Kelamin'
		elif obj[3] == 'SUNAT':
			return 'Bedah'
		else: return 'Bedah'
	elif obj[2] == 'MATA BERAIR':
		# {"feature": "usia", "instances": 7, "metric_value": 0.9852, "depth": 2}
		if obj[1] == 'dewasa':
			return 'Mata'
		elif obj[1] == 'anak':
			return 'Kesehatan Anak'
		else: return 'Kesehatan Anak'
	elif obj[2] == 'SAKIT TENGGOROKAN':
		# {"feature": "usia", "instances": 7, "metric_value": 0.8631, "depth": 2}
		if obj[1] == 'dewasa':
			return 'THT'
		elif obj[1] == 'anak':
			return 'Kesehatan Anak'
		else: return 'Kesehatan Anak'
	elif obj[2] == 'KB':
		return 'Kebidanan dan Kandungan'
	elif obj[2] == 'NYERI KAKI':
		# {"feature": "keluhan_2", "instances": 7, "metric_value": 1.3788, "depth": 2}
		if obj[3] == 'TIDAK ADA':
			# {"feature": "jk", "instances": 5, "metric_value": 0.7219, "depth": 3}
			if obj[0] == 'Perempuan':
				# {"feature": "usia", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[1] == 'dewasa':
					# {"feature": "keluhan_3", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[4] == 'TIDAK ADA':
						return 'Syaraf'
					else: return 'Syaraf'
				else: return 'Syaraf'
			elif obj[0] == 'Laki-laki':
				return 'Syaraf'
			else: return 'Syaraf'
		elif obj[3] == 'ROBEKAN DI LUTUT':
			return 'Bedah Tulang atau Orthopedi'
		elif obj[3] == 'MATA PENGLIHATAN KABUR':
			return 'Kardiologi atau Jantung'
		else: return 'Kardiologi atau Jantung'
	elif obj[2] == 'KEHAMILAN':
		return 'Kebidanan dan Kandungan'
	elif obj[2] == 'MATA MERAH':
		# {"feature": "jk", "instances": 7, "metric_value": 0.5917, "depth": 2}
		if obj[0] == 'Laki-laki':
			return 'Mata'
		elif obj[0] == 'Perempuan':
			# {"feature": "usia", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[1] == 'dewasa':
				return 'Mata'
			elif obj[1] == 'anak':
				return 'Kesehatan Anak'
			else: return 'Kesehatan Anak'
		else: return 'Mata'
	elif obj[2] == 'NYERI PERUT':
		# {"feature": "usia", "instances": 7, "metric_value": 1.3788, "depth": 2}
		if obj[1] == 'dewasa':
			# {"feature": "jk", "instances": 5, "metric_value": 0.7219, "depth": 3}
			if obj[0] == 'Laki-laki':
				return 'Penyakit Dalam'
			elif obj[0] == 'Perempuan':
				# {"feature": "keluhan_2", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[3] == 'TIDAK ADA':
					# {"feature": "keluhan_3", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[4] == 'TIDAK ADA':
						return 'Penyakit Dalam'
					else: return 'Penyakit Dalam'
				else: return 'Penyakit Dalam'
			else: return 'Penyakit Dalam'
		elif obj[1] == 'anak':
			return 'Kesehatan Anak'
		else: return 'Kesehatan Anak'
	elif obj[2] == 'LUTUT SAKIT':
		# {"feature": "jk", "instances": 7, "metric_value": 1.8424, "depth": 2}
		if obj[0] == 'Laki-laki':
			# {"feature": "usia", "instances": 4, "metric_value": 2.0, "depth": 3}
			if obj[1] == 'dewasa':
				# {"feature": "keluhan_2", "instances": 4, "metric_value": 2.0, "depth": 4}
				if obj[3] == 'TIDAK ADA':
					# {"feature": "keluhan_3", "instances": 4, "metric_value": 2.0, "depth": 5}
					if obj[4] == 'TIDAK ADA':
						return 'Syaraf'
					else: return 'Syaraf'
				else: return 'Syaraf'
			else: return 'Syaraf'
		elif obj[0] == 'Perempuan':
			# {"feature": "usia", "instances": 3, "metric_value": 0.9183, "depth": 3}
			if obj[1] == 'dewasa':
				# {"feature": "keluhan_2", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[3] == 'TIDAK ADA':
					# {"feature": "keluhan_3", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[4] == 'TIDAK ADA':
						return 'Penyakit Dalam'
					else: return 'Penyakit Dalam'
				else: return 'Penyakit Dalam'
			else: return 'Penyakit Dalam'
		else: return 'Penyakit Dalam'
	elif obj[2] == 'BAPIL ':
		return 'Kesehatan Anak'
	elif obj[2] == 'KONSULTASI':
		# {"feature": "usia", "instances": 7, "metric_value": 1.6645, "depth": 2}
		if obj[1] == 'anak':
			# {"feature": "jk", "instances": 5, "metric_value": 0.7219, "depth": 3}
			if obj[0] == 'Laki-laki':
				return 'Tumbuh Kembang Anak (REMEDIA)'
			elif obj[0] == 'Perempuan':
				# {"feature": "keluhan_2", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[3] == 'TIDAK ADA':
					# {"feature": "keluhan_3", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[4] == 'TIDAK ADA':
						return 'THT'
					else: return 'THT'
				else: return 'THT'
			else: return 'THT'
		elif obj[1] == 'dewasa':
			# {"feature": "jk", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[0] == 'Laki-laki':
				return 'Rehabilitasi Medik'
			elif obj[0] == 'Perempuan':
				return 'Sub Spesialis Bedah Tumor ( Onkologi )'
			else: return 'Sub Spesialis Bedah Tumor ( Onkologi )'
		else: return 'Rehabilitasi Medik'
	elif obj[2] == 'PANAS ':
		return 'Kesehatan Anak'
	elif obj[2] == 'KEPUTIHAN':
		# {"feature": "keluhan_2", "instances": 6, "metric_value": 0.9183, "depth": 2}
		if obj[3] == 'TIDAK ADA':
			# {"feature": "jk", "instances": 5, "metric_value": 0.971, "depth": 3}
			if obj[0] == 'Perempuan':
				# {"feature": "usia", "instances": 5, "metric_value": 0.971, "depth": 4}
				if obj[1] == 'dewasa':
					# {"feature": "keluhan_3", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[4] == 'TIDAK ADA':
						return 'Kebidanan dan Kandungan'
					else: return 'Kebidanan dan Kandungan'
				else: return 'Kebidanan dan Kandungan'
			else: return 'Kebidanan dan Kandungan'
		elif obj[3] == 'KONSUL LANJUTAN':
			return 'Kebidanan dan Kandungan'
		else: return 'Kebidanan dan Kandungan'
	elif obj[2] == 'PERIKSA MATA':
		return 'Mata'
	elif obj[2] == 'KONTROL GIGI':
		# {"feature": "usia", "instances": 6, "metric_value": 0.9183, "depth": 2}
		if obj[1] == 'dewasa':
			# {"feature": "jk", "instances": 5, "metric_value": 0.7219, "depth": 3}
			if obj[0] == 'Perempuan':
				# {"feature": "keluhan_2", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[3] == 'TIDAK ADA':
					# {"feature": "keluhan_3", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[4] == 'TIDAK ADA':
						return 'Gigi dan Mulut'
					else: return 'Gigi dan Mulut'
				else: return 'Gigi dan Mulut'
			elif obj[0] == 'Laki-laki':
				return 'Gigi dan Mulut'
			else: return 'Gigi dan Mulut'
		elif obj[1] == 'anak':
			return 'Gigi Spesialis Ortodonti'
		else: return 'Gigi Spesialis Ortodonti'
	elif obj[2] == 'KONTROL KAWAT GIGI':
		return 'Gigi Spesialis Ortodonti'
	elif obj[2] == 'TELINGA':
		return 'THT'
	elif obj[2] == 'PERAWATAN GIGI':
		# {"feature": "jk", "instances": 6, "metric_value": 0.65, "depth": 2}
		if obj[0] == 'Laki-laki':
			return 'Gigi dan Mulut'
		elif obj[0] == 'Perempuan':
			# {"feature": "usia", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[1] == 'anak':
				return 'Kesehatan Gigi dan Mulut Anak'
			elif obj[1] == 'dewasa':
				return 'Gigi dan Mulut'
			else: return 'Gigi dan Mulut'
		else: return 'Kesehatan Gigi dan Mulut Anak'
	elif obj[2] == 'TELINGA SAKIT':
		return 'THT'
	elif obj[2] == 'NYERI PINGGANG':
		# {"feature": "keluhan_2", "instances": 6, "metric_value": 0.65, "depth": 2}
		if obj[3] == 'TIDAK ADA':
			return 'Syaraf'
		elif obj[3] == 'KAKI SAKIT':
			return 'Penyakit Dalam'
		elif obj[3] == 'SARAF KEJEPIT':
			return 'Syaraf'
		else: return 'Syaraf'
	elif obj[2] == 'ASMA':
		# {"feature": "keluhan_2", "instances": 6, "metric_value": 1.4591, "depth": 2}
		if obj[3] == 'TIDAK ADA':
			# {"feature": "jk", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[0] == 'Perempuan':
				return 'Penyakit Dalam'
			elif obj[0] == 'Laki-laki':
				return 'Kesehatan Anak'
			else: return 'Kesehatan Anak'
		elif obj[3] == 'SESAK':
			return 'Paru-paru'
		elif obj[3] == 'BATUK':
			return 'Kesehatan Anak'
		elif obj[3] == 'BATUK KERING':
			return 'Paru-paru'
		else: return 'Paru-paru'
	elif obj[2] == 'SAKIT KAKI':
		# {"feature": "jk", "instances": 6, "metric_value": 1.7925, "depth": 2}
		if obj[0] == 'Perempuan':
			# {"feature": "usia", "instances": 5, "metric_value": 1.371, "depth": 3}
			if obj[1] == 'dewasa':
				# {"feature": "keluhan_2", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[3] == 'TIDAK ADA':
					# {"feature": "keluhan_3", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[4] == 'TIDAK ADA':
						return 'Bedah Tulang atau Orthopedi'
					else: return 'Bedah Tulang atau Orthopedi'
				else: return 'Bedah Tulang atau Orthopedi'
			elif obj[1] == 'anak':
				return 'Syaraf'
			else: return 'Syaraf'
		elif obj[0] == 'Laki-laki':
			return 'Penyakit Dalam'
		else: return 'Penyakit Dalam'
	elif obj[2] == 'MATA ':
		return 'Mata'
	elif obj[2] == 'MANTOUX':
		return 'Kesehatan Anak'
	elif obj[2] == 'RADANG TENGGOROKAN':
		# {"feature": "usia", "instances": 6, "metric_value": 0.9183, "depth": 2}
		if obj[1] == 'dewasa':
			return 'THT'
		elif obj[1] == 'anak':
			return 'Kesehatan Anak'
		else: return 'Kesehatan Anak'
	elif obj[2] == 'KAKI SAKIT':
		# {"feature": "keluhan_2", "instances": 6, "metric_value": 1.0, "depth": 2}
		if obj[3] == 'TIDAK ADA':
			# {"feature": "jk", "instances": 4, "metric_value": 1.0, "depth": 3}
			if obj[0] == 'Perempuan':
				# {"feature": "usia", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[1] == 'dewasa':
					# {"feature": "keluhan_3", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[4] == 'TIDAK ADA':
						return 'Syaraf'
					else: return 'Syaraf'
				else: return 'Syaraf'
			elif obj[0] == 'Laki-laki':
				return 'Penyakit Dalam'
			else: return 'Penyakit Dalam'
		elif obj[3] == 'NGILU':
			return 'Syaraf'
		elif obj[3] == 'MUAL':
			return 'Penyakit Dalam'
		else: return 'Penyakit Dalam'
	elif obj[2] == 'KAKI BENGKAK':
		# {"feature": "jk", "instances": 6, "metric_value": 1.7925, "depth": 2}
		if obj[0] == 'Laki-laki':
			# {"feature": "usia", "instances": 5, "metric_value": 1.371, "depth": 3}
			if obj[1] == 'dewasa':
				# {"feature": "keluhan_2", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[3] == 'TIDAK ADA':
					# {"feature": "keluhan_3", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[4] == 'TIDAK ADA':
						return 'Penyakit Dalam'
					else: return 'Penyakit Dalam'
				else: return 'Penyakit Dalam'
			elif obj[1] == 'anak':
				return 'Kesehatan Anak'
			else: return 'Kesehatan Anak'
		elif obj[0] == 'Perempuan':
			return 'Kardiologi atau Jantung'
		else: return 'Kardiologi atau Jantung'
	elif obj[2] == 'KONSUL GIGI':
		return 'Gigi dan Mulut'
	elif obj[2] == 'SINUS':
		return 'THT'
	elif obj[2] == 'BEHEL':
		return 'Gigi Spesialis Ortodonti'
	elif obj[2] == 'KEHAMILAN ':
		return 'Kebidanan dan Kandungan'
	elif obj[2] == 'HAID':
		return 'Kebidanan dan Kandungan'
	elif obj[2] == 'GIGI PATAH':
		# {"feature": "usia", "instances": 5, "metric_value": 0.971, "depth": 2}
		if obj[1] == 'dewasa':
			return 'Gigi dan Mulut'
		elif obj[1] == 'anak':
			return 'Kesehatan Gigi dan Mulut Anak'
		else: return 'Kesehatan Gigi dan Mulut Anak'
	elif obj[2] == 'NYERI DADA':
		# {"feature": "jk", "instances": 5, "metric_value": 0.7219, "depth": 2}
		if obj[0] == 'Perempuan':
			return 'Kardiologi atau Jantung'
		elif obj[0] == 'Laki-laki':
			# {"feature": "usia", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[1] == 'dewasa':
				# {"feature": "keluhan_2", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[3] == 'TIDAK ADA':
					# {"feature": "keluhan_3", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[4] == 'TIDAK ADA':
						return 'Kardiologi atau Jantung'
					else: return 'Kardiologi atau Jantung'
				else: return 'Kardiologi atau Jantung'
			else: return 'Kardiologi atau Jantung'
		else: return 'Kardiologi atau Jantung'
	elif obj[2] == 'PROSTAT':
		# {"feature": "jk", "instances": 5, "metric_value": 0.7219, "depth": 2}
		if obj[0] == 'Laki-laki':
			# {"feature": "usia", "instances": 5, "metric_value": 0.7219, "depth": 3}
			if obj[1] == 'dewasa':
				# {"feature": "keluhan_2", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[3] == 'TIDAK ADA':
					# {"feature": "keluhan_3", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[4] == 'TIDAK ADA':
						return 'Bedah Urologi'
					else: return 'Bedah Urologi'
				else: return 'Bedah Urologi'
			else: return 'Bedah Urologi'
		else: return 'Bedah Urologi'
	elif obj[2] == 'CEK MATA':
		return 'Mata'
	elif obj[2] == 'ALERGI ':
		# {"feature": "keluhan_2", "instances": 5, "metric_value": 0.971, "depth": 2}
		if obj[3] == 'TIDAK ADA':
			return 'Kesehatan Anak'
		elif obj[3] == 'BATUK':
			return 'Kesehatan Anak'
		elif obj[3] == 'WAJAH':
			return 'Kulit dan Kelamin'
		elif obj[3] == 'KULIT':
			return 'Kulit dan Kelamin'
		elif obj[3] == 'GATAL KULIT':
			return 'Kesehatan Anak'
		else: return 'Kesehatan Anak'
	elif obj[2] == 'PERUT SAKIT':
		# {"feature": "usia", "instances": 5, "metric_value": 1.371, "depth": 2}
		if obj[1] == 'anak':
			return 'Kesehatan Anak'
		elif obj[1] == 'dewasa':
			# {"feature": "keluhan_2", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[3] == 'TIDAK ADA':
				return 'Kebidanan dan Kandungan'
			elif obj[3] == 'DADA SAKIT ':
				return 'Penyakit Dalam'
			else: return 'Penyakit Dalam'
		else: return 'Kebidanan dan Kandungan'
	elif obj[2] == 'NYERI LAMBUNG':
		# {"feature": "usia", "instances": 5, "metric_value": 0.7219, "depth": 2}
		if obj[1] == 'dewasa':
			return 'Penyakit Dalam'
		elif obj[1] == 'anak':
			return 'Kesehatan Anak'
		else: return 'Kesehatan Anak'
	elif obj[2] == 'DIARE ':
		return 'Kesehatan Anak'
	elif obj[2] == 'SAKIT PUNGGUNG':
		# {"feature": "keluhan_2", "instances": 5, "metric_value": 1.9219, "depth": 2}
		if obj[3] == 'TIDAK ADA':
			# {"feature": "jk", "instances": 3, "metric_value": 1.585, "depth": 3}
			if obj[0] == 'Perempuan':
				# {"feature": "usia", "instances": 3, "metric_value": 1.585, "depth": 4}
				if obj[1] == 'dewasa':
					# {"feature": "keluhan_3", "instances": 3, "metric_value": 1.585, "depth": 5}
					if obj[4] == 'TIDAK ADA':
						return 'Syaraf'
					else: return 'Syaraf'
				else: return 'Syaraf'
			else: return 'Syaraf'
		elif obj[3] == 'SAKIT KEPALA':
			return 'Kesehatan Anak'
		elif obj[3] == 'SESAK NAFAS':
			return 'Penyakit Dalam'
		else: return 'Penyakit Dalam'
	elif obj[2] == 'SPESIALIS BEDAH':
		return 'Sub Spesialis Bedah Anak'
	elif obj[2] == 'DEMAM TINGGI':
		return 'Kesehatan Anak'
	elif obj[2] == 'BENJOLAN DI LEHER':
		# {"feature": "jk", "instances": 5, "metric_value": 1.371, "depth": 2}
		if obj[0] == 'Perempuan':
			# {"feature": "usia", "instances": 4, "metric_value": 0.8113, "depth": 3}
			if obj[1] == 'dewasa':
				# {"feature": "keluhan_2", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[3] == 'TIDAK ADA':
					# {"feature": "keluhan_3", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[4] == 'TIDAK ADA':
						return 'THT'
					else: return 'THT'
				else: return 'THT'
			else: return 'THT'
		elif obj[0] == 'Laki-laki':
			return 'Kesehatan Anak'
		else: return 'Kesehatan Anak'
	elif obj[2] == 'KONSUL GIGI DAN MULUT':
		return 'Kesehatan Gigi dan Mulut Anak'
	elif obj[2] == 'SAKIT DADA':
		# {"feature": "jk", "instances": 5, "metric_value": 1.371, "depth": 2}
		if obj[0] == 'Perempuan':
			return 'Kardiologi atau Jantung'
		elif obj[0] == 'Laki-laki':
			# {"feature": "usia", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[1] == 'anak':
				return 'Kesehatan Anak'
			elif obj[1] == 'dewasa':
				return 'Penyakit Dalam'
			else: return 'Penyakit Dalam'
		else: return 'Kesehatan Anak'
	elif obj[2] == 'ASAM LAMBUNG':
		# {"feature": "keluhan_2", "instances": 5, "metric_value": 0.7219, "depth": 2}
		if obj[3] == 'TIDAK ADA':
			return 'Penyakit Dalam'
		elif obj[3] == 'SESAK':
			return 'Kardiologi atau Jantung'
		else: return 'Kardiologi atau Jantung'
	elif obj[2] == 'GATAL ':
		# {"feature": "usia", "instances": 4, "metric_value": 0.8113, "depth": 2}
		if obj[1] == 'dewasa':
			return 'Kulit dan Kelamin'
		elif obj[1] == 'anak':
			return 'Kesehatan Anak'
		else: return 'Kesehatan Anak'
	elif obj[2] == 'LEPAS JAHITAN':
		return 'Bedah Mulut'
	elif obj[2] == 'MAAG':
		return 'Penyakit Dalam'
	elif obj[2] == 'SPEECH DELAY':
		return 'Kesehatan Anak'
	elif obj[2] == 'USG 4 DIMENSI':
		return 'Kebidanan dan Kandungan'
	elif obj[2] == 'RUAM':
		# {"feature": "keluhan_2", "instances": 4, "metric_value": 1.0, "depth": 2}
		if obj[3] == 'TIDAK ADA':
			# {"feature": "jk", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[0] == 'Perempuan':
				return 'Kesehatan Anak'
			elif obj[0] == 'Laki-laki':
				return 'Kulit dan Kelamin'
			else: return 'Kulit dan Kelamin'
		elif obj[3] == 'KULIT':
			return 'Kulit dan Kelamin'
		elif obj[3] == 'DEMAM':
			return 'Kesehatan Anak'
		else: return 'Kesehatan Anak'
	elif obj[2] == 'SAKIT LAMBUNG ':
		return 'Penyakit Dalam'
	elif obj[2] == 'TERAPI REHAB':
		return 'Rehabilitasi Medik'
	elif obj[2] == 'BEJOLAN PAYUDARA':
		return 'Bedah'
	elif obj[2] == 'MENCRET':
		return 'Kesehatan Anak'
	elif obj[2] == 'GIGI BOLONG':
		# {"feature": "usia", "instances": 4, "metric_value": 1.0, "depth": 2}
		if obj[1] == 'anak':
			# {"feature": "jk", "instances": 3, "metric_value": 0.9183, "depth": 3}
			if obj[0] == 'Laki-laki':
				# {"feature": "keluhan_2", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[3] == 'TIDAK ADA':
					# {"feature": "keluhan_3", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[4] == 'TIDAK ADA':
						return 'Kesehatan Gigi dan Mulut Anak'
					else: return 'Kesehatan Gigi dan Mulut Anak'
				else: return 'Kesehatan Gigi dan Mulut Anak'
			else: return 'Kesehatan Gigi dan Mulut Anak'
		elif obj[1] == 'dewasa':
			return 'Gigi dan Mulut'
		else: return 'Gigi dan Mulut'
	elif obj[2] == 'THT':
		return 'THT'
	elif obj[2] == 'BERSIHKAN TELINGA':
		return 'THT'
	elif obj[2] == 'TERAPI':
		# {"feature": "jk", "instances": 4, "metric_value": 0.8113, "depth": 2}
		if obj[0] == 'Laki-laki':
			return 'Tumbuh Kembang Anak (REMEDIA)'
		elif obj[0] == 'Perempuan':
			# {"feature": "usia", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[1] == 'anak':
				# {"feature": "keluhan_2", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[3] == 'TIDAK ADA':
					# {"feature": "keluhan_3", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[4] == 'TIDAK ADA':
						return 'Tumbuh Kembang Anak (REMEDIA)'
					else: return 'Tumbuh Kembang Anak (REMEDIA)'
				else: return 'Tumbuh Kembang Anak (REMEDIA)'
			else: return 'Tumbuh Kembang Anak (REMEDIA)'
		else: return 'Tumbuh Kembang Anak (REMEDIA)'
	elif obj[2] == 'SUSAH BAB':
		return 'Kesehatan Anak'
	elif obj[2] == 'TANGAN KESEMUTAN':
		# {"feature": "jk", "instances": 4, "metric_value": 1.5, "depth": 2}
		if obj[0] == 'Perempuan':
			# {"feature": "usia", "instances": 3, "metric_value": 0.9183, "depth": 3}
			if obj[1] == 'dewasa':
				# {"feature": "keluhan_2", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[3] == 'TIDAK ADA':
					# {"feature": "keluhan_3", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[4] == 'TIDAK ADA':
						return 'Syaraf'
					else: return 'Syaraf'
				else: return 'Syaraf'
			else: return 'Syaraf'
		elif obj[0] == 'Laki-laki':
			return 'Kardiologi atau Jantung'
		else: return 'Kardiologi atau Jantung'
	elif obj[2] == 'TELINGA BERDENGUNG ':
		return 'THT'
	elif obj[2] == 'PASANG KB':
		return 'Kebidanan dan Kandungan'
	elif obj[2] == 'MATA BENGKAK':
		# {"feature": "jk", "instances": 4, "metric_value": 0.8113, "depth": 2}
		if obj[0] == 'Perempuan':
			return 'Mata'
		elif obj[0] == 'Laki-laki':
			# {"feature": "usia", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[1] == 'anak':
				return 'Kesehatan Anak'
			elif obj[1] == 'dewasa':
				return 'Mata'
			else: return 'Mata'
		else: return 'Kesehatan Anak'
	elif obj[2] == 'LEMAS':
		# {"feature": "jk", "instances": 4, "metric_value": 1.5, "depth": 2}
		if obj[0] == 'Perempuan':
			# {"feature": "usia", "instances": 3, "metric_value": 0.9183, "depth": 3}
			if obj[1] == 'dewasa':
				return 'Penyakit Dalam'
			elif obj[1] == 'anak':
				return 'Kesehatan Anak'
			else: return 'Kesehatan Anak'
		elif obj[0] == 'Laki-laki':
			return 'Kardiologi atau Jantung'
		else: return 'Kardiologi atau Jantung'
	elif obj[2] == 'LAMBUNG':
		return 'Penyakit Dalam'
	elif obj[2] == 'HERNIA':
		# {"feature": "usia", "instances": 4, "metric_value": 0.8113, "depth": 2}
		if obj[1] == 'dewasa':
			return 'Bedah'
		elif obj[1] == 'anak':
			return 'Kesehatan Anak'
		else: return 'Kesehatan Anak'
	elif obj[2] == 'SAKIT':
		# {"feature": "usia", "instances": 4, "metric_value": 2.0, "depth": 2}
		if obj[1] == 'anak':
			# {"feature": "keluhan_2", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[3] == 'BERAIR':
				return 'THT'
			elif obj[3] == 'TIDAK ADA':
				return 'Kesehatan Gigi dan Mulut Anak'
			else: return 'Kesehatan Gigi dan Mulut Anak'
		elif obj[1] == 'dewasa':
			# {"feature": "jk", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[0] == 'Perempuan':
				return 'Rehabilitasi Medik'
			elif obj[0] == 'Laki-laki':
				return 'Gigi dan Mulut'
			else: return 'Gigi dan Mulut'
		else: return 'Rehabilitasi Medik'
	elif obj[2] == 'PERIKSA KANDUNGAN':
		return 'Kebidanan dan Kandungan'
	elif obj[2] == 'KONTROL KEHAMILAN':
		return 'Kebidanan dan Kandungan'
	elif obj[2] == 'KONTROL':
		return 'Kardiologi atau Jantung'
	elif obj[2] == 'SAKIT MATA ':
		return 'Mata'
	elif obj[2] == 'BENGKAK':
		# {"feature": "keluhan_2", "instances": 3, "metric_value": 0.9183, "depth": 2}
		if obj[3] == 'TIDAK ADA':
			return 'Mata'
		elif obj[3] == 'JATUH':
			return 'Bedah'
		else: return 'Bedah'
	elif obj[2] == 'ISK':
		# {"feature": "usia", "instances": 3, "metric_value": 0.9183, "depth": 2}
		if obj[1] == 'dewasa':
			return 'Penyakit Dalam'
		elif obj[1] == 'anak':
			return 'Kesehatan Anak'
		else: return 'Kesehatan Anak'
	elif obj[2] == 'SUNAT':
		return 'Bedah'
	elif obj[2] == 'SAKIT BADAN':
		# {"feature": "keluhan_2", "instances": 3, "metric_value": 0.9183, "depth": 2}
		if obj[3] == 'TIDAK ADA':
			# {"feature": "jk", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[0] == 'Perempuan':
				# {"feature": "usia", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[1] == 'dewasa':
					# {"feature": "keluhan_3", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[4] == 'TIDAK ADA':
						return 'Penyakit Dalam'
					else: return 'Penyakit Dalam'
				else: return 'Penyakit Dalam'
			else: return 'Penyakit Dalam'
		elif obj[3] == 'SAKIT TENGGOROKAN':
			return 'Penyakit Dalam'
		else: return 'Penyakit Dalam'
	elif obj[2] == 'TAMBAL':
		return 'Gigi dan Mulut'
	elif obj[2] == 'VERTIGO':
		return 'Syaraf'
	elif obj[2] == 'HHD':
		return 'Kardiologi atau Jantung'
	elif obj[2] == 'GATAL GATAL SELURUH BADAN':
		# {"feature": "jk", "instances": 3, "metric_value": 0.9183, "depth": 2}
		if obj[0] == 'Perempuan':
			return 'Kulit dan Kelamin'
		elif obj[0] == 'Laki-laki':
			return 'Paru-paru'
		else: return 'Paru-paru'
	elif obj[2] == 'RADIOLOGI':
		# {"feature": "jk", "instances": 3, "metric_value": 0.9183, "depth": 2}
		if obj[0] == 'Perempuan':
			return 'Kesehatan Anak'
		elif obj[0] == 'Laki-laki':
			return 'Bedah'
		else: return 'Bedah'
	elif obj[2] == 'PARU':
		# {"feature": "usia", "instances": 3, "metric_value": 0.9183, "depth": 2}
		if obj[1] == 'dewasa':
			return 'Paru-paru'
		elif obj[1] == 'anak':
			return 'Tumbuh Kembang Anak (REMEDIA)'
		else: return 'Tumbuh Kembang Anak (REMEDIA)'
	elif obj[2] == 'SAKIT LUTUT':
		# {"feature": "jk", "instances": 3, "metric_value": 0.9183, "depth": 2}
		if obj[0] == 'Perempuan':
			return 'Penyakit Dalam'
		elif obj[0] == 'Laki-laki':
			return 'Bedah Tulang atau Orthopedi'
		else: return 'Bedah Tulang atau Orthopedi'
	elif obj[2] == 'CHF':
		# {"feature": "jk", "instances": 3, "metric_value": 0.9183, "depth": 2}
		if obj[0] == 'Perempuan':
			# {"feature": "usia", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[1] == 'dewasa':
				# {"feature": "keluhan_2", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[3] == 'TIDAK ADA':
					# {"feature": "keluhan_3", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[4] == 'TIDAK ADA':
						return 'Kardiologi atau Jantung'
					else: return 'Kardiologi atau Jantung'
				else: return 'Kardiologi atau Jantung'
			else: return 'Kardiologi atau Jantung'
		elif obj[0] == 'Laki-laki':
			return 'Kardiologi atau Jantung'
		else: return 'Kardiologi atau Jantung'
	elif obj[2] == 'VAKSIN PCV':
		return 'Kesehatan Anak'
	elif obj[2] == 'OBAT HABIS':
		return 'Kardiologi atau Jantung'
	elif obj[2] == 'BENTOL BENTOL':
		# {"feature": "usia", "instances": 3, "metric_value": 0.9183, "depth": 2}
		if obj[1] == 'anak':
			return 'Kesehatan Anak'
		elif obj[1] == 'dewasa':
			return 'Kulit dan Kelamin'
		else: return 'Kulit dan Kelamin'
	elif obj[2] == 'DADA SAKIT':
		return 'Kardiologi atau Jantung'
	elif obj[2] == 'DADA NYERI':
		# {"feature": "keluhan_2", "instances": 3, "metric_value": 0.9183, "depth": 2}
		if obj[3] == 'TIDAK ADA':
			return 'Kardiologi atau Jantung'
		elif obj[3] == 'SESAK':
			return 'Penyakit Dalam'
		else: return 'Penyakit Dalam'
	elif obj[2] == 'DADA SESAK':
		# {"feature": "jk", "instances": 3, "metric_value": 0.9183, "depth": 2}
		if obj[0] == 'Perempuan':
			# {"feature": "usia", "instances": 3, "metric_value": 0.9183, "depth": 3}
			if obj[1] == 'dewasa':
				# {"feature": "keluhan_2", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[3] == 'TIDAK ADA':
					# {"feature": "keluhan_3", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[4] == 'TIDAK ADA':
						return 'Penyakit Dalam'
					else: return 'Penyakit Dalam'
				else: return 'Penyakit Dalam'
			else: return 'Penyakit Dalam'
		else: return 'Penyakit Dalam'
	elif obj[2] == 'DERMATITIS':
		return 'Kulit dan Kelamin'
	elif obj[2] == 'LBP':
		return 'Syaraf'
	elif obj[2] == 'VAKSIN DPT':
		return 'Kesehatan Anak'
	elif obj[2] == 'AMANDEL':
		# {"feature": "keluhan_2", "instances": 3, "metric_value": 0.9183, "depth": 2}
		if obj[3] == 'TIDAK ADA':
			return 'THT'
		elif obj[3] == 'BATUK':
			return 'Kesehatan Anak'
		else: return 'Kesehatan Anak'
	elif obj[2] == 'KONTROL KEHAMILAN ':
		return 'Kebidanan dan Kandungan'
	elif obj[2] == 'MIMISAN':
		# {"feature": "keluhan_2", "instances": 3, "metric_value": 0.9183, "depth": 2}
		if obj[3] == 'TIDAK ADA':
			# {"feature": "jk", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[0] == 'Laki-laki':
				# {"feature": "usia", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[1] == 'anak':
					# {"feature": "keluhan_3", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[4] == 'TIDAK ADA':
						return 'THT'
					else: return 'THT'
				else: return 'THT'
			else: return 'THT'
		elif obj[3] == 'BERDAHAK':
			return 'Kesehatan Anak'
		else: return 'Kesehatan Anak'
	elif obj[2] == 'BENJOLAN ':
		# {"feature": "usia", "instances": 3, "metric_value": 0.9183, "depth": 2}
		if obj[1] == 'dewasa':
			return 'Penyakit Dalam'
		elif obj[1] == 'anak':
			return 'Kesehatan Anak'
		else: return 'Kesehatan Anak'
	elif obj[2] == 'SAKIT MAAG':
		return 'Penyakit Dalam'
	elif obj[2] == 'VAKSIN ':
		return 'Kesehatan Anak'
	elif obj[2] == 'SETELAH LAHIRAN':
		return 'Kesehatan Anak'
	elif obj[2] == 'GIGI SAKIT':
		return 'Gigi dan Mulut'
	elif obj[2] == 'BURAM':
		return 'Mata'
	elif obj[2] == 'FISIOTERAPI':
		return 'Rehabilitasi Medik'
	elif obj[2] == 'EVALUASI':
		# {"feature": "keluhan_2", "instances": 3, "metric_value": 0.9183, "depth": 2}
		if obj[3] == 'TIDAK ADA':
			# {"feature": "jk", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[0] == 'Laki-laki':
				# {"feature": "usia", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[1] == 'anak':
					# {"feature": "keluhan_3", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[4] == 'TIDAK ADA':
						return 'Rehabilitasi Medik'
					else: return 'Rehabilitasi Medik'
				else: return 'Rehabilitasi Medik'
			else: return 'Rehabilitasi Medik'
		elif obj[3] == 'TERAPI':
			return 'Tumbuh Kembang Anak (REMEDIA)'
		else: return 'Tumbuh Kembang Anak (REMEDIA)'
	elif obj[2] == 'PAP SMEAR':
		return 'Kebidanan dan Kandungan'
	elif obj[2] == 'BEDAH SYARAF':
		return 'Bedah Syaraf'
	elif obj[2] == 'GATAL-GATAL':
		return 'Kesehatan Anak'
	elif obj[2] == 'KONSUL UROLOGI':
		return 'Bedah Urologi'
	elif obj[2] == 'BINTIK MERAH':
		return 'Kesehatan Anak'
	elif obj[2] == 'STROKE':
		return 'Syaraf'
	elif obj[2] == 'VAKSIN BCG':
		return 'Kesehatan Anak'
	elif obj[2] == 'LUKA BAKAR':
		return 'Kulit dan Kelamin'
	elif obj[2] == 'SARIAWAN ':
		return 'Kesehatan Anak'
	elif obj[2] == 'VAKSIN CAMPAK':
		return 'Kesehatan Anak'
	elif obj[2] == 'TELINGA BERDENGUNG':
		return 'THT'
	elif obj[2] == 'MERIANG':
		# {"feature": "usia", "instances": 3, "metric_value": 0.9183, "depth": 2}
		if obj[1] == 'anak':
			return 'Kesehatan Anak'
		elif obj[1] == 'dewasa':
			return 'Penyakit Dalam'
		else: return 'Penyakit Dalam'
	elif obj[2] == 'PERIKSA GIGI':
		# {"feature": "usia", "instances": 3, "metric_value": 1.585, "depth": 2}
		if obj[1] == 'dewasa':
			# {"feature": "jk", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[0] == 'Perempuan':
				# {"feature": "keluhan_2", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[3] == 'TIDAK ADA':
					# {"feature": "keluhan_3", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[4] == 'TIDAK ADA':
						return 'Gigi dan Mulut'
					else: return 'Gigi dan Mulut'
				else: return 'Gigi dan Mulut'
			else: return 'Gigi dan Mulut'
		elif obj[1] == 'anak':
			return 'Kesehatan Gigi dan Mulut Anak'
		else: return 'Kesehatan Gigi dan Mulut Anak'
	elif obj[2] == 'KONSUL JANTUNG':
		return 'Kardiologi atau Jantung'
	elif obj[2] == 'KENCING SAKIT':
		# {"feature": "keluhan_2", "instances": 3, "metric_value": 0.9183, "depth": 2}
		if obj[3] == 'TIDAK ADA':
			# {"feature": "jk", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[0] == 'Laki-laki':
				# {"feature": "usia", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[1] == 'dewasa':
					# {"feature": "keluhan_3", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[4] == 'TIDAK ADA':
						return 'Bedah Urologi'
					else: return 'Bedah Urologi'
				else: return 'Bedah Urologi'
			else: return 'Bedah Urologi'
		elif obj[3] == 'KELUAR DARAH':
			return 'Bedah Urologi'
		else: return 'Bedah Urologi'
	elif obj[2] == 'PERIODONTI':
		return 'Gigi Spesialis Periodonti'
	elif obj[2] == 'PASANG BEHEL':
		return 'Gigi Spesialis Ortodonti'
	elif obj[2] == 'JARI KAKU':
		return 'Syaraf'
	elif obj[2] == 'KONTROL IUD':
		return 'Kebidanan dan Kandungan'
	elif obj[2] == 'JATUH':
		# {"feature": "jk", "instances": 2, "metric_value": 1.0, "depth": 2}
		if obj[0] == 'Laki-laki':
			return 'Bedah Syaraf'
		elif obj[0] == 'Perempuan':
			return 'Kesehatan Anak'
		else: return 'Kesehatan Anak'
	elif obj[2] == 'GAMAU MAKAN':
		return 'Kesehatan Anak'
	elif obj[2] == 'PIPI BENGKAK':
		# {"feature": "jk", "instances": 2, "metric_value": 1.0, "depth": 2}
		if obj[0] == 'Perempuan':
			# {"feature": "usia", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[1] == 'dewasa':
				# {"feature": "keluhan_2", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[3] == 'TIDAK ADA':
					# {"feature": "keluhan_3", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[4] == 'TIDAK ADA':
						return 'THT'
					else: return 'THT'
				else: return 'THT'
			else: return 'THT'
		else: return 'THT'
	elif obj[2] == 'REMATOLOGI':
		return 'Penyakit Dalam'
	elif obj[2] == 'KATARAK':
		return 'Mata'
	elif obj[2] == 'PILEK TERSUMBAT':
		return 'THT'
	elif obj[2] == 'SAKIT BAK':
		return 'Bedah Urologi'
	elif obj[2] == 'KONTROL HAMIL ':
		return 'Kebidanan dan Kandungan'
	elif obj[2] == 'RUAM DI BAGIAN PANTAT':
		return 'Kesehatan Anak'
	elif obj[2] == 'HEMOROID':
		return 'Bedah'
	elif obj[2] == 'GUSI BERDARAH':
		# {"feature": "jk", "instances": 2, "metric_value": 1.0, "depth": 2}
		if obj[0] == 'Perempuan':
			return 'Gigi Spesialis Periodonti'
		elif obj[0] == 'Laki-laki':
			return 'Gigi dan Mulut'
		else: return 'Gigi dan Mulut'
	elif obj[2] == 'PENGLIHATAN BURAM':
		return 'Mata'
	elif obj[2] == 'HERPES':
		return 'Kulit dan Kelamin'
	elif obj[2] == 'NYERI GIGI':
		return 'Gigi dan Mulut'
	elif obj[2] == 'KONSLULTASI KESEHATAN':
		return 'Kesehatan Anak'
	elif obj[2] == 'GIGI GOYANG':
		# {"feature": "jk", "instances": 2, "metric_value": 1.0, "depth": 2}
		if obj[0] == 'Laki-laki':
			# {"feature": "usia", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[1] == 'anak':
				# {"feature": "keluhan_2", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[3] == 'TIDAK ADA':
					# {"feature": "keluhan_3", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[4] == 'TIDAK ADA':
						return 'Kesehatan Gigi dan Mulut Anak'
					else: return 'Kesehatan Gigi dan Mulut Anak'
				else: return 'Kesehatan Gigi dan Mulut Anak'
			else: return 'Kesehatan Gigi dan Mulut Anak'
		else: return 'Kesehatan Gigi dan Mulut Anak'
	elif obj[2] == 'CKD':
		return 'Penyakit Dalam'
	elif obj[2] == 'DIABET':
		return 'Penyakit Dalam'
	elif obj[2] == 'GATAL KULIT':
		return 'Kulit dan Kelamin'
	elif obj[2] == 'HIPERTENSI':
		return 'Penyakit Dalam'
	elif obj[2] == 'RUAM MERAH':
		return 'Kesehatan Anak'
	elif obj[2] == 'GATEL GATEL':
		return 'Kulit dan Kelamin'
	elif obj[2] == 'NYERI BAGIAN KAKI':
		return 'Rehabilitasi Medik'
	elif obj[2] == 'HNP':
		return 'Syaraf'
	elif obj[2] == 'IMM DPT':
		return 'Kesehatan Anak'
	elif obj[2] == 'GATAL GATAL DI KAKI':
		return 'Kulit dan Kelamin'
	elif obj[2] == 'IMUNIASI':
		return 'Kesehatan Anak'
	elif obj[2] == 'HYPERTIROID':
		return 'Penyakit Dalam'
	elif obj[2] == 'MUAL MUAL':
		return 'Penyakit Dalam'
	elif obj[2] == 'FIMOSIS':
		return 'Bedah'
	elif obj[2] == 'TIDAK BISA PIPIS':
		# {"feature": "jk", "instances": 2, "metric_value": 1.0, "depth": 2}
		if obj[0] == 'Laki-laki':
			# {"feature": "usia", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[1] == 'anak':
				# {"feature": "keluhan_2", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[3] == 'TIDAK ADA':
					# {"feature": "keluhan_3", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[4] == 'TIDAK ADA':
						return 'Bedah Urologi'
					else: return 'Bedah Urologi'
				else: return 'Bedah Urologi'
			else: return 'Bedah Urologi'
		else: return 'Bedah Urologi'
	elif obj[2] == 'BATUK SESAK':
		return 'Kesehatan Anak'
	elif obj[2] == 'ASAM LAMBUNG NAIK':
		return 'Penyakit Dalam'
	elif obj[2] == 'OPERASI':
		return 'Bedah'
	elif obj[2] == 'TUMBUH GIGI':
		# {"feature": "jk", "instances": 2, "metric_value": 1.0, "depth": 2}
		if obj[0] == 'Laki-laki':
			return 'Kesehatan Anak'
		elif obj[0] == 'Perempuan':
			return 'Kesehatan Gigi dan Mulut Anak'
		else: return 'Kesehatan Gigi dan Mulut Anak'
	elif obj[2] == 'TELINGA SAKIT ':
		return 'THT'
	elif obj[2] == 'KONTROL RUTIN':
		# {"feature": "keluhan_2", "instances": 2, "metric_value": 1.0, "depth": 2}
		if obj[3] == 'TIDAK ADA':
			return 'Sub Spesialis Bedah Tumor ( Onkologi )'
		elif obj[3] == 'BUKAN HAMIL':
			return 'Kebidanan dan Kandungan'
		else: return 'Kebidanan dan Kandungan'
	elif obj[2] == 'CABUT JAITAN':
		return 'Bedah Mulut'
	elif obj[2] == 'TELINGA BINDENG':
		return 'THT'
	elif obj[2] == 'KTKA':
		# {"feature": "jk", "instances": 2, "metric_value": 1.0, "depth": 2}
		if obj[0] == 'Laki-laki':
			# {"feature": "usia", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[1] == 'anak':
				# {"feature": "keluhan_2", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[3] == 'TIDAK ADA':
					# {"feature": "keluhan_3", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[4] == 'TIDAK ADA':
						return 'Kesehatan Anak'
					else: return 'Kesehatan Anak'
				else: return 'Kesehatan Anak'
			else: return 'Kesehatan Anak'
		else: return 'Kesehatan Anak'
	elif obj[2] == 'MANTUK':
		return 'Kesehatan Anak'
	elif obj[2] == 'LAMBUNG SAKIT':
		return 'Penyakit Dalam'
	elif obj[2] == 'SINUSITIS':
		return 'THT'
	elif obj[2] == 'ANGKAT IUD':
		return 'Kebidanan dan Kandungan'
	elif obj[2] == 'MATA BURAM':
		return 'Mata'
	elif obj[2] == 'BUANG AIR KECIL NYERI':
		return 'Kesehatan Anak'
	elif obj[2] == 'KETERLAMBATAN BICARA':
		return 'Tumbuh Kembang Anak (REMEDIA)'
	elif obj[2] == 'BAK TIDAK LANCAR':
		return 'Bedah Urologi'
	elif obj[2] == 'SUSAH BAK':
		return 'Bedah Urologi'
	elif obj[2] == 'BINTIK2 MERAH':
		return 'Kesehatan Anak'
	elif obj[2] == 'BAK SAKIT':
		# {"feature": "keluhan_2", "instances": 2, "metric_value": 1.0, "depth": 2}
		if obj[3] == 'TIDAK ADA':
			return 'Bedah Urologi'
		elif obj[3] == 'NYERI ULUHATI':
			return 'Penyakit Dalam'
		else: return 'Penyakit Dalam'
	elif obj[2] == 'TANGAN SAKIT':
		# {"feature": "jk", "instances": 2, "metric_value": 1.0, "depth": 2}
		if obj[0] == 'Laki-laki':
			return 'Paru-paru'
		elif obj[0] == 'Perempuan':
			return 'Syaraf'
		else: return 'Syaraf'
	elif obj[2] == 'KONTROL ULANG':
		# {"feature": "usia", "instances": 2, "metric_value": 1.0, "depth": 2}
		if obj[1] == 'dewasa':
			return 'Sub Spesialis Bedah Tumor ( Onkologi )'
		elif obj[1] == 'anak':
			return 'Kesehatan Gigi dan Mulut Anak'
		else: return 'Kesehatan Gigi dan Mulut Anak'
	elif obj[2] == 'SAKIT LAMBUNG':
		# {"feature": "jk", "instances": 2, "metric_value": 1.0, "depth": 2}
		if obj[0] == 'Laki-laki':
			return 'Penyakit Dalam'
		elif obj[0] == 'Perempuan':
			return 'Kesehatan Anak'
		else: return 'Kesehatan Anak'
	elif obj[2] == 'TAMBALAN LEPAS':
		return 'Gigi dan Mulut'
	elif obj[2] == 'PASCA MELAHIRKAN':
		return 'Kebidanan dan Kandungan'
	elif obj[2] == 'ANYANG ANYANGAN':
		# {"feature": "jk", "instances": 2, "metric_value": 1.0, "depth": 2}
		if obj[0] == 'Perempuan':
			return 'Penyakit Dalam'
		elif obj[0] == 'Laki-laki':
			return 'Bedah Urologi'
		else: return 'Bedah Urologi'
	elif obj[2] == 'CEK KB':
		return 'Kebidanan dan Kandungan'
	elif obj[2] == 'TUMIT SAKIT':
		# {"feature": "jk", "instances": 2, "metric_value": 1.0, "depth": 2}
		if obj[0] == 'Laki-laki':
			return 'Rehabilitasi Medik'
		elif obj[0] == 'Perempuan':
			return 'Bedah Tulang atau Orthopedi'
		else: return 'Bedah Tulang atau Orthopedi'
	elif obj[2] == 'KURANG DENGAR':
		return 'THT'
	elif obj[2] == 'SAKIT NELAN':
		# {"feature": "usia", "instances": 2, "metric_value": 1.0, "depth": 2}
		if obj[1] == 'anak':
			return 'Kesehatan Anak'
		elif obj[1] == 'dewasa':
			return 'THT'
		else: return 'THT'
	elif obj[2] == 'SAKIT LEHER':
		# {"feature": "usia", "instances": 2, "metric_value": 1.0, "depth": 2}
		if obj[1] == 'anak':
			return 'Kesehatan Anak'
		elif obj[1] == 'dewasa':
			return 'Syaraf'
		else: return 'Syaraf'
	elif obj[2] == 'SAKIT PERUT ':
		# {"feature": "jk", "instances": 2, "metric_value": 1.0, "depth": 2}
		if obj[0] == 'Laki-laki':
			return 'Penyakit Dalam'
		elif obj[0] == 'Perempuan':
			return 'Kesehatan Anak'
		else: return 'Kesehatan Anak'
	elif obj[2] == 'KULIT KERING':
		return 'Kulit dan Kelamin'
	elif obj[2] == 'CEK KESEHATAN':
		# {"feature": "jk", "instances": 2, "metric_value": 1.0, "depth": 2}
		if obj[0] == 'Perempuan':
			return 'Kulit dan Kelamin'
		elif obj[0] == 'Laki-laki':
			return 'Kesehatan Anak'
		else: return 'Kesehatan Anak'
	elif obj[2] == 'KULIT MERAH MERAH':
		return 'Kulit dan Kelamin'
	elif obj[2] == 'JAMUR KAKI':
		return 'Kulit dan Kelamin'
	elif obj[2] == 'SAKIT PIPIS':
		# {"feature": "usia", "instances": 2, "metric_value": 1.0, "depth": 2}
		if obj[1] == 'dewasa':
			return 'Bedah Urologi'
		elif obj[1] == 'anak':
			return 'Kesehatan Anak'
		else: return 'Kesehatan Anak'
	elif obj[2] == 'TUMIT SAKIT ':
		# {"feature": "jk", "instances": 2, "metric_value": 1.0, "depth": 2}
		if obj[0] == 'Laki-laki':
			return 'Syaraf'
		elif obj[0] == 'Perempuan':
			return 'Rehabilitasi Medik'
		else: return 'Rehabilitasi Medik'
	elif obj[2] == 'CEPAT LELAH':
		return 'Penyakit Dalam'
	elif obj[2] == 'DIABETES':
		return 'Penyakit Dalam'
	elif obj[2] == 'ABSES':
		# {"feature": "jk", "instances": 2, "metric_value": 1.0, "depth": 2}
		if obj[0] == 'Perempuan':
			return 'Bedah Mulut'
		elif obj[0] == 'Laki-laki':
			return 'Bedah'
		else: return 'Bedah'
	elif obj[2] == 'WASIR':
		return 'Bedah'
	elif obj[2] == 'EKSIM':
		return 'Kulit dan Kelamin'
	elif obj[2] == 'SAKIT TANGAN':
		# {"feature": "jk", "instances": 2, "metric_value": 1.0, "depth": 2}
		if obj[0] == 'Perempuan':
			# {"feature": "usia", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[1] == 'dewasa':
				# {"feature": "keluhan_2", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[3] == 'TIDAK ADA':
					# {"feature": "keluhan_3", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[4] == 'TIDAK ADA':
						return 'Penyakit Dalam'
					else: return 'Penyakit Dalam'
				else: return 'Penyakit Dalam'
			else: return 'Penyakit Dalam'
		else: return 'Penyakit Dalam'
	elif obj[2] == 'MASIH SESAK':
		return 'Kardiologi atau Jantung'
	elif obj[2] == 'CEK SPIRAL':
		return 'Kebidanan dan Kandungan'
	elif obj[2] == 'EKSIM ':
		return 'Kulit dan Kelamin'
	elif obj[2] == 'TELINGA MENDENGUNG':
		return 'THT'
	elif obj[2] == 'SAKIT TENGGOROKAN ':
		# {"feature": "jk", "instances": 2, "metric_value": 1.0, "depth": 2}
		if obj[0] == 'Perempuan':
			return 'Penyakit Dalam'
		elif obj[0] == 'Laki-laki':
			return 'Kesehatan Anak'
		else: return 'Kesehatan Anak'
	elif obj[2] == 'EXIM':
		return 'Kulit dan Kelamin'
	elif obj[2] == 'KONTROL KB':
		return 'Kebidanan dan Kandungan'
	elif obj[2] == 'NYERI TELINGA KURANG DENGAR':
		return 'THT'
	elif obj[2] == 'NYERI ULUHATI':
		return 'Penyakit Dalam'
	elif obj[2] == 'NYERI TULANG EKOR':
		return 'Bedah Tulang atau Orthopedi'
	elif obj[2] == 'NYERI TELINGA':
		return 'THT'
	elif obj[2] == 'NYERI TULANG BELAKANG':
		return 'Rehabilitasi Medik'
	elif obj[2] == 'MATA KURANG FOKUS':
		return 'Mata'
	elif obj[2] == 'NYERI TELINGA KANAN':
		return 'THT'
	elif obj[2] == 'MATA KABUR ':
		return 'Mata'
	elif obj[2] == 'MATA AGAK BINTIT':
		return 'Mata'
	elif obj[2] == 'ODONTECTOMY':
		return 'Bedah Mulut'
	elif obj[2] == 'MATA MERAH BENGKAK':
		return 'Mata'
	elif obj[2] == 'MATA IRITASI':
		return 'Mata'
	elif obj[2] == 'MATA BERAIR TERUS':
		return 'Mata'
	elif obj[2] == 'OSTEOPOROSIS':
		return 'Bedah Tulang atau Orthopedi'
	elif obj[2] == 'BADAN SAKIT':
		return 'Syaraf'
	elif obj[2] == 'LUTUT LUKA':
		return 'Kesehatan Anak'
	elif obj[2] == 'LUTUT NYERI':
		return 'Rehabilitasi Medik'
	elif obj[2] == 'MAMPET':
		return 'THT'
	elif obj[2] == 'PENAMBALAN GIGI':
		return 'Kesehatan Gigi dan Mulut Anak'
	elif obj[2] == 'PEMBENGKAKAN JANTUNG':
		return 'Kardiologi atau Jantung'
	elif obj[2] == 'PEGAL DI PINGGANG':
		return 'Kardiologi atau Jantung'
	elif obj[2] == 'PEGAL':
		return 'Syaraf'
	elif obj[2] == 'MASIH SESAK NAFAS':
		return 'Kardiologi atau Jantung'
	elif obj[2] == 'PASCA DEMAM':
		return 'Kesehatan Anak'
	elif obj[2] == 'MATA AGAK BENGKAK':
		return 'Mata'
	elif obj[2] == 'MATA BELEKAN':
		return 'Mata'
	elif obj[2] == 'PASANG KAWAT GIGI':
		return 'Gigi Spesialis Ortodonti'
	elif obj[2] == 'MATA KANAN SEPERTI ADA TITIK':
		return 'Penyakit Dalam'
	elif obj[2] == 'MATA BERBAYANG':
		return 'Mata'
	elif obj[2] == 'PANAS TINGGI':
		return 'Kesehatan Anak'
	elif obj[2] == 'PANAS DINGIN':
		return 'Kesehatan Anak'
	elif obj[2] == 'PANAS DALAM':
		return 'Kesehatan Anak'
	elif obj[2] == 'MATA BURAM ':
		return 'Mata'
	elif obj[2] == 'MATA GATAL':
		return 'Mata'
	elif obj[2] == 'NYERI TANGAN':
		return 'Bedah'
	elif obj[2] == 'MATA PERIH':
		return 'Mata'
	elif obj[2] == 'NYERI SENDI':
		return 'Syaraf'
	elif obj[2] == 'NYERI KUPING KANAN':
		return 'THT'
	elif obj[2] == 'NYERI DI SELURUH BADAN':
		return 'Penyakit Dalam'
	elif obj[2] == 'NYERI DI LUTUT ':
		return 'Syaraf'
	elif obj[2] == 'MENS TIDAK NORMAL':
		return 'Kebidanan dan Kandungan'
	elif obj[2] == 'MENS TIDAK TERATUR':
		return 'Kebidanan dan Kandungan'
	elif obj[2] == 'MENSTRUASI SAKIT':
		return 'Kebidanan dan Kandungan'
	elif obj[2] == 'NYERI DADA KIRI':
		return 'Kardiologi atau Jantung'
	elif obj[2] == 'MENSTRUASI TIDAK LANCAR':
		return 'Kebidanan dan Kandungan'
	elif obj[2] == 'MERAH MERAH':
		return 'Kulit dan Kelamin'
	elif obj[2] == 'NYERI BERKURANG':
		return 'Rehabilitasi Medik'
	elif obj[2] == 'MINUS':
		return 'Mata'
	elif obj[2] == 'NYERI BAGIAN PERUT':
		return 'Bedah Urologi'
	elif obj[2] == 'NYERI BAGIAN LUTUT DAN PINGGANG':
		return 'Syaraf'
	elif obj[2] == 'MINUS NAMBAH':
		return 'Mata'
	elif obj[2] == 'NYERI BAG LUTUT':
		return 'Bedah Tulang atau Orthopedi'
	elif obj[2] == 'MSH ADA SESAK NAFAS':
		return 'Kardiologi atau Jantung'
	elif obj[2] == 'NYERI BAGIAN DADA':
		return 'Kardiologi atau Jantung'
	elif obj[2] == 'MUAL ':
		return 'Penyakit Dalam'
	elif obj[2] == 'NYERI BAGIAN BELAKANG':
		return 'Rehabilitasi Medik'
	elif obj[2] == 'NYERI AREA PERUT':
		return 'Penyakit Dalam'
	elif obj[2] == 'MUKA KERING':
		return 'Kulit dan Kelamin'
	elif obj[2] == 'MUNTAH DARAH':
		return 'Kesehatan Anak'
	elif obj[2] == 'NGILU DI PINGGANG BELAKANG ':
		return 'Syaraf'
	elif obj[2] == 'MUNTAH DIARE':
		return 'Penyakit Dalam'
	elif obj[2] == 'NELEN SAKIT':
		return 'Kesehatan Anak'
	elif obj[2] == 'NAFAS SESAK':
		return 'Kardiologi atau Jantung'
	elif obj[2] == 'MENS BANYAK':
		return 'Kebidanan dan Kandungan'
	elif obj[2] == 'MENDENGUNG':
		return 'THT'
	elif obj[2] == 'NYERI PUNGGUNG':
		return 'Syaraf'
	elif obj[2] == 'MENCRET TERUS ':
		return 'Kesehatan Anak'
	elif obj[2] == 'NYERI PUNDAK':
		return 'Penyakit Dalam'
	elif obj[2] == 'NYERI PERUT KIRI':
		return 'Bedah Urologi'
	elif obj[2] == 'NYERI PERUT KANAN BAWAH':
		return 'Penyakit Dalam'
	elif obj[2] == 'NYERI PERUT DAN DADA':
		return 'Penyakit Dalam'
	elif obj[2] == 'NYERI PERUT BAWAH':
		return 'Kebidanan dan Kandungan'
	elif obj[2] == 'MATA KELUAR KOTORAN':
		return 'Kesehatan Anak'
	elif obj[2] == 'MATA KEMASUKAN DEBU':
		return 'Mata'
	elif obj[2] == 'MATA NYERI':
		return 'Mata'
	elif obj[2] == 'NYERI PERGELANGAN TANGAN':
		return 'Kesehatan Anak'
	elif obj[2] == 'NAFAS BERAT':
		return 'Kardiologi atau Jantung'
	elif obj[2] == 'MATA SEBELAH KIRI':
		return 'Mata'
	elif obj[2] == 'MATA SEBELAH KIRI SPT ADA MENGGANJAL':
		return 'Mata'
	elif obj[2] == 'MATA GAK NYAMAN':
		return 'Mata'
	elif obj[2] == 'MATANYA GATAL':
		return 'Mata'
	elif obj[2] == 'MAU BUSINASI':
		return 'Bedah Urologi'
	elif obj[2] == 'MAU KB':
		return 'Kebidanan dan Kandungan'
	elif obj[2] == 'ALAT KELAMIN':
		return 'Kulit dan Kelamin'
	elif obj[2] == 'PERIKSA FESES':
		return 'Kesehatan Anak'
	elif obj[2] == 'SKIN CARE ':
		return 'Skin Care'
	elif obj[2] == 'TEST PENDENGARAN':
		return 'THT'
	elif obj[2] == 'NYERI PADA KAKI':
		return 'Penyakit Dalam'
	elif obj[2] == 'MAU USG':
		return 'Kebidanan dan Kandungan'
	elif obj[2] == 'NYERI OTOT KAKI':
		return 'Syaraf'
	elif obj[2] == 'NYERI LUTUT':
		return 'Penyakit Dalam'
	elif obj[2] == 'MELEPUH DI WAJAH':
		return 'Kulit dan Kelamin'
	elif obj[2] == 'TERGIGIT':
		return 'Gigi dan Mulut'
	elif obj[2] == 'RAMBUT RONTOK':
		return 'Kulit dan Kelamin'
	elif obj[2] == 'PENDARAHAN':
		return 'Kebidanan dan Kandungan'
	elif obj[2] == 'SYARAF KEJEPIT':
		return 'Syaraf'
	elif obj[2] == 'SKOLIOSIS':
		return 'Bedah Tulang atau Orthopedi'
	elif obj[2] == 'SPONDYLOSIS':
		return 'Bedah Tulang atau Orthopedi'
	elif obj[2] == 'STERIL GIGI':
		return 'Kesehatan Gigi dan Mulut Anak'
	elif obj[2] == 'SUKA SESAK ':
		return 'Penyakit Dalam'
	elif obj[2] == 'SULIT BAB':
		return 'Kesehatan Anak'
	elif obj[2] == 'SULIT NAFAS':
		return 'THT'
	elif obj[2] == 'SUNTIK HEMOFILI':
		return 'Kesehatan Anak'
	elif obj[2] == 'SUSAH NELEN':
		return 'Kesehatan Anak'
	elif obj[2] == 'SUSP HEPATITIS':
		return 'Kesehatan Anak'
	elif obj[2] == 'TAI LALAT DIGARUK BERDARAH':
		return 'Kulit dan Kelamin'
	elif obj[2] == 'TANGAN INFEKSI':
		return 'Bedah'
	elif obj[2] == 'TAMBAL ':
		return 'Gigi dan Mulut'
	elif obj[2] == 'TAMBAL GIGI ':
		return 'Gigi dan Mulut'
	elif obj[2] == 'TAMBAL GIGI BERLUBANG':
		return 'Kesehatan Gigi dan Mulut Anak'
	elif obj[2] == 'TAMBAL GIGI PERMANEN':
		return 'Gigi dan Mulut'
	elif obj[2] == 'TAMBAL SAKIT':
		return 'Gigi dan Mulut'
	elif obj[2] == 'TAMBALAN':
		return 'Kesehatan Gigi dan Mulut Anak'
	elif obj[2] == 'TAMBALAN GIGI':
		return 'Gigi dan Mulut'
	elif obj[2] == 'TAMBALAN GIGI GOYANG':
		return 'Gigi dan Mulut'
	elif obj[2] == 'TAMBALAN GIGI LEPAS ':
		return 'Gigi dan Mulut'
	elif obj[2] == 'SESEK NAFAS':
		return 'Kesehatan Anak'
	elif obj[2] == 'SESAK KALAU PAGI':
		return 'Paru-paru'
	elif obj[2] == 'SERUMEN':
		return 'THT'
	elif obj[2] == 'SERING MIMISAN':
		return 'THT'
	elif obj[2] == 'SAKIT SENDI':
		return 'Penyakit Dalam'
	elif obj[2] == 'SAKIT TULANG BELAKANG':
		return 'Syaraf'
	elif obj[2] == 'SAKIT TULANG RUSUK':
		return 'Syaraf'
	elif obj[2] == 'SAKIT ULUHATI ':
		return 'Penyakit Dalam'
	elif obj[2] == 'HABIS KECELAKAAN':
		return 'Bedah Tulang atau Orthopedi'
	elif obj[2] == 'SALIT PERUT':
		return 'Penyakit Dalam'
	elif obj[2] == 'SCALLING':
		return 'Gigi dan Mulut'
	elif obj[2] == 'SCHIZOPHRENIA':
		return 'Kesehatan Jiwa'
	elif obj[2] == 'SCIATICA ':
		return 'Syaraf'
	elif obj[2] == 'SCOLIOSIS':
		return 'Rehabilitasi Medik'
	elif obj[2] == 'BINTIK MERAH BAGIAN PERUT':
		return 'Kesehatan Anak'
	elif obj[2] == 'DADA KANAN NYERI ':
		return 'Kardiologi atau Jantung'
	elif obj[2] == 'MUKA MERAH':
		return 'Kesehatan Anak'
	elif obj[2] == 'SEKITARAN KUPING SAKIT':
		return 'THT'
	elif obj[2] == 'SERING JATUH ':
		return 'Kesehatan Anak'
	elif obj[2] == 'SERING KELUAR KOTORAN':
		return 'Mata'
	elif obj[2] == 'SERING KRAM':
		return 'Syaraf'
	elif obj[2] == 'LEBAM DI TANGAN DAN KAKI':
		return 'Penyakit Dalam'
	elif obj[2] == 'SERING MEMEGANG DADA':
		return 'Kesehatan Anak'
	elif obj[2] == 'TANGAN LUKA':
		return 'Kesehatan Anak'
	elif obj[2] == 'TANGAN KAKU':
		return 'Penyakit Dalam'
	elif obj[2] == 'SAKIT SEKITAR BAHU':
		return 'Penyakit Dalam'
	elif obj[2] == 'TUMBUH GIGI BARU':
		return 'Kesehatan Gigi dan Mulut Anak'
	elif obj[2] == 'TIDAK NAFSU MAKAN':
		return 'Kesehatan Anak'
	elif obj[2] == 'TINDAKAN':
		return 'Bedah Mulut'
	elif obj[2] == 'TINDAKAN ':
		return 'Bedah Mulut'
	elif obj[2] == 'TINNITUS':
		return 'THT'
	elif obj[2] == 'TREMOR TANGAN DAN KAKI':
		return 'Penyakit Dalam'
	elif obj[2] == 'TULANG EKOR':
		return 'Syaraf'
	elif obj[2] == 'TULANG PINGGUL RETAK':
		return 'Syaraf'
	elif obj[2] == 'TULANG RUSUK SAKIT':
		return 'Kesehatan Anak'
	elif obj[2] == 'TULANG SAKIT':
		return 'Bedah Tulang atau Orthopedi'
	elif obj[2] == 'VAKSIN DBD':
		return 'Kesehatan Anak'
	elif obj[2] == 'TANGAN KRAM':
		return 'Penyakit Dalam'
	elif obj[2] == 'VAKSIN DPT ':
		return 'Kesehatan Anak'
	elif obj[2] == 'VAKSIN MR':
		return 'Kesehatan Anak'
	elif obj[2] == 'VAKSIN PCV ':
		return 'Kesehatan Anak'
	elif obj[2] == 'VASKIN':
		return 'Kesehatan Anak'
	elif obj[2] == 'VERUKA VULGARIS':
		return 'Kulit dan Kelamin'
	elif obj[2] == 'VIRUS':
		return 'Kesehatan Anak'
	elif obj[2] == 'VISUME':
		return 'Kebidanan dan Kandungan'
	elif obj[2] == 'WAJAH ADA BRUNTUSAN':
		return 'Kulit dan Kelamin'
	elif obj[2] == 'WAJAH BERUNTUSAN DAN PUTIH ':
		return 'Kulit dan Kelamin'
	elif obj[2] == 'TIDAK MENS':
		return 'Kebidanan dan Kandungan'
	elif obj[2] == 'TESPEK POSITIF':
		return 'Kebidanan dan Kandungan'
	elif obj[2] == 'NYERI DI PAYUDARA':
		return 'Sub Spesialis Bedah Tumor ( Onkologi )'
	elif obj[2] == 'TENSI TIDAK STABIL':
		return 'Penyakit Dalam'
	elif obj[2] == 'TB USUS':
		return 'Kesehatan Anak'
	elif obj[2] == 'TIDAK BISA TIDUR':
		return 'Kesehatan Jiwa'
	elif obj[2] == 'TELAT BERBICARA':
		return 'Tumbuh Kembang Anak (REMEDIA)'
	elif obj[2] == 'TELING BERDARAH':
		return 'THT'
	elif obj[2] == 'TELINGA ADA CAIRAN':
		return 'THT'
	elif obj[2] == 'TELINGA BERDENGUNG DAN BERAIR':
		return 'THT'
	elif obj[2] == 'TELINGA BINDENG ':
		return 'THT'
	elif obj[2] == 'TELINGA GATAL':
		return 'THT'
	elif obj[2] == 'TELINGA KADANG MENDENGUNG':
		return 'THT'
	elif obj[2] == 'TELINGA BERDARAH':
		return 'THT'
	elif obj[2] == 'TELINGA KANAN GAK ENAK ':
		return 'THT'
	elif obj[2] == 'TELINGA KELUAR DARAH ':
		return 'THT'
	elif obj[2] == 'TELINGA KANAN NYERI':
		return 'Kesehatan Anak'
	elif obj[2] == 'TELINGA KELUAR AIR':
		return 'THT'
	elif obj[2] == 'TELINGA KEMASUKAN SEMUT':
		return 'THT'
	elif obj[2] == 'TELINGA BERNANAH':
		return 'THT'
	elif obj[2] == 'TELINGA NGEUREUBEUK':
		return 'THT'
	elif obj[2] == 'TELINGA SERING BERDENGUNG ':
		return 'THT'
	elif obj[2] == 'TENGGOROKAN SAKIT':
		return 'Kesehatan Anak'
	elif obj[2] == 'SAKIT SENDI ':
		return 'Penyakit Dalam'
	elif obj[2] == 'SAKIT PUNDAK ':
		return 'Penyakit Dalam'
	elif obj[2] == 'PENDARAHAN ':
		return 'Kebidanan dan Kandungan'
	elif obj[2] == 'PIPIS SAKIT':
		return 'Bedah Urologi'
	elif obj[2] == 'PERUT TEGANG DAN NYERI':
		return 'Penyakit Dalam'
	elif obj[2] == 'PERUTNYA SAKIT':
		return 'Kesehatan Anak'
	elif obj[2] == 'PILEK TIDAK KUNJUNG SEMBUH':
		return 'THT'
	elif obj[2] == 'PINGGANG KECETIT':
		return 'Syaraf'
	elif obj[2] == 'PINGGANG PEGEL':
		return 'Penyakit Dalam'
	elif obj[2] == 'PINGGUL SAKIT':
		return 'Syaraf'
	elif obj[2] == 'PINGGUL SAKIT ':
		return 'Syaraf'
	elif obj[2] == 'PINGSAN':
		return 'Kesehatan Anak'
	elif obj[2] == 'PIPI KANAN SAKIT ':
		return 'Syaraf'
	elif obj[2] == 'PIPISNYA SAKIT':
		return 'Bedah'
	elif obj[2] == 'PUNGGUNG SAKIT':
		return 'Kardiologi atau Jantung'
	elif obj[2] == 'POLIP':
		return 'Kebidanan dan Kandungan'
	elif obj[2] == 'PORT RI':
		return 'Kebidanan dan Kandungan'
	elif obj[2] == 'KELUAR DARAH TERUS':
		return 'Kebidanan dan Kandungan'
	elif obj[2] == 'SIRCUM':
		return 'Bedah'
	elif obj[2] == 'PREMATUR':
		return 'Kesehatan Anak'
	elif obj[2] == 'PROGRAM HAMIL':
		return 'Kebidanan dan Kandungan'
	elif obj[2] == 'PROGRAM KEHAMILAN':
		return 'Kebidanan dan Kandungan'
	elif obj[2] == 'PROMIL':
		return 'Kebidanan dan Kandungan'
	elif obj[2] == 'PTERYGIUM':
		return 'Mata'
	elif obj[2] == 'PERUT SERING SAKIT':
		return 'Kesehatan Anak'
	elif obj[2] == 'PERUT SEBELAH KIRI SAKIT ':
		return 'Penyakit Dalam'
	elif obj[2] == 'PERUT PERIH':
		return 'Penyakit Dalam'
	elif obj[2] == 'PERUT PANAS':
		return 'Kesehatan Anak'
	elif obj[2] == 'PENDENGARAN KURANG':
		return 'THT'
	elif obj[2] == 'PENDENGARAN TERASA BERKURANG':
		return 'THT'
	elif obj[2] == 'PENGAPURAN KAKI KIRI ':
		return 'Bedah Tulang atau Orthopedi'
	elif obj[2] == 'PENGLIHATAN AGAK SILAU':
		return 'Mata'
	elif obj[2] == 'PENGLIHATAN KABUR':
		return 'Mata'
	elif obj[2] == 'PERAWATAN CABUT GIGI':
		return 'Gigi dan Mulut'
	elif obj[2] == 'PERAWATAN GIGI ':
		return 'Gigi dan Mulut'
	elif obj[2] == 'PERAWATN GIGI':
		return 'Gigi dan Mulut'
	elif obj[2] == 'PERAWTAN GIGI BERLUBANG':
		return 'Gigi dan Mulut'
	elif obj[2] == 'PERIKSA GIGI LANJUTAN':
		return 'Gigi dan Mulut'
	elif obj[2] == 'PERIKSA LANJUTAN':
		return 'Gigi dan Mulut'
	elif obj[2] == 'PERIKSA MINUS DAN PLUS MATA':
		return 'Mata'
	elif obj[2] == 'PERIKSA RAHANG':
		return 'Bedah'
	elif obj[2] == 'TENGGOROKAN':
		return 'THT'
	elif obj[2] == 'PERLU TERAPI':
		return 'Kesehatan Anak'
	elif obj[2] == 'PERUT KEMBUNG':
		return 'Penyakit Dalam'
	elif obj[2] == 'PERUT MELILIT DAN BEGAH ':
		return 'Penyakit Dalam'
	elif obj[2] == 'PERUT MELILIT':
		return 'Penyakit Dalam'
	elif obj[2] == 'PERUT NYERI':
		return 'Kebidanan dan Kandungan'
	elif obj[2] == 'PUNGGUNG DAN TANGAN SAKIT':
		return 'Penyakit Dalam'
	elif obj[2] == 'PUSER BERDARAH':
		return 'Kesehatan Anak'
	elif obj[2] == 'SAKIT PINGGUL':
		return 'Bedah Tulang atau Orthopedi'
	elif obj[2] == 'SAKIT KUPING':
		return 'THT'
	elif obj[2] == 'SAKIT LUTUT KANAN':
		return 'Bedah Tulang atau Orthopedi'
	elif obj[2] == 'SAKIT DI PUNGGUNG':
		return 'Penyakit Dalam'
	elif obj[2] == 'SAKIT EKSIM':
		return 'Kulit dan Kelamin'
	elif obj[2] == 'SAKIT GIGI ':
		return 'Kesehatan Gigi dan Mulut Anak'
	elif obj[2] == 'SAKIT GIGI GRAHAM ':
		return 'Gigi dan Mulut'
	elif obj[2] == 'SAKIT GUSI':
		return 'Kesehatan Gigi dan Mulut Anak'
	elif obj[2] == 'SAKIT KEPALA SEBELAH':
		return 'Syaraf'
	elif obj[2] == 'SAKIT KEPALA TERUS':
		return 'Kesehatan Anak'
	elif obj[2] == 'SAKIT SAAT BERJALAN':
		return 'Bedah Tulang atau Orthopedi'
	elif obj[2] == 'SAKIT LENGAN':
		return 'Syaraf'
	elif obj[2] == 'PUSING ':
		return 'Kebidanan dan Kandungan'
	elif obj[2] == 'SAKIT LIDAH':
		return 'THT'
	elif obj[2] == 'SAKIT MATA MERAH':
		return 'Mata'
	elif obj[2] == 'SAKIT PANGGUL':
		return 'Kebidanan dan Kandungan'
	elif obj[2] == 'SAKIT PASCA OPERASI':
		return 'Penyakit Dalam'
	elif obj[2] == 'SAKIT PERSENDIAN BAHU':
		return 'Syaraf'
	elif obj[2] == 'SAKIT PERUT BAGIAN BAWAH':
		return 'Kebidanan dan Kandungan'
	elif obj[2] == 'SAKIT PERUT BAGIAN RAHIM':
		return 'Kebidanan dan Kandungan'
	elif obj[2] == 'SAKIT PERUT BAWAH':
		return 'Kebidanan dan Kandungan'
	elif obj[2] == 'SAKIT PINGGANG ':
		return 'Syaraf'
	elif obj[2] == 'SAKIT DI LEHER':
		return 'Rehabilitasi Medik'
	elif obj[2] == 'SAKIT DI KELAMIN ':
		return 'Kulit dan Kelamin'
	elif obj[2] == 'SAKIT DI BAGIAN PINGGANG':
		return 'Penyakit Dalam'
	elif obj[2] == 'SAKIT BAGIAN KAKI':
		return 'Syaraf'
	elif obj[2] == 'PUSING LIAT CAHAYA':
		return 'Syaraf'
	elif obj[2] == 'RADANG SAKIT TENGGOROKAN':
		return 'THT'
	elif obj[2] == 'RADANG TENGGOROKAN ':
		return 'THT'
	elif obj[2] == 'RADIASI':
		return 'Mata'
	elif obj[2] == 'LUPUS':
		return 'Penyakit Dalam'
	elif obj[2] == 'REMATIK':
		return 'Penyakit Dalam'
	elif obj[2] == 'BATU GINJAL':
		return 'Bedah Urologi'
	elif obj[2] == 'RENCANA SC':
		return 'Kebidanan dan Kandungan'
	elif obj[2] == 'RETINAL DISORDER':
		return 'Mata'
	elif obj[2] == 'REUMATIK':
		return 'Penyakit Dalam'
	elif obj[2] == 'REWEL':
		return 'Kesehatan Anak'
	elif obj[2] == 'RUAM ':
		return 'Kulit dan Kelamin'
	elif obj[2] == 'RUAM DI MUKA':
		return 'Kulit dan Kelamin'
	elif obj[2] == 'RUAM DI BADAN':
		return 'Kesehatan Anak'
	elif obj[2] == 'RUJUKAN DR LAURA':
		return 'Kardiologi atau Jantung'
	elif obj[2] == 'SAKI GIGI':
		return 'Gigi dan Mulut'
	elif obj[2] == 'SAKI GUSI BAGIAN ATAS ':
		return 'Gigi dan Mulut'
	elif obj[2] == 'SAKI KAKI ':
		return 'Penyakit Dalam'
	elif obj[2] == 'SAKIT BAGIAN BAHU SAMPAI BAWAH':
		return 'Rehabilitasi Medik'
	elif obj[2] == 'LUTUT KERAM ':
		return 'Bedah'
	elif obj[2] == 'TELINGA BENGKAK ':
		return 'THT'
	elif obj[2] == 'LUKA TAPI TIDAK SEMBUH SEMBUH ':
		return 'Kulit dan Kelamin'
	elif obj[2] == 'DPT':
		return 'Kesehatan Anak'
	elif obj[2] == 'TBC ':
		return 'Paru-paru'
	elif obj[2] == 'TELINGA ':
		return 'THT'
	elif obj[2] == 'UPPUSIN':
		return 'THT'
	elif obj[2] == 'CEREBRAL PALSY':
		return 'Kesehatan Anak'
	elif obj[2] == 'CERVICAL DISC DISORDERS':
		return 'Syaraf'
	elif obj[2] == 'BIOPSI':
		return 'Bedah'
	elif obj[2] == 'COTTON BUD KETINGGALAN DI KUPING':
		return 'THT'
	elif obj[2] == 'DADA BERDEBAR':
		return 'Kardiologi atau Jantung'
	elif obj[2] == 'DADA KIRI SAKIT':
		return 'Kesehatan Anak'
	elif obj[2] == 'DADA TERASA NYERI':
		return 'Kardiologi atau Jantung'
	elif obj[2] == 'DAHAK':
		return 'Penyakit Dalam'
	elif obj[2] == 'DAHAK BERDARAH':
		return 'Kesehatan Anak'
	elif obj[2] == 'DARAH TINGGI ':
		return 'Penyakit Dalam'
	elif obj[2] == 'DBD':
		return 'Kesehatan Anak'
	elif obj[2] == 'DEBAR GAK NYAMAN':
		return 'Kardiologi atau Jantung'
	elif obj[2] == 'DECUBITUS':
		return 'Kulit dan Kelamin'
	elif obj[2] == 'DEMAM MUNTAH':
		return 'Kesehatan Anak'
	elif obj[2] == 'DENGKUL SAKIT ':
		return 'Bedah Tulang atau Orthopedi'
	elif obj[2] == 'DIARE CAIR':
		return 'Kesehatan Anak'
	elif obj[2] == 'PENDENGARAN':
		return 'THT'
	elif obj[2] == 'CEK KANDUNGAN ':
		return 'Kebidanan dan Kandungan'
	elif obj[2] == 'TERTUSUK PAKU':
		return 'Bedah'
	elif obj[2] == 'CAK KANDUNGAN':
		return 'Kebidanan dan Kandungan'
	elif obj[2] == 'BUKA PERBAN':
		return 'Bedah'
	elif obj[2] == 'BUKA VERBAN':
		return 'Kebidanan dan Kandungan'
	elif obj[2] == 'BUKIT MAKMUR':
		return 'Kebidanan dan Kandungan'
	elif obj[2] == 'BUSINASI ':
		return 'Bedah Urologi'
	elif obj[2] == 'CABUT':
		return 'Gigi dan Mulut'
	elif obj[2] == 'CABUT GIGI ':
		return 'Bedah Mulut'
	elif obj[2] == 'CACAR ':
		return 'Kulit dan Kelamin'
	elif obj[2] == 'CACAR AIR':
		return 'Kesehatan Anak'
	elif obj[2] == 'CAMPAK':
		return 'Kesehatan Anak'
	elif obj[2] == 'CEK IUD':
		return 'Kebidanan dan Kandungan'
	elif obj[2] == 'CEDERA OTOT PUNGGUNG':
		return 'Rehabilitasi Medik'
	elif obj[2] == 'DARAH':
		return 'Kesehatan Anak'
	elif obj[2] == 'GERAHAM ':
		return 'Gigi dan Mulut'
	elif obj[2] == 'GIGI ':
		return 'Gigi dan Mulut'
	elif obj[2] == 'GULA DARAH':
		return 'Penyakit Dalam'
	elif obj[2] == 'GUSI':
		return 'Gigi dan Mulut'
	elif obj[2] == 'CEK HAMIL ':
		return 'Kebidanan dan Kandungan'
	elif obj[2] == 'TIDAK BISA MENCIUM BAU':
		return 'THT'
	elif obj[2] == 'KEPALA ADA KULIT KERING':
		return 'Kulit dan Kelamin'
	elif obj[2] == 'DUDUK LAMA KELEYENGAN':
		return 'Syaraf'
	elif obj[2] == 'BUKA JAHITAN':
		return 'Sub Spesialis Bedah Tumor ( Onkologi )'
	elif obj[2] == 'DYSPEPSI':
		return 'Penyakit Dalam'
	elif obj[2] == 'GATAL PERIH ':
		return 'Kesehatan Anak'
	elif obj[2] == 'GATAL GATAL DI KEMALUAN':
		return 'Kesehatan Anak'
	elif obj[2] == 'GATAL GATAL DI TELAPAK KAKI':
		return 'Kulit dan Kelamin'
	elif obj[2] == 'GATEL':
		return 'Kulit dan Kelamin'
	elif obj[2] == 'GATEL TANGAN':
		return 'Kulit dan Kelamin'
	elif obj[2] == 'GEA':
		return 'Kesehatan Anak'
	elif obj[2] == 'GEJALA TIFUS':
		return 'Kesehatan Anak'
	elif obj[2] == 'GERAHAM BELAKANG SAKIT ':
		return 'Gigi dan Mulut'
	elif obj[2] == 'GIG BERLUBANG':
		return 'Kesehatan Gigi dan Mulut Anak'
	elif obj[2] == 'GIGI ATAS KANAN SAKIT':
		return 'Gigi dan Mulut'
	elif obj[2] == 'GIGI BENGKAK KANAN KIRI':
		return 'Gigi dan Mulut'
	elif obj[2] == 'GIGI COPOT':
		return 'Gigi dan Mulut'
	elif obj[2] == 'GIGI GOYANG ':
		return 'Gigi dan Mulut'
	elif obj[2] == 'GIGI LEPAS':
		return 'Gigi dan Mulut'
	elif obj[2] == 'GIGI LUBANG':
		return 'Gigi dan Mulut'
	elif obj[2] == 'GIGI MASUK KE GUSI':
		return 'Kesehatan Gigi dan Mulut Anak'
	elif obj[2] == 'HABIS JATUH':
		return 'Penyakit Dalam'
	elif obj[2] == 'HAID TIDAK NORMAL':
		return 'Kebidanan dan Kandungan'
	elif obj[2] == 'HEPATITITIS ':
		return 'Kesehatan Anak'
	elif obj[2] == 'GATAL TENGGOROKAN':
		return 'THT'
	elif obj[2] == 'GATAL DI TELINGA':
		return 'THT'
	elif obj[2] == 'GATAL PADA TANGAN/SIKU DAN KULIT VAGINA':
		return 'Kulit dan Kelamin'
	elif obj[2] == 'GANGGUAN MOOD':
		return 'Kesehatan Jiwa'
	elif obj[2] == 'DYSPEPSIA':
		return 'Kesehatan Anak'
	elif obj[2] == 'EPILEPSI':
		return 'Syaraf'
	elif obj[2] == 'FISSURA ANI':
		return 'Sub Spesialis Bedah Anak'
	elif obj[2] == 'FLEK ':
		return 'Kebidanan dan Kandungan'
	elif obj[2] == 'FLU ':
		return 'THT'
	elif obj[2] == 'GA BISA BAK':
		return 'Bedah Urologi'
	elif obj[2] == 'HALUSINASI':
		return 'Kesehatan Jiwa'
	elif obj[2] == 'GANGGUAN BICARA':
		return 'Kesehatan Anak'
	elif obj[2] == 'GANGGUAN SENSORI':
		return 'Kesehatan Anak'
	elif obj[2] == 'TIMBUL BENTOL BENTOL YANG BERISI CAIRAN BENING':
		return 'Kulit dan Kelamin'
	elif obj[2] == 'GANTI KARET':
		return 'Gigi Spesialis Ortodonti'
	elif obj[2] == 'GANTI TAMBALAN':
		return 'Gigi dan Mulut'
	elif obj[2] == 'GATAL DI BAGIAN KAKI':
		return 'Kulit dan Kelamin'
	elif obj[2] == 'GATAL DI LUTUT':
		return 'Kulit dan Kelamin'
	elif obj[2] == 'GATAL DI PAHA':
		return 'Kulit dan Kelamin'
	elif obj[2] == 'GATAL DI TANGAN DAN KAKI':
		return 'Kulit dan Kelamin'
	elif obj[2] == 'GATAL DI TANGAN':
		return 'Kulit dan Kelamin'
	elif obj[2] == 'GATAL DI TELINGA ':
		return 'THT'
	elif obj[2] == 'BUKA KB':
		return 'Kebidanan dan Kandungan'
	elif obj[2] == 'BUANG AIR KECIL SAKIT DAN BERDARAH':
		return 'Kesehatan Anak'
	elif obj[2] == 'LUKA OPERASI BERAIR':
		return 'Bedah'
	elif obj[2] == 'BCG VAKSIN':
		return 'Kesehatan Anak'
	elif obj[2] == 'BAB BERLENDIR':
		return 'Kesehatan Anak'
	elif obj[2] == 'BAB SUSAH':
		return 'Kesehatan Anak'
	elif obj[2] == 'SERING BUANG AIR KECIL':
		return 'Bedah Urologi'
	elif obj[2] == 'RADIOLOGI ':
		return 'Penyakit Dalam'
	elif obj[2] == 'BADAN LEMES PUSING':
		return 'Penyakit Dalam'
	elif obj[2] == 'BADAN MENGGIGIL':
		return 'Kesehatan Anak'
	elif obj[2] == 'BADAN MERAH MERAH':
		return 'Kesehatan Anak'
	elif obj[2] == 'BADAN PADA SAKIT ':
		return 'Penyakit Dalam'
	elif obj[2] == 'BADAN SEBELAH SAKIT':
		return 'Syaraf'
	elif obj[2] == 'BAK BERDARAH':
		return 'Bedah Urologi'
	elif obj[2] == 'BANYAK BINTIK MERAH':
		return 'Kulit dan Kelamin'
	elif obj[2] == 'BAPIL GATAL':
		return 'Kesehatan Anak'
	elif obj[2] == 'BATUK ADA DARAH ':
		return 'Kesehatan Anak'
	elif obj[2] == 'BATUK ALERGI':
		return 'Kesehatan Anak'
	elif obj[2] == 'BATUK BERDAHAK SUDAH SEMINGGU':
		return 'Kesehatan Anak'
	elif obj[2] == 'BATUK KERING ':
		return 'THT'
	elif obj[2] == 'BATUK PANAS':
		return 'Kesehatan Anak'
	elif obj[2] == 'BATUK KELUAR DARAH':
		return 'Paru-paru'
	elif obj[2] == 'BATUK BATUK':
		return 'Penyakit Dalam'
	elif obj[2] == 'ASTRA':
		return 'Kesehatan Anak'
	elif obj[2] == 'ASAM URAT TINGGI':
		return 'Penyakit Dalam'
	elif obj[2] == 'ASAM MUAL':
		return 'Penyakit Dalam'
	elif obj[2] == 'ANUS':
		return 'Kesehatan Anak'
	elif obj[2] == 'SAKIT TEGGOROKAN':
		return 'THT'
	elif obj[2] == 'BEJOLAN':
		return 'Kesehatan Anak'
	elif obj[2] == 'BENGKAK DI TELINGA':
		return 'THT'
	elif obj[2] == 'BENJOLAN ANUS':
		return 'Bedah'
	elif obj[2] == 'BENJOLAN LEHER':
		return 'Bedah'
	elif obj[2] == 'BENJOLAN LENGAN':
		return 'Bedah'
	elif obj[2] == 'BENJOLAN LUTUT':
		return 'Bedah'
	elif obj[2] == 'BEJOLAN PUNDAK':
		return 'Bedah'
	elif obj[2] == 'KAKI':
		return 'Kulit dan Kelamin'
	elif obj[2] == 'ASAM LAMBUNG TINGGI':
		return 'Penyakit Dalam'
	elif obj[2] == 'PERUT':
		return 'Kulit dan Kelamin'
	elif obj[2] == 'TANGAN':
		return 'Kulit dan Kelamin'
	elif obj[2] == 'BADAN':
		return 'Kesehatan Anak'
	elif obj[2] == 'DURI DI TENGGOROKAN':
		return 'THT'
	elif obj[2] == 'GURATAN MERAH':
		return 'Kulit dan Kelamin'
	elif obj[2] == 'PENGGUMPALAN DARAH OTAK':
		return 'Syaraf'
	elif obj[2] == 'ALERGI OBAT':
		return 'Paru-paru'
	elif obj[2] == 'IMPLAN':
		return 'Kebidanan dan Kandungan'
	elif obj[2] == 'BCG':
		return 'Kesehatan Anak'
	elif obj[2] == 'BELIKAT NGILU':
		return 'Syaraf'
	elif obj[2] == 'BUANG AIR KECIL PERIH':
		return 'Kulit dan Kelamin'
	elif obj[2] == 'BELUM BAK':
		return 'Kesehatan Anak'
	elif obj[2] == 'BIANG KERINGAT ':
		return 'Kesehatan Anak'
	elif obj[2] == 'BIBIR KERING':
		return 'Kulit dan Kelamin'
	elif obj[2] == 'BIBIR PECAH PECAH':
		return 'Kulit dan Kelamin'
	elif obj[2] == 'BIDURAN':
		return 'Kesehatan Anak'
	elif obj[2] == 'BINTIK BINTIK MERAH':
		return 'Kesehatan Anak'
	elif obj[2] == 'BINTIK DI BAGIAN MULUT':
		return 'Kulit dan Kelamin'
	elif obj[2] == 'BINTIK HITAM DI WAJAH':
		return 'Kulit dan Kelamin'
	elif obj[2] == 'BINTIK MERAH DEKAT MATA':
		return 'Kulit dan Kelamin'
	elif obj[2] == 'BINTIK MERAH DI DADA DAN DI PUNGGUNG':
		return 'Kesehatan Anak'
	elif obj[2] == 'BINTIK MERAH DI KEPALA':
		return 'Kesehatan Anak'
	elif obj[2] == 'BINTIK MERAH DI LEHER DAN BADAN':
		return 'Kesehatan Anak'
	elif obj[2] == 'BINTIK2 MERAH DI KULIT':
		return 'Kesehatan Anak'
	elif obj[2] == 'BINTIK MERAH DI WAJAH':
		return 'Kulit dan Kelamin'
	elif obj[2] == 'BISUL':
		return 'Kulit dan Kelamin'
	elif obj[2] == 'BLIGHTED OVUM':
		return 'Kebidanan dan Kandungan'
	elif obj[2] == 'BRONCHITIS':
		return 'Penyakit Dalam'
	elif obj[2] == 'BRUNTUS':
		return 'Kulit dan Kelamin'
	elif obj[2] == 'BRUNTUSAN GATAL':
		return 'Kesehatan Anak'
	elif obj[2] == 'BUAH ZAKAR BESAR SEBELAH ':
		return 'Bedah'
	elif obj[2] == 'BERUNTUSAN DI WAJAH':
		return 'Kulit dan Kelamin'
	elif obj[2] == 'BERSIHKAN TELINGA ':
		return 'THT'
	elif obj[2] == 'BERSIHKAN CERUMEN':
		return 'THT'
	elif obj[2] == 'BENTOL BENTOL DI TANGAN DAN BADAN':
		return 'Kesehatan Anak'
	elif obj[2] == 'BENGKAK BEKAS SUNTIKAN':
		return 'Bedah'
	elif obj[2] == 'BENGKAK DI BAGIAN KELAMIN ':
		return 'Kulit dan Kelamin'
	elif obj[2] == 'BENGKAK DI BAGIAN MATA':
		return 'Mata'
	elif obj[2] == 'BENGKAK DI MATA':
		return 'Kesehatan Anak'
	elif obj[2] == 'BENJOLAN DI TELINGA':
		return 'Kesehatan Anak'
	elif obj[2] == 'BENJOLAN DI SELANGKANGAN':
		return 'Kulit dan Kelamin'
	elif obj[2] == 'BENJOLANNYA TETEP ADA':
		return 'Mata'
	elif obj[2] == 'BENOL BENTOL DI BADAN ':
		return 'Kulit dan Kelamin'
	elif obj[2] == 'BERASA ADA CAHAYA PUTIH':
		return 'Mata'
	elif obj[2] == 'BERSIHIN TELINGA':
		return 'THT'
	elif obj[2] == 'BERAT BADAN TIDAK NAIK SIGNIFIKAN':
		return 'Kesehatan Anak'
	elif obj[2] == 'BERCAK BERNANAH DI PUNGUNG':
		return 'Kulit dan Kelamin'
	elif obj[2] == 'BERDENGUNG':
		return 'THT'
	elif obj[2] == 'BERLUBANG':
		return 'Gigi dan Mulut'
	elif obj[2] == 'BEROBAT':
		return 'Bedah Urologi'
	elif obj[2] == 'BERSIHIN GIGI':
		return 'Gigi dan Mulut'
	elif obj[2] == 'BERSIHIN KOTORAN TELINGA':
		return 'THT'
	elif obj[2] == 'BERSIHIN KUPING':
		return 'THT'
	elif obj[2] == 'HIDUNG KEMASUKAN':
		return 'THT'
	elif obj[2] == 'HIDUNG MAMPET':
		return 'THT'
	elif obj[2] == 'HIDUNG SAKIT ':
		return 'THT'
	elif obj[2] == 'KONTROL TELINGA':
		return 'THT'
	elif obj[2] == 'LUTUT':
		return 'Bedah Tulang atau Orthopedi'
	elif obj[2] == 'KONTROL MENINGITIS':
		return 'Kesehatan Anak'
	elif obj[2] == 'KONTROL OBAT':
		return 'Kesehatan Anak'
	elif obj[2] == 'KONTROL ORTHO':
		return 'Gigi Spesialis Ortodonti'
	elif obj[2] == 'PARKINSON':
		return 'Syaraf'
	elif obj[2] == 'PASCA KURET':
		return 'Kebidanan dan Kandungan'
	elif obj[2] == 'KONTROL PASCA LAHIR':
		return 'Kesehatan Anak'
	elif obj[2] == 'PASCA OPERASI':
		return 'Bedah'
	elif obj[2] == 'PERAWAT GIGI':
		return 'Gigi dan Mulut'
	elif obj[2] == 'KONTROL PILEK':
		return 'Kesehatan Anak'
	elif obj[2] == 'KONTROL POST LAHIR':
		return 'Kesehatan Anak'
	elif obj[2] == 'PTERIGIUM':
		return 'Mata'
	elif obj[2] == 'GINEKOLOGI':
		return 'Sub Spesialis Onkologi Ginekologi'
	elif obj[2] == 'RENCANA TINDAKAN ':
		return 'Penyakit Dalam'
	elif obj[2] == 'PEGAL DI LEHER':
		return 'Kardiologi atau Jantung'
	elif obj[2] == 'SUSAH TIDUR':
		return 'Kardiologi atau Jantung'
	elif obj[2] == 'SAKIT GINJAL':
		return 'Bedah Urologi'
	elif obj[2] == 'SAKIT TENGGOROK':
		return 'THT'
	elif obj[2] == 'SETELAH SESAR':
		return 'Kebidanan dan Kandungan'
	elif obj[2] == 'KAWAT GIGI':
		return 'Gigi dan Mulut'
	elif obj[2] == 'KONTROL KANDUNGAN ':
		return 'Kebidanan dan Kandungan'
	elif obj[2] == 'KACA MATA':
		return 'Mata'
	elif obj[2] == 'DIABET ':
		return 'Penyakit Dalam'
	elif obj[2] == 'ONKOLOGI':
		return 'Sub Spesialis Onkologi Ginekologi'
	elif obj[2] == 'BARU MELAHIRKAN':
		return 'Kebidanan dan Kandungan'
	elif obj[2] == 'BBLR':
		return 'Kesehatan Anak'
	elif obj[2] == 'BPH':
		return 'Bedah Urologi'
	elif obj[2] == 'KONTROL CABUT KUKU':
		return 'Bedah'
	elif obj[2] == 'CAD':
		return 'Kardiologi atau Jantung'
	elif obj[2] == 'CHOLELITIASIS':
		return 'Bedah'
	elif obj[2] == 'COLIC RENAL':
		return 'Bedah Urologi'
	elif obj[2] == 'ENDOMETRIOSIS':
		return 'Kebidanan dan Kandungan'
	elif obj[2] == 'K2':
		return 'Penyakit Dalam'
	elif obj[2] == 'KONTROL FLEK':
		return 'Kesehatan Anak'
	elif obj[2] == 'KONTROL FLEK ':
		return 'Kesehatan Anak'
	elif obj[2] == 'GANGGUAN ANXIETAS':
		return 'Kesehatan Jiwa'
	elif obj[2] == 'GULA':
		return 'Penyakit Dalam'
	elif obj[2] == 'ESWL':
		return 'Bedah Urologi'
	elif obj[2] == 'PAPSMEAR':
		return 'Kebidanan dan Kandungan'
	elif obj[2] == 'ISK ':
		return 'Penyakit Dalam'
	elif obj[2] == 'KONTROL JANTUNG':
		return 'Kardiologi atau Jantung'
	elif obj[2] == 'SPIRAL':
		return 'Kebidanan dan Kandungan'
	elif obj[2] == 'BENJOLAN DI LUBANG TELINGA':
		return 'THT'
	elif obj[2] == 'HIDUNG SAKIT':
		return 'THT'
	elif obj[2] == 'SAKIT BELAKANG TELINGA':
		return 'THT'
	elif obj[2] == 'KUPING MENDENGING':
		return 'Penyakit Dalam'
	elif obj[2] == 'KUPING SAKIT':
		return 'THT'
	elif obj[2] == 'LAMBUNG NYERI':
		return 'Penyakit Dalam'
	elif obj[2] == 'LAMBUNG SAKIT ':
		return 'Penyakit Dalam'
	elif obj[2] == 'LEHER BENGKAK':
		return 'Kesehatan Anak'
	elif obj[2] == 'LEHER NYERI':
		return 'Kesehatan Anak'
	elif obj[2] == 'LEMES':
		return 'Penyakit Dalam'
	elif obj[2] == 'LENGAN SUKA KESEMUTAN':
		return 'Syaraf'
	elif obj[2] == 'LENGAN SAKIT':
		return 'Penyakit Dalam'
	elif obj[2] == 'LEPAS BEHEL':
		return 'Gigi dan Mulut'
	elif obj[2] == 'LEPAS IUD':
		return 'Kebidanan dan Kandungan'
	elif obj[2] == 'LEPAS KB':
		return 'Kebidanan dan Kandungan'
	elif obj[2] == 'LIDAH DAN TENGGOROKAN ADA BENJOLAN':
		return 'THT'
	elif obj[2] == 'LIDAH PUTIH':
		return 'Kesehatan Anak'
	elif obj[2] == 'LIVER':
		return 'Penyakit Dalam'
	elif obj[2] == 'LUKA BASAH':
		return 'Bedah Urologi'
	elif obj[2] == 'LUKA DI KAKI ':
		return 'Kulit dan Kelamin'
	elif obj[2] == 'LUKA DIKAKI':
		return 'Bedah'
	elif obj[2] == 'LUKA MATA':
		return 'Mata'
	elif obj[2] == 'KUNING':
		return 'Kesehatan Anak'
	elif obj[2] == 'KULIT WAJAH MERAH':
		return 'Kulit dan Kelamin'
	elif obj[2] == 'KULIT SIKU KERING':
		return 'Kulit dan Kelamin'
	elif obj[2] == 'TANGAN PEGAL':
		return 'Paru-paru'
	elif obj[2] == 'TELINGA TERSUMBAT':
		return 'THT'
	elif obj[2] == 'TUMOR':
		return 'Bedah Tumor'
	elif obj[2] == 'MRI':
		return 'Syaraf'
	elif obj[2] == 'BERAT BADAN KURANG':
		return 'Kesehatan Anak'
	elif obj[2] == 'HABIS OBAT':
		return 'Kardiologi atau Jantung'
	elif obj[2] == 'JARI KESEMUTAN':
		return 'Penyakit Dalam'
	elif obj[2] == 'LEPAS JAITAN':
		return 'Bedah'
	elif obj[2] == 'NYERI BAK':
		return 'Bedah Urologi'
	elif obj[2] == 'AGAK LEMES':
		return 'Kesehatan Anak'
	elif obj[2] == 'KULIT SENSITIF':
		return 'Kesehatan Anak'
	elif obj[2] == 'TELINGA KOTOR':
		return 'THT'
	elif obj[2] == 'OPERSI AMANDEL':
		return 'Kesehatan Anak'
	elif obj[2] == 'KULIT HIDUNG HITAM':
		return 'Kulit dan Kelamin'
	elif obj[2] == 'KULIT KAKI GATAL ':
		return 'Kulit dan Kelamin'
	elif obj[2] == 'KULIT KELUPAS ':
		return 'Kulit dan Kelamin'
	elif obj[2] == 'KULIT KERAS DI BAGIAN KAKI':
		return 'Kulit dan Kelamin'
	elif obj[2] == 'KULIT KERING DI TANGAN DAN PAYUDARA':
		return 'Kulit dan Kelamin'
	elif obj[2] == 'KULIT PUTIH PUTIH DI WAJAH':
		return 'Kulit dan Kelamin'
	elif obj[2] == 'TEKANAN DARAH TIDAK STABIL':
		return 'Syaraf'
	elif obj[2] == 'KONSULTASI USG':
		return 'Kebidanan dan Kandungan'
	elif obj[2] == 'KONSULTASI SC':
		return 'Penyakit Dalam'
	elif obj[2] == 'PILEK BAU':
		return 'THT'
	elif obj[2] == 'KAKI KESEMUTAN':
		return 'Syaraf'
	elif obj[2] == 'KAKI PECAH PECAH':
		return 'Kulit dan Kelamin'
	elif obj[2] == 'KAKI PEGAL':
		return 'Syaraf'
	elif obj[2] == 'KAKI PEGAL-PEGAL':
		return 'Kardiologi atau Jantung'
	elif obj[2] == 'KALAU CAPEK ADA NYERI DADA':
		return 'Kardiologi atau Jantung'
	elif obj[2] == 'TULANG BUNYI':
		return 'Bedah Tulang atau Orthopedi'
	elif obj[2] == 'KALO JALAN SAKIT':
		return 'Syaraf'
	elif obj[2] == 'KANKER':
		return 'Bedah'
	elif obj[2] == 'KAPALAN DI KAKI':
		return 'Kulit dan Kelamin'
	elif obj[2] == 'DOKTER KULIT':
		return 'Kulit dan Kelamin'
	elif obj[2] == 'KEJANG NYERI KEPALA':
		return 'Syaraf'
	elif obj[2] == 'KEL':
		return 'Kulit dan Kelamin'
	elif obj[2] == 'KELENJAR':
		return 'Kesehatan Anak'
	elif obj[2] == 'KELOPAK MATA KANAN BENGKAK':
		return 'Mata'
	elif obj[2] == 'KELUAR BINTIK DI BADAN':
		return 'Kesehatan Anak'
	elif obj[2] == 'KELUAR CAIRAN HIDUNG':
		return 'THT'
	elif obj[2] == 'KELUAR DARAH':
		return 'Kebidanan dan Kandungan'
	elif obj[2] == 'KELUAR FLEK':
		return 'Kebidanan dan Kandungan'
	elif obj[2] == 'KEMASUKAN KERTAS ':
		return 'THT'
	elif obj[2] == 'KAKI KESELEO':
		return 'Rehabilitasi Medik'
	elif obj[2] == 'KAKI KANAN BAAL':
		return 'Syaraf'
	elif obj[2] == 'KAKI GATAL':
		return 'Kulit dan Kelamin'
	elif obj[2] == 'JARI TANGAN KAKU':
		return 'Syaraf'
	elif obj[2] == 'IMUNISASI DPT':
		return 'Kesehatan Anak'
	elif obj[2] == 'IMUNISASI ROTAVIRUS':
		return 'Kesehatan Anak'
	elif obj[2] == 'INFEKSI TELINGA':
		return 'THT'
	elif obj[2] == 'INGIN TAMPIL CANTIK':
		return 'Kulit dan Kelamin'
	elif obj[2] == 'IPD':
		return 'Kesehatan Anak'
	elif obj[2] == 'IRITASI MATA':
		return 'Mata'
	elif obj[2] == 'IUD':
		return 'Kebidanan dan Kandungan'
	elif obj[2] == 'JAMUR':
		return 'Kulit dan Kelamin'
	elif obj[2] == 'JARI TIDAK BISA DIGERAKKAN':
		return 'Syaraf'
	elif obj[2] == 'KAKI BENGKAK DAN SAKIT':
		return 'Penyakit Dalam'
	elif obj[2] == 'JARI TELUNJUK BENGKAK':
		return 'Kardiologi atau Jantung'
	elif obj[2] == 'JARI TIDAK BISA DI TEKUK':
		return 'Penyakit Dalam'
	elif obj[2] == 'JATUH TERKENA KEPALA':
		return 'Kesehatan Anak'
	elif obj[2] == 'JATUNG BERDEBAR':
		return 'Kardiologi atau Jantung'
	elif obj[2] == 'JEMPOL BENGKAK':
		return 'Kulit dan Kelamin'
	elif obj[2] == 'JERAWAT KULIT KEPALA':
		return 'Kulit dan Kelamin'
	elif obj[2] == 'AGAK PEGAL':
		return 'Kardiologi atau Jantung'
	elif obj[2] == 'KADAR GULA TINGGL':
		return 'Penyakit Dalam'
	elif obj[2] == 'KEMBUNG':
		return 'Penyakit Dalam'
	elif obj[2] == 'KEMUNGKINAN CACAR ':
		return 'Kesehatan Anak'
	elif obj[2] == 'KENCING TIDAK LANCAR KALO TIDAK MINUM OBAT':
		return 'Bedah Urologi'
	elif obj[2] == 'MASALAH KULIT':
		return 'Kulit dan Kelamin'
	elif obj[2] == 'KONSUL PRE CURRETAGE':
		return 'Penyakit Dalam'
	elif obj[2] == 'SIKLUS HAID':
		return 'Kebidanan dan Kandungan'
	elif obj[2] == 'KONSUL TERAPI ':
		return 'Rehabilitasi Medik'
	elif obj[2] == 'KONSUL TERAPI':
		return 'Rehabilitasi Medik'
	elif obj[2] == 'KONSUL TULANG':
		return 'Bedah Tulang atau Orthopedi'
	elif obj[2] == 'KONSUL TULANG BELAKANG':
		return 'Rehabilitasi Medik'
	elif obj[2] == 'KONSUL TYPOID':
		return 'Kesehatan Anak'
	elif obj[2] == 'TERAPI WICARA':
		return 'Tumbuh Kembang Anak (REMEDIA)'
	elif obj[2] == 'KONSULEN DR DIAN':
		return 'THT'
	elif obj[2] == 'KONSUL LUKA':
		return 'Kulit dan Kelamin'
	elif obj[2] == 'SUKA MIMISAN':
		return 'THT'
	elif obj[2] == 'KONSULTASI ':
		return 'Sub Spesialis Bedah Tumor ( Onkologi )'
	elif obj[2] == 'KONSULTASI GIGI':
		return 'Gigi dan Mulut'
	elif obj[2] == 'BENJOLAN KULIT':
		return 'Bedah'
	elif obj[2] == 'BELUM HAMIL':
		return 'Kebidanan dan Kandungan'
	elif obj[2] == 'HSG':
		return 'Kebidanan dan Kandungan'
	elif obj[2] == 'KANTUNG KEMIH ':
		return 'Bedah Urologi'
	elif obj[2] == 'KOLESTEROL':
		return 'Penyakit Dalam'
	elif obj[2] == 'MELAHIRKAN':
		return 'Kebidanan dan Kandungan'
	elif obj[2] == 'KONSUL KUKU TANGAN':
		return 'Kulit dan Kelamin'
	elif obj[2] == 'KEPALA GATAL':
		return 'Kulit dan Kelamin'
	elif obj[2] == 'REUMATIK ':
		return 'Penyakit Dalam'
	elif obj[2] == 'KEPALA PUSING':
		return 'Syaraf'
	elif obj[2] == 'KEPALA PUSING ':
		return 'Syaraf'
	elif obj[2] == 'KEPALA TERBENTUR':
		return 'Kesehatan Anak'
	elif obj[2] == 'KERAM PERUT':
		return 'Kulit dan Kelamin'
	elif obj[2] == 'KESEDAK DURI':
		return 'THT'
	elif obj[2] == 'KESEMUTAN DI TANGAN':
		return 'Penyakit Dalam'
	elif obj[2] == 'KETOMBE DI KULIT KEPALA':
		return 'Kulit dan Kelamin'
	elif obj[2] == 'KETUSUK DURI':
		return 'THT'
	elif obj[2] == 'HABIS INSISI HORDEULUM':
		return 'Mata'
	elif obj[2] == 'KB ':
		return 'Kebidanan dan Kandungan'
	elif obj[2] == 'KONSULTASI KESEHATAN JIWA':
		return 'Kesehatan Jiwa'
	elif obj[2] == 'KONSUL ':
		return 'Tumbuh Kembang Anak (REMEDIA)'
	elif obj[2] == 'KETINGGALAN KAPAS':
		return 'THT'
	elif obj[2] == 'KONSUL BERAT BADAN':
		return 'Kesehatan Anak'
	elif obj[2] == 'KONSUL DR HERLINA':
		return 'Rehabilitasi Medik'
	elif obj[2] == 'KONSUL EVALUASI TERAPI':
		return 'Bedah Tulang atau Orthopedi'
	elif obj[2] == 'KONSUL HIPERBILIRUBIN':
		return 'Kesehatan Anak'
	elif obj[2] == 'JALAN JINJIT':
		return 'Tumbuh Kembang Anak (REMEDIA)'
	elif obj[2] == 'WASIR ':
		return 'Bedah'
	else: return 'Bedah'
