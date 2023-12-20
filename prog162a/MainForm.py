import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._btnCalculate = System.Windows.Forms.Button()
		self._btnClear = System.Windows.Forms.Button()
		self._btnExit = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._lblValue = System.Windows.Forms.Label()
		self._lblNum = System.Windows.Forms.TextBox()
		self.SuspendLayout()
		# 
		# btnCalculate
		# 
		self._btnCalculate.Location = System.Drawing.Point(12, 316)
		self._btnCalculate.Name = "btnCalculate"
		self._btnCalculate.Size = System.Drawing.Size(75, 23)
		self._btnCalculate.TabIndex = 1
		self._btnCalculate.Text = "Calculate"
		self._btnCalculate.UseVisualStyleBackColor = True
		self._btnCalculate.Click += self.BtnCalculateClick
		# 
		# btnClear
		# 
		self._btnClear.Location = System.Drawing.Point(93, 316)
		self._btnClear.Name = "btnClear"
		self._btnClear.Size = System.Drawing.Size(75, 23)
		self._btnClear.TabIndex = 2
		self._btnClear.Text = "Clear"
		self._btnClear.UseVisualStyleBackColor = True
		# 
		# btnExit
		# 
		self._btnExit.Location = System.Drawing.Point(174, 316)
		self._btnExit.Name = "btnExit"
		self._btnExit.Size = System.Drawing.Size(75, 23)
		self._btnExit.TabIndex = 3
		self._btnExit.Text = "Exit"
		self._btnExit.UseVisualStyleBackColor = True
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(12, 25)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 20)
		self._label1.TabIndex = 4
		self._label1.Text = "Enter A number:"
		# 
		# label2
		# 
		self._label2.Location = System.Drawing.Point(12, 45)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(74, 20)
		self._label2.TabIndex = 5
		self._label2.Text = "The Value is:"
		# 
		# lblValue
		# 
		self._lblValue.BackColor = System.Drawing.SystemColors.ControlLightLight
		self._lblValue.Location = System.Drawing.Point(93, 45)
		self._lblValue.Name = "lblValue"
		self._lblValue.Size = System.Drawing.Size(159, 23)
		self._lblValue.TabIndex = 7
		# 
		# lblNum
		# 
		self._lblNum.Location = System.Drawing.Point(93, 25)
		self._lblNum.Name = "lblNum"
		self._lblNum.Size = System.Drawing.Size(159, 20)
		self._lblNum.TabIndex = 8
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(264, 351)
		self.Controls.Add(self._lblNum)
		self.Controls.Add(self._lblValue)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._btnExit)
		self.Controls.Add(self._btnClear)
		self.Controls.Add(self._btnCalculate)
		self.Name = "MainForm"
		self.Text = "prog162a"
		self.ResumeLayout(False)
		self.PerformLayout()


	def BtnCalculateClick(self, sender, e):
		num1 = str(self._lblNum)
		
		self._lblValue = num1 * 1 * 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9 * 10 * 11 * 12