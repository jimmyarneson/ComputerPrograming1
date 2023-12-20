import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label2 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._label8 = System.Windows.Forms.Label()
		self._label9 = System.Windows.Forms.Label()
		self._label10 = System.Windows.Forms.Label()
		self._label11 = System.Windows.Forms.Label()
		self._label13 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self.SuspendLayout()
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.CornflowerBlue
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.ForeColor = System.Drawing.Color.Coral
		self._label2.Location = System.Drawing.Point(1, 126)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(195, 31)
		self._label2.TabIndex = 2
		self._label2.Text = "Total Charge"
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(1, 200)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(101, 51)
		self._button1.TabIndex = 4
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(125, 200)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(101, 51)
		self._button2.TabIndex = 5
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(232, 200)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(101, 51)
		self._button3.TabIndex = 6
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.SystemColors.ControlLightLight
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(232, 126)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(100, 31)
		self._label3.TabIndex = 7
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.SystemColors.ControlLightLight
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(232, 36)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(100, 31)
		self._label4.TabIndex = 8
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.SystemColors.ControlLightLight
		self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.Location = System.Drawing.Point(232, 67)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(100, 31)
		self._label5.TabIndex = 9
		self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.SystemColors.ControlLightLight
		self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.Location = System.Drawing.Point(232, 95)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(100, 31)
		self._label6.TabIndex = 10
		self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._label6.Click += self.Label6Click
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.SystemColors.ControlLightLight
		self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label7.Location = System.Drawing.Point(232, 157)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(100, 31)
		self._label7.TabIndex = 11
		self._label7.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label8
		# 
		self._label8.BackColor = System.Drawing.Color.CornflowerBlue
		self._label8.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label8.ForeColor = System.Drawing.Color.Coral
		self._label8.Location = System.Drawing.Point(1, 157)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(195, 31)
		self._label8.TabIndex = 12
		self._label8.Text = "After May 20th"
		# 
		# label9
		# 
		self._label9.BackColor = System.Drawing.Color.CornflowerBlue
		self._label9.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label9.ForeColor = System.Drawing.Color.Coral
		self._label9.Location = System.Drawing.Point(1, 95)
		self._label9.Name = "label9"
		self._label9.Size = System.Drawing.Size(195, 31)
		self._label9.TabIndex = 13
		self._label9.Text = "City Tax"
		# 
		# label10
		# 
		self._label10.BackColor = System.Drawing.Color.CornflowerBlue
		self._label10.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label10.ForeColor = System.Drawing.Color.Coral
		self._label10.Location = System.Drawing.Point(1, 67)
		self._label10.Name = "label10"
		self._label10.Size = System.Drawing.Size(195, 31)
		self._label10.TabIndex = 14
		self._label10.Text = "Surcharge"
		# 
		# label11
		# 
		self._label11.BackColor = System.Drawing.Color.CornflowerBlue
		self._label11.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label11.ForeColor = System.Drawing.Color.Coral
		self._label11.Location = System.Drawing.Point(1, 36)
		self._label11.Name = "label11"
		self._label11.Size = System.Drawing.Size(195, 31)
		self._label11.TabIndex = 15
		self._label11.Text = "Base Rate"
		# 
		# label13
		# 
		self._label13.BackColor = System.Drawing.Color.CornflowerBlue
		self._label13.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label13.ForeColor = System.Drawing.Color.Coral
		self._label13.Location = System.Drawing.Point(1, 5)
		self._label13.Name = "label13"
		self._label13.Size = System.Drawing.Size(195, 31)
		self._label13.TabIndex = 19
		self._label13.Text = "KW Used"
		# 
		# textBox1
		# 
		self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(232, 5)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 31)
		self._textBox1.TabIndex = 20
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.SystemColors.ControlLight
		self.ClientSize = System.Drawing.Size(344, 259)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label13)
		self.Controls.Add(self._label11)
		self.Controls.Add(self._label10)
		self.Controls.Add(self._label9)
		self.Controls.Add(self._label8)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label2)
		self.Name = "MainForm"
		self.Text = "lang93a"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Label6Click(self, sender, e):
		pass

	def TextBox1TextChanged(self, sender, e):
		self._textBox1 = sum
	
	def Button1Click(self, sender, e):
		num1 = float(self._textBox1.Text)
		bsrt = num1 * 0.0475
		surchrg = bsrt * 0.10
		citytax = bsrt * 0.03
		totalchrg = round(bsrt, 2) + round(surchrg, 2) + round(citytax, 2)
		aftertw = totalchrg * 0.04 + totalchrg
		self._label4.Text = str(round(bsrt, 2))
		self._label5.Text = str(round(surchrg, 2))
		self._label6.Text = str(round(citytax, 2))
		self._label3.Text = str(round(totalchrg, 2))
		self._label7.Text = str(round(aftertw, 2))

	def TextBox2TextChanged(self, sender, e):
		pass
		

	def Button3Click(self, sender, e):
		Application.Exit()

	def Button2Click(self, sender, e):
		self._Textbox1 = ""
		self._label4.Text = ""
		self._label5.Text = ""
		self._label6.Text = ""
		self._label3.Text = ""
		self._label7.Text = ""