import phonenumbers
import opencage
import folium
number = "+919574224491"

from phonenumbers import geocoder

pepnumber=phonenumbers.parse(number)
location=geocoder.description_for_number(pepnumber, "en")
print(location)

from phonenumbers import carrier
service_pro = phonenumbers.parse(number)
print(carrier.name_for_number(service_pro, 'en'))

from opencage.geocoder import OpenCageGeocode

key="2f81b8e2ca254dd6b517237b83cdbd62"

geocoder=OpenCageGeocode(key)
query=str(location)
results=geocoder.geocode(query)
#print(results)

lat=results[0]["geometry"]["lat"]
lng=results[0]["geometry"]["lng"]

print(lat,lng)

mymap=folium.Map(location=[lat,lng], zoom_start=9)
folium.Marker([lat,lng], popup=location).add_to(mymap)

mymap.save("mylocation.html")



