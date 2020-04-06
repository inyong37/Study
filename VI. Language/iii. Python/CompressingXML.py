# 2020-04-06-Mon
# Source code
# https://www.example-code.com/python/xml_compress_content.asp
# Test xml
# http://www.chilkatsoft.com/data/compress1.xml

import sys
import chilkat

xml = chilkat.CkXml()

#  The sample input XML is available at http://www.chilkatsoft.com/data/compress1.xml
success = xml.LoadXmlFile("./compress1.xml")
if (success != True):
    print(xml.lastErrorText())
    sys.exit()

#  Navigate to the "fox" node, which is the 1st child:
success = xml.FirstChild2()

#  Zip compress the content:
success = xml.ZipContent()

#  Navigate back to the root:
xml.GetRoot2()

#  Examine the new XML document:
print(xml.getXml())

#  This is the XML w/ the compressed content in Base64 encoded format:

#  Now uncompress and show that the original content was restored:
success = xml.FirstChild2()
success = xml.UnzipContent()
xml.GetRoot2()
print(xml.getXml())
