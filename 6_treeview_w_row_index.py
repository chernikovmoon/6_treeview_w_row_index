# Copyright (C) 2022 The Qt Company Ltd.
# SPDX-License-Identifier: LicenseRef-Qt-Commercial OR BSD-3-Clause

# Copyright (C) 2026 Modified by Ivan Chernikov
# SPDX-License-Identifier: BSD-3-Clause
from __future__ import annotations

import sys

from PySide6.QtGui import QStandardItem, QStandardItemModel
from PySide6.QtWidgets import QApplication, QMainWindow, QTreeView

class MyStandardItem(QStandardItem):
    def __init__(self, row_index: int, text: str):
        super().__init__(text)
        self.row_index = row_index
        self.text = text

"""PySide6 port of the widgets/tutorials/modelview/6_treeview example from Qt v6.x"""


#! [1]
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._standard_model = QStandardItemModel(self)
        self._tree_view = QTreeView(self)
        self.setCentralWidget(self._tree_view)

        # prepared_row = self.prepare_row("first", "second", "third")
        # item = self._standard_model.invisibleRootItem()
        # # adding a row to the invisible root item produces a root element
        # item.appendRow(prepared_row)
        #
        # second_row = self.prepare_row("111", "222", "333")
        # # adding a row to an item starts a subtree
        # prepared_row[0].appendRow(second_row)

        my_prepared_row = self.my_prepare_row(1, "first", "second", "third")
        item = self._standard_model.invisibleRootItem()
        # adding a row to the invisible root item produces a root element
        item.appendRow(my_prepared_row)

        second_row = self.my_prepare_row(2,"111", "222", "333")
        # adding a row to an item starts a subtree
        my_prepared_row[0].appendRow(second_row)

        self._tree_view.setModel(self._standard_model)
        self._tree_view.expandAll()

    @staticmethod
    def my_prepare_row(index, first, second, third):
        return [MyStandardItem(index, first), MyStandardItem(index, second),
                MyStandardItem(index, third)]

    # def prepare_row(self, index, first, second, third):
    #     return [MyStandardItem(first), MyStandardItem(second),
    #             QStandardItem(third)]
#! [1]


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())