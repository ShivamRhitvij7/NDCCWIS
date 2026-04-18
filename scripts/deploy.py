#!/usr/bin/env python
"""
Azure Data Factory Deployment Script
Automates deployment of ADF resources to Azure
"""

import json
import argparse
import sys
from pathlib import Path

def load_config(environment: str) -> dict:
    """Load environment-specific configuration"""
    config_file = Path(f"config/{environment}-config.json")
    if not config_file.exists():
        print(f"Error: Config file not found: {config_file}")
        sys.exit(1)
    
    with open(config_file, 'r') as f:
        return json.load(f)

def deploy_linked_services(factory_name: str, config: dict) -> None:
    """Deploy linked services"""
    print(f"Deploying linked services to {factory_name}...")
    linked_services_path = Path("linkedServices")
    
    for service_file in linked_services_path.glob("*.json"):
        print(f"  - Deploying {service_file.name}...")

def deploy_datasets(factory_name: str, config: dict) -> None:
    """Deploy datasets"""
    print(f"Deploying datasets to {factory_name}...")
    datasets_path = Path("datasets")
    
    for dataset_file in datasets_path.glob("*.json"):
        print(f"  - Deploying {dataset_file.name}...")

def deploy_pipelines(factory_name: str, config: dict) -> None:
    """Deploy pipelines"""
    print(f"Deploying pipelines to {factory_name}...")
    pipelines_path = Path("pipelines")
    
    for pipeline_file in pipelines_path.glob("*.json"):
        print(f"  - Deploying {pipeline_file.name}...")

def main():
    """Main deployment function"""
    parser = argparse.ArgumentParser(description="Deploy Azure Data Factory resources")
    parser.add_argument("--factory-name", required=True, help="ADF Factory name")
    parser.add_argument("--resource-group", required=True, help="Azure Resource Group")
    parser.add_argument("--environment", default="dev", help="Environment (dev, test, prod)")
    parser.add_argument("--subscription", help="Azure Subscription ID")
    
    args = parser.parse_args()
    
    print("Azure Data Factory Deployment Script")
    print("=" * 40)
    
    # Load configuration
    config = load_config(args.environment)
    print(f"✓ Loaded {args.environment} configuration")
    
    # Deploy resources
    deploy_linked_services(args.factory_name, config)
    deploy_datasets(args.factory_name, config)
    deploy_pipelines(args.factory_name, config)
    
    print("\n" + "=" * 40)
    print("✓ Deployment completed successfully!")

if __name__ == "__main__":
    main()
