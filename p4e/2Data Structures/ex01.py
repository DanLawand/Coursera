text = "X-DSPAM-Confidence:    0.8475";

zeropos = text.find('0')
snum = text[zeropos:]
print(float(snum))
