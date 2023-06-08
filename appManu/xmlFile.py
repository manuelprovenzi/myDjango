from .oggetto import libro
from .oggetto import cd
from .oggetto import oggetto


import xml.etree.cElementTree as et

class XMLSerializer:
    def __init__(self,nomeFile):
        self.fileXML = open(nomeFile,"rt")
        self.listLibri,self.listCD = self.Serialize()

    def Serialize(self):
        tree=et.parse(self.fileXML)
        root = tree.getroot()
        catalogo_libri = root.find('catalogo_libri')

        arrayLibri = list()

        for el in catalogo_libri.findall('libro'):
            #print('-------------------')
            l = libro()
            for value in el.attrib.items():
                l.add(value[0],value[1])
                break
            for ch in list(el):
                #print('{:>15}: {:<30}'.format(ch.tag, ch.text)) 
                l.add(ch.tag,ch.text)
            arrayLibri.append(l)
            del l    
        
        catalogo_cd = root.find('CATALOGO_CD')

        arrayCD = list()

        for el in catalogo_cd.findall('CD'):
            #print('-------------------')
            cdTmp = cd()
            for value in el.attrib.items():
                cdTmp.add(value[0],value[1])
                break
            for ch in list(el):
                #print('{:>15}: {:<30}'.format(ch.tag, ch.text)) 
                cdTmp.add(ch.tag,ch.text)
            arrayCD.append(cdTmp)
            del cdTmp    
        
        return arrayLibri,arrayCD

