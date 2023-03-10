# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'homeScr.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_homeScr(object):
    def setupUi(self, homeScr):
        homeScr.setObjectName("homeScr")
        homeScr.resize(941, 650)
        homeScr.setWhatsThis("")
        self.homeScrGrid = QtWidgets.QWidget(homeScr)
        self.homeScrGrid.setObjectName("homeScrGrid")
        self.gridLayout = QtWidgets.QGridLayout(self.homeScrGrid)
        self.gridLayout.setObjectName("gridLayout")
        self.tabMenus = QtWidgets.QTabWidget(self.homeScrGrid)
        self.tabMenus.setObjectName("tabMenus")
        self.stock_catTab = QtWidgets.QWidget()
        self.stock_catTab.setObjectName("stock_catTab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.stock_catTab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.SC_topLayoutMain = QtWidgets.QVBoxLayout()
        self.SC_topLayoutMain.setObjectName("SC_topLayoutMain")
        self.SC_topLayout = QtWidgets.QVBoxLayout()
        self.SC_topLayout.setObjectName("SC_topLayout")
        self.SC_lbl = QtWidgets.QLabel(self.stock_catTab)
        self.SC_lbl.setMaximumSize(QtCore.QSize(16777215, 70))
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setUnderline(True)
        self.SC_lbl.setFont(font)
        self.SC_lbl.setTextFormat(QtCore.Qt.AutoText)
        self.SC_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.SC_lbl.setObjectName("SC_lbl")
        self.SC_topLayout.addWidget(self.SC_lbl)
        self.SC_table = QtWidgets.QTableWidget(self.stock_catTab)
        self.SC_table.setObjectName("SC_table")
        self.SC_table.setColumnCount(3)
        self.SC_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        item.setFont(font)
        self.SC_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        item.setFont(font)
        self.SC_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        item.setFont(font)
        self.SC_table.setHorizontalHeaderItem(2, item)
        self.SC_table.horizontalHeader().setCascadingSectionResizes(False)
        self.SC_table.horizontalHeader().setDefaultSectionSize(256)
        self.SC_table.horizontalHeader().setStretchLastSection(True)
        self.SC_topLayout.addWidget(self.SC_table)
        self.SC_topLayoutMain.addLayout(self.SC_topLayout)
        self.SC_midLayoutMain = QtWidgets.QHBoxLayout()
        self.SC_midLayoutMain.setObjectName("SC_midLayoutMain")
        self.SC_midLayout = QtWidgets.QGridLayout()
        self.SC_midLayout.setContentsMargins(-1, -1, 20, -1)
        self.SC_midLayout.setHorizontalSpacing(25)
        self.SC_midLayout.setObjectName("SC_midLayout")
        self.SC_IdEbox = QtWidgets.QPlainTextEdit(self.stock_catTab)
        self.SC_IdEbox.setEnabled(True)
        self.SC_IdEbox.setMaximumSize(QtCore.QSize(65, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.SC_IdEbox.setFont(font)
        self.SC_IdEbox.setFrameShape(QtWidgets.QFrame.Box)
        self.SC_IdEbox.setReadOnly(True)
        self.SC_IdEbox.setPlainText("")
        self.SC_IdEbox.setObjectName("SC_IdEbox")
        self.SC_midLayout.addWidget(self.SC_IdEbox, 0, 0, 1, 1)
        self.SC_stockCatEbox = QtWidgets.QPlainTextEdit(self.stock_catTab)
        self.SC_stockCatEbox.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.SC_stockCatEbox.setFont(font)
        self.SC_stockCatEbox.setFrameShape(QtWidgets.QFrame.Box)
        self.SC_stockCatEbox.setPlainText("")
        self.SC_stockCatEbox.setObjectName("SC_stockCatEbox")
        self.SC_midLayout.addWidget(self.SC_stockCatEbox, 0, 1, 1, 1)
        self.SC_midLayout.setColumnStretch(0, 1)
        self.SC_midLayout.setColumnStretch(1, 10)
        self.SC_midLayoutMain.addLayout(self.SC_midLayout)
        self.SC_spinBox = QtWidgets.QSpinBox(self.stock_catTab)
        self.SC_spinBox.setMinimumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.SC_spinBox.setFont(font)
        self.SC_spinBox.setStyleSheet("")
        self.SC_spinBox.setMaximum(99999)
        self.SC_spinBox.setObjectName("SC_spinBox")
        self.SC_midLayoutMain.addWidget(self.SC_spinBox)
        self.SC_midLayoutMain.setStretch(0, 10)
        self.SC_midLayoutMain.setStretch(1, 1)
        self.SC_topLayoutMain.addLayout(self.SC_midLayoutMain)
        self.SC_topLayoutMain.setStretch(0, 10)
        self.SC_topLayoutMain.setStretch(1, 1)
        self.gridLayout_3.addLayout(self.SC_topLayoutMain, 0, 0, 1, 1)
        self.SC_downLayoutMain = QtWidgets.QHBoxLayout()
        self.SC_downLayoutMain.setContentsMargins(-1, -1, 0, -1)
        self.SC_downLayoutMain.setObjectName("SC_downLayoutMain")
        self.SC_plusBtn = QtWidgets.QPushButton(self.stock_catTab)
        font = QtGui.QFont()
        font.setPointSize(21)
        self.SC_plusBtn.setFont(font)
        self.SC_plusBtn.setStyleSheet("background-color: rgb(250, 175, 35); color: rgb(13, 13, 13);  ")
        self.SC_plusBtn.setObjectName("SC_plusBtn")
        self.SC_downLayoutMain.addWidget(self.SC_plusBtn)
        self.SC_downLayout2 = QtWidgets.QHBoxLayout()
        self.SC_downLayout2.setContentsMargins(80, -1, -1, -1)
        self.SC_downLayout2.setSpacing(80)
        self.SC_downLayout2.setObjectName("SC_downLayout2")
        self.SC_addBtn = QtWidgets.QPushButton(self.stock_catTab)
        self.SC_addBtn.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.SC_addBtn.setFont(font)
        self.SC_addBtn.setStyleSheet("background-color: rgb(250, 175, 35); color: rgb(13, 13, 13);  ")
        self.SC_addBtn.setObjectName("SC_addBtn")
        self.SC_downLayout2.addWidget(self.SC_addBtn)
        self.SC_downLayout1 = QtWidgets.QHBoxLayout()
        self.SC_downLayout1.setObjectName("SC_downLayout1")
        self.SC_updateBtn = QtWidgets.QPushButton(self.stock_catTab)
        self.SC_updateBtn.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.SC_updateBtn.setFont(font)
        self.SC_updateBtn.setStyleSheet("background-color: rgb(250, 175, 35); color: rgb(13, 13, 13);  ")
        self.SC_updateBtn.setObjectName("SC_updateBtn")
        self.SC_downLayout1.addWidget(self.SC_updateBtn)
        self.SC_deleteBtn = QtWidgets.QPushButton(self.stock_catTab)
        self.SC_deleteBtn.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.SC_deleteBtn.setFont(font)
        self.SC_deleteBtn.setStyleSheet("background-color: rgb(250, 175, 35); color: rgb(13, 13, 13);  ")
        self.SC_deleteBtn.setObjectName("SC_deleteBtn")
        self.SC_downLayout1.addWidget(self.SC_deleteBtn)
        self.SC_cancelBtn = QtWidgets.QPushButton(self.stock_catTab)
        self.SC_cancelBtn.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.SC_cancelBtn.setFont(font)
        self.SC_cancelBtn.setStyleSheet("background-color: rgb(250, 175, 35); color: rgb(13, 13, 13);  ")
        self.SC_cancelBtn.setObjectName("SC_cancelBtn")
        self.SC_downLayout1.addWidget(self.SC_cancelBtn)
        self.SC_downLayout2.addLayout(self.SC_downLayout1)
        self.SC_downLayoutMain.addLayout(self.SC_downLayout2)
        self.SC_downLayoutMain.setStretch(0, 1)
        self.SC_downLayoutMain.setStretch(1, 10)
        self.gridLayout_3.addLayout(self.SC_downLayoutMain, 1, 0, 1, 1)
        self.tabMenus.addTab(self.stock_catTab, "")
        self.stock_itemTab = QtWidgets.QWidget()
        self.stock_itemTab.setObjectName("stock_itemTab")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.stock_itemTab)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.SI_topLayout = QtWidgets.QVBoxLayout()
        self.SI_topLayout.setObjectName("SI_topLayout")
        self.SI_lbl = QtWidgets.QLabel(self.stock_itemTab)
        self.SI_lbl.setMaximumSize(QtCore.QSize(16777215, 70))
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setUnderline(True)
        self.SI_lbl.setFont(font)
        self.SI_lbl.setTextFormat(QtCore.Qt.AutoText)
        self.SI_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.SI_lbl.setObjectName("SI_lbl")
        self.SI_topLayout.addWidget(self.SI_lbl)
        self.SI_table = QtWidgets.QTableWidget(self.stock_itemTab)
        self.SI_table.setMinimumSize(QtCore.QSize(0, 327))
        self.SI_table.setObjectName("SI_table")
        self.SI_table.setColumnCount(7)
        self.SI_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        item.setFont(font)
        self.SI_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        item.setFont(font)
        self.SI_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        item.setFont(font)
        self.SI_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        item.setFont(font)
        self.SI_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        item.setFont(font)
        self.SI_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        item.setFont(font)
        self.SI_table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        item.setFont(font)
        self.SI_table.setHorizontalHeaderItem(6, item)
        self.SI_table.horizontalHeader().setCascadingSectionResizes(False)
        self.SI_table.horizontalHeader().setDefaultSectionSize(172)
        self.SI_table.horizontalHeader().setHighlightSections(True)
        self.SI_table.horizontalHeader().setMinimumSectionSize(49)
        self.SI_table.horizontalHeader().setSortIndicatorShown(False)
        self.SI_table.horizontalHeader().setStretchLastSection(True)
        self.SI_table.verticalHeader().setCascadingSectionResizes(False)
        self.SI_table.verticalHeader().setSortIndicatorShown(False)
        self.SI_table.verticalHeader().setStretchLastSection(False)
        self.SI_topLayout.addWidget(self.SI_table)
        self.gridLayout_4.addLayout(self.SI_topLayout, 0, 0, 1, 1)
        self.SI_mid1Layout = QtWidgets.QHBoxLayout()
        self.SI_mid1Layout.setSpacing(8)
        self.SI_mid1Layout.setObjectName("SI_mid1Layout")
        self.SI_idEbox = QtWidgets.QPlainTextEdit(self.stock_itemTab)
        self.SI_idEbox.setMaximumSize(QtCore.QSize(65, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.SI_idEbox.setFont(font)
        self.SI_idEbox.setFrameShape(QtWidgets.QFrame.Box)
        self.SI_idEbox.setReadOnly(True)
        self.SI_idEbox.setObjectName("SI_idEbox")
        self.SI_mid1Layout.addWidget(self.SI_idEbox)
        self.SI_itemNameEbox = QtWidgets.QPlainTextEdit(self.stock_itemTab)
        self.SI_itemNameEbox.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.SI_itemNameEbox.setFont(font)
        self.SI_itemNameEbox.setFrameShape(QtWidgets.QFrame.Box)
        self.SI_itemNameEbox.setObjectName("SI_itemNameEbox")
        self.SI_mid1Layout.addWidget(self.SI_itemNameEbox)
        self.SI_itemUnitEbox = QtWidgets.QPlainTextEdit(self.stock_itemTab)
        self.SI_itemUnitEbox.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.SI_itemUnitEbox.setFont(font)
        self.SI_itemUnitEbox.setFrameShape(QtWidgets.QFrame.Box)
        self.SI_itemUnitEbox.setObjectName("SI_itemUnitEbox")
        self.SI_mid1Layout.addWidget(self.SI_itemUnitEbox)
        self.SI_itemPriceEbox = QtWidgets.QPlainTextEdit(self.stock_itemTab)
        self.SI_itemPriceEbox.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.SI_itemPriceEbox.setFont(font)
        self.SI_itemPriceEbox.setFrameShape(QtWidgets.QFrame.Box)
        self.SI_itemPriceEbox.setObjectName("SI_itemPriceEbox")
        self.SI_mid1Layout.addWidget(self.SI_itemPriceEbox)
        self.SI_mid1Layout.setStretch(0, 1)
        self.SI_mid1Layout.setStretch(1, 5)
        self.SI_mid1Layout.setStretch(2, 3)
        self.SI_mid1Layout.setStretch(3, 2)
        self.gridLayout_4.addLayout(self.SI_mid1Layout, 1, 0, 1, 1)
        self.SI_mid2Layout = QtWidgets.QHBoxLayout()
        self.SI_mid2Layout.setObjectName("SI_mid2Layout")
        self.SI_categoryCbox = QtWidgets.QComboBox(self.stock_itemTab)
        self.SI_categoryCbox.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.SI_categoryCbox.setFont(font)
        self.SI_categoryCbox.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.SI_categoryCbox.setAcceptDrops(False)
        self.SI_categoryCbox.setAutoFillBackground(False)
        self.SI_categoryCbox.setMaxVisibleItems(15)
        self.SI_categoryCbox.setDuplicatesEnabled(False)
        self.SI_categoryCbox.setFrame(True)
        self.SI_categoryCbox.setObjectName("SI_categoryCbox")
        self.SI_categoryCbox.addItem("")
        self.SI_categoryCbox.addItem("")
        self.SI_categoryCbox.addItem("")
        self.SI_mid2Layout.addWidget(self.SI_categoryCbox)
        self.SI_addInfoEbox = QtWidgets.QPlainTextEdit(self.stock_itemTab)
        self.SI_addInfoEbox.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.SI_addInfoEbox.setFont(font)
        self.SI_addInfoEbox.setFrameShape(QtWidgets.QFrame.Box)
        self.SI_addInfoEbox.setPlainText("")
        self.SI_addInfoEbox.setObjectName("SI_addInfoEbox")
        self.SI_mid2Layout.addWidget(self.SI_addInfoEbox)
        self.SI_availCbox = QtWidgets.QComboBox(self.stock_itemTab)
        self.SI_availCbox.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.SI_availCbox.setFont(font)
        self.SI_availCbox.setMaxVisibleItems(15)
        self.SI_availCbox.setObjectName("SI_availCbox")
        self.SI_availCbox.addItem("")
        self.SI_availCbox.addItem("")
        self.SI_availCbox.addItem("")
        self.SI_mid2Layout.addWidget(self.SI_availCbox)
        self.gridLayout_4.addLayout(self.SI_mid2Layout, 2, 0, 1, 1)
        self.SI_downLayout = QtWidgets.QHBoxLayout()
        self.SI_downLayout.setContentsMargins(-1, -1, 0, -1)
        self.SI_downLayout.setObjectName("SI_downLayout")
        self.SI_plusBtn1 = QtWidgets.QPushButton(self.stock_itemTab)
        font = QtGui.QFont()
        font.setPointSize(21)
        self.SI_plusBtn1.setFont(font)
        self.SI_plusBtn1.setStyleSheet("background-color: rgb(250, 175, 35); color: rgb(13, 13, 13);  ")
        self.SI_plusBtn1.setObjectName("SI_plusBtn1")
        self.SI_downLayout.addWidget(self.SI_plusBtn1)
        self.SI_downLayout2 = QtWidgets.QHBoxLayout()
        self.SI_downLayout2.setContentsMargins(80, -1, -1, -1)
        self.SI_downLayout2.setSpacing(80)
        self.SI_downLayout2.setObjectName("SI_downLayout2")
        self.SI_addBtn1 = QtWidgets.QPushButton(self.stock_itemTab)
        self.SI_addBtn1.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.SI_addBtn1.setFont(font)
        self.SI_addBtn1.setStyleSheet("background-color: rgb(250, 175, 35); color: rgb(13, 13, 13);  ")
        self.SI_addBtn1.setObjectName("SI_addBtn1")
        self.SI_downLayout2.addWidget(self.SI_addBtn1)
        self.SI_downLayout1 = QtWidgets.QHBoxLayout()
        self.SI_downLayout1.setObjectName("SI_downLayout1")
        self.SI_updateBtn1 = QtWidgets.QPushButton(self.stock_itemTab)
        self.SI_updateBtn1.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.SI_updateBtn1.setFont(font)
        self.SI_updateBtn1.setStyleSheet("background-color: rgb(250, 175, 35); color: rgb(13, 13, 13);  ")
        self.SI_updateBtn1.setObjectName("SI_updateBtn1")
        self.SI_downLayout1.addWidget(self.SI_updateBtn1)
        self.SI_deleteBtn1 = QtWidgets.QPushButton(self.stock_itemTab)
        self.SI_deleteBtn1.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.SI_deleteBtn1.setFont(font)
        self.SI_deleteBtn1.setStyleSheet("background-color: rgb(250, 175, 35); color: rgb(13, 13, 13);  ")
        self.SI_deleteBtn1.setObjectName("SI_deleteBtn1")
        self.SI_downLayout1.addWidget(self.SI_deleteBtn1)
        self.SI_cancelBtn1 = QtWidgets.QPushButton(self.stock_itemTab)
        self.SI_cancelBtn1.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.SI_cancelBtn1.setFont(font)
        self.SI_cancelBtn1.setStyleSheet("background-color: rgb(250, 175, 35); color: rgb(13, 13, 13);  ")
        self.SI_cancelBtn1.setObjectName("SI_cancelBtn1")
        self.SI_downLayout1.addWidget(self.SI_cancelBtn1)
        self.SI_downLayout2.addLayout(self.SI_downLayout1)
        self.SI_downLayout.addLayout(self.SI_downLayout2)
        self.SI_downLayout.setStretch(0, 1)
        self.SI_downLayout.setStretch(1, 10)
        self.gridLayout_4.addLayout(self.SI_downLayout, 3, 0, 1, 1)
        self.tabMenus.addTab(self.stock_itemTab, "")
        self.gridLayout.addWidget(self.tabMenus, 0, 0, 1, 1)
        homeScr.setCentralWidget(self.homeScrGrid)

        self.retranslateUi(homeScr)
        self.tabMenus.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(homeScr)

    def retranslateUi(self, homeScr):
        _translate = QtCore.QCoreApplication.translate
        homeScr.setWindowTitle(_translate("homeScr", "Home"))
        self.SC_lbl.setAccessibleName(_translate("homeScr", "sddvsdv"))
        self.SC_lbl.setText(_translate("homeScr", "Stock Categories:"))
        item = self.SC_table.horizontalHeaderItem(0)
        item.setText(_translate("homeScr", "Id"))
        item = self.SC_table.horizontalHeaderItem(1)
        item.setText(_translate("homeScr", "Stock Category"))
        item = self.SC_table.horizontalHeaderItem(2)
        item.setText(_translate("homeScr", "Display Order"))
        self.SC_plusBtn.setText(_translate("homeScr", "+"))
        self.SC_addBtn.setText(_translate("homeScr", "Add"))
        self.SC_updateBtn.setText(_translate("homeScr", "Update"))
        self.SC_deleteBtn.setText(_translate("homeScr", "Delete"))
        self.SC_cancelBtn.setText(_translate("homeScr", "Cancel"))
        self.tabMenus.setTabText(self.tabMenus.indexOf(self.stock_catTab), _translate("homeScr", "Stock Categories"))
        self.SI_lbl.setAccessibleName(_translate("homeScr", "sddvsdv"))
        self.SI_lbl.setText(_translate("homeScr", "Stock Items:"))
        item = self.SI_table.horizontalHeaderItem(0)
        item.setText(_translate("homeScr", "Id"))
        item = self.SI_table.horizontalHeaderItem(1)
        item.setText(_translate("homeScr", "Item Name"))
        item = self.SI_table.horizontalHeaderItem(2)
        item.setText(_translate("homeScr", "Item Unit"))
        item = self.SI_table.horizontalHeaderItem(3)
        item.setText(_translate("homeScr", "Item Price"))
        item = self.SI_table.horizontalHeaderItem(4)
        item.setText(_translate("homeScr", "Category"))
        item = self.SI_table.horizontalHeaderItem(5)
        item.setText(_translate("homeScr", "Availability"))
        item = self.SI_table.horizontalHeaderItem(6)
        item.setText(_translate("homeScr", "Additional Information"))
        self.SI_categoryCbox.setItemText(0, _translate("homeScr", "Example 1"))
        self.SI_categoryCbox.setItemText(1, _translate("homeScr", "Example 2"))
        self.SI_categoryCbox.setItemText(2, _translate("homeScr", "Example 3"))
        self.SI_availCbox.setItemText(0, _translate("homeScr", "Example 1"))
        self.SI_availCbox.setItemText(1, _translate("homeScr", "Example 2"))
        self.SI_availCbox.setItemText(2, _translate("homeScr", "Example 3"))
        self.SI_plusBtn1.setText(_translate("homeScr", "+"))
        self.SI_addBtn1.setText(_translate("homeScr", "Add"))
        self.SI_updateBtn1.setText(_translate("homeScr", "Update"))
        self.SI_deleteBtn1.setText(_translate("homeScr", "Delete"))
        self.SI_cancelBtn1.setText(_translate("homeScr", "Cancel"))
        self.tabMenus.setTabText(self.tabMenus.indexOf(self.stock_itemTab), _translate("homeScr", "Stock Items"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    homeScr = QtWidgets.QMainWindow()
    ui = Ui_homeScr()
    ui.setupUi(homeScr)
    homeScr.show()
    sys.exit(app.exec_())
