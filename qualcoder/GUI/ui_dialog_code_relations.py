# Form implementation generated from reading ui file 'ui_dialog_code_relations.ui'
#
# Created by: PyQt6 UI code generator 6.2.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog_CodeRelations(object):
    def setupUi(self, Dialog_CodeRelations):
        Dialog_CodeRelations.setObjectName("Dialog_CodeRelations")
        Dialog_CodeRelations.setWindowModality(QtCore.Qt.WindowModality.NonModal)
        Dialog_CodeRelations.resize(859, 803)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog_CodeRelations)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(Dialog_CodeRelations)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 90))
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 90))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label_header = QtWidgets.QLabel(self.groupBox)
        self.label_header.setGeometry(QtCore.QRect(10, -4, 651, 26))
        self.label_header.setMinimumSize(QtCore.QSize(0, 26))
        self.label_header.setMaximumSize(QtCore.QSize(16777215, 26))
        self.label_header.setWordWrap(True)
        self.label_header.setObjectName("label_header")
        self.pushButton_exportcsv = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_exportcsv.setGeometry(QtCore.QRect(690, 30, 28, 28))
        self.pushButton_exportcsv.setText("")
        self.pushButton_exportcsv.setObjectName("pushButton_exportcsv")
        self.pushButton_calculate = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_calculate.setGeometry(QtCore.QRect(360, 30, 28, 28))
        self.pushButton_calculate.setText("")
        self.pushButton_calculate.setObjectName("pushButton_calculate")
        self.radioButton_this = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_this.setGeometry(QtCore.QRect(10, 30, 151, 23))
        self.radioButton_this.setChecked(True)
        self.radioButton_this.setObjectName("radioButton_this")
        self.radioButton_all = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_all.setGeometry(QtCore.QRect(10, 60, 161, 23))
        self.radioButton_all.setObjectName("radioButton_all")
        self.pushButton_select_files = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_select_files.setGeometry(QtCore.QRect(330, 30, 28, 28))
        self.pushButton_select_files.setText("")
        self.pushButton_select_files.setObjectName("pushButton_select_files")
        self.comboBox_relation_type = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_relation_type.setGeometry(QtCore.QRect(170, 60, 221, 25))
        self.comboBox_relation_type.setObjectName("comboBox_relation_type")
        self.comboBox_relation_type.addItem("")
        self.comboBox_relation_type.addItem("")
        self.comboBox_relation_type.addItem("")
        self.comboBox_relation_type.addItem("")
        self.comboBox_relation_type.addItem("")
        self.comboBox_relation_type.addItem("")
        self.comboBox_relation_type.addItem("")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(170, 30, 131, 22))
        self.label.setObjectName("label")
        self.pushButton_boxplots = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_boxplots.setGeometry(QtCore.QRect(660, 30, 28, 28))
        self.pushButton_boxplots.setText("")
        self.pushButton_boxplots.setObjectName("pushButton_boxplots")
        self.label_search_results = QtWidgets.QLabel(self.groupBox)
        self.label_search_results.setGeometry(QtCore.QRect(410, 30, 181, 20))
        self.label_search_results.setWordWrap(True)
        self.label_search_results.setObjectName("label_search_results")
        self.lineEdit_search_results = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_search_results.setGeometry(QtCore.QRect(410, 57, 181, 28))
        self.lineEdit_search_results.setObjectName("lineEdit_search_results")
        self.pushButton_search_next = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_search_next.setGeometry(QtCore.QRect(594, 57, 30, 28))
        self.pushButton_search_next.setText("")
        self.pushButton_search_next.setObjectName("pushButton_search_next")
        self.verticalLayout.addWidget(self.groupBox)
        self.label_codes = QtWidgets.QLabel(Dialog_CodeRelations)
        self.label_codes.setMinimumSize(QtCore.QSize(0, 30))
        self.label_codes.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label_codes.setScaledContents(True)
        self.label_codes.setWordWrap(True)
        self.label_codes.setObjectName("label_codes")
        self.verticalLayout.addWidget(self.label_codes)
        self.groupBox_tables = QtWidgets.QGroupBox(Dialog_CodeRelations)
        self.groupBox_tables.setTitle("")
        self.groupBox_tables.setObjectName("groupBox_tables")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_tables)
        self.gridLayout.setObjectName("gridLayout")
        self.splitter_2 = QtWidgets.QSplitter(self.groupBox_tables)
        self.splitter_2.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.groupBox_results = QtWidgets.QGroupBox(self.splitter_2)
        self.groupBox_results.setTitle("")
        self.groupBox_results.setObjectName("groupBox_results")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_results)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.splitter = QtWidgets.QSplitter(self.groupBox_results)
        self.splitter.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.splitter.setObjectName("splitter")
        self.treeWidget = QtWidgets.QTreeWidget(self.splitter)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setText(0, "1")
        self.tableWidget = QtWidgets.QTableWidget(self.splitter)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout_3.addWidget(self.splitter, 0, 0, 1, 1)
        self.groupBox_statistics = QtWidgets.QGroupBox(self.splitter_2)
        self.groupBox_statistics.setTitle("")
        self.groupBox_statistics.setObjectName("groupBox_statistics")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_statistics)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tableWidget_statistics = QtWidgets.QTableWidget(self.groupBox_statistics)
        self.tableWidget_statistics.setObjectName("tableWidget_statistics")
        self.tableWidget_statistics.setColumnCount(0)
        self.tableWidget_statistics.setRowCount(0)
        self.gridLayout_2.addWidget(self.tableWidget_statistics, 1, 0, 1, 1)
        self.label_summary_stats = QtWidgets.QLabel(self.groupBox_statistics)
        self.label_summary_stats.setObjectName("label_summary_stats")
        self.gridLayout_2.addWidget(self.label_summary_stats, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.splitter_2, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_tables)

        self.retranslateUi(Dialog_CodeRelations)
        QtCore.QMetaObject.connectSlotsByName(Dialog_CodeRelations)

    def retranslateUi(self, Dialog_CodeRelations):
        _translate = QtCore.QCoreApplication.translate
        Dialog_CodeRelations.setWindowTitle(_translate("Dialog_CodeRelations", "Code relations"))
        self.label_header.setText(_translate("Dialog_CodeRelations", "Relations between codes in text files."))
        self.pushButton_exportcsv.setToolTip(_translate("Dialog_CodeRelations", "<html><head/><body><p>Export csv file</p></body></html>"))
        self.pushButton_calculate.setToolTip(_translate("Dialog_CodeRelations", "<html><head/><body><p>Calculate</p></body></html>"))
        self.radioButton_this.setText(_translate("Dialog_CodeRelations", "This coder"))
        self.radioButton_all.setText(_translate("Dialog_CodeRelations", "All coders"))
        self.pushButton_select_files.setToolTip(_translate("Dialog_CodeRelations", "Select text files."))
        self.comboBox_relation_type.setItemText(0, _translate("Dialog_CodeRelations", "All"))
        self.comboBox_relation_type.setItemText(1, _translate("Dialog_CodeRelations", "Overlap"))
        self.comboBox_relation_type.setItemText(2, _translate("Dialog_CodeRelations", "Inclusion"))
        self.comboBox_relation_type.setItemText(3, _translate("Dialog_CodeRelations", "Exact"))
        self.comboBox_relation_type.setItemText(4, _translate("Dialog_CodeRelations", "Proximity"))
        self.comboBox_relation_type.setItemText(5, _translate("Dialog_CodeRelations", "Overlap Inclusion"))
        self.comboBox_relation_type.setItemText(6, _translate("Dialog_CodeRelations", "Overlap Inclusion Exact"))
        self.label.setText(_translate("Dialog_CodeRelations", "Relationship"))
        self.pushButton_boxplots.setToolTip(_translate("Dialog_CodeRelations", "Boxplots of distance between code pairs."))
        self.label_search_results.setText(_translate("Dialog_CodeRelations", "Search Results for:"))
        self.lineEdit_search_results.setToolTip(_translate("Dialog_CodeRelations", "Search results for text"))
        self.pushButton_search_next.setToolTip(_translate("Dialog_CodeRelations", "Search for next occurence in results"))
        self.label_codes.setText(_translate("Dialog_CodeRelations", "Codes:"))
        self.label_summary_stats.setText(_translate("Dialog_CodeRelations", "Summary statistics"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_CodeRelations = QtWidgets.QDialog()
    ui = Ui_Dialog_CodeRelations()
    ui.setupUi(Dialog_CodeRelations)
    Dialog_CodeRelations.show()
    sys.exit(app.exec())
