# 2020-04-06-Mon
# Source code
# https://www.example-code.com/python/xml_encrypt_decrypt.asp
# Test code
# http://www.chilkatsoft.com/data/fox.xml

import sys
import chilkat

xml = chilkat.CkXml()

#  The sample input XML is available at http://www.chilkatsoft.com/data/fox.xml
success = xml.LoadXmlFile("./fox.xml")
if (success != True):
    print(xml.lastErrorText())
    sys.exit()

#  Navigate to the "fox1" node, which is the 1st child:
success = xml.FirstChild2()

#  Encrypt the content:
success = xml.EncryptContent("myPassword")

#  Navigate back to the root:
xml.GetRoot2()

#  Examine the new XML document:
print(xml.getXml())

#  This is the XML w/ the encrypted content:

#  Now decrypt and show that the original content was restored:
success = xml.FirstChild2()
success = xml.DecryptContent("myPassword")
xml.GetRoot2()
print(xml.getXml())

#  Now encrypt the content of the "fox2" node.
#  First navigate to the "fox2" child.
success = xml.FindChild2("fox2")
success = xml.EncryptContent("myPassword")
xml.GetRoot2()
print(xml.getXml())

#  This is the XML w/ the "fox2" encrypted content:

#  Notice that the *content* of the node is encrypted.  The child nodes are NOT encrypted.
#  This is intentional.  To encrypt the content + the subtrees rooted at a given node,
#  one would call ZipTree to transform the content and subtrees
#  to Base64-encoded compressed content, and then call
#  EncryptContent to encrypt.

#  Finally, decrypt the "fox2" content:
success = xml.FindChild2("fox2")
success = xml.DecryptContent("myPassword")
xml.GetRoot2()
print(xml.getXml())
