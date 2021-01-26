from PyQt5 import QtCore, QtGui, QtWidgets
import datetime

symbolRequireExpList = [12, 15, 20, 27, 36, 47, 60, 75, 92, 111, 132, 155, 180, 207, 236, 267, 300, 335, 372]
requireMesoList_VJ = [9500000, 16630000, 23760000, 30890000, 38020000, 45150000, 52280000, 59410000, 66540000, 73670000, 80800000, 87930000, 95060000, 102190000, 109320000, 116450000, 123580000, 130710000, 137840000]
requireMesoList = [19040000, 25640000, 32240000, 38850000, 45440000, 52040000, 58640000, 65240000, 71840000, 78440000, 85040000, 91640000, 98240000, 104840000, 111440000, 124640000, 131240000, 137840000]
today = datetime.date.today()

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1114, 650)
        self.vanishingJourney = QtWidgets.QGroupBox(Dialog)
        self.vanishingJourney.setGeometry(QtCore.QRect(40, 50, 251, 371))
        self.vanishingJourney.setObjectName("vanishingJourney")
        self.formLayoutWidget = QtWidgets.QWidget(self.vanishingJourney)
        self.formLayoutWidget.setGeometry(QtCore.QRect(30, 30, 161, 57))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.currentLevelLabel_VJ = QtWidgets.QLabel(self.formLayoutWidget)
        self.currentLevelLabel_VJ.setObjectName("currentLevelLabel_VJ")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.currentLevelLabel_VJ)
        self.currentExpLabel_VJ = QtWidgets.QLabel(self.formLayoutWidget)
        self.currentExpLabel_VJ.setObjectName("currentExpLabel_VJ")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.currentExpLabel_VJ)
        self.currentLevel_VJ = QtWidgets.QSpinBox(self.formLayoutWidget)
        self.currentLevel_VJ.setObjectName("currentLevel_VJ")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.currentLevel_VJ)
        self.currentExp_VJ = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.currentExp_VJ.setObjectName("currentExp_VJ")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.currentExp_VJ)
        self.expRatio_VJ = QtWidgets.QLabel(self.vanishingJourney)
        self.expRatio_VJ.setGeometry(QtCore.QRect(70, 90, 151, 20))
        self.expRatio_VJ.setObjectName("expRatio_VJ")
        self.result_VJ = QtWidgets.QGroupBox(self.vanishingJourney)
        self.result_VJ.setGeometry(QtCore.QRect(10, 190, 231, 131))
        self.result_VJ.setObjectName("result_VJ")
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.result_VJ)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(10, 30, 211, 91))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.requireMesoLabel_VJ = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.requireMesoLabel_VJ.setObjectName("requireMesoLabel_VJ")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.requireMesoLabel_VJ)
        self.finishDateLabel_VJ = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.finishDateLabel_VJ.setObjectName("finishDateLabel_VJ")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.finishDateLabel_VJ)
        self.remainDateLabel_VJ = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.remainDateLabel_VJ.setObjectName("remainDateLabel_VJ")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.remainDateLabel_VJ)
        self.requireMeso_VJ = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.requireMeso_VJ.setObjectName("requireMeso_VJ")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.requireMeso_VJ)
        self.remainDate_VJ = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.remainDate_VJ.setObjectName("remainDate_VJ")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.remainDate_VJ)
        self.finishDate_VJ = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.finishDate_VJ.setObjectName("finishDate_VJ")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.finishDate_VJ)
        self.quest_VJ = QtWidgets.QCheckBox(self.vanishingJourney)
        self.quest_VJ.setGeometry(QtCore.QRect(130, 120, 16, 19))
        self.quest_VJ.setText("")
        self.quest_VJ.setObjectName("quest_VJ")
        self.spectrum = QtWidgets.QCheckBox(self.vanishingJourney)
        self.spectrum.setGeometry(QtCore.QRect(130, 150, 16, 19))
        self.spectrum.setText("")
        self.spectrum.setObjectName("spectrum")
        self.questLabel_VJ = QtWidgets.QLabel(self.vanishingJourney)
        self.questLabel_VJ.setGeometry(QtCore.QRect(20, 120, 81, 16))
        self.questLabel_VJ.setObjectName("questLabel_VJ")
        self.spectrumLabel = QtWidgets.QLabel(self.vanishingJourney)
        self.spectrumLabel.setGeometry(QtCore.QRect(20, 150, 64, 15))
        self.spectrumLabel.setObjectName("spectrumLabel")
        
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.currentExp_VJ.textChanged.connect(self.calcVanishingJourney)

    def calcVanishingJourney(self):
        currentLevel_VJ = int(self.currentLevel_VJ.text())
        currentExp_VJ = int(self.currentExp_VJ.text())
        requireExp_VJ = symbolRequireExpList[currentLevel_VJ - 1]
        requireMeso_VJ = sum(requireMesoList_VJ[currentLevel_VJ-1:])
        requireSymbol_VJ = sum(symbolRequireExpList[currentLevel_VJ:]) + (symbolRequireExpList[currentLevel_VJ-1] - currentExp_VJ)
        
        dailySymbol_VJ = 0
        if self.quest_VJ.isChecked() == True:
            dailySymbol_VJ += 16
        if self.spectrum.isChecked() == True:
            dailySymbol_VJ += 6
        
        self.expRatio_VJ.setText(str(currentExp_VJ) + " / " + str(requireExp_VJ) + "(" + str(int(currentExp_VJ / requireExp_VJ * 100)) + "%)")
        self.requireMeso_VJ.setText(str(format(requireMeso_VJ, ',') + " meso"))
        
        if dailySymbol_VJ != 0:
            dayLeft = int(requireSymbol_VJ/dailySymbol_VJ) + 1
            self.remainDate_VJ.setText(str(dayLeft)+ " days left")
            self.finishDate_VJ.setText(str(today + datetime.timedelta(days=dayLeft)))
    
        
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.vanishingJourney.setTitle(_translate("Dialog", "Vanishing Journey"))
        self.currentLevelLabel_VJ.setText(_translate("Dialog", "Current Lv"))
        self.currentExpLabel_VJ.setText(_translate("Dialog", "Exp"))
        self.expRatio_VJ.setText(_translate("Dialog", "0 / 0 (0%)"))
        self.result_VJ.setTitle(_translate("Dialog", "Result"))
        self.requireMesoLabel_VJ.setText(_translate("Dialog", "Required Cost"))
        self.finishDateLabel_VJ.setText(_translate("Dialog", "Date of Completion"))
        self.remainDateLabel_VJ.setText(_translate("Dialog", "Remaining Days"))
        self.requireMeso_VJ.setText(_translate("Dialog", "0 meso"))
        self.remainDate_VJ.setText(_translate("Dialog", "0 days left"))
        self.finishDate_VJ.setText(_translate("Dialog", str(today)))
        self.questLabel_VJ.setText(_translate("Dialog", "Daily Quest"))
        self.spectrumLabel.setText(_translate("Dialog", "Erda Spectrum"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
