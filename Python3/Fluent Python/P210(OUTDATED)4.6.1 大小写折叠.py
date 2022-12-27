micro = 'μ'
print(name(micro))
#'MICRO SIGN'
micro_cf = micro.casefold()
print(name(micro_cf))
#'GREEK SMALL LETTER MU'
print(micro, micro_cf)
eszett = 'ß'
print(name(eszett))
#'LATIN SMALL LETTER SHARP S'
eszett_cf = eszett.casefold()
print(eszett, eszett_cf)
#('ß', 'ss')
