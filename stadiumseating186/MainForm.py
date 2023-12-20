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
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._textBox3 = System.Windows.Forms.TextBox()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._label8 = System.Windows.Forms.Label()
		self._label9 = System.Windows.Forms.Label()
		self._label10 = System.Windows.Forms.Label()
		self._label11 = System.Windows.Forms.Label()
		self._label12 = System.Windows.Forms.Label()
		self._label13 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(13, 13)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(162, 27)
		self._label1.TabIndex = 0
		self._label1.Text = "Tickets Sold:"
		# 
		# label2
		# 
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(13, 59)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 23)
		self._label2.TabIndex = 1
		self._label2.Text = "Section A:"
		# 
		# label3
		# 
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(12, 93)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(100, 23)
		self._label3.TabIndex = 2
		self._label3.Text = "Section B:"
		# 
		# label4
		# 
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(13, 126)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(100, 23)
		self._label4.TabIndex = 3
		self._label4.Text = "Section C:"
		# 
		# textBox1
		# 
		self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(119, 59)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 29)
		self._textBox1.TabIndex = 4
		# 
		# textBox2
		# 
		self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.Location = System.Drawing.Point(119, 90)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 29)
		self._textBox2.TabIndex = 5
		# 
		# textBox3
		# 
		self._textBox3.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox3.Location = System.Drawing.Point(119, 120)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(100, 29)
		self._textBox3.TabIndex = 6
		# 
		# label5
		# 
		self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.Location = System.Drawing.Point(252, 62)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(100, 23)
		self._label5.TabIndex = 7
		self._label5.Text = "Section A:"
		# 
		# label6
		# 
		self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.Location = System.Drawing.Point(252, 90)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(100, 23)
		self._label6.TabIndex = 8
		self._label6.Text = "Section B:"
		# 
		# label7
		# 
		self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label7.Location = System.Drawing.Point(252, 126)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(100, 23)
		self._label7.TabIndex = 9
		self._label7.Text = "Section C:"
		# 
		# label8
		# 
		self._label8.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label8.Location = System.Drawing.Point(252, 13)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(204, 27)
		self._label8.TabIndex = 10
		self._label8.Text = "Revenue Generated:"
		# 
		# label9
		# 
		self._label9.BackColor = System.Drawing.Color.White
		self._label9.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label9.Location = System.Drawing.Point(210, 163)
		self._label9.Name = "label9"
		self._label9.Size = System.Drawing.Size(142, 23)
		self._label9.TabIndex = 11
		self._label9.Text = "Total Revenue:"
		# 
		# label10
		# 
		self._label10.BackColor = System.Drawing.Color.White
		self._label10.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label10.Location = System.Drawing.Point(358, 65)
		self._label10.Name = "label10"
		self._label10.Size = System.Drawing.Size(126, 23)
		self._label10.TabIndex = 12
		# 
		# label11
		# 
		self._label11.BackColor = System.Drawing.Color.White
		self._label11.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label11.Location = System.Drawing.Point(358, 93)
		self._label11.Name = "label11"
		self._label11.Size = System.Drawing.Size(126, 23)
		self._label11.TabIndex = 13
		# 
		# label12
		# 
		self._label12.BackColor = System.Drawing.Color.White
		self._label12.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label12.Location = System.Drawing.Point(358, 126)
		self._label12.Name = "label12"
		self._label12.Size = System.Drawing.Size(126, 23)
		self._label12.TabIndex = 14
		# 
		# label13
		# 
		self._label13.BackColor = System.Drawing.Color.White
		self._label13.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label13.Location = System.Drawing.Point(358, 163)
		self._label13.Name = "label13"
		self._label13.Size = System.Drawing.Size(126, 23)
		self._label13.TabIndex = 15
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(13, 225)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(216, 45)
		self._button1.TabIndex = 16
		self._button1.Text = "Revenue Generated:"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(236, 225)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(128, 45)
		self._button2.TabIndex = 17
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(370, 225)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(128, 45)
		self._button3.TabIndex = 18
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(510, 282)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label13)
		self.Controls.Add(self._label12)
		self.Controls.Add(self._label11)
		self.Controls.Add(self._label10)
		self.Controls.Add(self._label9)
		self.Controls.Add(self._label8)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._textBox3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "stadiumseating186"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		num1 = int(self._textBox1.Text)
		num2 = int(self._textBox2.Text)
		num3 = int(self._textBox3.Text)
		secta = num1 * 15
		sectb = num2 * 12
		sectc = num3 * 9
		total = secta + sectb + sectc
		self._label10.Text = str(secta)
		self._label11.Text = str(sectb)
		self._label12.Text = str(sectc)
		self._label13.Text = str(total)
		

	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._textBox3.Text = ""
		self._label10.Text = ""
		self._label11.Text = ""
		self._label12.Text = ""
		self._label13.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()