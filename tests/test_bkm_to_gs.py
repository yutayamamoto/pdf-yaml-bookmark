import unittest

# Workaround
import pathlib
import sys
sys.path.append(str(pathlib.Path(__file__).parent.parent) + "/src")

from pdf_yaml_bookmark import bkm_to_yaml
from pdf_yaml_bookmark import yaml_to_gs

sample_bkm = '''\
# this is a comment
First Chapter 1
    First section 1
        Second section 1
+5
First Chapter 1
    First section 1
    Second section 1\
'''

def fmtGsString(s):
    return "FEFF" + s.encode("utf-16-be").hex()
    # return s

sample_gs=f'''\
[/Page 1 /View [/XYZ null null null] /Title <{fmtGsString("First Chapter")}> /Count 1 /OUT pdfmark
[/Page 1 /View [/XYZ null null null] /Title <{fmtGsString("First section")}> /Count 1 /OUT pdfmark
[/Page 1 /View [/XYZ null null null] /Title <{fmtGsString("Second section")}> /Count 0 /OUT pdfmark
[/Page 6 /View [/XYZ null null null] /Title <{fmtGsString("First Chapter")}> /Count 2 /OUT pdfmark
[/Page 6 /View [/XYZ null null null] /Title <{fmtGsString("First section")}> /Count 0 /OUT pdfmark
[/Page 6 /View [/XYZ null null null] /Title <{fmtGsString("Second section")}> /Count 0 /OUT pdfmark\
'''

class TestBkmToYaml(unittest.TestCase):
    def test_bkm_to_yaml(self):
        self.assertEqual(yaml_to_gs(bkm_to_yaml(sample_bkm)), sample_gs)

    def helper_heading_to_assertion(self, heading):
        self.assertEqual(yaml_to_gs(bkm_to_yaml(heading + " 1")), f"[/Page 1 /View [/XYZ null null null] /Title <{fmtGsString(heading)}> /Count 0 /OUT pdfmark")

    def test_bkm_to_yaml_special_chars(self):
        self.helper_heading_to_assertion('Title: with a colon')
        self.helper_heading_to_assertion('Colon: with "double"')
        self.helper_heading_to_assertion("Colon: with 'single'")
        # Currently not supported:
        # self.helper_heading_to_assertion("Colon: 'with' \"both\"")

