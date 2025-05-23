import unittest

# Workaround
import pathlib
import sys
sys.path.append(str(pathlib.Path(__file__).parent.parent) + "/src")

from pdf_yaml_bookmark import yaml_to_gs

sample_yaml = '''\
# this is a comment
-
 heading: First Chapter
 page: 1
 offset: 0
 children:
    -
     heading: First section
     page: 1
     offset: 0
     children:
        -
         heading: Second section
         page: 1
         offset: 0
         children:
-
 heading: First Chapter
 page: 1
 offset: 5
 children:
    -
     heading: First section
     page: 1
     offset: 5
     children:
    -
     heading: Second section
     page: 1
     offset: 5
     children:
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

class TestYamlToGs(unittest.TestCase):
    def test_yaml_to_gs(self):
        self.assertEqual(yaml_to_gs(sample_yaml), sample_gs)

