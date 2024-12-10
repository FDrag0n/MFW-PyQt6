from PyQt6.QtCore import QSize, QMetaObject, QCoreApplication
from PyQt6.QtWidgets import (
    QSizePolicy,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
    QFrame,
    QAbstractItemView,
)
from qfluentwidgets import PushButton, BodyLabel, ComboBox, TextEdit
from ..components.listwidge_menu_draggable import ListWidge_Menu_Draggable


class Ui_Task_Interface(object):
    def setupUi(self, Task_Interface):
        Task_Interface.setObjectName("Task_Interface")
        Task_Interface.resize(900, 600)
        Task_Interface.setMinimumSize(QSize(0, 0))
        # 设置主窗口
        self.main_layout = QHBoxLayout(self)

        # 自动检测按钮,资源和控制器标签布局
        self.LD2_layout = QVBoxLayout()
        self.Resource_Title = BodyLabel(Task_Interface)
        self.Control_Title = BodyLabel(Task_Interface)
        self.AutoDetect_Button = PushButton(Task_Interface)
        self.Resource_Title.setObjectName("Resource_Title")
        self.Control_Title.setObjectName("Control_Title")
        self.AutoDetect_Button.setObjectName("AutoDetect_Button")

        self.Resource_Title.setSizePolicy(
            QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed
        )
        self.Control_Title.setSizePolicy(
            QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed
        )
        self.Resource_Title.setMinimumSize(0, 33)
        self.Control_Title.setMinimumSize(0, 33)

        self.LD2_layout.addWidget(self.Resource_Title)
        self.LD2_layout.addWidget(self.Control_Title)
        self.LD2_layout.addWidget(self.AutoDetect_Button)

        # 左下二级整体布局
        self.LD3_layout = QVBoxLayout()
        self.LD3_layout.addLayout(self.LD2_layout)

        # 左下下拉栏布局
        self.LD4_layout = QVBoxLayout()
        self.Resource_Combox = ComboBox(Task_Interface)
        self.Control_Combox = ComboBox(Task_Interface)
        self.Autodetect_combox = ComboBox(Task_Interface)

        self.Resource_Combox.setObjectName("Resource_Combox")
        self.Control_Combox.setObjectName("Control_Combox")
        self.Autodetect_combox.setObjectName("Autodetect_combox")

        self.LD4_layout.addWidget(self.Resource_Combox)
        self.LD4_layout.addWidget(self.Control_Combox)
        self.LD4_layout.addWidget(self.Autodetect_combox)
        
        # 左下完整布局
        self.LD5_layout = QHBoxLayout()
        self.LD5_layout.addLayout(self.LD3_layout)
        self.LD5_layout.addLayout(self.LD4_layout)

        # 完成后操作
        self.Finish_combox = ComboBox(Task_Interface)
        self.Finish_combox_res = ComboBox(Task_Interface)
        self.Finish_combox_cfg = ComboBox(Task_Interface)
        self.Finish_combox_layout = QHBoxLayout()
        self.Finish_combox_layout.addWidget(self.Finish_combox)
        self.Finish_combox_layout.addWidget(self.Finish_combox_res)
        self.Finish_combox_layout.addWidget(self.Finish_combox_cfg)
        self.Finish_combox.setObjectName("Finish_combox")
        self.Finish_combox_res.setObjectName("Finish_combox_res")
        self.Finish_combox_cfg.setObjectName("Finish_combox_cfg")

        # 启动/停止按钮和完成后操作标签

        self.LD1_layout = QHBoxLayout()
        self.S2_Button = PushButton(Task_Interface)
        self.S2_Button.setObjectName("S2_Button")

        self.LD1_layout.addWidget(self.S2_Button)
        self.LD1_layout.addStretch()
        self.LD1_layout.addLayout(self.Finish_combox_layout)

        self.LD7_layout = QVBoxLayout()
        self.LD7_layout.addLayout(self.LD5_layout)
        self.LD7_layout.addLayout(self.LD1_layout)

        # 添加任务区布局
        self.AddMission_layout = QGridLayout()

        self.TaskName_Title_1 = BodyLabel(Task_Interface)
        self.TaskName_Title_2 = BodyLabel(Task_Interface)
        self.TaskName_Title_3 = BodyLabel(Task_Interface)
        self.TaskName_Title_4 = BodyLabel(Task_Interface)

        self.TaskName_Title_1.setObjectName("TaskName_Title_1")
        self.TaskName_Title_2.setObjectName("TaskName_Title_2")
        self.TaskName_Title_3.setObjectName("TaskName_Title_3")
        self.TaskName_Title_4.setObjectName("TaskName_Title_4")

        self.SelectTask_Combox_1 = ComboBox(Task_Interface)
        self.SelectTask_Combox_2 = ComboBox(Task_Interface)
        self.SelectTask_Combox_3 = ComboBox(Task_Interface)
        self.SelectTask_Combox_4 = ComboBox(Task_Interface)

        self.MoveUp_Button = PushButton(Task_Interface)
        self.MoveDown_Button = PushButton(Task_Interface)
        self.Delete_Button = PushButton(Task_Interface)
        self.AddTask_Button = PushButton(Task_Interface)

        self.MoveUp_Button.setObjectName("MoveUp_Button")
        self.MoveDown_Button.setObjectName("MoveDown_Button")
        self.Delete_Button.setObjectName("Delete_Button")
        self.AddTask_Button.setObjectName("AddTask_Button")

        self.line = QFrame()
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Plain)

        self.line1 = QFrame()
        self.line1.setFrameShape(QFrame.Shape.HLine)
        self.line1.setFrameShadow(QFrame.Shadow.Plain)

        self.AddMission_layout.addWidget(self.TaskName_Title_1, 0, 0)
        self.AddMission_layout.addWidget(self.line, 1, 0)
        self.AddMission_layout.addWidget(self.TaskName_Title_2, 2, 0)
        self.AddMission_layout.addWidget(self.TaskName_Title_3, 3, 0)
        self.AddMission_layout.addWidget(self.TaskName_Title_4, 4, 0)

        self.AddMission_layout.addWidget(self.SelectTask_Combox_1, 0, 1)
        self.AddMission_layout.addWidget(self.line1, 1, 1)
        self.AddMission_layout.addWidget(self.SelectTask_Combox_2, 2, 1)
        self.AddMission_layout.addWidget(self.SelectTask_Combox_3, 3, 1)
        self.AddMission_layout.addWidget(self.SelectTask_Combox_4, 4, 1)

        self.AddMission_layout.addWidget(self.AddTask_Button, 0, 2)
        self.AddMission_layout.addWidget(self.MoveUp_Button, 2, 2)
        self.AddMission_layout.addWidget(self.MoveDown_Button, 3, 2)
        self.AddMission_layout.addWidget(self.Delete_Button, 4, 2)

        self.AddMission_layout.setColumnStretch(1, 10)

        # 左侧布局
        self.line2 = QFrame()
        self.line2.setFrameShape(QFrame.Shape.HLine)
        self.line2.setFrameShadow(QFrame.Shadow.Plain)

        self.left_layout = QVBoxLayout()
        self.left_layout.addLayout(self.AddMission_layout)
        self.left_layout.addStretch()
        self.left_layout.addWidget(self.line2)
        self.left_layout.addLayout(self.LD7_layout)

        # 中间布局（包含任务列表）
        self.middle_layout = QVBoxLayout()
        self.Task_List = ListWidge_Menu_Draggable(Task_Interface)
        self.Task_List.setDragEnabled(True)
        self.Task_List.setDragDropMode(QAbstractItemView.DragDropMode.InternalMove)
        self.Topic_Text = TextEdit(Task_Interface)
        self.Topic_Text.setReadOnly(True)
        self.Topic_Text.setObjectName("Topic_Text")

        self.middle_layout.addWidget(self.Task_List)
        self.middle_layout.addWidget(self.Topic_Text)

        # 右侧布局（包含文本编辑区域）
        self.right_layout = QVBoxLayout()
        self.TaskOutput_Text = TextEdit(Task_Interface)
        self.TaskOutput_Text.setReadOnly(True)
        self.TaskOutput_Text.setObjectName("TaskOutput_Text")
        self.right_layout.addWidget(self.TaskOutput_Text)

        # 将子布局添加到主布局中
        self.main_layout.addLayout(self.left_layout)
        self.main_layout.addLayout(self.middle_layout)
        self.main_layout.addLayout(self.right_layout)

        self.retranslateUi(Task_Interface)
        QMetaObject.connectSlotsByName(Task_Interface)

    def retranslateUi(self, Task_Interface):
        _translate = QCoreApplication.translate
        Task_Interface.setWindowTitle(_translate("Task_Interface", "Task Interface"))
        self.S2_Button.setText(_translate("Task_Interface", "Start"))
        self.Resource_Title.setText(_translate("Task_Interface", "Resource"))
        self.Control_Title.setText(_translate("Task_Interface", "Controller"))
        self.TaskName_Title_1.setText(_translate("Task_Interface", "Task"))
        self.AutoDetect_Button.setText(_translate("Task_Interface", "Auto Detect"))
        self.MoveUp_Button.setText(_translate("Task_Interface", "Move Up"))
        self.MoveDown_Button.setText(_translate("Task_Interface", "Move Down"))
        self.Delete_Button.setText(_translate("Task_Interface", "Delete"))
        self.AddTask_Button.setText(_translate("Task_Interface", "Add Task"))
