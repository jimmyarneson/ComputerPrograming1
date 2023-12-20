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
		@textBox1 = System::Windows::Forms::TextBox.new()
		@textBox2 = System::Windows::Forms::TextBox.new()
		@label1 = System::Windows::Forms::Label.new()
		@button1 = System::Windows::Forms::Button.new()
		@button2 = System::Windows::Forms::Button.new()
		@button3 = System::Windows::Forms::Button.new()
		@textBox3 = System::Windows::Forms::TextBox.new()
		self.SuspendLayout()
		# 
		# textBox1
		# 
		@textBox1.Location = System::Drawing::Point.new(113, 15)
		@textBox1.Name = "textBox1"
		@textBox1.Size = System::Drawing::Size.new(326, 20)
		@textBox1.TabIndex = 1
		# 
		# textBox2
		# 
		@textBox2.Location = System::Drawing::Point.new(113, 41)
		@textBox2.Name = "textBox2"
		@textBox2.Size = System::Drawing::Size.new(326, 20)
		@textBox2.TabIndex = 3
		# 
		# label1
		# 
		@label1.BackColor = System::Drawing::Color.Cornsilk
		@label1.Font = System::Drawing::Font.new("Microsoft Sans Serif", 14.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label1.ForeColor = System::Drawing::Color.CornflowerBlue
		@label1.Location = System::Drawing::Point.new(12, 10)
		@label1.Name = "label1"
		@label1.Size = System::Drawing::Size.new(95, 57)
		@label1.TabIndex = 4
		@label1.Text = "Input    Output"
		# 
		# button1
		# 
		@button1.BackColor = System::Drawing::Color.Coral
		@button1.Font = System::Drawing::Font.new("Microsoft Sans Serif", 14.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button1.ForeColor = System::Drawing::Color.CornflowerBlue
		@button1.Location = System::Drawing::Point.new(12, 142)
		@button1.Name = "button1"
		@button1.Size = System::Drawing::Size.new(104, 52)
		@button1.TabIndex = 5
		@button1.Text = "Calculate"
		@button1.UseVisualStyleBackColor = false
		@button1.Click { |sender, e| self.Button1Click(sender, e) }
		# 
		# button2
		# 
		@button2.BackColor = System::Drawing::Color.Coral
		@button2.Font = System::Drawing::Font.new("Microsoft Sans Serif", 14.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button2.ForeColor = System::Drawing::Color.CornflowerBlue
		@button2.Location = System::Drawing::Point.new(195, 144)
		@button2.Name = "button2"
		@button2.Size = System::Drawing::Size.new(104, 52)
		@button2.TabIndex = 6
		@button2.Text = "Clear"
		@button2.UseVisualStyleBackColor = false
		@button2.Click { |sender, e| self.Button2Click(sender, e) }
		# 
		# button3
		# 
		@button3.BackColor = System::Drawing::Color.Coral
		@button3.Font = System::Drawing::Font.new("Microsoft Sans Serif", 14.25, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button3.ForeColor = System::Drawing::Color.CornflowerBlue
		@button3.Location = System::Drawing::Point.new(379, 144)
		@button3.Name = "button3"
		@button3.Size = System::Drawing::Size.new(104, 52)
		@button3.TabIndex = 7
		@button3.Text = "Exit"
		@button3.UseVisualStyleBackColor = false
		@button3.Click { |sender, e| self.Button3Click(sender, e) }
		# 
		# textBox3
		# 
		@textBox3.Location = System::Drawing::Point.new(113, 68)
		@textBox3.Name = "textBox3"
		@textBox3.Size = System::Drawing::Size.new(326, 20)
		@textBox3.TabIndex = 8
		# 
		# MainForm
		# 
		self.BackColor = System::Drawing::SystemColors.ControlLight
		self.ClientSize = System::Drawing::Size.new(495, 218)
		self.Controls.Add(@textBox3)
		self.Controls.Add(@button3)
		self.Controls.Add(@button2)
		self.Controls.Add(@button1)
		self.Controls.Add(@label1)
		self.Controls.Add(@textBox2)
		self.Controls.Add(@textBox1)
		self.Name = "MainForm"
		self.Text = "lang58b"
		self.Load { |sender, e| self.MainFormLoad(sender, e) }
		self.ResumeLayout(false)
		self.PerformLayout()
	end

	def MainFormLoad(sender, e)
		
	end

	def Label1Click(sender, e)
		
	end

	def Button1Click(sender, e)
		a = int(texBox1.Text)
		b = int(textBox2.Text)
		c = int(textBox3.Text)
		posroot = -a + $mathsqrt(-b + 5**2 -4ac) / 2a
		negroot = a - $mathsqrt(-b	+ 1**2 -4ac) / 2a
	end

	def Button2Click(sender, e)
		
	end

	def Button3Click(sender, e)
		Application.Exit()
	end
end

