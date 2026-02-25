Write-Host "Checking environment..."

docker --version
docker compose version

if ($LASTEXITCODE -ne 0) {
    Write-Host "Docker not available"
    exit 1
}

Write-Host "Docker OK"