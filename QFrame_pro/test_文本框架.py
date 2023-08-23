from PyQt5.QtGui import QTextDocument, QTextCursor
from PyQt5.QtWidgets import QApplication

app = QApplication([])

# 创建一个文档对象
document = QTextDocument()

# 获取文档的根框架
root_frame = document.rootFrame()

# 在根框架中添加文本内容
cursor = QTextCursor(root_frame)
cursor.insertText("Hello, this is a QTextDocument example.")

# 显示文档内容
print(document.toPlainText())

app.exec_()

QTextCursor.MoveOperation()
