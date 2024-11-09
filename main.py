import requests

# URL del sitio Moodle para descargar grabaciones
url = "https://api.frankfurter.app/latest?symbols=CHF"



response = requests.get(url)

if response.status_code == 200:
    print("Grabaciones descargadas correctamente.")
    print (response.json())
else:
    print(f"Error al descargar las grabaciones. Código de estado: {response.status_code}")
