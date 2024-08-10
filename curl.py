#CURL POST
# # Define la URL y el encabezado de autorización para el servicio dos
# $uri = "http://127.0.0.1:5000/logs"
# $headers = @{
#     "Authorization" = "service2_token"  # Asegúrate de usar el token correcto para el servicio dos
# }

# # Define el cuerpo del mensaje de log
# $body = @{
#     "timestamp" = "2024-08-10T14:00:00"
#     "service_name" = "Service2"
#     "severity" = "INFO"
#     "message" = "Mensaje de log desde el servicio dos"
# } | ConvertTo-Json

# # Envía el log usando Invoke-RestMethod
# $response = Invoke-RestMethod -Uri $uri -Method Post -Headers $headers -Body $body -ContentType "application/json"

# # Muestra la respuesta del servidor
# $response

# #CURL GET
# # Define la URL de la consulta GET
# $uri = "http://127.0.0.1:5000/logs?start_date=2024-08-01T00:00:00&end_date=2024-08-10T23:59:59"

# # Define el encabezado de autorización
# $headers = @{
#     "Authorization" = "service2_token"  # Asegúrate de usar el token correcto para el servicio dos
# }

# # Realiza la solicitud GET
# $response = Invoke-RestMethod -Uri $uri -Method Get -Headers $headers

# # Muestra la respuesta del servidor
# $response