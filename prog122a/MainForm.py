import math
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._listBox1 = System.Windows.Forms.ListBox()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# listBox1
		# 
		self._listBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._listBox1.FormattingEnabled = True
		self._listBox1.ItemHeight = 29
		self._listBox1.Location = System.Drawing.Point(2, 1)
		self._listBox1.Name = "listBox1"
		self._listBox1.Size = System.Drawing.Size(387, 352)
		self._listBox1.TabIndex = 0
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(2, 352)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(107, 94)
		self._button1.TabIndex = 1
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(152, 352)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(107, 94)
		self._button2.TabIndex = 2
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(282, 352)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(107, 94)
		self._button3.TabIndex = 3
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(390, 442)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._listBox1)
		self.Name = "MainForm"
		self.Text = "prog122a"
		self.ResumeLayout(False)


	def Button2Click(self, sender, e):
		self._listBox1.Items.Clear()

	def Button1Click(self, sender, e):
		header = "Number\t\tSquare\t\tSquare Root"
		self._listBox1.Items.Add(header)
		for num in range(1, 50+1):
			numsqrd = num**2
			numsqrt = math.sqrt(num)
			msg = str(num) + "\t\t" + str(numsqrd) + \
					"\t\t" + str(round(numsqrt, 4))
			self._listBox1.Items.Add(msg)
			

	def Button3Click(self, sender, e):
		Application.Exit()