from django.shortcuts import render
import folium

# Create your views here.

def leaflet_map(request):
    # Create the map
    cologne = folium.Map(location=[50.9375, 6.9603], zoom_start=10)

    # Add a marker for Cologne, Germany
    folium.Marker(
        location=[50.9375, 6.9603],
        popup="Cologne, Germany"
    ).add_to(cologne)

    # Convert the Folium map to HTML
    map_html = cologne._repr_html_()


    # Pass the map HTML to the template context
    context = {
        'map_html': map_html
    }

    # Render the template with the map
    return render(request, 'map_template.html', context)


