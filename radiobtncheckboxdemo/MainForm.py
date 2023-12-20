import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._radioButton1 = System.Windows.Forms.RadioButton()
		self._radioButton2 = System.Windows.Forms.RadioButton()
		self._radioButton3 = System.Windows.Forms.RadioButton()
		self._checkBox1 = System.Windows.Forms.CheckBox()
		self._checkBox2 = System.Windows.Forms.CheckBox()
		self._checkBox3 = System.Windows.Forms.CheckBox()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(12, 131)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(100, 23)
		self._button1.TabIndex = 0
		self._button1.Text = "Okay"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(164, 131)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(100, 23)
		self._button2.TabIndex = 1
		self._button2.Text = "Exit"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# radioButton1
		# 
		self._radioButton1.Location = System.Drawing.Point(12, 13)
		self._radioButton1.Name = "radioButton1"
		self._radioButton1.Size = System.Drawing.Size(104, 24)
		self._radioButton1.TabIndex = 2
		self._radioButton1.TabStop = True
		self._radioButton1.Text = "Option 1"
		self._radioButton1.UseVisualStyleBackColor = True
		# 
		# radioButton2
		# 
		self._radioButton2.Location = System.Drawing.Point(12, 43)
		self._radioButton2.Name = "radioButton2"
		self._radioButton2.Size = System.Drawing.Size(100, 28)
		self._radioButton2.TabIndex = 3
		self._radioButton2.TabStop = True
		self._radioButton2.Text = "Option 2"
		self._radioButton2.UseVisualStyleBackColor = True
		# 
		# radioButton3
		# 
		self._radioButton3.Location = System.Drawing.Point(12, 77)
		self._radioButton3.Name = "radioButton3"
		self._radioButton3.Size = System.Drawing.Size(104, 24)
		self._radioButton3.TabIndex = 4
		self._radioButton3.TabStop = True
		self._radioButton3.Text = "Option 3"
		self._radioButton3.UseVisualStyleBackColor = True
		# 
		# checkBox1
		# 
		self._checkBox1.Location = System.Drawing.Point(139, 13)
		self._checkBox1.Name = "checkBox1"
		self._checkBox1.Size = System.Drawing.Size(104, 24)
		self._checkBox1.TabIndex = 5
		self._checkBox1.Text = "Option 4"
		self._checkBox1.UseVisualStyleBackColor = True
		# 
		# checkBox2
		# 
		self._checkBox2.Location = System.Drawing.Point(139, 46)
		self._checkBox2.Name = "checkBox2"
		self._checkBox2.Size = System.Drawing.Size(104, 24)
		self._checkBox2.TabIndex = 6
		self._checkBox2.Text = "Option 5"
		self._checkBox2.UseVisualStyleBackColor = True
		# 
		# checkBox3
		# 
		self._checkBox3.Location = System.Drawing.Point(139, 78)
		self._checkBox3.Name = "checkBox3"
		self._checkBox3.Size = System.Drawing.Size(104, 24)
		self._checkBox3.TabIndex = 7
		self._checkBox3.Text = "Option 6"
		self._checkBox3.UseVisualStyleBackColor = True
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(276, 160)
		self.Controls.Add(self._checkBox3)
		self.Controls.Add(self._checkBox2)
		self.Controls.Add(self._checkBox1)
		self.Controls.Add(self._radioButton3)
		self.Controls.Add(self._radioButton2)
		self.Controls.Add(self._radioButton1)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "radiobtncheckboxdemo"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		if self._radioButton1.Checked == True:
			strMessage = "You selected Choice 1"
		elif self._radioButton2.Checked == True:
			strMessage = "You selected Choice 2"
		elif self._radioButton3.Checked == True:
			strMessage = "You selected Choice 3"
			
		if self._checkBox1.Checked == True:
			strMessage += " and Choice 4"
		elif self._checkBox2.Checked == True:
			strMessage += " and Choice 5"
		elif self._checkBox3.Checked == True:
			strMessage += " and Choice 6"
			
		MessageBox.Show(strMessage)

	def Button2Click(self, sender, e):
		Application.Exit()