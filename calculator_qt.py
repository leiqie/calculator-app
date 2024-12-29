"""
使用 PyQt6 的加法计算器
"""
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, 
                           QVBoxLayout, QPushButton, QLabel, 
                           QLineEdit, QMessageBox)
from PyQt6.QtCore import Qt
import sys

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        # 设置窗口标题和大小
        self.setWindowTitle("加法计算器")
        self.setFixedSize(300, 200)
        
        # 创建中央部件
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # 创建垂直布局
        layout = QVBoxLayout(central_widget)
        layout.setContentsMargins(20, 20, 20, 20)
        
        # 第一个输入框
        self.label1 = QLabel("第一个数字：")
        layout.addWidget(self.label1)
        self.num1_entry = QLineEdit()
        layout.addWidget(self.num1_entry)
        
        # 第二个输入框
        self.label2 = QLabel("第二个数字：")
        layout.addWidget(self.label2)
        self.num2_entry = QLineEdit()
        layout.addWidget(self.num2_entry)
        
        # 添加一些空间
        layout.addSpacing(10)
        
        # 计算按钮
        self.calc_button = QPushButton("计算")
        self.calc_button.clicked.connect(self.calculate)
        layout.addWidget(self.calc_button)
        
        # 设置样式
        self.setStyleSheet("""
            QMainWindow {
                background-color: white;
            }
            QLabel {
                font-size: 14px;
                color: #333333;
            }
            QLineEdit {
                padding: 8px;
                font-size: 14px;
                border: 1px solid #CCCCCC;
                border-radius: 4px;
                background-color: white;
            }
            QPushButton {
                padding: 10px;
                font-size: 14px;
                background-color: #4CAF50;
                color: white;
                border: none;
                border-radius: 4px;
                min-height: 20px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        
    def calculate(self):
        try:
            # 获取输入值并计算
            num1 = float(self.num1_entry.text())
            num2 = float(self.num2_entry.text())
            result = num1 + num2
            
            # 显示结果
            QMessageBox.information(self, 
                                  "计算结果", 
                                  f"{num1} + {num2} = {result}")
        except ValueError:
            QMessageBox.warning(self, 
                              "错误", 
                              "请输入有效的数字！")

def main():
    # 创建应用程序实例
    app = QApplication(sys.argv)
    
    # 创建并显示计算器窗口
    calculator = Calculator()
    calculator.show()
    
    # 运行应用程序
    sys.exit(app.exec())

if __name__ == "__main__":
    main() 