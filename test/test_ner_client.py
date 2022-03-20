import unittest
from ner_client import NamedEntityClient
from test_doubles import NERModelTestDouble

"""
python -m pytest
"""


class TestNewClient(unittest.TestCase):
    def test_get_ents_return_directory_given_empty_string_causes_empty_spacy_doc_ents(self):
        model = NERModelTestDouble('eng')
        model.returns_doc_ents([])
        ner = NamedEntityClient(model)
        ents = ner.get_ents('')
        self.assertIsInstance(ents, dict)

    def test_get_ents_returns_dictionary_given_noempty_string_causes_empty_spacy_doc_ents(self):
        model = NERModelTestDouble('eng')
        model.returns_doc_ents([])
        ner = NamedEntityClient(model)
        ents = ner.get_ents('Madison is a city in Wisconsin')
        self.assertIsInstance(ents, dict)

    def test_get_ents_given_spacy_PERSIN_is_returned_serializes_to_person(self):
        model = NERModelTestDouble('eng')
        doc_ents = [{'text': 'Zhang San', 'label_': 'PERSON'}]
        model.returns_doc_ents(doc_ents)

        ner = NamedEntityClient(model)
        result = ner.get_ents('...')
        expected_result = {'ents': [{'ent': 'Zhang San','label': 'Person'}], 'html': ''}
        self.assertListEqual(result['ents'], expected_result['ents'])

    def test_get_ents_given_spacy_NORP_is_returned_serializes_to_Group(self):
        model = NERModelTestDouble('eng')
        doc_ents = [{'text': 'Entity', 'label_': 'NORP'}]
        model.returns_doc_ents(doc_ents)

        ner = NamedEntityClient(model)
        result = ner.get_ents('...')
        expected_result = {'ents': [{'ent': 'Entity', 'label': 'Group'}], 'html': ''}
        self.assertListEqual(result['ents'], expected_result['ents'])

    def test_get_ents_given_spacy_LOC_is_returned_serializes_to_Location(self):
        model = NERModelTestDouble('eng')
        doc_ents = [{'text': 'Shanghai', 'label_': 'LOC'}]
        model.returns_doc_ents(doc_ents)

        ner = NamedEntityClient(model)
        result = ner.get_ents('...')
        expected_result = {'ents': [{'ent': 'Shanghai', 'label': 'Location'}], 'html': ''}
        self.assertListEqual(result['ents'], expected_result['ents'])

    def test_get_ents_given_spacy_LANGUAGE_is_returned_serializes_to_Language(self):
        model = NERModelTestDouble('eng')
        doc_ents = [{'text': 'Cantonese', 'label_': 'LANGUAGE'}]
        model.returns_doc_ents(doc_ents)

        ner = NamedEntityClient(model)
        result = ner.get_ents('...')
        expected_result = {'ents': [{'ent': 'Cantonese', 'label': 'Language'}], 'html': ''}
        self.assertListEqual(result['ents'], expected_result['ents'])

    def test_get_ents_given_spacy_GPE_is_returned_serializes_to_Location(self):
        model = NERModelTestDouble('eng')
        doc_ents = [{'text': 'China', 'label_': 'GPE'}]
        model.returns_doc_ents(doc_ents)

        ner = NamedEntityClient(model)
        result = ner.get_ents('...')
        expected_result = {'ents': [{'ent': 'China', 'label': 'Location'}], 'html': ''}
        self.assertListEqual(result['ents'], expected_result['ents'])

    def test_get_ents_given_multiple_ents_serializes_all(self):
        model = NERModelTestDouble('eng')
        doc_ents = [{'text': 'China', 'label_': 'GPE'},{'text': 'Li Si', 'label_': 'PERSON'}]
        model.returns_doc_ents(doc_ents)

        ner = NamedEntityClient(model)
        result = ner.get_ents('...')
        expected_result = {'ents': [{'ent': 'China', 'label': 'Location'},
                                    {'ent': 'Li Si', 'label': 'Person'}], 'html': ''}
        self.assertListEqual(result['ents'], expected_result['ents'])