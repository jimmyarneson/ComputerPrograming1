import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
		self.decDiscount4to6 = 0.05
		self.decDiscount7to9 = 0.08
		self.decDiscount10orMore = 0.1
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._radAdult = System.Windows.Forms.RadioButton()
		self._radChild = System.Windows.Forms.RadioButton()
		self._radStudent = System.Windows.Forms.RadioButton()
		self._radSenior = System.Windows.Forms.RadioButton()
		self._chkKarate = System.Windows.Forms.CheckBox()
		self._chkTrainer = System.Windows.Forms.CheckBox()
		self._label5 = System.Windows.Forms.Label()
		self._txtMonths = System.Windows.Forms.TextBox()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._lblMonthlyFee = System.Windows.Forms.Label()
		self._lblTotalFee = System.Windows.Forms.Label()
		self._btnCalculate = System.Windows.Forms.Button()
		self._btnClear = System.Windows.Forms.Button()
		self._btnExit = System.Windows.Forms.Button()
		self._chkYoga = System.Windows.Forms.CheckBox()
		self._chk = System.Windows.Forms.CheckBox()
		self._label8 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(12, 9)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(222, 32)
		self._label1.TabIndex = 0
		self._label1.Text = "Type Of Membership:"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label2
		# 
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(415, 9)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(222, 32)
		self._label2.TabIndex = 1
		self._label2.Text = "Options:"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label3
		# 
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(12, 235)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(222, 32)
		self._label3.TabIndex = 2
		self._label3.Text = "Membership Length:"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label4
		# 
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(415, 235)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(222, 32)
		self._label4.TabIndex = 3
		self._label4.Text = "Membership Fees:"
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# radAdult
		# 
		self._radAdult.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._radAdult.Location = System.Drawing.Point(13, 45)
		self._radAdult.Name = "radAdult"
		self._radAdult.Size = System.Drawing.Size(205, 28)
		self._radAdult.TabIndex = 4
		self._radAdult.TabStop = True
		self._radAdult.Text = "Standard Adult"
		self._radAdult.UseVisualStyleBackColor = True
		# 
		# radChild
		# 
		self._radChild.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._radChild.Location = System.Drawing.Point(12, 79)
		self._radChild.Name = "radChild"
		self._radChild.Size = System.Drawing.Size(222, 28)
		self._radChild.TabIndex = 5
		self._radChild.TabStop = True
		self._radChild.Text = "Child(12 and under)"
		self._radChild.UseVisualStyleBackColor = True
		# 
		# radStudent
		# 
		self._radStudent.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._radStudent.Location = System.Drawing.Point(12, 113)
		self._radStudent.Name = "radStudent"
		self._radStudent.Size = System.Drawing.Size(205, 28)
		self._radStudent.TabIndex = 6
		self._radStudent.TabStop = True
		self._radStudent.Text = "Student"
		self._radStudent.UseVisualStyleBackColor = True
		# 
		# radSenior
		# 
		self._radSenior.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._radSenior.Location = System.Drawing.Point(13, 147)
		self._radSenior.Name = "radSenior"
		self._radSenior.Size = System.Drawing.Size(205, 28)
		self._radSenior.TabIndex = 7
		self._radSenior.TabStop = True
		self._radSenior.Text = "Senior Citizen"
		self._radSenior.UseVisualStyleBackColor = True
		# 
		# chkKarate
		# 
		self._chkKarate.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._chkKarate.Location = System.Drawing.Point(415, 122)
		self._chkKarate.Name = "chkKarate"
		self._chkKarate.Size = System.Drawing.Size(222, 38)
		self._chkKarate.TabIndex = 9
		self._chkKarate.Text = "Karate"
		self._chkKarate.UseVisualStyleBackColor = True
		# 
		# chkTrainer
		# 
		self._chkTrainer.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._chkTrainer.Location = System.Drawing.Point(415, 109)
		self._chkTrainer.Name = "chkTrainer"
		self._chkTrainer.Size = System.Drawing.Size(222, 38)
		self._chkTrainer.TabIndex = 10
		self._chkTrainer.Text = "Personal Trainer"
		self._chkTrainer.UseVisualStyleBackColor = True
		# 
		# label5
		# 
		self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.Location = System.Drawing.Point(12, 267)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(222, 54)
		self._label5.TabIndex = 11
		self._label5.Text = "Enter Number of Months:"
		self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# txtMonths
		# 
		self._txtMonths.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._txtMonths.Location = System.Drawing.Point(68, 324)
		self._txtMonths.Name = "txtMonths"
		self._txtMonths.Size = System.Drawing.Size(115, 31)
		self._txtMonths.TabIndex = 12
		# 
		# label6
		# 
		self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.Location = System.Drawing.Point(395, 267)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(140, 32)
		self._label6.TabIndex = 13
		self._label6.Text = "Monthly Fee:"
		self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label7
		# 
		self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label7.Location = System.Drawing.Point(460, 299)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(75, 32)
		self._label7.TabIndex = 14
		self._label7.Text = "Total:"
		self._label7.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# lblMonthlyFee
		# 
		self._lblMonthlyFee.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._lblMonthlyFee.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._lblMonthlyFee.Location = System.Drawing.Point(541, 267)
		self._lblMonthlyFee.Name = "lblMonthlyFee"
		self._lblMonthlyFee.Size = System.Drawing.Size(75, 32)
		self._lblMonthlyFee.TabIndex = 15
		self._lblMonthlyFee.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# lblTotalFee
		# 
		self._lblTotalFee.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._lblTotalFee.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._lblTotalFee.Location = System.Drawing.Point(-172, -44)
		self._lblTotalFee.Name = "lblTotalFee"
		self._lblTotalFee.Size = System.Drawing.Size(75, 32)
		self._lblTotalFee.TabIndex = 16
		self._lblTotalFee.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# btnCalculate
		# 
		self._btnCalculate.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._btnCalculate.Location = System.Drawing.Point(13, 389)
		self._btnCalculate.Name = "btnCalculate"
		self._btnCalculate.Size = System.Drawing.Size(135, 34)
		self._btnCalculate.TabIndex = 17
		self._btnCalculate.Text = "Calculate"
		self._btnCalculate.UseVisualStyleBackColor = True
		self._btnCalculate.Click += self.Button1Click
		# 
		# btnClear
		# 
		self._btnClear.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._btnClear.Location = System.Drawing.Point(265, 389)
		self._btnClear.Name = "btnClear"
		self._btnClear.Size = System.Drawing.Size(135, 34)
		self._btnClear.TabIndex = 18
		self._btnClear.Text = "Clear"
		self._btnClear.UseVisualStyleBackColor = True
		self._btnClear.Click += self.Button2Click
		# 
		# btnExit
		# 
		self._btnExit.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._btnExit.Location = System.Drawing.Point(502, 389)
		self._btnExit.Name = "btnExit"
		self._btnExit.Size = System.Drawing.Size(135, 34)
		self._btnExit.TabIndex = 19
		self._btnExit.Text = "Exit"
		self._btnExit.UseVisualStyleBackColor = True
		self._btnExit.Click += self.Button3Click
		# 
		# chkYoga
		# 
		self._chkYoga.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._chkYoga.Location = System.Drawing.Point(415, 45)
		self._chkYoga.Name = "chkYoga"
		self._chkYoga.Size = System.Drawing.Size(222, 38)
		self._chkYoga.TabIndex = 8
		self._chkYoga.Text = "Yoga"
		self._chkYoga.UseVisualStyleBackColor = True
		# 
		# chk
		# 
		self._chk.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._chk.Location = System.Drawing.Point(415, 75)
		self._chk.Name = "chk"
		self._chk.Size = System.Drawing.Size(222, 38)
		self._chk.TabIndex = 20
		self._chk.Text = "Karate"
		self._chk.UseVisualStyleBackColor = True
		# 
		# label8
		# 
		self._label8.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._label8.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label8.Location = System.Drawing.Point(541, 299)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(75, 32)
		self._label8.TabIndex = 21
		self._label8.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(649, 435)
		self.Controls.Add(self._label8)
		self.Controls.Add(self._chk)
		self.Controls.Add(self._btnExit)
		self.Controls.Add(self._btnClear)
		self.Controls.Add(self._btnCalculate)
		self.Controls.Add(self._lblTotalFee)
		self.Controls.Add(self._lblMonthlyFee)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._txtMonths)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._chkTrainer)
		self.Controls.Add(self._chkKarate)
		self.Controls.Add(self._chkYoga)
		self.Controls.Add(self._radSenior)
		self.Controls.Add(self._radStudent)
		self.Controls.Add(self._radChild)
		self.Controls.Add(self._radAdult)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "membershipfeecalc"
		self.ResumeLayout(False)
		self.PerformLayout()

	def Button1Click(self, sender, e):
		decBaseFee = 0.0
		decDiscount = 0.0
		decTotalFee = 0.0
		intMonths = 0
		
		try:
			int(self._txtMonths.Text)
		except:
			MessageBox.Show("Months must be a valid integer:, :Input Error")
			return
		
		if intMonths < 1 or intMonths > 24:
			MessageBox.Show("Months must be a valid integer", "Input Error")
			return 
		
		if self.radAdult.Checked == True:
			decBaseFee = 40
		elif self._radChild.Checked == True:
			decBasefee = 20
		elif self.radStudent.Checked == True:
			decBasefee = 25
		elif self.radSenior.Checked == True:
			decBaseFee = 30
			
		if self._chkYoga.Checked == True:
			decBaseFee += 10
		if self.chk.Checked == True:
			decBaseFee += 30
		if self._chkTrainer.Checked == True:
			decBaseFee += 50
		
		if intMonths <= 3:
			decDiscount = 0.0
		elif intMonths >= 4 and intMonths <= 6:
			decDiscount = decBaseFee * self.decDiscount4to6
		elif intMonths >= 7 and intMonths <=9:
			decDiscount = decBaseFee * self.decDiscount7to9
		elif intMonths >= 10:
			decDiscount = decBaseFee * self.decDiscount10orMore
			
			decBaseFee -= decDiscount
			decTotalFee = decBaseFee * intMonths
			self._lblMothlyFee.Text = str(round(decBaseFee, 2))
			self._lblTotal.Text = str(round(decTotalFee, 2))
		
		
		
		
	def Button2Click(self, sender, e):
		self._radAdult.Checked = True
		self.chkYoga.Checked = False
		self.chk.Checked = False
		self.chkTrainer.Checked = False
		self._txtMonths.Clear()
		self.lblMothlyFee.Text = ""
		self.label8.Text = ""
	def Button2Click(self, sender, e):
		pass

	def Button3Click(self, sender, e):
		Application.Exit()