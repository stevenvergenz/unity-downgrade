import yaml

class MatFile(yaml.YAMLObject):

	yaml_tag = 'tag:unity3d.com,2011:21'

	def __init__(self, matDef):
		self.Material = matDef

	def transform(self):

		oldProps = self.Material['m_SavedProperties']
		self.Material['m_SavedProperties'] = {}
		newProps = self.Material['m_SavedProperties']

		for (typeName, mapList) in oldProps.items():

			if typeName[0:2] != 'm_':
				newProps[typeName] = mapList
				continue
			
			newMapList = []
			newProps[typeName] = newMapList
			for mapping in mapList:
				(name, mapDef) = mapping.popitem()
				newDef = {'first': {'name': name}, 'second': mapDef}
				newMapList.append(newDef)