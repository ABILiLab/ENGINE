from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.verticalLayout_utilres_status = QtWidgets.QVBoxLayout()
        self.verticalLayout_utilres_status.setObjectName("verticalLayout_utilres_status")
        self.horizontalLayout_utils_res = QtWidgets.QHBoxLayout()
        self.horizontalLayout_utils_res.setObjectName("horizontalLayout_utils_res")
        self.verticalLayout_utils = QtWidgets.QVBoxLayout()
        self.verticalLayout_utils.setObjectName("verticalLayout_utils")
        self.groupBox_input = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_input.setObjectName("groupBox_input")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_input)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.groupBox_input)
        self.tabWidget.setObjectName("tabWidget")
        # self.TextInput = QtWidgets.QWidget()
        # self.TextInput.setObjectName("TextInput")
        # self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.TextInput)
        # self.verticalLayout_3.setObjectName("verticalLayout_3")
        # self.text_smiles = QtWidgets.QPlainTextEdit(self.TextInput)
        # self.text_smiles.setObjectName("text_smiles")
        # self.verticalLayout_3.addWidget(self.text_smiles)
        # self.tabWidget.addTab(self.TextInput, "")
        
        self.UploadFile = QtWidgets.QWidget()
        self.UploadFile.setObjectName("UploadFile")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.UploadFile)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.filename = QtWidgets.QLineEdit(self.UploadFile)
        self.filename.setObjectName("filename")
        self.horizontalLayout.addWidget(self.filename)
        
        self.pushButton_select_file = QtWidgets.QPushButton(self.UploadFile)
        self.pushButton_select_file.setObjectName("pushButton_select_file")
        self.horizontalLayout.addWidget(self.pushButton_select_file)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        
        # self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        # self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        
        # self.label = QtWidgets.QLabel(self.UploadFile)
        # self.label.setObjectName("label")
        # self.horizontalLayout_2.addWidget(self.label)
        # self.LineEdit_smile_column = QtWidgets.QLineEdit(self.UploadFile)
        # self.LineEdit_smile_column.setObjectName("LineEdit_smile_column")
        # self.horizontalLayout_2.addWidget(self.LineEdit_smile_column)
        # self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        # spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        # self.horizontalLayout_3.addItem(spacerItem)
        self.tabWidget.addTab(self.UploadFile, "")
        
        # self.DrawMolecule = QtWidgets.QWidget()
        # self.DrawMolecule.setObjectName("DrawMolecule")
        # self.tabWidget.addTab(self.DrawMolecule, "")
        # self.Example = QtWidgets.QWidget()
        # self.Example.setObjectName("Example")
        # self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.Example)
        # self.verticalLayout_2.setObjectName("verticalLayout_2")
        # self.text_example = QtWidgets.QPlainTextEdit(self.Example)
        # self.text_example.setObjectName("text_example")
        # self.verticalLayout_2.addWidget(self.text_example)
        # self.tabWidget.addTab(self.Example, "")
        
        self.verticalLayout.addWidget(self.tabWidget)
        self.verticalLayout_utils.addWidget(self.groupBox_input)
        self.groupBox_ATCcode = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_ATCcode.setObjectName("groupBox_ATCcode")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox_ATCcode)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.groupBox_ATCcode)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_5.addWidget(self.label_2)
        
        self.treeWidget_ATCcode = QtWidgets.QTreeWidget(self.groupBox_ATCcode)
        self.treeWidget_ATCcode.setObjectName("treeWidget_ATCcode")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_ATCcode)
        
        # with open("../resources/data/drugbank_table.txt") as f:
        #     lines = f.readlines()
        # for i in range(len(lines)):
        for i in range(2):   
            item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_ATCcode)

        self.verticalLayout_5.addWidget(self.treeWidget_ATCcode)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        self.verticalLayout_utils.addWidget(self.groupBox_ATCcode)
        
        self.groupBox_parameters = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_parameters.setObjectName("groupBox_parameters")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.groupBox_parameters)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_4 = QtWidgets.QLabel(self.groupBox_parameters)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_7.addWidget(self.label_4)
        # self.label_3 = QtWidgets.QLabel(self.groupBox_parameters)
        # self.label_3.setObjectName("label_3")
        # self.verticalLayout_7.addWidget(self.label_3)
        self.label_5 = QtWidgets.QLabel(self.groupBox_parameters)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_7.addWidget(self.label_5)
        # self.label_6 = QtWidgets.QLabel(self.groupBox_parameters)
        # self.label_6.setObjectName("label_6")
        # self.verticalLayout_7.addWidget(self.label_6)
        self.horizontalLayout_6.addLayout(self.verticalLayout_7)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        
        self.LineEdit_atc_code = QtWidgets.QLineEdit(self.groupBox_parameters)
        self.LineEdit_atc_code.setObjectName("LineEdit_atc_code")
        self.LineEdit_atc_code.setText("mf")
        self.verticalLayout_8.addWidget(self.LineEdit_atc_code)
        
        # self.LineEdit_include_physchem = QtWidgets.QLineEdit(self.groupBox_parameters)
        # self.LineEdit_include_physchem.setObjectName("LineEdit_include_physchem")
        # self.LineEdit_include_physchem.setText("True")
        # # self.LineEdit_include_physchem.setPlaceholderText("True")
        # self.verticalLayout_8.addWidget(self.LineEdit_include_physchem)
        
        self.LineEdit_num_workers = QtWidgets.QLineEdit(self.groupBox_parameters)
        self.LineEdit_num_workers.setObjectName("LineEdit_num_workers")
        self.LineEdit_num_workers.setText("1")
        self.verticalLayout_8.addWidget(self.LineEdit_num_workers)
        
        # self.LineEdit_cache_molecules = QtWidgets.QLineEdit(self.groupBox_parameters)
        # self.LineEdit_cache_molecules.setObjectName("LineEdit_cache_molecules")
        # self.LineEdit_cache_molecules.setText("True")
        # self.verticalLayout_8.addWidget(self.LineEdit_cache_molecules)
        
        self.horizontalLayout_6.addLayout(self.verticalLayout_8)
        
        self.verticalLayout_utils.addWidget(self.groupBox_parameters)
        self.groupBox_operator = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_operator.setObjectName("groupBox_operator")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.groupBox_operator)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")

        self.button_predict = QtWidgets.QPushButton(self.groupBox_operator)
        self.button_predict.setObjectName("button_predict")
        self.horizontalLayout_4.addWidget(self.button_predict)

        self.buttonn_save = QtWidgets.QPushButton(self.groupBox_operator)
        self.buttonn_save.setObjectName("buttonn_save")
        self.horizontalLayout_4.addWidget(self.buttonn_save)

        self.buttonn_clean = QtWidgets.QPushButton(self.groupBox_operator)
        self.buttonn_clean.setObjectName("buttonn_clean")
        self.horizontalLayout_4.addWidget(self.buttonn_clean)


        
        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)
        self.verticalLayout_utils.addWidget(self.groupBox_operator)
        self.verticalLayout_utils.setStretch(0, 2)
        self.verticalLayout_utils.setStretch(1, 6)
        self.verticalLayout_utils.setStretch(2, 1)
        self.verticalLayout_utils.setStretch(3, 1)
        self.horizontalLayout_utils_res.addLayout(self.verticalLayout_utils)
        self.groupBox_res = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_res.setObjectName("groupBox_res")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.groupBox_res)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.Tab_res = QtWidgets.QTabWidget(self.groupBox_res)
        self.Tab_res.setObjectName("Tab_res")
        self.tab_summayplot = QtWidgets.QWidget()
        self.tab_summayplot.setObjectName("tab_summayplot")
        self.Tab_res.addTab(self.tab_summayplot, "")
        
        
        self.tab_meloculesdata = QtWidgets.QWidget()
        self.tab_meloculesdata.setObjectName("tab_meloculesdata")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.tab_meloculesdata)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.Tab_res.addTab(self.tab_meloculesdata, "")
        # self.tableWidget_preds = QTableWidget(self.tab_meloculesdata)
        # self.tableWidget_preds.setObjectName("tableWidget_preds")
        # self.verticalLayout_20.addWidget(self.tableWidget_preds)


        # show_tabSon_meloculesdata 


        self.horizontalLayout_8.addWidget(self.Tab_res)
        self.horizontalLayout_utils_res.addWidget(self.groupBox_res)
        self.horizontalLayout_utils_res.setStretch(0, 4)
        self.horizontalLayout_utils_res.setStretch(1, 6)



        self.verticalLayout_utilres_status.addLayout(self.horizontalLayout_utils_res)
        self.groupBox_status = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_status.setObjectName("groupBox_status")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.groupBox_status)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.textBrowser_status = QtWidgets.QTextBrowser(self.groupBox_status)
        self.textBrowser_status.setObjectName("textBrowser_status")
        self.verticalLayout_9.addWidget(self.textBrowser_status)
        self.verticalLayout_utilres_status.addWidget(self.groupBox_status)
        self.verticalLayout_utilres_status.setStretch(0, 9)
        self.verticalLayout_utilres_status.setStretch(1, 1)
        self.verticalLayout_19.addLayout(self.verticalLayout_utilres_status)
        
        MainWindow.setCentralWidget(self.centralwidget) #设置为中央部件
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1614, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.Tab_res.setCurrentIndex(1)
        self.button_predict.clicked.connect(MainWindow.predict) # type: ignore
        self.buttonn_save.clicked.connect(MainWindow.getSavePath)
        self.buttonn_clean.clicked.connect(MainWindow.clean)
        self.pushButton_select_file.clicked.connect(MainWindow.selectFile) # type: ignore
        self.treeWidget_ATCcode.itemClicked['QTreeWidgetItem*','int'].connect(MainWindow.selectATCcode) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ENGINE"))
        self.groupBox_input.setTitle(_translate("MainWindow", "Select a protein pdb file."))
        # self.text_smiles.setPlaceholderText(_translate("MainWindow", "SMILES (one per line)"))
        # self.tabWidget.setTabText(self.tabWidget.indexOf(self.TextInput), _translate("MainWindow", "Text Input"))
        self.pushButton_select_file.setText(_translate("MainWindow", "select pdb file"))
        # self.label.setText(_translate("MainWindow", "SMILES column:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.UploadFile), _translate("MainWindow", "Upload File"))
        # self.tabWidget.setTabText(self.tabWidget.indexOf(self.DrawMolecule), _translate("MainWindow", "Draw Molecule"))
        # self.text_example.setPlainText(_translate("MainWindow", "O(c1ccc(cc1)CCOC)CC(O)CNC(C)C"))
        # self.tabWidget.setTabText(self.tabWidget.indexOf(self.Example), _translate("MainWindow", "Example"))
        self.groupBox_ATCcode.setTitle(_translate("MainWindow", "Protein Annotation"))
        self.label_2.setText(_translate("MainWindow", "ENGINE supports the prediction of three major Go annotation types (MF, BP, CC). The prediction result is the probability value of the input protein being annotated as multiple Goterms. Please select the GO annotation type to be predicted."))
        self.treeWidget_ATCcode.headerItem().setText(0, _translate("MainWindow", "id"))
        self.treeWidget_ATCcode.headerItem().setText(1, _translate("MainWindow", "Go"))
        self.treeWidget_ATCcode.headerItem().setText(2, _translate("MainWindow", "Description"))
        __sortingEnabled = self.treeWidget_ATCcode.isSortingEnabled()
        self.treeWidget_ATCcode.setSortingEnabled(False)
        self.treeWidget_ATCcode.topLevelItem(0).setText(0, _translate("MainWindow", "1"))
        self.treeWidget_ATCcode.topLevelItem(0).setText(1, _translate("MainWindow", "mf"))
        self.treeWidget_ATCcode.topLevelItem(0).setText(2, _translate("MainWindow", "Molecular Function"))
        self.treeWidget_ATCcode.topLevelItem(1).setText(0, _translate("MainWindow", "2"))
        self.treeWidget_ATCcode.topLevelItem(1).setText(1, _translate("MainWindow", "bp"))
        self.treeWidget_ATCcode.topLevelItem(1).setText(2, _translate("MainWindow", "Biological Process"))
        self.treeWidget_ATCcode.topLevelItem(2).setText(0, _translate("MainWindow", "3"))
        self.treeWidget_ATCcode.topLevelItem(2).setText(1, _translate("MainWindow", "cc"))
        self.treeWidget_ATCcode.topLevelItem(2).setText(2, _translate("MainWindow", "Cellular Component"))
        # # 将drugbank_table.txt中的数据导入GUI
        # with open("../resources/data/drugbank_table.txt") as f:
        #     lines = f.readlines()
        # for i in range(len(lines)):
        # # for i in range(2):
        #     data = lines[i].split(';')
        #     idx = data[0]
        #     atc_code = data[1]
        #     counts = data[2].strip('\n')
        #     self.treeWidget_ATCcode.topLevelItem(i+1).setText(0, _translate("MainWindow", idx))
        #     self.treeWidget_ATCcode.topLevelItem(i+1).setText(1, _translate("MainWindow", atc_code))
        #     self.treeWidget_ATCcode.topLevelItem(i+1).setText(2, _translate("MainWindow", counts))

        self.treeWidget_ATCcode.setSortingEnabled(__sortingEnabled)
        self.groupBox_parameters.setTitle(_translate("MainWindow", "Paramenters"))
        self.label_4.setText(_translate("MainWindow", "Model:"))
        # self.label_3.setText(_translate("MainWindow", "include_physchem:"))
        self.label_5.setText(_translate("MainWindow", "num_workers:"))
        # self.label_6.setText(_translate("MainWindow", "cache_molecules:"))
        self.groupBox_operator.setTitle(_translate("MainWindow", "Operator"))
        self.button_predict.setText(_translate("MainWindow", "Predict"))
        self.buttonn_save.setText(_translate("MainWindow", "Save results"))
        self.buttonn_clean.setText(_translate("MainWindow", "Clean"))
        self.groupBox_res.setTitle(_translate("MainWindow", "Results"))
        self.Tab_res.setTabText(self.Tab_res.indexOf(self.tab_summayplot), _translate("MainWindow", "Plot"))
        self.Tab_res.setTabText(self.Tab_res.indexOf(self.tab_meloculesdata), _translate("MainWindow", "Prediction"))
        self.groupBox_status.setTitle(_translate("MainWindow", "Status"))
    
    def show_tabSon_meloculesdata(self):
        
        self.tabSon_meloculesdata = QtWidgets.QTabWidget(self.tab_meloculesdata)
        self.tabSon_meloculesdata.setObjectName("tabSon_meloculesdata")
        self.tabItem_alldata = QtWidgets.QWidget()
        self.tabItem_alldata.setObjectName("tabItem_alldata")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.tabItem_alldata)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.table_alldata = QtWidgets.QTableWidget(self.tabItem_alldata)
        self.table_alldata.setObjectName("table_alldata")
        self.verticalLayout_12.addWidget(self.table_alldata)
        self.tabSon_meloculesdata.addTab(self.tabItem_alldata, "Results")
        # self.tabItem_singlemelocule = QtWidgets.QWidget()
        # self.tabItem_singlemelocule.setObjectName("tabItem_singlemelocule")
        # self.verticalLayout_21 = QtWidgets.QVBoxLayout(self.tabItem_singlemelocule)
        # self.verticalLayout_21.setObjectName("verticalLayout_21")
        # self.label_selectmelocule = QtWidgets.QLabel(self.tabItem_singlemelocule)
        # self.label_selectmelocule.setObjectName("label_selectmelocule")
        # self.verticalLayout_21.addWidget(self.label_selectmelocule)
        # self.label_selectmelocule.setText("Select Melocule by Id")
        # self.comboBox_selectMelocule = QtWidgets.QComboBox(self.tabItem_singlemelocule)
        # self.comboBox_selectMelocule.setObjectName("comboBox_selectMelocule")
        # self.verticalLayout_21.addWidget(self.comboBox_selectMelocule)
        



        # self.scrollArea_single = QtWidgets.QScrollArea(self.tabItem_singlemelocule)
        # self.scrollArea_single.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        # self.scrollArea_single.setWidgetResizable(True)
        # self.scrollArea_single.setObjectName("scrollArea_single")
        self.scrollAreaWidgetContents_single = QtWidgets.QWidget()
        # self.scrollAreaWidgetContents_single.setGeometry(QtCore.QRect(0, 0, 867, 849))
        self.scrollAreaWidgetContents_single.setObjectName("scrollAreaWidgetContents_single")
        
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_single)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        
        # self.frame_image = QtWidgets.QFrame(self.scrollAreaWidgetContents_single)
        # self.frame_image.setFrameShape(QtWidgets.QFrame.StyledPanel)
        # self.frame_image.setFrameShadow(QtWidgets.QFrame.Raised)
        # self.frame_image.setObjectName("frame_image")
        # self.horizontalLayout_22 = QtWidgets.QVBoxLayout(self.frame_image)
        # self.horizontalLayout_22.setObjectName("verticalLayout_22")
        # self.label_image = QtWidgets.QLabel(self.frame_image)
        # self.label_image.setObjectName("label_image")
        # self.horizontalLayout_22.addWidget(self.label_image)
        # self.verticalLayout_14.addWidget(self.frame_image)
        

        self.frame_image = QtWidgets.QFrame(self.scrollAreaWidgetContents_single)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_image.sizePolicy().hasHeightForWidth())
        self.frame_image.setSizePolicy(sizePolicy)
        self.frame_image.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_image.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_image.setObjectName("frame_image")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame_image)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_image_1 = QtWidgets.QLabel(self.frame_image)
        self.label_image_1.setObjectName("label_image_1")
        self.label_image_1.setScaledContents(True)
        self.label_image_1.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.horizontalLayout_10.addWidget(self.label_image_1)
        self.label_image_2 = QtWidgets.QLabel(self.frame_image)
        self.label_image_2.setObjectName("label_image_2")
        self.label_image_2.setScaledContents(True)
        self.label_image_2.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.horizontalLayout_10.addWidget(self.label_image_2)
        self.horizontalLayout_10.setStretch(0, 5)
        self.horizontalLayout_10.setStretch(1, 5)
        self.horizontalLayout_11.addLayout(self.horizontalLayout_10)
        self.verticalLayout_14.addWidget(self.frame_image)



        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.frame_PhyChe = QtWidgets.QFrame(self.scrollAreaWidgetContents_single)
        self.frame_PhyChe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_PhyChe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_PhyChe.setObjectName("frame_PhyChe")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.frame_PhyChe)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_phyche = QtWidgets.QLabel(self.frame_PhyChe)
        self.label_phyche.setObjectName("label_phyche")
        self.label_phyche.setText("Physicochemical")
        self.verticalLayout_13.addWidget(self.label_phyche)
        self.table_Phyche = QtWidgets.QTableWidget(self.frame_PhyChe)
        self.table_Phyche.setObjectName("table_Phyche")
        self.verticalLayout_13.addWidget(self.table_Phyche)
        self.horizontalLayout_7.addWidget(self.frame_PhyChe)
        self.frame_absorption = QtWidgets.QFrame(self.scrollAreaWidgetContents_single)
        self.frame_absorption.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_absorption.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_absorption.setObjectName("frame_absorption")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.frame_absorption)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.label_absorption = QtWidgets.QLabel(self.frame_absorption)
        self.label_absorption.setObjectName("label_absorption")
        self.label_absorption.setText("Absorption")
        self.verticalLayout_15.addWidget(self.label_absorption)
        self.table__absorption = QtWidgets.QTableWidget(self.frame_absorption)
        self.table__absorption.setObjectName("table__absorption")
        self.verticalLayout_15.addWidget(self.table__absorption)
        self.horizontalLayout_7.addWidget(self.frame_absorption)
        self.frame_distribution = QtWidgets.QFrame(self.scrollAreaWidgetContents_single)
        self.frame_distribution.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_distribution.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_distribution.setObjectName("frame_distribution")
        self.verticalLayout_frame_distribution = QtWidgets.QVBoxLayout(self.frame_distribution)
        self.verticalLayout_frame_distribution.setObjectName("verticalLayout_frame_distribution")
        self.label_distribution = QtWidgets.QLabel(self.frame_distribution)
        self.label_distribution.setObjectName("label_distribution")
        self.verticalLayout_frame_distribution.addWidget(self.label_distribution)
        self.label_distribution.setText("Distribution")
        self.table_distribution = QtWidgets.QTableWidget(self.frame_distribution)
        self.table_distribution.setObjectName("table_distribution")
        self.verticalLayout_frame_distribution.addWidget(self.table_distribution)
        self.horizontalLayout_7.addWidget(self.frame_distribution)
        self.verticalLayout_14.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.frame_metabolism = QtWidgets.QFrame(self.scrollAreaWidgetContents_single)
        self.frame_metabolism.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_metabolism.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_metabolism.setObjectName("frame_metabolism")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.frame_metabolism)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.label_metabolism = QtWidgets.QLabel(self.frame_metabolism)
        self.label_metabolism.setObjectName("label_metabolism")
        self.verticalLayout_16.addWidget(self.label_metabolism)
        self.label_metabolism.setText("Metabolism")
        self.table_metabolism = QtWidgets.QTableWidget(self.frame_metabolism)
        self.table_metabolism.setObjectName("table_metabolism")
        self.verticalLayout_16.addWidget(self.table_metabolism)
        self.horizontalLayout_9.addWidget(self.frame_metabolism)
        self.frame_excretion = QtWidgets.QFrame(self.scrollAreaWidgetContents_single)
        self.frame_excretion.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_excretion.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_excretion.setObjectName("frame_excretion")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.frame_excretion)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.label_excretion = QtWidgets.QLabel(self.frame_excretion)
        self.label_excretion.setObjectName("label_excretion")
        self.label_excretion.setText("Excretion")
        self.verticalLayout_18.addWidget(self.label_excretion)
        self.table_excretion = QtWidgets.QTableWidget(self.frame_excretion)
        self.table_excretion.setObjectName("table_excretion")
        self.verticalLayout_18.addWidget(self.table_excretion)
        self.horizontalLayout_9.addWidget(self.frame_excretion)
        self.frame_toxicity = QtWidgets.QFrame(self.scrollAreaWidgetContents_single)
        self.frame_toxicity.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_toxicity.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_toxicity.setObjectName("frame_toxicity")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.frame_toxicity)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.label_toxicity = QtWidgets.QLabel(self.frame_toxicity)
        self.label_toxicity.setObjectName("label_toxicity")
        self.verticalLayout_17.addWidget(self.label_toxicity)
        self.label_toxicity.setText("Toxicity")
        self.table_toxicity = QtWidgets.QTableWidget(self.frame_toxicity)
        self.table_toxicity.setObjectName("table_toxicity")
        self.verticalLayout_17.addWidget(self.table_toxicity)
        self.horizontalLayout_9.addWidget(self.frame_toxicity)
        self.verticalLayout_14.addLayout(self.horizontalLayout_9)
        self.verticalLayout_14.setStretch(0, 9)
        self.verticalLayout_14.setStretch(1, 10)
        self.verticalLayout_14.setStretch(2, 10)
        # self.tabSon_meloculesdata.addTab(self.tabItem_singlemelocule, "Single Melocule")
        self.verticalLayout_20.addWidget(self.tabSon_meloculesdata)
        # self.comboBox_selectMelocule.currentTextChanged.connect(self.show_single_melocule)

        self.table_Phyche.resizeColumnsToContents()
        self.table__absorption.resizeColumnsToContents()
        self.table_distribution.resizeColumnsToContents()
        self.table_metabolism.resizeColumnsToContents()
        self.table_excretion.resizeColumnsToContents()
        self.table_toxicity.resizeColumnsToContents()


        # self.scrollArea_single.setWidget(self.scrollAreaWidgetContents_single)
        # self.verticalLayout_21.addWidget(self.scrollArea_single)
        # self.verticalLayout_14.setStretch(0,2)
        # self.verticalLayout_14.setStretch(1,5)
        # self.verticalLayout_14.setStretch(2,5)
        self.scrollAreaWidgetContents_single.setMinimumSize(600,1200)

        # 调节scrollArea中的控件大小
        
        # self.frame_image.setGeometry(9,9,100,100)
        # self.frame_PhyChe.setGeometry(1,1,250,448)
        # self.frame_absorption.setGeometry(257,1,250,448)
        # self.frame_distribution.setGeometry(512,1,250,448)
        # self.frame_metabolism.setGeometry(257,1,250,448)
        # self.frame_excretion.setGeometry(1,1,250,448)
        # self.frame_toxicity.setGeometry(512,1,250,448)
        



        
        
        # self.Tab_res.setTabText(self.Tab_res.indexOf(self.tab_meloculesdata), _translate("MainWindow", "Melocules Data"))

from PyQt5.QtWidgets import QTreeWidgetItem
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog, QInputDialog, QTableWidget, QTableWidgetItem, QLabel, QSizePolicy
from PyQt5.QtGui import QPixmap
from pathlib import Path
from engine import GOpredict
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import os
#from rdkit import Chem
#from rdkit.Chem import Draw
import datetime

def clear_layout(layout):
    while layout.count():
        item = layout.takeAt(0)
        widget = item.widget()
        if widget is not None:
            widget.deleteLater()
        else:
            clear_layout(item.layout())
   
class MyDesigner(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.textBrowser_status.setText("\nWelcome to the ENGINE!")

    def selectFile(self):
        filePath,_ = QFileDialog.getOpenFileName(self.filename, "Open Files")
        self.filename.setText(filePath)

    
    def selectATCcode(self, item:QTreeWidgetItem, column:int):
        self.atc_code = item.text(1)
        self.LineEdit_atc_code.setText(self.atc_code)
        
    

    def clean(self):
    
        # 删除已经删除的 Qt 对象的引用
        self.centralwidget.deleteLater()
        self.centralwidget = None
        self.layout = None
        self.label = None
        self.combo_box = None
        self.button = None

        # 重新初始化界面
        self.setupUi(self)
        self.show_tabSon_meloculesdata()

    def getSavePath(self):
        time_str = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        savePath = QFileDialog.getExistingDirectory(self, "Save Results")
        # savePath, ok = QInputDialog.getText(self, "Save Results", "Input Path")
        #if ok:
        self.save_path = Path(savePath+f'/predict_results_{time_str}.csv')
        self.data_with_preds.to_csv(self.save_path)
        self.textBrowser_status.setText("\nThe result has been saved to"+ savePath+f"/predict_results_{time_str}.csv !")
        self.textBrowser_status.moveCursor(QtGui.QTextCursor.End)
    
    def predict(self):
        self.textBrowser_status.setText("\nStart predicting!")
        self.textBrowser_status.moveCursor(QtGui.QTextCursor.End)
        # 运行前判断参数是否完整
        # if self.LineEdit_atc_code == '' or self.LineEdit_include_physchem.text() == ''  or self.LineEdit_num_workers.text() == '' or self.LineEdit_cache_molecules.text()=='':
        if self.LineEdit_atc_code == '':
            self.textBrowser_status.setText("\nPlease slect GO category!")
            self.textBrowser_status.moveCursor(QtGui.QTextCursor.End)
            return 
        
        # 首次运行后组件显示
        if not hasattr(self, "tabSon_meloculesdata"):
            self.show_tabSon_meloculesdata()  
        # 状态栏显示运行前的异常信息
        # if self.text_smiles.toPlainText() == "" and self.filename.text() == "":
        #     self.textBrowser_status.setText("\nPlease provide molecular information!")
        #     return
        # if self.LineEdit_atc_code.text() == "":
        #     self.textBrowser_status.setText("\nPlease provide DrugBank reference set information! ")
        

        
        # self.smile_lines = self.text_smiles.toPlainText()
        self.data_path = Path(self.filename.text())
        # self.atc_code = None if self.atc_code=='all' else self.atc_code
        self.atc_code= None if self.LineEdit_atc_code.text() =='None' else self.LineEdit_atc_code.text()
        print("self.atc_code",self.atc_code)
        # self.smile_column = self.LineEdit_smile_column.text()
        #self.include_physchem = self.LineEdit_include_physchem.text()
        # print(self.LineEdit_num_workers.text())
        self.num_workers = None if self.LineEdit_num_workers.text()=='None' else int(self.LineEdit_num_workers.text())
        # self.cache_molecules = bool(self.LineEdit_cache_molecules.text())
        # 获取当前脚本的绝对路径
        script_path = os.path.abspath(__file__)
        # 提取脚本所在目录
        script_dir = os.path.dirname(script_path)
        self.save_path =script_dir 
        # text和csv不能同时提交
        # if self.smile_lines!="" and self.filename.text()!="":
        #     self.textBrowser_status.setText("\nYou can't submit text and csv file at the same time!")
        #     return
        if self.filename.text()=="":
            self.textBrowser_status.setText("\nPlsease select a pdb file!")
            self.textBrowser_status.moveCursor(QtGui.QTextCursor.End)
            return
        if self.atc_code==None:
            self.textBrowser_status.setText("\nPlsease select Go type!")
            self.textBrowser_status.moveCursor(QtGui.QTextCursor.End)
            return

        # models_dir = Path("../resources/models")
        # drugbank_path = Path("../resources/data/drugbank_approved.csv")
        
        # self.all_smiles = []
        # 预测
        # if self.smile_lines == '':
        #     if self.smile_column == '':
        #         self.textBrowser_status.setText("\nYou must provide the column name which contains SMILES!")
        #         return
        #     elif self.smile_column not in pd.read_csv(self.filename.text()).columns:
        #         self.textBrowser_status.setText("\nYou must provide the correct column name which contains SMILES!")
        #         return
        #     else:
        #         self.data_with_preds = admet_predict(data_path=self.data_path, atc_code=self.atc_code, models_dir=models_dir, save_path=self.save_path, drugbank_path=drugbank_path, smiles_column=self.smile_column, num_workers=self.num_workers, cache_molecules=self.cache_molecules)
        #         self.all_smiles = [pd.read_csv(self.filename.text())[self.smile_column]]
        # else:
        #     lines = self.smile_lines.split('\n')
        #     temp_dict = {"id":range(1, len(lines)+1), "smile":lines}
        #     data = pd.DataFrame(temp_dict)
        #     data.set_index("id", inplace=True)
        #     data.to_csv("temp_data.csv")
        #     self.data_with_preds = admet_predict(data_path="temp_data.csv", atc_code=self.atc_code, models_dir=models_dir, save_path=self.save_path,drugbank_path=drugbank_path, smiles_column="smile", num_workers=self.num_workers, cache_molecules=self.cache_molecules)
        #     os.remove("temp_data.csv")
        # predict
        self.data_with_preds = GOpredict(self.data_path, CATE=self.atc_code,save_path=self.save_path,num_workers=self.num_workers)
    
        # 显示单个分子选择框
        # for id in list(self.data_with_preds['Proteins']):
        #     # 如果SMILE有误则不显示
        #     logP_value = self.data_with_preds[self.data_with_preds['id']==id]['logP'].values[0]
        #     print(logP_value)
        #     print(type(logP_value))
        #     if not np.isnan(self.data_with_preds[self.data_with_preds['id']==id]['logP'].values[0]):
        #         self.comboBox_selectMelocule.addItem(str(id))
        self.show_preds_table()
        self.show_preds_plot()
        # self.show_single_melocule_plot()
        # self.show_single_melocule()
        # self.plot_radial_summary()
        
            

        # 状态栏显示运行过程中的异常信息
        # self.textBrowser_status.clear()
        if os.path.exists("logs.txt"):
            with open("logs.txt") as f:
                lines = f.readline()
                for line in lines:
                    self.textBrowser_status.insertPlainText(line)
        self.textBrowser_status.insertPlainText("\nFinished!")
        self.textBrowser_status.moveCursor(QtGui.QTextCursor.End)
        self.button_predict.setEnabled(False)

    
    def show_preds_table(self):
        self.table_alldata.clear()
        # 取子dataframe
        self.sub_data = self.data_with_preds[self.data_with_preds['Probability'] > 0.0].reset_index(drop=True)

        # 设置表格属性
        colum_num = self.sub_data.shape[1]
        index_num = self.sub_data.shape[0]
        # header = self.data_with_preds.columns.insert(0, "smile")
        header = self.sub_data.columns
        self.table_alldata.setColumnCount(colum_num)
        self.table_alldata.setRowCount(index_num)
        self.table_alldata.setHorizontalHeaderLabels(header)
        
        # 设置表格内容
        for i in range(0, index_num):
            for j in range(0, colum_num):
                # if j==0:
                #     cell = QTableWidgetItem(str(self.sub_data.index[i]))
                # else:
                cell = QTableWidgetItem(str(self.sub_data.values[i][j]))
                self.table_alldata.setItem(i, j, cell)

    # def show_single_melocule(self):
    #     # 根据id索引到对应smile的属性，分组展示
    #     melocule_id = self.comboBox_selectMelocule.currentText()
    #     smile = self.data_with_preds.index[self.data_with_preds['id'] == int(melocule_id)][0]
    #     self.property_id_to_percentile: dict[str, dict[str, float]] = self.data_with_preds[
    #         ~self.data_with_preds.index.duplicated(keep="first")  # drop duplicate SMILES indices
    #         ].to_dict(orient="index")[smile]
    #     self.percentile_suffix=self.atc_code if self.atc_code!=None else ""

    #     props = self.data_with_preds[self.data_with_preds['id']==int(melocule_id)]
    #     # props_name = list(self.data_with_preds.columns)[1:]
        
    #     # 获取属性id、属性名、属性Units和属性所属类别的对应关系
    #     self.admet_attribute_category = pd.read_csv("../resources/data/admet.csv")[['category', 'id', 'name', 'units']]
    #     self.phyche_attr = self.admet_attribute_category[self.admet_attribute_category['category']=='Physicochemical']['id'].values
    #     self.absorption_attr = self.admet_attribute_category[self.admet_attribute_category['category']=='Absorption']['id'].values
    #     self.distribution_attr = self.admet_attribute_category[self.admet_attribute_category['category']=='Distribution']['id'].values
    #     self.metabolism_attr = self.admet_attribute_category[self.admet_attribute_category['category']=='Metabolism']['id'].values
    #     self.excretion_attr = self.admet_attribute_category[self.admet_attribute_category['category']=='Excretion']['id'].values
    #     self.toxicity_attr = self.admet_attribute_category[self.admet_attribute_category['category']=='Toxicity']['id'].values

    #     self.phyche_attr_name = self.admet_attribute_category[self.admet_attribute_category['category']=='Physicochemical']['name'].values
    #     self.absorption_attr_name = self.admet_attribute_category[self.admet_attribute_category['category']=='Absorption']['name'].values
    #     self.distribution_attr_name = self.admet_attribute_category[self.admet_attribute_category['category']=='Distribution']['name'].values
    #     self.metabolism_attr_name = self.admet_attribute_category[self.admet_attribute_category['category']=='Metabolism']['name'].values
    #     self.excretion_attr_name = self.admet_attribute_category[self.admet_attribute_category['category']=='Excretion']['name'].values
    #     self.toxicity_attr_name = self.admet_attribute_category[self.admet_attribute_category['category']=='Toxicity']['name'].values
        
    #     self.phyche_attr_units = self.admet_attribute_category[self.admet_attribute_category['category']=='Physicochemical']['units'].values
    #     self.absorption_attr_units = self.admet_attribute_category[self.admet_attribute_category['category']=='Absorption']['units'].values
    #     self.distribution_attr_units = self.admet_attribute_category[self.admet_attribute_category['category']=='Distribution']['units'].values
    #     self.metabolism_attr_units = self.admet_attribute_category[self.admet_attribute_category['category']=='Metabolism']['units'].values
    #     self.excretion_attr_units = self.admet_attribute_category[self.admet_attribute_category['category']=='Excretion']['units'].values
    #     self.toxicity_attr_units = self.admet_attribute_category[self.admet_attribute_category['category']=='Toxicity']['units'].values
        
    #     phyche_num, absorption_num, distribution_num, metabolism_num, excretion_num, toxicity_num = 8,8,3,8,3,19

    #     self.table_Phyche.setColumnCount(4)
    #     self.table_Phyche.setRowCount(phyche_num)
    #     self.table_Phyche.setHorizontalHeaderLabels(["Property","Value","DrugBank Percentile","Units"])
    #     # self.table_Phyche.setHorizontalHeaderLabels(["Property","Value"])
    #     for i in range(phyche_num):
    #         for j in range(4):
    #             if j==0:
    #                 # 展示属性名
    #                 cell = QTableWidgetItem(self.phyche_attr_name[i])
    #             elif j==1:
    #                 # 展示属性值
    #                 cell = QTableWidgetItem(str(round(props[self.phyche_attr[i]].values[0],2)))
    #             elif j==2:
    #                 # 展示drugbank percentage
    #                 if self.percentile_suffix == "":
    #                     cell = QTableWidgetItem(str(self.property_id_to_percentile[f"{self.phyche_attr[i]}_drugbank_approved{self.percentile_suffix}_percentile"])+'%')
    #                 else:
    #                     cell = QTableWidgetItem(str(self.property_id_to_percentile[f"{self.phyche_attr[i]}_drugbank_approved_{self.percentile_suffix}_percentile"])+'%')
    #             else:
    #                 cell = QTableWidgetItem(self.phyche_attr_units[i])
    #             self.table_Phyche.setItem(i, j, cell)

    #     self.table__absorption.setColumnCount(4)
    #     self.table__absorption.setRowCount(absorption_num)
    #     # self.table__absorption.setHorizontalHeaderLabels(["Property","Prediction","DrugBank Percentile","Units"])
    #     self.table__absorption.setHorizontalHeaderLabels(["Property","Value","DrugBank Percentile","Units"])
    #     for i in range(absorption_num):
    #         for j in range(4):
    #             if j==0:
    #                 cell = QTableWidgetItem(self.absorption_attr_name[i])
    #             elif j==1:
    #                 cell = QTableWidgetItem(str(round(props[self.absorption_attr[i]].values[0],2)))
    #             elif j==2:
    #                 # 展示drugbank percentage
    #                 if self.percentile_suffix == "":
    #                     cell = QTableWidgetItem(str(self.property_id_to_percentile[f"{self.absorption_attr[i]}_drugbank_approved{self.percentile_suffix}_percentile"])+'%')
    #                 else:
    #                     cell = QTableWidgetItem(str(self.property_id_to_percentile[f"{self.absorption_attr[i]}_drugbank_approved_{self.percentile_suffix}_percentile"])+'%')
    #             else:
    #                 cell = QTableWidgetItem(self.absorption_attr_units[i])
    #             self.table__absorption.setItem(i, j, cell)

    #     self.table_distribution.setColumnCount(4)
    #     self.table_distribution.setRowCount(distribution_num)
    #     # self.table_distribution.setHorizontalHeaderLabels(["Property","Prediction","DrugBank Percentile","Units"])
    #     self.table_distribution.setHorizontalHeaderLabels(["Property","Value","DrugBank Percentile","Units"])
    #     for i in range(distribution_num):
    #         for j in range(4):
    #             if j==0:
    #                 cell = QTableWidgetItem(self.distribution_attr_name[i])
    #             elif j==1:
    #                 cell = QTableWidgetItem(str(round(props[self.distribution_attr[i]].values[0],2)))
    #             elif j==2:
    #                 # 展示drugbank percentage
    #                 if self.percentile_suffix == "":
    #                     cell = QTableWidgetItem(str(self.property_id_to_percentile[f"{self.distribution_attr[i]}_drugbank_approved{self.percentile_suffix}_percentile"])+'%')
    #                 else:
    #                     cell = QTableWidgetItem(str(self.property_id_to_percentile[f"{self.distribution_attr[i]}_drugbank_approved_{self.percentile_suffix}_percentile"])+'%')
    #             else:
    #                 cell = QTableWidgetItem(self.distribution_attr_units[i])
    #             self.table_distribution.setItem(i, j, cell)

    #     self.table_metabolism.setColumnCount(4)
    #     self.table_metabolism.setRowCount(metabolism_num)
    #     # self.table_metabolism.setHorizontalHeaderLabels(["Property","Prediction","DrugBank Percentile","Units"])
    #     self.table_metabolism.setHorizontalHeaderLabels(["Property","Value","DrugBank Percentile","Units"])
    #     for i in range(metabolism_num):
    #         for j in range(4):
    #             if j==0:
    #                 cell = QTableWidgetItem(self.metabolism_attr_name[i])
    #             elif j==1:
    #                 cell = QTableWidgetItem(str(round(props[self.metabolism_attr[i]].values[0],2)))
    #             elif j==2:
    #                 # 展示drugbank percentage
    #                 if self.percentile_suffix == "":
    #                     cell = QTableWidgetItem(str(self.property_id_to_percentile[f"{self.metabolism_attr[i]}_drugbank_approved{self.percentile_suffix}_percentile"])+'%')
    #                 else:
    #                     cell = QTableWidgetItem(str(self.property_id_to_percentile[f"{self.metabolism_attr[i]}_drugbank_approved_{self.percentile_suffix}_percentile"])+'%')
    #             else:
    #                 cell = QTableWidgetItem(self.metabolism_attr_units[i])
    #             self.table_metabolism.setItem(i, j, cell)

    #     self.table_toxicity.setColumnCount(4)
    #     self.table_toxicity.setRowCount(toxicity_num)
    #     # self.table_toxicity.setHorizontalHeaderLabels(["Property","Prediction","DrugBank Percentile","Units"])
    #     self.table_toxicity.setHorizontalHeaderLabels(["Property","Value","DrugBank Percentile","Units"])
    #     for i in range(toxicity_num):
    #         for j in range(4):
    #             if j==0:
    #                 cell = QTableWidgetItem(self.toxicity_attr_name[i])
    #             elif j==1:
    #                 cell = QTableWidgetItem(str(round(props[self.toxicity_attr[i]].values[0],2)))
    #             elif j==2:
    #                 # 展示drugbank percentage
    #                 if self.percentile_suffix == "":
    #                     cell = QTableWidgetItem(str(self.property_id_to_percentile[f"{self.toxicity_attr[i]}_drugbank_approved{self.percentile_suffix}_percentile"])+'%')
    #                 else:
    #                     cell = QTableWidgetItem(str(self.property_id_to_percentile[f"{self.toxicity_attr[i]}_drugbank_approved_{self.percentile_suffix}_percentile"])+'%')
    #             else:
    #                 cell = QTableWidgetItem(self.toxicity_attr_units[i])
    #             self.table_toxicity.setItem(i, j, cell)

    #     self.table_excretion.setColumnCount(4)
    #     self.table_excretion.setRowCount(excretion_num)
    #     # self.table_excretion.setHorizontalHeaderLabels(["Property","Prediction","DrugBank Percentile","Units"])
    #     self.table_excretion.setHorizontalHeaderLabels(["Property","Value","DrugBank Percentile","Units"])
    #     for i in range(excretion_num):
    #         for j in range(4):
    #             if j==0:
    #                 cell = QTableWidgetItem(self.excretion_attr_name[i])
    #             elif j==1:
    #                 cell = QTableWidgetItem(str(round(props[self.excretion_attr[i]].values[0],2)))
    #             elif j==2:
    #                 # 展示drugbank percentage
    #                 if self.percentile_suffix == "":
    #                     cell = QTableWidgetItem(str(self.property_id_to_percentile[f"{self.excretion_attr[i]}_drugbank_approved{self.percentile_suffix}_percentile"])+'%')
    #                 else:
    #                     cell = QTableWidgetItem(str(self.property_id_to_percentile[f"{self.excretion_attr[i]}_drugbank_approved_{self.percentile_suffix}_percentile"])+'%')
    #             else:
    #                 cell = QTableWidgetItem(self.excretion_attr_units[i])
    #             self.table_excretion.setItem(i, j, cell)
    #     # self.table_Phyche.resizeColumnsToContents()
    #     # self.table__absorption.resizeColumnsToContents()
    #     # self.table_distribution.resizeColumnsToContents()
    #     # self.table_metabolism.resizeColumnsToContents()
    #     # self.table_excretion.resizeColumnsToContents()
    #     # self.table_toxicity.resizeColumnsToContents()

    #     self.show_single_melocule_plot()

    def show_preds_plot(self):

        # 首次运行显示图和属性选择按钮
        # if not hasattr(self, "verticalLayout_tab_summaryplot"):
        self.verticalLayout_tab_summaryplot = QtWidgets.QVBoxLayout(self.tab_summayplot)
        self.verticalLayout_tab_summaryplot.setObjectName("verticalLayout_tab_summaryplot")
        self.frame_plot = QtWidgets.QFrame(self.tab_summayplot)
        self.frame_plot.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_plot.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_plot.setObjectName("frame_plot")

        self.verticalLayout_frameplot = QtWidgets.QVBoxLayout(self.frame_plot)
        self.verticalLayout_frameplot.setObjectName("verticalLayout_frameplot")
        self.label_plot = QtWidgets.QLabel(self.frame_plot)
        self.label_plot.setText("")
        self.label_plot.setObjectName("label_plot")
        self.label_plot.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.verticalLayout_frameplot.addWidget(self.label_plot)
        self.verticalLayout_frameplot.setContentsMargins(30,30,30,30)

        self.verticalLayout_tab_summaryplot.addWidget(self.frame_plot)
        self.horizontalLayout_choose_xy = QtWidgets.QHBoxLayout()
        self.horizontalLayout_choose_xy.setObjectName("horizontalLayout_choose_xy")
        # self.label_choose_y = QtWidgets.QLabel(self.tab_summayplot)
        # self.label_choose_y.setObjectName("label_choose_y")
        # self.label_choose_y.setText("Select Drugbank y-axis property")
        # self.horizontalLayout_choose_xy.addWidget(self.label_choose_y)
        # self.comboBox_choose_y = QtWidgets.QComboBox(self.tab_summayplot)
        # self.comboBox_choose_y.setObjectName("comboBox_choose_y")
        
        # # for attr in self.data_with_preds.columns[1:]:
        # for attr in ['10','30','50']:
        #     self.comboBox_choose_y.addItem(attr)
        # self.horizontalLayout_choose_xy.addWidget(self.comboBox_choose_y)
        
        # spacerItem1 = QtWidgets.QSpacerItem(48, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        # self.horizontalLayout_choose_xy.addItem(spacerItem1)
        self.label_choose_x = QtWidgets.QLabel(self.tab_summayplot)
        self.label_choose_x.setObjectName("label_choose_x")
        self.label_choose_x.setText("Select Top x")
        self.horizontalLayout_choose_xy.addWidget(self.label_choose_x)
        self.comboBox_choose_x = QtWidgets.QComboBox(self.tab_summayplot)
        self.comboBox_choose_x.setObjectName("comboBox_choose_x")
        # for attr in self.data_with_preds.columns[1:]:
        for attr in ['10','30','50']:
            self.comboBox_choose_x.addItem(attr)

        self.horizontalLayout_choose_xy.addWidget(self.comboBox_choose_x)
        self.verticalLayout_tab_summaryplot.addLayout(self.horizontalLayout_choose_xy)
        self.verticalLayout_tab_summaryplot.setStretch(3,1)

        # self.comboBox_choose_y.setFixedSize(QtCore.QSize(200,30))
        self.comboBox_choose_x.setFixedSize(QtCore.QSize(200,30))
        self.comboBox_choose_x.currentTextChanged.connect(self.change_preds_plot)
        # self.comboBox_choose_y.currentTextChanged.connect(self.change_preds_plot)
            # print(self.comboBox_choose_x.size())
            # print(self.comboBox_choose_y.size())
        
        # # 获取纵轴和横轴的属性
        # x_property_name = self.comboBox_choose_x.currentText()
        # y_property_name = self.comboBox_choose_y.currentText()
        # self.drugbank = pd.read_csv("../resources/data/drugbank_approved.csv")
        # x_drugbank_property = self.drugbank[x_property_name]
        # y_drugbank_property = self.drugbank[y_property_name]
        # x_data_property = self.data_with_preds[x_property_name]
        # y_data_property = self.data_with_preds[y_property_name]
        # # 绘制散点图和边缘直方图
        # fig = plt.figure()
        # grid = fig.add_gridspec(6,6)
        # ax_scatter = fig.add_subplot(grid[1:, :-1])
        # ax_right = fig.add_subplot(grid[1:, -1])
        # ax_top = fig.add_subplot(grid[0, :-1])
        # ax_scatter.scatter(x_drugbank_property, y_drugbank_property, c='#448cbc', marker='o', alpha=0.7,edgecolors='white') # steelblue
        # ax_scatter.scatter(x_data_property, y_data_property, c='r', marker='*', alpha=0.7)
        # ax_scatter.set_xlabel(x_property_name)
        # ax_scatter.set_ylabel(y_property_name)
        # for i, (x,y) in enumerate(zip(x_data_property, y_data_property)):
        #     ax_scatter.text(x, y, list(range(len(x_data_property)))[i], color='r')
        # ax_top.hist(x_drugbank_property, 55, histtype="bar", color="#448cbc", orientation="vertical", edgecolor="black", linewidth=0.5, alpha=0.7)
        # ax_top.axis("off")
        # ax_right.hist(y_drugbank_property, 55, histtype="bar", color="#448cbc", orientation="horizontal", edgecolor="black", linewidth=0.5, alpha=0.7)
        # ax_right.axis("off")
        
        # 取蛋白质ID
        protein_id = self.data_with_preds['Proteins'].unique()[0]

        # 按照 Probability 降序排序并取前10个GO term
        top10 = self.data_with_preds.sort_values(by='Probability', ascending=False).head(10)

        # 绘图
        plt.figure(figsize=(10, 8))
        plt.bar(top10['Goterms'], top10['Probability'], color='skyblue')
        plt.xlabel('GO Terms')
        plt.ylabel('Probability')
        plt.title(f'GO Annotation Prediction Results (Top 10) for Protein {protein_id}')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        # plt.show()
        
        plt.savefig("bar_top_10.jpg", dpi=300)
        pixmap = QPixmap("bar_top_10.jpg")
        # resized_pixmap = pixmap.scaled(self.label_plot.size(), aspectRatioMode=True)
        self.label_plot.setPixmap(pixmap)
        self.label_plot.setScaledContents(True)
        # os.remove("bar.jpg")
        
        
    
    def change_preds_plot(self):
    #     # 获取改变后纵轴和横轴的属性
        x_property_name = self.comboBox_choose_x.currentText()
    #     y_property_name = self.comboBox_choose_y.currentText()
    #     self.drugbank = pd.read_csv("../resources/data/drugbank_approved.csv")
    #     x_drugbank_property = self.drugbank[x_property_name]
    #     y_drugbank_property = self.drugbank[y_property_name]
    #     x_data_property = self.data_with_preds[x_property_name]
    #     y_data_property = self.data_with_preds[y_property_name]
        
        # # 重新展示散点图
        # fig = plt.figure()
        # grid = fig.add_gridspec(6,6)
        # ax_scatter = fig.add_subplot(grid[1:, :-1])
        # ax_right = fig.add_subplot(grid[1:, -1])
        # ax_top = fig.add_subplot(grid[0, :-1])
        # ax_scatter.scatter(x_drugbank_property, y_drugbank_property, c='#448cbc', marker='o', alpha=0.7,edgecolors='white') # steelblue
        # ax_scatter.scatter(x_data_property, y_data_property, c='r', marker='*', alpha=0.7)
        # ax_scatter.set_xlabel(x_property_name)
        # ax_scatter.set_ylabel(y_property_name)
        # for i, (x,y) in enumerate(zip(x_data_property, y_data_property)):
        #     ax_scatter.text(x, y, list(range(len(x_data_property)))[i], color='r')
        # ax_top.hist(x_drugbank_property, 55, histtype="bar", color="#448cbc", orientation="vertical", edgecolor="black", linewidth=0.5, alpha=0.7)
        # ax_top.axis("off")
        # # ax_top.invert_xaxis()
        # ax_right.hist(y_drugbank_property, 55, histtype="bar", color="#448cbc", orientation="horizontal", edgecolor="black", linewidth=0.5, alpha=0.7)
        # ax_right.axis("off")
        # # ax_right.invert_yaxis()
        # plt.savefig("scatter.jpg", dpi=500)
        # pixmap = QPixmap("scatter.jpg")
        # # resized_pixmap = pixmap.scaled(self.label_plot.size(), aspectRatioMode=True)
        # self.label_plot.setPixmap(pixmap)
        # self.label_plot.setScaledContents(True)
        # os.remove("scatter.jpg")
        # 取蛋白质ID
        protein_id = self.data_with_preds['Proteins'].unique()[0]

        # 按照 Probability 降序排序并取前10个GO term
        top_x_df = self.data_with_preds.sort_values(by='Probability', ascending=False).head(int(x_property_name))

        # 绘图
        plt.figure(figsize=(10, 8))
        plt.bar(top_x_df['Goterms'], top_x_df['Probability'], color='skyblue')
        plt.xlabel('GO Terms')
        plt.ylabel('Probability')
        plt.title(f'GO Annotation Prediction Results (Top {x_property_name}) for Protein {protein_id}')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        # plt.show()
        
        plt.savefig(f"bar_top_{x_property_name}.jpg", dpi=300)
        pixmap = QPixmap(f"bar_top_{x_property_name}.jpg")
        # resized_pixmap = pixmap.scaled(self.label_plot.size(), aspectRatioMode=True)
        self.label_plot.setPixmap(pixmap)
        self.label_plot.setScaledContents(True)
        
        

    # def show_single_melocule_plot(self):
    #     # 雷达图展示
    #     fig = plt.figure() 
    #     dim_num = 5
    #     radians = np.linspace(0, 2 * np.pi, dim_num, endpoint=False)
    #     radians = np.concatenate((radians, [radians[0]]))  
    #     # 根据分子id检索对应的雷达图属性
    #     # melocule_id = self.comboBox_selectMelocule.currentText()
    #     # props = self.data_with_preds[self.data_with_preds['id']==int(melocule_id)]
    #     # hERG_Safe = self.data_with_preds[self.data_with_preds['id']==int(melocule_id)]['hERG'].values[0]
    #     # BBB_Martins = self.data_with_preds[self.data_with_preds['id']==int(melocule_id)]['BBB_Martins'].values[0]
    #     # Bioavailability_Ma = self.data_with_preds[self.data_with_preds['id']==int(melocule_id)]['Bioavailability_Ma'].values[0]
    #     # Solubility_AqSolDB = self.data_with_preds[self.data_with_preds['id']==int(melocule_id)]['Solubility_AqSolDB'].values[0]
    #     # NonToxity = 1-np.array([props[i].values[0] for i in self.toxicity_attr]).max()
    #     melocule_id = self.comboBox_selectMelocule.currentText()
    #     smile = self.data_with_preds.index[self.data_with_preds['id'] == int(melocule_id)][0]
    #     self.property_id_to_percentile: dict[str, dict[str, float]] = self.data_with_preds[
    #         ~self.data_with_preds.index.duplicated(keep="first")  # drop duplicate SMILES indices
    #         ].to_dict(orient="index")[smile]
    #     self.percentile_suffix="_"+ self.atc_code if self.atc_code!=None else ""
    #     # print(self.toxicity_attr_name)
    #     # print(self.toxicity_attr)

    #     # Set up properties
    #     max_percentile = 100
        
    #     properties = {
    #         "Blood-Brain Barrier Safe": {
    #             "percentile": max_percentile
    #             - self.property_id_to_percentile[f"BBB_Martins_drugbank_approved{self.percentile_suffix}_percentile"],
    #         },
    #         "Non-\nToxic": {
    #             "percentile": max_percentile
    #             - max(
    #                 self.property_id_to_percentile[f"{toxicity_name}_drugbank_approved{self.percentile_suffix}_percentile"]
    #                 for toxicity_name in self.toxicity_attr
    #             ),
    #             "vertical_alignment": "bottom",
    #         },
    #         "Soluble": {
    #             "percentile": self.property_id_to_percentile[
    #                 f"Solubility_AqSolDB_drugbank_approved{self.percentile_suffix}_percentile"
    #             ],
    #             "vertical_alignment": "top",
    #         },
    #         "Bioavailable": {
    #             "percentile": self.property_id_to_percentile[
    #                 f"Bioavailability_Ma_drugbank_approved{self.percentile_suffix}_percentile"
    #             ],
    #             "vertical_alignment": "top",
    #         },
    #         "hERG\nSafe": {
    #             "percentile": max_percentile
    #             - self.property_id_to_percentile[f"hERG_drugbank_approved{self.percentile_suffix}_percentile"],
    #             "vertical_alignment": "bottom",
    #         },
    #     }
    #     property_names = [property_name for property_name in properties]
    #     percentiles = [
    #         properties[property_name]["percentile"] for property_name in properties
    #     ]


    #     # data1 = np.array([BBB_Martins,hERG_Safe,Bioavailability_Ma,Solubility_AqSolDB,NonToxity])
    #     percentiles = np.concatenate((percentiles, [percentiles[0]]))

    #     # data2 = np.array([73,61,54,34,48])
    #     # data2 = np.concatenate((data2, [data2[0]]))

    #     # radar_labels = ['Blood-Brain Barrier Safe','hERG Safe','Bioavailable','Soluble','Non-Toxic']
    #     radar_labels = np.concatenate((property_names, [property_names[0]]))

    #     plt.polar(radians, percentiles, 'r') # 绘制雷达图
    #     plt.fill(radians, percentiles, 'r', alpha=0.25) # 

    #     angles = radians * 180/np.pi  # 弧度转角度
    #     plt.thetagrids(angles, labels=radar_labels) # 设置新的刻度标签


    #     plt.savefig("single_melocule_plot_1.jpg",bbox_inches='tight',pad_inches=0.3)

    #     pixmap1 = QPixmap("single_melocule_plot_1.jpg")
    #     #pixmap = pixmap.scaled(self.label_image_1.size(), aspectRatioMode=True)
    #     # pixmap = pixmap.scaled(self.label_image_1.size(), aspectRatioMode=True, transformMode=Qt.SmoothTransformation)
    #     self.label_image_1.setScaledContents(True)
    #     self.label_image_1.setPixmap(pixmap1)

    #     # plt.cla()
    #     # plt.polar(radians, data2, 'r')
    #     # plt.fill(radians, data2, 'r', alpha=0.25)
    #     # plt.thetagrids(angles, labels=radar_labels) # 设置新的刻度标签
    #     # plt.savefig("single_melocule_plot_2.jpg",bbox_inches='tight',pad_inches=0.3)
    #     # pixmap2 = QPixmap("single_melocule_plot_2.jpg")

    #     # self.label_image_2.setScaledContents(True)
    #     # self.label_image_2.setPixmap(pixmap2)
        
    #     # 分子图展示
    #     plt.cla()
        
    #     Benzene = self.data_with_preds.index[self.data_with_preds['id'] == int(melocule_id)][0]
    #     mol = Chem.MolFromSmiles(Benzene)
    #     img = Draw.MolsToGridImage([mol],molsPerRow=1,subImgSize=(500,500))
    #     plt.imshow(img)
    #     plt.axis('off')
    #     img.save("single_melocule_shape.jpg")
    #     pixmap2 = QPixmap("single_melocule_shape.jpg")
        
    #     self.label_image_2.setScaledContents(True)
    #     self.label_image_2.setPixmap(pixmap2)
    #     os.remove("single_melocule_shape.jpg")
    #     os.remove("single_melocule_plot_1.jpg")

                                                                                                
from qt_material import apply_stylesheet
import qdarkstyle
from qdarkstyle.light.palette import LightPalette

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    # apply_stylesheet(app, theme='light_blue.xml')
    # apply_stylesheet(app, theme='dark_teal.xml')
    app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5'))
    # app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5', palette=LightPalette()))
    main_ui = MyDesigner()
    main_ui.show()
    app.exec_()
