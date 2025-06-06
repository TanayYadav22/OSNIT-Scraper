import argparse
import json
from scrapers import linkedin, github, whois_lookup

def main():
    parser = argparse.ArgumentParser(description="OSINT Scraper Tool")
    parser.add_argument('--target', required=True, help='Target username or domain')
    parser.add_argument('--source', nargs='+', required=True, choices=['linkedin', 'github', 'whois'], help='Data sources')
    parser.add_argument('--output', help='Output file to save results in JSON')

    args = parser.parse_args()
    results = {}

    if 'linkedin' in args.source:
        results['linkedin'] = linkedin.scrape(args.target)
    if 'github' in args.source:
        results['github'] = github.scrape(args.target)
    if 'whois' in args.source:
        results['whois'] = whois_lookup.scrape(args.target)

    if args.output:
        with open(args.output, 'w') as f:
            json.dump(results, f, indent=2)
    else:
        print(json.dumps(results, indent=2))

if __name__ == '__main__':
    main()
