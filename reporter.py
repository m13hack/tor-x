from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import argparse

def generate_report(data, output_file):
    c = canvas.Canvas(output_file, pagesize=letter)
    width, height = letter
    c.drawString(72, height - 72, "Report")
    c.drawString(72, height - 100, data)
    c.save()

def main():
    parser = argparse.ArgumentParser(description='Generate a PDF report.')
    parser.add_argument('--data', required=True, help='Data to include in the report')
    parser.add_argument('--output', required=True, help='Output PDF file')
    args = parser.parse_args()

    generate_report(args.data, args.output)
    print(f'Report saved to {args.output}')

if __name__ == '__main__':
    main()
