single_map = str.maketrans(""",ƒ,,†ˆ‹‘’“”•––˜›""","""'f"*^<''""---~>""")

multi_map = str.maketrans({
'€': '<euro>',
'…': '...',
'OE': 'OE',
'™': '(TM)',
'oe': 'oe',
'‰': '<per mille>',
'‡': '**',
})

multi_map.update(single_map)

def dewinize(txt):
    """把Win1252符号替换成ASCII字符或序列"""
    return txt.translate(multi_map)

def asciize(txt):
    no_marks = shave_marks_latin(dewinize(txt))
    no_marks = no_marks.replace('ß', 'ss')
    return unicodedata.normalize('NFKC', no_marks)