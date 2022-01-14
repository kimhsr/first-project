import folium

map = folium.Map(location=[37.494, 127.029], zoom_start=17)
map.save("./map.html")