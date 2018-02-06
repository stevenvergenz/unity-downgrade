import yaml, copy

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

def transformTexMeta(inputData):

	newImporter = copy.deepcopy(inputData['TextureImporter'])

	newImporter['cubemapConvolutionExponent'] = 1.5
	del newImporter['maxTextureSizeSet']
	del newImporter['textureShape']
	newImporter['textureFormat'] = inputData['TextureImporter']['platformSettings'][0]['textureFormat']
	newImporter['buildTargetSettings'] = []
	del newImporter['compressionQualitySet']
	newImporter['rGBM'] = 0
	del newImporter['alphaUsage']
	newImporter['generateCubemap'] = 0
	newImporter['textureType'] = -1
	newImporter['cubemapConvolutionSteps'] = 7
	newImporter['serializedVersion'] = 2
	newImporter['allowsAlphaSplitting'] = inputData['TextureImporter']['platformSettings'][0]['allowsAlphaSplitting']
	del newImporter['textureFormatSet']
	del newImporter['platformSettings']
	del newImporter['mipmaps']['sRGBTexture']
	newImporter['mipmaps']['correctGamma'] = 0

	inputData['TextureImporter'] = newImporter