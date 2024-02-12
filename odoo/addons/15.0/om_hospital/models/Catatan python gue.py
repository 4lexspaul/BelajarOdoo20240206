# purchase_user_id = fields.Many2one(
#         'res.users', string='Purchase Representative',
#         domain=lambda self: [('groups_id', 'in', self.env.ref('stock.group_stock_user').id)],
#         states={'done': [('readonly', True)], 'cancel': [('readonly', True)]},
#         default=lambda self: self.env.user, related='purchase_id.user_id')

# 1) domain=lambda self: [('groups_id', 'in', self.env.ref('stock.group_stock_user').id)]
# Fungsi domain digunakan untuk mengatur domain pada field purchase_user_id.
# Domain ini membatasi pilihan user yang bisa dipilih dalam field tersebut.
# Dalam kasus ini, domain tersebut akan memfilter hanya user yang tergabung dalam grup dengan ID
# yang sesuai (dalam hal ini, grup dengan ID yang sesuai dari referensi 'stock.group_stock_user')
# yang dapat dipilih sebagai Purchase Representative. Artinya, hanya user dalam grup
# tersebut yang akan muncul dalam daftar pilihan.

# 2) default=lambda self: self.env.user
# Fungsi default digunakan untuk mengatur nilai default dari field purchase_user_id.
# Nilai default adalah user yang saat ini sedang menggunakan sistem.
# Dalam hal ini, ketika Anda membuat catatan baru (record) di stock.picking,
# nilai purchase_user_id akan diatur secara default sebagai user yang sedang masuk.
#
# Kedua fungsi ini bersifat opsional, tergantung pada kebutuhan bisnis Anda:
# Domain: Anda bisa menggunakan domain jika Anda ingin membatasi pilihan user yang dapat dipilih
# sebagai Purchase Representative. Jika Anda ingin semua user bisa dipilih tanpa batasan grup,
# Anda bisa menghapus bagian domain dari definisi field tersebut.
# Default: Penggunaan default berguna jika Anda ingin setiap kali membuat catatan baru,
# nilai purchase_user_id diisi dengan user yang sedang masuk. Jika Anda ingin field tersebut
# tetap kosong saat membuat catatan baru, Anda bisa menghapus bagian default dari definisi field tersebut.