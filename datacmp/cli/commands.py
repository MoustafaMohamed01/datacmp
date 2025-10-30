"""
Command-line interface for Datacmp.
"""

import argparse
import sys
from pathlib import Path

from ..pipeline.runner import run_pipeline
from ..pipeline.config import get_default_config, save_config
from ..utils.logger import get_logger

logger = get_logger(__name__)


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Datacmp: Data cleaning and exploratory analysis tool",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  datacmp run data.csv --config config.yaml
  datacmp run data.csv --export cleaned.csv --report report.html
  datacmp init config.yaml
  
For more information, visit: https://github.com/MoustafaMohamed01/datacmp
        """
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Run command
    run_parser = subparsers.add_parser('run', help='Run data cleaning pipeline')
    run_parser.add_argument('input', help='Path to input CSV file')
    run_parser.add_argument('--config', '-c', help='Path to config YAML file')
    run_parser.add_argument('--export', '-e', help='Path to export cleaned CSV')
    run_parser.add_argument('--report', '-r', help='Path to export report (HTML or TXT)')
    run_parser.add_argument('--quiet', '-q', action='store_true', help='Suppress output')
    
    # Init command
    init_parser = subparsers.add_parser('init', help='Create default config file')
    init_parser.add_argument('output', nargs='?', default='datacmp_config.yaml',
                            help='Output config file path (default: datacmp_config.yaml)')
    
    # Version command
    version_parser = subparsers.add_parser('version', help='Show version information')
    
    args = parser.parse_args()
    
    if args.command == 'run':
        run_command(args)
    elif args.command == 'init':
        init_command(args)
    elif args.command == 'version':
        version_command()
    else:
        parser.print_help()
        sys.exit(1)


def run_command(args):
    """Execute run command."""
    try:
        input_path = Path(args.input)
        
        if not input_path.exists():
            print(f"Error: Input file not found: {input_path}")
            sys.exit(1)
        
        print(f"\n🚀 Running Datacmp pipeline on {input_path.name}...\n")
        
        run_pipeline(
            data=input_path,
            config_path=args.config,
            export_csv_path=args.export,
            export_report_path=args.report,
            verbose=not args.quiet
        )
        
        print("\n✅ Pipeline completed successfully!\n")
        
    except Exception as e:
        print(f"\n❌ Error: {e}\n")
        logger.error(f"Pipeline failed: {e}", exc_info=True)
        sys.exit(1)


def init_command(args):
    """Execute init command."""
    try:
        output_path = Path(args.output)
        
        if output_path.exists():
            response = input(f"{output_path} already exists. Overwrite? (y/n): ")
            if response.lower() != 'y':
                print("Cancelled.")
                return
        
        config = get_default_config()
        save_config(config, output_path)
        
        print(f"\n✅ Created default configuration file: {output_path}\n")
        print("Edit this file to customize your data cleaning pipeline.")
        
    except Exception as e:
        print(f"\n❌ Error: {e}\n")
        sys.exit(1)


def version_command():
    """Execute version command."""
    from .. import __version__, __author__
    
    print(f"\nDatacmp v{__version__}")
    print(f"Author: {__author__}")
    print("GitHub: https://github.com/MoustafaMohamed01/datacmp")
    print("License: MIT\n")


if __name__ == "__main__":
    main()