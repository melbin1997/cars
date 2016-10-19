a=[u'-Select Brand-\nMaruti\nHyundai\nHonda\nToyota\nMahindra\nTata\nFord\nChevrolet\nRenault\nVolkswagen\nNissan\nDatsun\n-All Brands-\nAbarth\nAston Martin\nAudi\nBentley\nBMW\nBugatti\nCaterham\nChevrolet\nConquest\nDatsun\nDC\nFerrari\nFiat\nForce\nFord\nHonda\nHyundai\nICML\nIsuzu\nJaguar\nJeep\nKoenigsegg\nLamborghini\nLand Rover\nMahindra\nMahindra Ssangyong\nMaruti\nMaserati\nMercedes-Benz\nMini\nMitsubishi\nNissan\nPorsche\nPremier\nRenault\nRolls-Royce\nSkoda\nTata\nTesla\nToyota\nVolkswagen\nVolvo']
a=[a[0].encode('UTF8') for x in a]
a=a[0].split('\n')
print a[14:]
#b=a[0].replace("u'-Select Brand-\n"," ")
#b=b.split('\n')
#print type(b)