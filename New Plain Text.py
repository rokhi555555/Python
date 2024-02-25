import geo
ip = geo.getIP()
print(ip)

country = geo.getCountry(ip,'plain')
print(country)

country = geo.getCountry(ip,'json')
print(country)

geoData =geo.getGeodata(ip)
print(geoData)

ptrdata = geo.getPTR(ip)
print(ptrdata)

geo.showIpDetails('216.239.32.0')

geo.showCountryDetails('216.239.32.0')
