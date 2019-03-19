class printClass:
    def __init__(self, classFile):
        self.classFile = classFile

    def class_handler(self, classDiagramFile):
        file = open(classDiagramFile, 'r').readlines()
        classList = [[]]
        for i, m in enumerate(file[1:-1]):  # remove 1st and last character
            if m == "\n":
                if i != len(file[1:-1]) - 1:
                    classList.append([])
            else:
                classList[-1].append(m)
        return classList

    def get_class_name(self, classArray):
        for listItem in classArray:  # for each list item in each class array,
            if "class" in listItem:
                return listItem[:listItem.index(" {")]

    def get_attributes(self, classArray):
        attributes = []
        for listItem in classArray:
            if ":" in listItem and "(" not in listItem:
                result = listItem.split(' ')
                attributes.append(result[4])
        return attributes

    def get_methods(self, classArray):
        methods = []
        for listItem in classArray:
            if "(" in listItem:
                methods.append(listItem[:listItem.index("\n")-2].strip())
        return methods  # result: ['size', 'add']

    def output_class(self, classItem):
        result = self.get_class_name(classItem) + ":\n  def __init__(self"

        for listItem in self.get_attributes(classItem):
            result += ', ' + listItem
        result += '):\n'
        for listItem in self.get_attributes(classItem):
            result += '    self.' + listItem + ' = ' + listItem + '\n'
        result += '\n'
        for listItem in self.get_methods(classItem):
            result += 'def ' + listItem + '(self):\n # Todo: incomplete\n   pass\n'
            result += '\n'
        return result

    def outputClasses(self):
        files = []
        for classItem in self.class_handler(self.classFile):
            files.append(self.get_class_name(classItem)[5:] + '.py')
        for classItem, file in zip(self.class_handler(self.classFile), files):
            result = self.output_class(classItem)
            with open(file, "w") as output:
                output.write(result)


printClass('classDiagram.txt').outputClasses()
