x=2
karton_çevre=320
karton_uzun_kenar=50*x
ayraç_uzun_kenar=karton_uzun_kenar/10
ayrac_uzun_kenar=5*x
ayrac_kısa_kenar=karton_uzun_kenar/25
ayrac_kısa_kenar=2*x
karton_kısa_kenar=ayrac_kısa_kenar*15
karton_kısa_kenar=30*x
karton_çevre=2*(karton_uzun_kenar+karton_kısa_kenar)
x=2
ayrac_çevre=2*(ayrac_uzun_kenar+ayrac_kısa_kenar)
print(ayrac_çevre)