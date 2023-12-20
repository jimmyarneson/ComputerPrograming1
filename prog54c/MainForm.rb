require "mscorlib"
require "System.Windows.Forms, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089"
require "System.Drawing, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a"



def int(text)     return text.to_i end
def float(text)   return text.to_f end
def str(text)     return text.to_s end
def list(obj)     return obj.to_a  end
def len(arr)      return arr.length end
def input(msg="") print msg; return gets end
def print(*args)  Kernel.print(*args, "\n") end
def round(x, y)   return float((x * 10**y).round) / 10**y end
def range(*args)  if len(args) == 1 then 
    return  list((0...args[0]).step(1)); elsif len(args) == 2 then 
    return  list((args[0]...args[1]).step(1)); elsif len(args) == 3 then 
    return  list((args[0]...args[1]).step(args[2])) end; end
class MyRandom;   def randint(min, max) return rand(max-min) + min; end; 
    def random() return rand() end; 
    def shuffle(arr) return arr.shuffle end; 
    def choice(arr) return arr[randint(0, len(arr))] end; 
end; $random = MyRandom.new(); $math = Math
MessageBox = System::Windows::Forms::MessageBox



class MainForm < System::Windows::Forms::Form
	def initialize()
		self.InitializeComponent()
	end

	def InitializeComponent()
		@button1 = System::Windows::Forms::Button.new()
		@button2 = System::Windows::Forms::Button.new()
		@button3 = System::Windows::Forms::Button.new()
		@label1 = System::Windows::Forms::Label.new()
		@label3 = System::Windows::Forms::Label.new()
		@label4 = System::Windows::Forms::Label.new()
		@textBox1 = System::Windows::Forms::TextBox.new()
		self.SuspendLayout()
		# 
		# button1
		# 
		@button1.BackColor = System::Drawing::SystemColors.ControlDarkDark
		@button1.Font = System::Drawing::Font.new("Microsoft Sans Serif", 15.75, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button1.ForeColor = System::Drawing::Color.Coral
		@button1.Location = System::Drawing::Point.new(40, 383)
		@button1.Name = "button1"
		@button1.Size = System::Drawing::Size.new(121, 57)
		@button1.TabIndex = 0
		@button1.Text = "Calculate"
		@button1.UseVisualStyleBackColor = false
		@button1.Click { |sender, e| self.Button1Click(sender, e) }
		# 
		# button2
		# 
		@button2.BackColor = System::Drawing::SystemColors.ControlDarkDark
		@button2.Font = System::Drawing::Font.new("Microsoft Sans Serif", 15.75, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button2.ForeColor = System::Drawing::Color.Coral
		@button2.Location = System::Drawing::Point.new(262, 383)
		@button2.Name = "button2"
		@button2.Size = System::Drawing::Size.new(121, 57)
		@button2.TabIndex = 1
		@button2.Text = "Clear"
		@button2.UseVisualStyleBackColor = false
		@button2.Click { |sender, e| self.Button2Click(sender, e) }
		# 
		# button3
		# 
		@button3.BackColor = System::Drawing::SystemColors.ControlDarkDark
		@button3.Font = System::Drawing::Font.new("Microsoft Sans Serif", 15.75, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button3.ForeColor = System::Drawing::Color.Coral
		@button3.Location = System::Drawing::Point.new(488, 383)
		@button3.Name = "button3"
		@button3.Size = System::Drawing::Size.new(121, 57)
		@button3.TabIndex = 2
		@button3.Text = "Exit"
		@button3.UseVisualStyleBackColor = false
		@button3.Click { |sender, e| self.Button3Click(sender, e) }
		# 
		# label1
		# 
		@label1.BackColor = System::Drawing::SystemColors.ControlDark
		@label1.Font = System::Drawing::Font.new("Microsoft Sans Serif", 15.75, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label1.ForeColor = System::Drawing::Color.Cyan
		@label1.Location = System::Drawing::Point.new(15, 9)
		@label1.Name = "label1"
		@label1.Size = System::Drawing::Size.new(146, 57)
		@label1.TabIndex = 3
		@label1.Text = "Radius"
		@label1.Click { |sender, e| self.Label1Click(sender, e) }
		# 
		# label3
		# 
		@label3.BackColor = System::Drawing::SystemColors.ControlDark
		@label3.Font = System::Drawing::Font.new("Microsoft Sans Serif", 15.75, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label3.ForeColor = System::Drawing::Color.Cyan
		@label3.Location = System::Drawing::Point.new(15, 205)
		@label3.Name = "label3"
		@label3.Size = System::Drawing::Size.new(665, 57)
		@label3.TabIndex = 5
		@label3.Click { |sender, e| self.Label3Click(sender, e) }
		# 
		# label4
		# 
		@label4.BackColor = System::Drawing::SystemColors.ControlDark
		@label4.Font = System::Drawing::Font.new("Microsoft Sans Serif", 15.75, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label4.ForeColor = System::Drawing::Color.Cyan
		@label4.Location = System::Drawing::Point.new(15, 289)
		@label4.Name = "label4"
		@label4.Size = System::Drawing::Size.new(665, 57)
		@label4.TabIndex = 6
		@label4.Click { |sender, e| self.Label4Click(sender, e) }
		# 
		# textBox1
		# 
		@textBox1.Font = System::Drawing::Font.new("Microsoft Sans Serif", 15.75, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@textBox1.Location = System::Drawing::Point.new(192, 21)
		@textBox1.Name = "textBox1"
		@textBox1.Size = System::Drawing::Size.new(488, 31)
		@textBox1.TabIndex = 7
		@textBox1.TextChanged { |sender, e| self.TextBox1TextChanged(sender, e) }
		# 
		# MainForm
		# 
		self.BackColor = System::Drawing::Color.FromArgb(255, 192, 255)
		self.ClientSize = System::Drawing::Size.new(692, 452)
		self.Controls.Add(@textBox1)
		self.Controls.Add(@label4)
		self.Controls.Add(@label3)
		self.Controls.Add(@label1)
		self.Controls.Add(@button3)
		self.Controls.Add(@button2)
		self.Controls.Add(@button1)
		self.Name = "MainForm"
		self.Text = "prog54c"
		self.ResumeLayout(false)
		self.PerformLayout()
	end


	def Button2Click(sender, e)
		@textBox1.Text = ""
		@label3.Text = ""
		@label4.Text = ""
	end

	def Button3Click(sender, e)
		Application.Exit()
	end

	def Button1Click(sender, e)
		rad=float(@textBox1.Text)
		pi=3.14159
		area = pi * rad **2 area 
		rouarea = round(area, 3)
		cirufrence = 2 * pi * rad
		roucircufrence = round(circufrence, 3)
		@label3.Text = "area: " + str(rouarea) 
		@label4.Text = "circufrence" + str(roucircufrence)
		
	end

end

