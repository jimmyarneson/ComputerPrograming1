import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label7 = System.Windows.Forms.Label()
		self._label8 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._label9 = System.Windows.Forms.Label()
		self._label10 = System.Windows.Forms.Label()
		self._label11 = System.Windows.Forms.Label()
		self._label12 = System.Windows.Forms.Label()
		self._label13 = System.Windows.Forms.Label()
		self._label14 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.SystemColors.ControlDark
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.ForeColor = System.Drawing.Color.Coral
		self._label1.Location = System.Drawing.Point(-1, 0)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(174, 33)
		self._label1.TabIndex = 0
		self._label1.Text = "purchase price"
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.SystemColors.ControlDark
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.ForeColor = System.Drawing.Color.Coral
		self._label2.Location = System.Drawing.Point(-1, 33)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(174, 33)
		self._label2.TabIndex = 1
		self._label2.Text = "amount recived"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.SystemColors.ControlDark
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.ForeColor = System.Drawing.Color.Coral
		self._label3.Location = System.Drawing.Point(-1, 66)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(174, 33)
		self._label3.TabIndex = 2
		self._label3.Text = "change due"
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.SystemColors.ControlDark
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.ForeColor = System.Drawing.Color.Coral
		self._label4.Location = System.Drawing.Point(-1, 99)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(174, 33)
		self._label4.TabIndex = 3
		self._label4.Text = "dollars"
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.SystemColors.ControlDark
		self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.ForeColor = System.Drawing.Color.Coral
		self._label5.Location = System.Drawing.Point(-1, 132)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(174, 33)
		self._label5.TabIndex = 4
		self._label5.Text = "quarters"
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.SystemColors.ControlDark
		self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.ForeColor = System.Drawing.Color.Coral
		self._label6.Location = System.Drawing.Point(-1, 165)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(174, 33)
		self._label6.TabIndex = 5
		self._label6.Text = "dimes"
		self._label6.Click += self.Label6Click
		# 
		# textBox1
		# 
		self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(171, 0)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(158, 31)
		self._textBox1.TabIndex = 6
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.SystemColors.ControlDark
		self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label7.ForeColor = System.Drawing.Color.Coral
		self._label7.Location = System.Drawing.Point(-1, 198)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(174, 33)
		self._label7.TabIndex = 7
		self._label7.Text = "nikels"
		# 
		# label8
		# 
		self._label8.BackColor = System.Drawing.SystemColors.ControlDark
		self._label8.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label8.ForeColor = System.Drawing.Color.Coral
		self._label8.Location = System.Drawing.Point(-1, 231)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(174, 33)
		self._label8.TabIndex = 8
		self._label8.Text = "penies"
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(-1, 267)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(110, 72)
		self._button1.TabIndex = 9
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(115, 267)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(110, 72)
		self._button2.TabIndex = 10
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(224, 267)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(110, 72)
		self._button3.TabIndex = 11
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# textBox2
		# 
		self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.Location = System.Drawing.Point(171, 30)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(158, 31)
		self._textBox2.TabIndex = 12
		# 
		# label9
		# 
		self._label9.BackColor = System.Drawing.SystemColors.ControlDark
		self._label9.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label9.ForeColor = System.Drawing.Color.Coral
		self._label9.Location = System.Drawing.Point(171, 64)
		self._label9.Name = "label9"
		self._label9.Size = System.Drawing.Size(174, 33)
		self._label9.TabIndex = 13
		# 
		# label10
		# 
		self._label10.BackColor = System.Drawing.SystemColors.ControlDark
		self._label10.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label10.ForeColor = System.Drawing.Color.Coral
		self._label10.Location = System.Drawing.Point(171, 97)
		self._label10.Name = "label10"
		self._label10.Size = System.Drawing.Size(174, 33)
		self._label10.TabIndex = 14
		# 
		# label11
		# 
		self._label11.BackColor = System.Drawing.SystemColors.ControlDark
		self._label11.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label11.ForeColor = System.Drawing.Color.Coral
		self._label11.Location = System.Drawing.Point(171, 130)
		self._label11.Name = "label11"
		self._label11.Size = System.Drawing.Size(174, 33)
		self._label11.TabIndex = 15
		# 
		# label12
		# 
		self._label12.BackColor = System.Drawing.SystemColors.ControlDark
		self._label12.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label12.ForeColor = System.Drawing.Color.Coral
		self._label12.Location = System.Drawing.Point(171, 163)
		self._label12.Name = "label12"
		self._label12.Size = System.Drawing.Size(174, 33)
		self._label12.TabIndex = 16
		# 
		# label13
		# 
		self._label13.BackColor = System.Drawing.SystemColors.ControlDark
		self._label13.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label13.ForeColor = System.Drawing.Color.Coral
		self._label13.Location = System.Drawing.Point(171, 196)
		self._label13.Name = "label13"
		self._label13.Size = System.Drawing.Size(174, 33)
		self._label13.TabIndex = 17
		# 
		# label14
		# 
		self._label14.BackColor = System.Drawing.SystemColors.ControlDark
		self._label14.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label14.ForeColor = System.Drawing.Color.Coral
		self._label14.Location = System.Drawing.Point(171, 229)
		self._label14.Name = "label14"
		self._label14.Size = System.Drawing.Size(174, 33)
		self._label14.TabIndex = 18
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(335, 339)
		self.Controls.Add(self._label14)
		self.Controls.Add(self._label13)
		self.Controls.Add(self._label12)
		self.Controls.Add(self._label11)
		self.Controls.Add(self._label10)
		self.Controls.Add(self._label9)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label8)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "prog58t"
		self.ResumeLayout(False)
		self.PerformLayout()
		#125.32

	def Label6Click(self, sender, e):
		pass

	def Button1Click(self, sender, e):
		num1 = float(self._textBox1.Text)
		num2 = float(self._textBox2.Text) 
		dollar = 1.00
		quarter = 0.25
		dime = 0.10
		nikel = 0.05
		pennie = 0.01
		cd = num2 - num1
		dd = cd // dollar
		change = cd - dd
		qd = change // quarter
		dimechange = qd - change
		dimesdue = dimechange
		nikelchange = dimesdue // change
		nikelsdue = nikelchange
		pennychange = change + qd + nikelsdue - dimesdue + nikelsdue
		penniesdue = pennychange
		self._label9.Text = "" + str(cd)
		self._label10.Text = "" + str(dd)
		self._label11.Text = "" + str(qd)
		self._label12.Text = "" + str(round(dimesdue, 0))
		self._label13.Text = "" + str(nikelsdue)
		self._label14.Text = "" + str(round(penniesdue, 0))
	def Button3Click(self, sender, e):
		Application.Exit()

	def Button2Click(self, sender, e):
		self._label9.Text = ""
		self._label10.Text = ""
		self._label11.Text = ""
		self._label12.Text = "" 
		self._label13.Text = ""
		self._label14.Text = ""
		self._textBox1.Text = ""
		self._textBox2.Text = ""