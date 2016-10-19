g1=[u'Ex-showroom Price New Delhi', u'` 3,85,00,000 Finance Quotes', u'City / Highway Mileage', u'5.2 kmpl / 10.9 kmpl', u'Fuel Type', u'Petrol', u'Engine Displacement', u'5950 cc', u'BHP', u'600bhp@5250rpm', u'Torque', u'900Nm@1250-4500rpm']
g2=[]
g3=0
while g3<len(g1):
	g2.append(g1[g3].encode('UTF8'))
	g3+=1
print g2