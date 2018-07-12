#note: in running this code write like this- python google_nlp.py G:\\LifCare\\vision\\filteredtext.txt
import argparse
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import json
import io
import math
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'G:\\LifCare\\visionapi.json'

def entities_text(movie_review_filename):
    """Detects entities in the text."""
    client = language.LanguageServiceClient()

    #if isinstance(movie_review_filename, six.binary_type):
    #    movie_review_filename = movie_review_filename.decode('utf-8')
    with open(movie_review_filename, 'r') as review_file:
        # Instantiates a plain text document.
        content = review_file.read()
    # Instantiates a plain text document.
    document = types.Document(
        content=content,
        type=enums.Document.Type.PLAIN_TEXT)

    # Detects entities in the document. You can also analyze HTML with:
    #   document.type == enums.Document.Type.HTML
    entities = client.analyze_entities(document).entities

    # entity types from enums.Entity.Type
    entity_type = ('UNKNOWN', 'PERSON', 'LOCATION', 'ORGANIZATION',
                   'EVENT', 'WORK_OF_ART', 'CONSUMER_GOOD', 'OTHER')
    text_file = open("textnlp.txt", "w")
    for entity in entities:
        text_file.write(entity.name + " ")
    #    text_file.write('=' * 20)
    #    text_file.write(u'{:<16}: {}'.format('name', entity.name))
    #    text_file.write(u'{:<16}: {}'.format('type', entity_type[entity.type]))
    #  text_file.write(u'{:<16}: {}'.format('metadata', entity.metadata))
    #    text_file.write(u'{:<16}: {}'.format('salience', entity.salience))
    #    text_file.write(u'{:<16}: {}'.format('wikipedia_url',
    #          entity.metadata.get('wikipedia_url', '-')))
    # Print the results
  
if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        'movie_review_filename',
        help='movie review')
    args = parser.parse_args()

    entities_text(args.movie_review_filename)