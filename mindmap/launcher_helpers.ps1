param(
  [Parameter(Mandatory = $true)]
  [ValidateSet("select-port", "wait-ready")]
  [string]$Action,
  [int]$Port = 0,
  [int]$TimeoutSeconds = 45
)

$ErrorActionPreference = "Stop"

if ($Action -eq "select-port") {
  $listener = [System.Net.Sockets.TcpListener]::new([System.Net.IPAddress]::Loopback, 0)
  $listener.Start()
  try {
    [Console]::Out.WriteLine($listener.LocalEndpoint.Port)
  } finally {
    $listener.Stop()
  }
  exit 0
}

$deadline = [DateTime]::UtcNow.AddSeconds($TimeoutSeconds)
$uri = "http://127.0.0.1:$Port/api/config"
while ([DateTime]::UtcNow -lt $deadline) {
  try {
    $config = Invoke-RestMethod -Uri $uri -TimeoutSec 2
    if (($config.available_modes -contains "owner") -and ($config.owner_snapshot_read_only -eq $true)) {
      exit 0
    }
  } catch {
    # The preview process can need a moment to load the selected snapshots.
  }
  Start-Sleep -Milliseconds 500
}
[Console]::Error.WriteLine("The preview server did not expose its read-only owner snapshot within $TimeoutSeconds seconds.")
exit 1
