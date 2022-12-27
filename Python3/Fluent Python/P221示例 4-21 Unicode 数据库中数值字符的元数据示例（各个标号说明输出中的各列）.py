import unicodedata
import re

re_digit = re.compile(r'\d')

sample = '1\xbc\xb2\u0969\u136b\u216b\u2466\u2480\u3285'

for char in sample:
    try:
        print('U+%04x' % ord(char),
        char.center(6),
        're_dig' if re_digit.match(char) else '-',
        'isdig' if char.isdigit() else '-',
        format(unicodedata.numeric(char), '5.2f'),
        unicodedata.name(char),
        sep='\t',
        )
    except Exception:
        pass

# U+0031	  1   	re_dig	isdig	 1.00	DIGIT ONE
# U+00bc	  ¼   	-	-	 0.25	VULGAR FRACTION ONE QUARTER
# U+00b2	  ²   	-	isdig	 2.00	SUPERSCRIPT TWO
# U+0969	  ३   	re_dig	isdig	 3.00	DEVANAGARI DIGIT THREE
# U+136b	  ፫   	-	isdig	 3.00	ETHIOPIC DIGIT THREE
# U+216b	  Ⅻ   	-	-	12.00	ROMAN NUMERAL TWELVE
# U+2466	  ⑦   	-	isdig	 7.00	CIRCLED DIGIT SEVEN
# U+2480	  ⒀   	-	-	13.00	PARENTHESIZED NUMBER THIRTEEN
# U+3285	  ㊅   	-	-	 6.00	CIRCLED IDEOGRAPH SIX
# > 