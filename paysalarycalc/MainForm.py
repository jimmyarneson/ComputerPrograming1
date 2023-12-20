import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# textBox1
		# 
		self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(208, 8)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(183, 29)
		self._textBox1.TabIndex = 0
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(12, 7)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(190, 30)
		self._label1.TabIndex = 1
		self._label1.Text = "Annual Salary:"
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(12, 37)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(190, 30)
		self._label2.TabIndex = 2
		self._label2.Text = "Pay periods in a year:"
		# 
		# textBox2
		# 
		self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.Location = System.Drawing.Point(208, 38)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(183, 29)
		self._textBox2.TabIndex = 3
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(12, 67)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(190, 30)
		self._label3.TabIndex = 4
		self._label3.Text = "Salary per period:"
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(208, 70)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(190, 30)
		self._label4.TabIndex = 5
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(12, 117)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(113, 48)
		self._button1.TabIndex = 6
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(146, 117)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(113, 48)
		self._button2.TabIndex = 7
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(278, 117)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(113, 48)
		self._button3.TabIndex = 8
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(403, 172)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._textBox1)
		self.Name = "MainForm"
		self.Text = "paysalarycalc"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button3Click(self, sender, e):
		Application.Exit()

	def Button1Click(self, sender, e):
		num1 = int(self._textBox1.Text)
		num2 = int(self._textBox2.Text)
		#spp = num1 / num2
		self._label4.Text = str(round(num1 / float(num2), 2))

	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._label4.Text = ""