import argparse
import sys
from src.scraper import scrape
from src.analyzer import analyze
from src.reporter import generate_report
from src.integrator import integrate
from src.sanitizer import sanitize

def main():
    parser = argparse.ArgumentParser(
        description='Welcome to Tor-X! A friendly CLI tool for dark web data extraction and analysis.'
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # Scraper Command
    parser_scrape = subparsers.add_parser('scrape', help='Scrape data from an onion URL')
    parser_scrape.add_argument('--url', required=True, help='Onion URL to scrape')

    # Analyzer Command
    parser_analyze = subparsers.add_parser('analyze', help='Analyze text for entities')
    parser_analyze.add_argument('--text', required=True, help='Text to analyze')

    # Reporter Command
    parser_report = subparsers.add_parser('report', help='Generate a PDF report')
    parser_report.add_argument('--data', required=True, help='Data to include in the report')
    parser_report.add_argument('--output', required=True, help='Output PDF file')

    # Integrator Command
    parser_integrate = subparsers.add_parser('integrate', help='Integrate data with a SIEM tool')
    parser_integrate.add_argument('--data', required=True, help='Data to integrate')
    parser_integrate.add_argument('--siem', required=True, help='SIEM tool for integration')

    # Sanitizer Command
    parser_sanitize = subparsers.add_parser('sanitize', help='Sanitize sensitive information from text')
    parser_sanitize.add_argument('--text', required=True, help='Text to sanitize')

    # Parse Arguments
    args = parser.parse_args()

    try:
        if args.command == 'scrape':
            print(f'Scraping URL: {args.url}')
            result = scrape(args.url)
            print(result)
        elif args.command == 'analyze':
            print(f'Analyzing text...')
            entities = analyze(args.text)
            for entity in entities:
                print(f'{entity[0]}: {entity[1]}')
        elif args.command == 'report':
            print(f'Generating report...')
            generate_report(args.data, args.output)
            print(f'Report saved to {args.output}')
        elif args.command == 'integrate':
            print(f'Integrating data with {args.siem}...')
            integrate(args.data, args.siem)
        elif args.command == 'sanitize':
            print(f'Sanitizing text...')
            sanitized_text = sanitize(args.text)
            print(sanitized_text)
        else:
            print('Error: Unknown command')
            parser.print_help()
            sys.exit(1)
    except Exception as e:
        print(f'Error: {str(e)}')
        sys.exit(1)

if __name__ == '__main__':
    main()
