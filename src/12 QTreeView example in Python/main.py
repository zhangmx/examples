from os.path import expanduser
from PyQt6.QtWidgets import QApplication, QTreeView
from PyQt6.QtGui import QFileSystemModel

home_directory = expanduser('~')

app = QApplication([])

model = QFileSystemModel()
model.setRootPath(home_directory)

view = QTreeView()
view.setModel(model)
view.setRootIndex(model.index(home_directory))
view.show()

app.exec()
