# Azure Data Factory Deployment Script
# This script deploys ADF resources to Azure

param (
    [string]$ResourceGroupName = "myResourceGroup",
    [string]$FactoryName = "myDataFactory",
    [string]$Location = "eastus",
    [string]$Environment = "dev"
)

Write-Host "Starting Azure Data Factory deployment..."
Write-Host "Resource Group: $ResourceGroupName"
Write-Host "Factory Name: $FactoryName"
Write-Host "Location: $Location"
Write-Host "Environment: $Environment"

# Check if resource group exists
$resourceGroup = Get-AzResourceGroup -Name $ResourceGroupName -ErrorAction SilentlyContinue
if (-not $resourceGroup) {
    Write-Host "Creating resource group: $ResourceGroupName"
    New-AzResourceGroup -Name $ResourceGroupName -Location $Location
}

# Create or update Data Factory
Write-Host "Creating/updating Data Factory: $FactoryName"
$dataFactory = Set-AzDataFactoryV2 `
    -ResourceGroupName $ResourceGroupName `
    -Name $FactoryName `
    -Location $Location

Write-Host "Data Factory created/updated successfully"
Write-Host "Deployment complete!"
