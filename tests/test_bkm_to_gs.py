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

sample_bkm_with_colon = '''\
# this is a comment
First Chapter 1
    First section 1
        Second section 1
        Title: with a colon 1
+5
First Chapter 1
    First section 1
    Second section 1\
'''

sample_gs_with_colon=f'''\
[/Page 1 /View [/XYZ null null null] /Title <{fmtGsString("First Chapter")}> /Count 1 /OUT pdfmark
[/Page 1 /View [/XYZ null null null] /Title <{fmtGsString("First section")}> /Count 2 /OUT pdfmark
[/Page 1 /View [/XYZ null null null] /Title <{fmtGsString("Second section")}> /Count 0 /OUT pdfmark
[/Page 1 /View [/XYZ null null null] /Title <{fmtGsString("Title: with a colon")}> /Count 0 /OUT pdfmark
[/Page 6 /View [/XYZ null null null] /Title <{fmtGsString("First Chapter")}> /Count 2 /OUT pdfmark
[/Page 6 /View [/XYZ null null null] /Title <{fmtGsString("First section")}> /Count 0 /OUT pdfmark
[/Page 6 /View [/XYZ null null null] /Title <{fmtGsString("Second section")}> /Count 0 /OUT pdfmark\
'''

class TestBkmToYaml(unittest.TestCase):
    def test_bkm_to_yaml(self):
        self.assertEqual(yaml_to_gs(bkm_to_yaml(sample_bkm)), sample_gs)

    def test_bkm_to_yaml_special_chars(self):
        self.assertEqual(yaml_to_gs(bkm_to_yaml(sample_bkm_with_colon)),
                         sample_gs_with_colon)

