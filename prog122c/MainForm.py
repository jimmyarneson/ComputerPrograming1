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
		self._button3 = System.Windows.Forms.Button()
		self._listBox1 = System.Windows.Forms.ListBox()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.FromArgb(128, 128, 255)
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(12, 326)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(117, 53)
		self._button1.TabIndex = 0
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.FromArgb(128, 128, 255)
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(135, 326)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(117, 53)
		self._button2.TabIndex = 1
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.FromArgb(128, 128, 255)
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(258, 326)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(117, 53)
		self._button3.TabIndex = 2
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		# 
		# listBox1
		# 
		self._listBox1.BackColor = System.Drawing.Color.FromArgb(128, 128, 255)
		self._listBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._listBox1.FormattingEnabled = True
		self._listBox1.ItemHeight = 31
		self._listBox1.Location = System.Drawing.Point(11, 12)
		self._listBox1.Name = "listBox1"
		self._listBox1.Size = System.Drawing.Size(363, 283)
		self._listBox1.TabIndex = 3
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.FromArgb(0, 0, 192)
		self.ClientSize = System.Drawing.Size(386, 391)
		self.Controls.Add(self._listBox1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "prog122c"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		header = "Function\tChart"
		self._listBox1.Items.Add(header)
		num1 = 2
		num2 = 3
		num3 = 4
		msg = str(num) 
		
		self._listBox1 = "2\t3\t4t\4"