#!/usr/bin/env python
"""
Azure Data Factory Deployment Script
Automates deployment of ADF resources to Azure
"""

import json
import argparse
import sys
from pathlib import Path
from azure.identity import DefaultAzureCredential
from azure.mgmt.datafactory import DataFactoryManagementClient
from azure.mgmt.resource import ResourceManagementClient

def load_config(environment: str) -> dict:
    """Load environment-specific configuration"""
    config_file = Path(f"config/{environment}-config.json")
    if not config_file.exists():
        print(f"Error: Config file not found: {config_file}")
        sys.exit(1)
    
    with open(config_file, 'r') as f:
        return json.load(f)

def deploy_linked_services(client: DataFactoryManagementClient, factory_name: str, resource_group: str, config: dict) -> None:
    """Deploy linked services"""
    print(f"Deploying linked services to {factory_name}...")
    linked_services_path = Path("linkedServices")
    
    for service_file in linked_services_path.glob("*.json"):
        with open(service_file, 'r') as f:
            service_def = json.load(f)
        
        service_name = service_file.stem  # Remove .json extension
        print(f"  - Deploying linked service: {service_name}...")
        
        client.linked_services.create_or_update(
            resource_group_name=resource_group,
            factory_name=factory_name,
            linked_service_name=service_name,
            linked_service={'properties': service_def['properties']}
        )
        print(f"    ✓ {service_name} deployed")

def deploy_datasets(client: DataFactoryManagementClient, factory_name: str, resource_group: str, config: dict) -> None:
    """Deploy datasets"""
    print(f"Deploying datasets to {factory_name}...")
    datasets_path = Path("datasets")
    
    for dataset_file in datasets_path.glob("*.json"):
        with open(dataset_file, 'r') as f:
            dataset_def = json.load(f)
        
        dataset_name = dataset_file.stem
        print(f"  - Deploying dataset: {dataset_name}...")
        
        client.datasets.create_or_update(
            resource_group_name=resource_group,
            factory_name=factory_name,
            dataset_name=dataset_name,
            dataset={'properties': dataset_def['properties']}
        )
        print(f"    ✓ {dataset_name} deployed")

def deploy_pipelines(client: DataFactoryManagementClient, factory_name: str, resource_group: str, config: dict) -> None:
    """Deploy pipelines"""
    print(f"Deploying pipelines to {factory_name}...")
    pipelines_path = Path("pipelines")
    
    for pipeline_file in pipelines_path.glob("*.json"):
        with open(pipeline_file, 'r') as f:
            pipeline_def = json.load(f)
        
        pipeline_name = pipeline_file.stem
        print(f"  - Deploying pipeline: {pipeline_name}...")
        
        client.pipelines.create_or_update(
            resource_group_name=resource_group,
            factory_name=factory_name,
            pipeline_name=pipeline_name,
            pipeline={'properties': pipeline_def['properties']}
        )
        print(f"    ✓ {pipeline_name} deployed")

def deploy_triggers(client: DataFactoryManagementClient, factory_name: str, resource_group: str, config: dict) -> None:
    """Deploy triggers"""
    print(f"Deploying triggers to {factory_name}...")
    triggers_path = Path("triggers")
    
    for trigger_file in triggers_path.glob("*.json"):
        with open(trigger_file, 'r') as f:
            trigger_def = json.load(f)
        
        trigger_name = trigger_file.stem
        print(f"  - Deploying trigger: {trigger_name}...")
        
        client.triggers.create_or_update(
            resource_group_name=resource_group,
            factory_name=factory_name,
            trigger_name=trigger_name,
            trigger={'properties': trigger_def['properties']}
        )
        print(f"    ✓ {trigger_name} deployed")

def main():
    """Main deployment function"""
    parser = argparse.ArgumentParser(description="Deploy Azure Data Factory resources")
    parser.add_argument("--factory-name", required=True, help="ADF Factory name")
    parser.add_argument("--resource-group", required=True, help="Azure Resource Group")
    parser.add_argument("--subscription-id", required=True, help="Azure Subscription ID")
    parser.add_argument("--environment", default="dev", help="Environment (dev, test, prod)")
    
    args = parser.parse_args()
    
    print("Azure Data Factory Deployment Script")
    print("=" * 40)
    
    # Authenticate
    credential = DefaultAzureCredential()
    
    # Create clients
    adf_client = DataFactoryManagementClient(credential, args.subscription_id)
    resource_client = ResourceManagementClient(credential, args.subscription_id)
    
    # Load configuration
    config = load_config(args.environment)
    print(f"✓ Loaded {args.environment} configuration")
    
    # Deploy resources in order
    deploy_linked_services(adf_client, args.factory_name, args.resource_group, config)
    deploy_datasets(adf_client, args.factory_name, args.resource_group, config)
    deploy_pipelines(adf_client, args.factory_name, args.resource_group, config)
    deploy_triggers(adf_client, args.factory_name, args.resource_group, config)
    
    print("\n" + "=" * 40)
    print("✓ Deployment completed successfully!")

if __name__ == "__main__":
    main()
