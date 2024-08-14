class Settings:
	def __init__(self):
		self.daily = True
		self.weekly = True
		self.monthly = True
		self.yearly = True
		self.thems = {
			'dark': {
				'tab_color': 'grey50',
				'send-btn_color': 'grey70',
				'etr_color': 'grey50',
				'lbl-frame_color': 'grey60',
				'output_color': "grey50"
			},
			'light': {
				'tab_color': 'grey90',
				'send-btn_color': 'grey80',
				'etr_color': 'grey90',
				'lbl-frame_color': 'grey80',
				'output_color': "grey90"
			}
		}
