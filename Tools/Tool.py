class QSSTool:
    @staticmethod
    def setQssToObject(file_path, obj):
        with open(file_path, 'r') as f:
            content = f.read()
            obj.setStyleSheet(content)
