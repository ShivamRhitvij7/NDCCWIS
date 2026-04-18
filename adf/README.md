# Azure Data Factory (ADF) Pipeline Structure

This directory contains the Azure Data Factory pipeline definitions, configurations, and supporting files for the NDCCWIS project.

## Directory Structure

```
adf/
├── pipelines/              # Pipeline definitions (JSON)
├── datasets/               # Dataset definitions (JSON)
├── linkedServices/         # Linked service definitions (JSON)
├── dataflows/             # Data flow definitions (JSON)
├── integrationRuntimes/   # Integration runtime configurations
├── triggers/              # Trigger definitions (JSON)
├── templates/             # Reusable ARM templates
├── scripts/               # Deployment scripts (PowerShell, Python)
├── config/                # Environment-specific configurations
└── README.md              # This file
```

## Components

### Pipelines
Located in `adf/pipelines/`
- Contains main pipeline definitions
- Orchestrates data movement and transformation activities
- Example: `SampleCopyPipeline.json`

### Datasets
Located in `adf/datasets/`
- Defines data sources and sinks
- Supports multiple formats (CSV, Parquet, SQL, etc.)
- Example: `SampleCSVDataset.json`, `SampleSqlDataset.json`

### Linked Services
Located in `adf/linkedServices/`
- Connection information to external services
- Stores authentication credentials (Azure Key Vault recommended)
- Example: `AzureDataLakeStorageGen2.json`, `AzureSqlDatabase.json`

### Data Flows
Located in `adf/dataflows/`
- Visual data transformations
- Code-free transformation logic
- Maps inputs to outputs through transformation activities

### Integration Runtimes
Located in `adf/integrationRuntimes/`
- Azure Integration Runtime (for cloud services)
- Self-hosted Integration Runtime (for on-premises)
- Configuration files for compute resources

### Triggers
Located in `adf/triggers/`
- Schedule-based triggers (time-based)
- Tumbling window triggers
- Event-based triggers
- Example: `DailyTrigger.json`

### Templates
Located in `adf/templates/`
- Reusable ARM templates for infrastructure
- Parameter templates for common patterns
- Shared deployment configurations

### Scripts
Located in `adf/scripts/`
- Deployment automation scripts
- Setup and configuration scripts
- Monitoring and maintenance scripts
- Example: `deploy.ps1`

### Configuration
Located in `adf/config/`
- Environment-specific settings (dev, test, prod)
- Parameter files for different deployments
- Example: `dev-config.json`, `prod-config.json`

## Getting Started

1. **Set up Linked Services**: Configure connections to your data sources in `linkedServices/`
2. **Define Datasets**: Create datasets in `datasets/` that reference your linked services
3. **Create Pipelines**: Build pipelines in `pipelines/` that use datasets and activities
4. **Configure Triggers**: Set up triggers in `triggers/` to schedule pipeline execution
5. **Deploy**: Use scripts in `scripts/` to deploy to Azure

## Deployment

### Using PowerShell
```bash
.\scripts\deploy.ps1 -ResourceGroupName "myResourceGroup" `
                     -FactoryName "myDataFactory" `
                     -Location "eastus" `
                     -Environment "dev"
```

### Using Azure CLI
```bash
az datafactory create --resource-group myResourceGroup --factory-name myDataFactory
```

## Best Practices

- **Parameterize**: Use parameters for environment-specific values
- **Version Control**: Commit all JSON definitions to Git
- **Naming Conventions**: Use consistent naming for pipelines, datasets, and linked services
- **Security**: Store sensitive data in Azure Key Vault
- **Documentation**: Add descriptions to pipelines and activities
- **Testing**: Test pipelines in dev environment before production deployment
- **Monitoring**: Set up alerts and logging for pipeline runs

## References

- [Azure Data Factory Documentation](https://docs.microsoft.com/en-us/azure/data-factory/)
- [ADF JSON Schema](https://docs.microsoft.com/en-us/azure/data-factory/concepts-pipelines-activities)
- [ADF Best Practices](https://docs.microsoft.com/en-us/azure/data-factory/best-practices)
