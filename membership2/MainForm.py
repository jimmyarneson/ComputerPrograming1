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
		self._radAdult = System.Windows.Forms.RadioButton()
		self._radChild = System.Windows.Forms.RadioButton()
		self._radStudent = System.Windows.Forms.RadioButton()
		self._radSenior = System.Windows.Forms.RadioButton()
		self._label2 = System.Windows.Forms.Label()
		self._chkYoga = System.Windows.Forms.CheckBox()
		self._chkKarate = System.Windows.Forms.CheckBox()
		self._chkTrainer = System.Windows.Forms.CheckBox()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._txtMonths = System.Windows.Forms.TextBox()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._lblTotalFee = System.Windows.Forms.Label()
		self._lblMonthlyFee = System.Windows.Forms.Label()
		self._btnCalculate = System.Windows.Forms.Button()
		self._btnClear = System.Windows.Forms.Button()
		self._btnExit = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(13, 13)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(214, 30)
		self._label1.TabIndex = 0
		self._label1.Text = "Type of Membership:"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# radAdult
		# 
		self._radAdult.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._radAdult.Location = System.Drawing.Point(33, 46)
		self._radAdult.Name = "radAdult"
		self._radAdult.Size = System.Drawing.Size(194, 24)
		self._radAdult.TabIndex = 1
		self._radAdult.TabStop = True
		self._radAdult.Text = "Standard Adult"
		self._radAdult.UseVisualStyleBackColor = True
		# 
		# radChild
		# 
		self._radChild.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._radChild.Location = System.Drawing.Point(33, 76)
		self._radChild.Name = "radChild"
		self._radChild.Size = System.Drawing.Size(194, 24)
		self._radChild.TabIndex = 2
		self._radChild.TabStop = True
		self._radChild.Text = "Child(12 & Under)"
		self._radChild.UseVisualStyleBackColor = True
		# 
		# radStudent
		# 
		self._radStudent.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._radStudent.Location = System.Drawing.Point(33, 106)
		self._radStudent.Name = "radStudent"
		self._radStudent.Size = System.Drawing.Size(194, 24)
		self._radStudent.TabIndex = 3
		self._radStudent.TabStop = True
		self._radStudent.Text = "Student"
		self._radStudent.UseVisualStyleBackColor = True
		# 
		# radSenior
		# 
		self._radSenior.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._radSenior.Location = System.Drawing.Point(33, 136)
		self._radSenior.Name = "radSenior"
		self._radSenior.Size = System.Drawing.Size(194, 24)
		self._radSenior.TabIndex = 4
		self._radSenior.TabStop = True
		self._radSenior.Text = "Senior Citizen"
		self._radSenior.UseVisualStyleBackColor = True
		# 
		# label2
		# 
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(405, 13)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(214, 30)
		self._label2.TabIndex = 5
		self._label2.Text = "Options:"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# chkYoga
		# 
		self._chkYoga.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._chkYoga.Location = System.Drawing.Point(440, 47)
		self._chkYoga.Name = "chkYoga"
		self._chkYoga.Size = System.Drawing.Size(157, 33)
		self._chkYoga.TabIndex = 6
		self._chkYoga.Text = "Yoga"
		self._chkYoga.TextAlign = System.Drawing.ContentAlignment.TopLeft
		self._chkYoga.UseVisualStyleBackColor = True
		# 
		# chkKarate
		# 
		self._chkKarate.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._chkKarate.Location = System.Drawing.Point(440, 75)
		self._chkKarate.Name = "chkKarate"
		self._chkKarate.Size = System.Drawing.Size(157, 33)
		self._chkKarate.TabIndex = 7
		self._chkKarate.Text = "Karate"
		self._chkKarate.TextAlign = System.Drawing.ContentAlignment.TopLeft
		self._chkKarate.UseVisualStyleBackColor = True
		# 
		# chkTrainer
		# 
		self._chkTrainer.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._chkTrainer.Location = System.Drawing.Point(440, 105)
		self._chkTrainer.Name = "chkTrainer"
		self._chkTrainer.Size = System.Drawing.Size(157, 33)
		self._chkTrainer.TabIndex = 8
		self._chkTrainer.Text = "Personal Trainer"
		self._chkTrainer.TextAlign = System.Drawing.ContentAlignment.TopLeft
		self._chkTrainer.UseVisualStyleBackColor = True
		# 
		# label3
		# 
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(12, 221)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(214, 24)
		self._label3.TabIndex = 9
		self._label3.Text = "Membership Length:"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label4
		# 
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(12, 245)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(214, 54)
		self._label4.TabIndex = 10
		self._label4.Text = "Enter Amount Of Months"
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# txtMonths
		# 
		self._txtMonths.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._txtMonths.Location = System.Drawing.Point(13, 303)
		self._txtMonths.Name = "txtMonths"
		self._txtMonths.Size = System.Drawing.Size(213, 26)
		self._txtMonths.TabIndex = 11
		# 
		# label5
		# 
		self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.Location = System.Drawing.Point(405, 221)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(214, 24)
		self._label5.TabIndex = 12
		self._label5.Text = "Membership Fees:"
		self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label6
		# 
		self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.Location = System.Drawing.Point(405, 251)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(81, 40)
		self._label6.TabIndex = 13
		self._label6.Text = "Total:"
		self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label7
		# 
		self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label7.Location = System.Drawing.Point(326, 291)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(160, 40)
		self._label7.TabIndex = 14
		self._label7.Text = "Cost A Months:"
		self._label7.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# lblTotalFee
		# 
		self._lblTotalFee.BackColor = System.Drawing.Color.White
		self._lblTotalFee.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._lblTotalFee.Location = System.Drawing.Point(492, 251)
		self._lblTotalFee.Name = "lblTotalFee"
		self._lblTotalFee.Size = System.Drawing.Size(81, 40)
		self._lblTotalFee.TabIndex = 15
		self._lblTotalFee.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# lblMonthlyFee
		# 
		self._lblMonthlyFee.BackColor = System.Drawing.Color.White
		self._lblMonthlyFee.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._lblMonthlyFee.Location = System.Drawing.Point(492, 294)
		self._lblMonthlyFee.Name = "lblMonthlyFee"
		self._lblMonthlyFee.Size = System.Drawing.Size(81, 40)
		self._lblMonthlyFee.TabIndex = 16
		self._lblMonthlyFee.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# btnCalculate
		# 
		self._btnCalculate.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._btnCalculate.Location = System.Drawing.Point(13, 377)
		self._btnCalculate.Name = "btnCalculate"
		self._btnCalculate.Size = System.Drawing.Size(182, 67)
		self._btnCalculate.TabIndex = 17
		self._btnCalculate.Text = "Calculate"
		self._btnCalculate.UseVisualStyleBackColor = True
		self._btnCalculate.Click += self.BtnCalculateClick
		# 
		# btnClear
		# 
		self._btnClear.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._btnClear.Location = System.Drawing.Point(230, 377)
		self._btnClear.Name = "btnClear"
		self._btnClear.Size = System.Drawing.Size(182, 67)
		self._btnClear.TabIndex = 18
		self._btnClear.Text = "Clear"
		self._btnClear.UseVisualStyleBackColor = True
		self._btnClear.Click += self.BtnClearClick
		# 
		# btnExit
		# 
		self._btnExit.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._btnExit.Location = System.Drawing.Point(437, 377)
		self._btnExit.Name = "btnExit"
		self._btnExit.Size = System.Drawing.Size(182, 67)
		self._btnExit.TabIndex = 19
		self._btnExit.Text = "Exit"
		self._btnExit.UseVisualStyleBackColor = True
		self._btnExit.Click += self.BtnExitClick
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(631, 456)
		self.Controls.Add(self._btnExit)
		self.Controls.Add(self._btnClear)
		self.Controls.Add(self._btnCalculate)
		self.Controls.Add(self._lblMonthlyFee)
		self.Controls.Add(self._lblTotalFee)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._txtMonths)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._chkTrainer)
		self.Controls.Add(self._chkKarate)
		self.Controls.Add(self._chkYoga)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._radSenior)
		self.Controls.Add(self._radStudent)
		self.Controls.Add(self._radChild)
		self.Controls.Add(self._radAdult)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "membership2"
		self.ResumeLayout(False)
		self.PerformLayout()


	def BtnCalculateClick(self, sender, e):
		decBaseFee = 0.0
		decDiscount = 0.0
		decTotalFee = 0.0
		intMonths = 0
		
		try:
			intMonths = int(self._txtMonths.Text)
		except:
			MessageBox.Show("Months must be a valid intefer", "Input Error")
		if intMonths < 1 or intMonths > 24:
			Message.Show("Months must be a valid integer", "Input Error")
			return
		
		if self._radAdult.Checked == True:
			decBaseFee = 40
		elif self._radChild.Checked == True:
			decBaseFee = 20
		elif self._radStudent.Checked == True:
			decBaseFee = 25
		elif self.radSenior.Checked == True:
			decBaseFee = 30
			
		if self._chkYoga.Checked == True:
			decBaseFee += 10
		if self._chkKarate.Checked == True:
			decBaseFee += 30
		if self._chkTrainer.Checked == True:
			decBaseFee += 50
		
		if intMonths <= 3:
			decDiscount = 0.0
		elif intMonths >=4 and intMonths <=6:
			decDiscount = decBaseFee * self.decDiscount4to6
		elif intMonths >= 7 and intMonths <= 9:
			decDiscount = decBaseFee *self.decDiscount7to9
		elif intMonths >= 10:
			decDiscount = decBaseFee * self.decDiscount10orMore
			
		decBaseFee -= decDiscount
		decTotalFee = decBaseFee * intMonths
		self._lblMonthlyFee.Text = str(round(decBaseFee, 2))
		self._lblTotalFee.Text = str(round(decTotalFee, 2))
			
			

	def BtnClearClick(self, sender, e):
		self._radAdult.Checked = True
		self._chkYoga.Checked = False
		self._chkKarate.Checked = False
		self._chkTrainer.Checked = False
		self._txtMonths.Clear()
		self._lblMonthlyFee.Text = ""
		self._lblMonthlyFee.Text = ""
		self._lblTotalFee.Text = ""

	def BtnExitClick(self, sender, e):
		Application.Exit()