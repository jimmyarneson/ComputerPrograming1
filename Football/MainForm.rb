require "mscorlib"
require "System.Windows.Forms, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089"
require "System.Drawing, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a"

class MainForm < System::Windows::Forms::Form
	def initialize()
		self.InitializeComponent()
	end

	def InitializeComponent()
		@button1 = System::Windows::Forms::Button.new()
		@button2 = System::Windows::Forms::Button.new()
		@label1 = System::Windows::Forms::Label.new()
		self.SuspendLayout()
		# 
		# button1
		# 
		@button1.BackColor = System::Drawing::SystemColors.ControlLight
		@button1.Font = System::Drawing::Font.new("Microsoft Sans Serif", 27.75, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button1.ForeColor = System::Drawing::Color.CornflowerBlue
		@button1.Location = System::Drawing::Point.new(91, 12)
		@button1.Name = "button1"
		@button1.Size = System::Drawing::Size.new(175, 89)
		@button1.TabIndex = 0
		@button1.Text = "button1"
		@button1.UseVisualStyleBackColor = false
		@button1.Click { |sender, e| self.Button1Click(sender, e) }
		# 
		# button2
		# 
		@button2.BackColor = System::Drawing::SystemColors.ControlLight
		@button2.Font = System::Drawing::Font.new("Microsoft Sans Serif", 27.75, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button2.ForeColor = System::Drawing::Color.CornflowerBlue
		@button2.Location = System::Drawing::Point.new(363, 12)
		@button2.Name = "button2"
		@button2.Size = System::Drawing::Size.new(175, 89)
		@button2.TabIndex = 1
		@button2.Text = "button2"
		@button2.UseVisualStyleBackColor = false
		@button2.Click { |sender, e| self.Button2Click(sender, e) }
		# 
		# label1
		# 
		@label1.BackColor = System::Drawing::SystemColors.ControlLight
		@label1.Font = System::Drawing::Font.new("Microsoft Sans Serif", 36, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label1.ForeColor = System::Drawing::Color.Coral
		@label1.Location = System::Drawing::Point.new(91, 220)
		@label1.Name = "label1"
		@label1.Size = System::Drawing::Size.new(447, 159)
		@label1.TabIndex = 2
		# 
		# MainForm
		# 
		self.BackColor = System::Drawing::SystemColors.ControlDark
		self.ClientSize = System::Drawing::Size.new(621, 423)
		self.Controls.Add(@label1)
		self.Controls.Add(@button2)
		self.Controls.Add(@button1)
		self.Name = "MainForm"
		self.Text = "Football"
		self.ResumeLayout(false)
	end

	def Button1Click(sender, e)
		@label1.Text = "football"
	end

	def Button2Click(sender, e)
		@label1.Text = ""
	end
end

