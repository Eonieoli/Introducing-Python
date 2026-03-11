# import xml.etree.ElementTree as et

# tree = et.ElementTree(file='menu.xml')
# root = tree.getroot()
# print(root.tag)

# for child in root:
#     print('tag:', child.tag, 'attributes:', child.attrib)
#     for grandchild in child:
#         print('\ttag:', grandchild.tag, 'attributes:', grandchild.attrib)

# print(len(root))
# print(len(root[0]))


# # 보안되지 않은 parse
# from xml.etree.ElementTree import parse
# et = parse(xmlfile)

# # 보안된 parse
# from defusedxml.ElementTree import parse
# et = parse(xmlfile)