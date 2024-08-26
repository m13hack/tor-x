import spacy
import argparse

nlp = spacy.load('en_core_web_sm')

def analyze(text):
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return entities

def main():
    parser = argparse.ArgumentParser(description='Analyze text for entities.')
    parser.add_argument('--text', required=True, help='Text to analyze')
    args = parser.parse_args()

    entities = analyze(args.text)
    for entity in entities:
        print(f'{entity[0]}: {entity[1]}')

if __name__ == '__main__':
    main()
