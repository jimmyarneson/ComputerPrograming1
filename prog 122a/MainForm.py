import System.Drawing
import math
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._listBox1 = System.Windows.Forms.ListBox()
		self._label1 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# listBox1
		# 
		self._listBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._listBox1.FormattingEnabled = True
		self._listBox1.ItemHeight = 24
		self._listBox1.Location = System.Drawing.Point(12, 68)
		self._listBox1.Name = "listBox1"
		self._listBox1.Size = System.Drawing.Size(328, 172)
		self._listBox1.TabIndex = 0
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.White
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(13, 13)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(327, 41)
		self._label1.TabIndex = 1
		self._label1.Text = "Hourly Pay"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(12, 247)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(103, 78)
		self._button1.TabIndex = 2
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(121, 246)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(108, 78)
		self._button2.TabIndex = 3
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(237, 246)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(103, 78)
		self._button3.TabIndex = 4
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.FromArgb(192, 192, 255)
		self.ClientSize = System.Drawing.Size(353, 337)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._listBox1)
		self.Name = "MainForm"
		self.Text = "prog 122a"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		header = "Hours\t\tPay\t\t4 Dollars"
		self._listBox1.Items.Add(header)
		for num in range(1, 41):
			numsqrd = num*4
			numsqrt = math.sqrt(num)
			msg = str(num) + "\t\t" + str(numsqrd) + \
					"\t\t" + str(round(numsqrt, 4))
			self._listBox1.Items.Add(msg)

	def Button2Click(self, sender, e):
		self._listBox1.Items.Clear()

	def Button3Click(self, sender, e):
		Application.Exit()