
$objetivo = "google.com"

$log = "C:\Scripts\log_red.txt"

$fechaHora = Get-Date -Format "yyyy-MM-dd HH:mm:ss"

if (Test-Connection -ComputerName $objetivo -Count 2 -Quiet) {
    $mensaje = "$fechaHora - Conexión exitosa con $objetivo"
} else {
    $mensaje = "$fechaHora - Falla en la conexión con $objetivo"
}

Add-Content -Path $log -Value $mensaje
