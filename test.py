import unittest
from elementt import xml_parser_xpath

class TestXmlParser(unittest.TestCase):

    def test_no_brackets(self):
        sample_result = xml_parser_xpath()
        self.assertNotIn("<", sample_result)
        
    def test_no_word_xml(self):
        sample_result = xml_parser_xpath()
        self.assertNotIn("xml", sample_result)

    def test_result_list(self):
        sample_result = xml_parser_xpath()
        self.assertEqual(type(sample_result), type([]))

if __name__ == "__main__":
    unittest.main()
