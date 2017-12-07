module Support
=begin
  support.rb - Ruby/GTK Dreamlinux Commons module.

  Copyright (c) 2007 Nelson Gomes da Silveira (nelsongs) <ngsilveira@gmail.com>
  This program is licenced under lgpl licence.

  $Id: support.rb, v 1.0 2007/01/04 07:15 nelsongs Exp $
  Last update: 2007/03/02
  Changes:
  2007/02/16, 15:30 => added fourth parameter to msgwin to allow closing the parent window together
  2007/03/02, 07:10 => added class BasicWindow, by mutoh
=end

# Define a generic Button Class to be be used throughout the application
# This StockButton portion code slightly modified from Benedikt Meurer's original one
# Added possibility to alig label both horizontally and vertically. Addition by nelsongs
class StockButton < Gtk::Button
    def initialize(text = nil, stock = nil, textalign = :horiz)
        super()
        align = Gtk::Alignment.new(0.5, 0.5, 0, 0)
        add align
        textalign == :horiz ? box = Gtk::HBox.new(false, 0) : box = Gtk::VBox.new(false, 0)
        align.add box
        @widget_image = Gtk::Image.new(stock, Gtk::IconSize::BUTTON)
        box.pack_start(@widget_image, false, false, 2)
        @widget_label = Gtk::Label.new(text)
        @widget_label.show
        box.pack_start(@widget_label, false, false, 2)
    end
private
    @widget_image
    @widget_label
end

# This class BasicWindow by mutoh
class BasicWindow < Gtk::Window
	def initialize(title = nil)
		super(Gtk::Window::TOPLEVEL)
		
		if title
			set_title("#{title}")
		end

		signal_connect("key_press_event") do |widget, event|
			if event.state.control_mask? and event.keyval == Gdk::Keyval::GDK_q
				destroy
				true
			else
				false
			end
		end

		signal_connect("delete_event") do |widget, event|
			quit
		end
	end

	def quit
		destroy
		true
	end
end

# by nelsongs. ProtoPage is a general class for defining a "windows" dialog
class ProtoPage < Gtk::Window
attr_accessor :label, :border_width
	
	def initialize(title)
		super
		title = title
		set_border_width(10)
		@table = Gtk::Table.new(3, 1, false)
		@hbox = Gtk::HBox.new(false, 5)
		@vbox = Gtk::VBox.new(false, 0)
		@frame = Gtk::Frame.new
		@table2 = Gtk::Table.new(1, 3, true)
		@label = Gtk::Label.new
		add(@table)
	end

	def table_resize(rows, cols)
		@table.resize(rows, cols)
	end
	
	def set_image(image)
		@image = Gtk::Image.new(image)
	end
	
	def set_table(button)
	end
	
end # class ProtoPage

#by nelsongs. Progress window
def progress_window(image, title, msg)
	progwin = Gtk::Window.new(title)
	progwin.set_border_width(10)
	progwin.destroy_with_parent = true
	table = Gtk::Table.new(3, 1)
	image = Gtk::Image.new(image)
	label = Gtk::Label.new(msg)
	table.attach_defaults(image, 0, 1, 0, 1)
	table.attach_defaults(label, 0, 1, 1, 2)
	@pbar = Gtk::ProgressBar.new
	show_progress = lambda do
		new_val = @pbar.pulse_step + 0.05
		new_val = 0.0 if new_val > 1.0
		@pbar.pulse_step = new_val
		@pbar.pulse
	end
	frame = Gtk::Frame.new
	frame.add(@pbar)
	table.attach_defaults(frame, 0, 1, 2, 3)
	progwin.add(table)
	closewin = lambda {progwin.destroy}
	while ! @finished
		@pbar.pulse
		show_progress.call
		progwin.show_all
	end
	progwin.signal_connect('destroy') {progwin.destroy}
	closewin.call
end

#by nelsongs. Progress window
def wait_window(image, title, msg)
	waitwin = Gtk::Window.new(title)
	waitwin.set_border_width(10)
	waitwin.destroy_with_parent = true
	table = Gtk::Table.new(2, 1)
	image = Gtk::Image.new(image)
	label = Gtk::Label.new(msg)
	frame = Gtk::Frame.new
	frame.add(label)
	table.attach_defaults(image, 0, 1, 0, 1)
	table.attach_defaults(frame, 0, 1, 1, 2)
	closewin = lambda {waitwin.destroy}
	waitwin.add(table)
	while ! @finished
		waitwin.show_all
	end
	waitwin.signal_connect('destroy') {waitwin.destroy}
	closewin.call
end

#by nelsongs. class MessageWindow used for simple, informative dialogs
class MsgWindow < ProtoPage
	attr_accessor :labelmsg
	
	def initialize(title)
		super
		@labelmsg = Gtk::Label.new
	end
	
	def set_table(button)
		@hbox.pack_start(@image) if @image != nil
		@hbox.pack_start(@label) if @label.text != ""
		@table.attach_defaults(@hbox, 0, 1, 0, 1)
		@frame.add(@labelmsg) if @labelmsg != nil
		@table.attach_defaults(@frame, 0, 1, 1, 2)
		@table2.attach_defaults(button, 1, 2, 0, 1)
		@table.attach(@table2, 0, 1, 2, 3, xopt = Gtk::EXPAND|Gtk::FILL, yopt = Gtk::EXPAND|Gtk::FILL, xpad = 0, ypad = 5)
	end
end # class MessageWindow

#by nelsongs. Ready-made message dialog box.
def msgwin(image, title, msg, window = nil)
	winmsg = MsgWindow.new(title)
	winmsg.destroy_with_parent = true
	winmsg.set_image(image)
	winmsg.labelmsg.text = msg 
	msgbutton = StockButton.new("Ok", Gtk::Stock::OK)
	winmsg.set_table(msgbutton)
	winmsg.show_all
	msgbutton.signal_connect('clicked') do
		if window != nil
			window.destroy
		else
			winmsg.destroy
		end
	end
	winmsg.signal_connect('destroy') {winmsg.destroy}
end

#by nelsongs. class InputWindow used for entering data
class InputWindow < ProtoPage
	attr_accessor :labelmsg, :entry
	
	def initialize(title)
		super
		@labelmsg = Gtk::Label.new
		@entry = Gtk::Entry.new
	end
	
	def set_table(button)
		@hbox.pack_start(@image) if @image != nil
		@hbox.pack_start(@label) if @label.text != ""
		@table.attach_defaults(@hbox, 0, 1, 0, 1)
		@vbox.pack_start(@labelmsg)
		@vbox.pack_start(@entry)
		@frame.add(@vbox) 
		@table.attach_defaults(@frame, 0, 1, 1, 2)
		@table2.attach_defaults(button, 1, 2, 0, 1)
		@table.attach(@table2, 0, 1, 2, 3, xopt = Gtk::EXPAND|Gtk::FILL, yopt = Gtk::EXPAND|Gtk::FILL, xpad = 0, ypad = 5)
	end
end # class InputWindow
	
#by nelsongs. class OptionWindow used for radio buttons optioned windows.
class OptionWindow < ProtoPage
	def initialize(title)
		super
		@rb = Array.new
		@count = Array.new
		@count << 0
		@rb[0] = Gtk::RadioButton.new
		@group = @rb[0]
	end
	
	def set_rbuttons(rb, text)
		@count << rb
		@rb[rb] = Gtk::RadioButton.new(@group, text)
	end
	
	def set_table(button, lin1type)
		table_resize(4, 1)
		if lin1type == :horizontal
			@hbox.pack_start(@image) if @image != nil
			@hbox.pack_start(@label) if @label.text != ""
			@table.attach_defaults(@hbox, 0, 1, 0, 1) # lin 1
		elsif lin1type == :vertical
			vbox2 = Gtk::VBox.new(false, 5)
			vbox2.pack_start(@image) if @image != nil
			vbox2.pack_start(@label) if @label.text != ""
			@table.attach_defaults(vbox2, 0, 1, 0, 1) # lin 1
		end
		i = 1
		for i in @count
			@vbox.pack_start(@rb[i]) if i > 0
			i += 1
		end
		@frame.add(@vbox)
		@table.attach_defaults(@frame, 0, 1, 2, 3) # lin2
		
		@table2.attach_defaults(button, 1, 2, 0, 1)
		@table.attach(@table2, 0, 1, 3, 4, xopt = Gtk::EXPAND|Gtk::FILL, yopt = Gtk::EXPAND|Gtk::FILL, xpad = 0, ypad = 5) # lin 3
	end
	
	def button_action 
		i = 1
		for i in @count
			if @rb[i].active?
				return "active#{i.to_s}"
			end
			i += 1
		end
	end
end # class OptionWindow

class EntryOptWin < OptionWindow
	attr_reader :entrylabel
	def initialize(title)
		super
		@entry = Gtk::Entry.new
		@entrylabel = Gtk::Label.new
	end
		
	def entry_text
		@entry.text
	end
		
	def set_table(button, lin1type)
		table_resize(4, 1)
		
		if lin1type == :horizontal
			@hbox.pack_start(@image) if @image != nil
			@hbox.pack_start(@label) if @label.text != ""
			@table.attach_defaults(@hbox, 0, 1, 0, 1) # lin 1
		elsif lin1type == :vertical
			vbox2 = Gtk::VBox.new
			vbox2.pack_start(@image) if @image != nil
			vbox2.pack_start(@label) if @label != nil
			@table.attach_defaults(vbox2, 0, 1, 0, 1) # lin 1
		end
		
		vbox3 = Gtk::VBox.new
		vbox3.pack_start(@entrylabel.set_alignment(0, 1))
		vbox3.pack_start(@entry)
		@table.attach_defaults(vbox3, 0, 1, 1, 2)
		
		i = 1
		for i in @count
			@vbox.pack_start(@rb[i]) if i > 0
			i += 1
		end
		@frame.add(@vbox)
		@table.attach_defaults(@frame, 0, 1, 2, 3)
		
		@table2.attach_defaults(button, 1, 2, 0, 1)
		@table.attach(@table2, 0, 1, 3, 4, xopt = Gtk::EXPAND|Gtk::FILL, yopt = Gtk::EXPAND|Gtk::FILL, xpad = 0, ypad = 5)
	end 
end # class EntryOptWin

class EntryOptWin2Col < OptionWindow
	attr_accessor :entry1label, :entry2label, :optgrp1label, :optgrp2label, :entry1, :entry2
	
	def initialize(title)
		super
		@entry1= Gtk::Entry.new 
		@entry2 = Gtk::Entry.new
		@entry1label = Gtk::Label.new
		@entry2label = Gtk::Label.new
		@optgrp1label = Gtk::Label.new
		@optgrp2label = Gtk::Label.new
		@rb2 = Array.new
		@count2 = Array.new
		@count2 << 0
		@rb2[0] = Gtk::RadioButton.new
		@group2 = @rb2[0]
	end
	
	def set_rbuttons2(rb, text)
		@count2 << rb
		@rb2[rb] = Gtk::RadioButton.new(@group2, text)
	end
		
	def set_table(cancelbutton, okbutton)
		vbox2 = Gtk::VBox.new
		vbox2.pack_start(@image) if @image != nil
		vbox2.pack_start(@label) if @label != nil
		@table.attach_defaults(vbox2, 0, 1, 0, 1) # lin1
		@table.set_row_spacing(1, 15)
		
		hbox2 = Gtk::HBox.new(true, 5)
		vbox3 = Gtk::VBox.new
		vbox4 = Gtk::VBox.new
		vbox3.pack_start(@entry1label.set_alignment(0, 1))
		vbox3.pack_start(@entry1)
		vbox4.pack_start(@entry2label.set_alignment(0, 1))
		vbox4.pack_start(@entry2)
		hbox2.pack_start(vbox3)
		hbox2.pack_start(vbox4)
		@table.attach_defaults(hbox2, 0, 1, 1, 2) # lin2
		@table.set_row_spacing(2, 10)
		
		vbox5 = Gtk::VBox.new
		vbox5.pack_start(@optgrp1label.set_alignment(0, 1))
		i = 1
		for i in @count
			@vbox.pack_start(@rb[i]) if i > 0
			i += 1
		end
		@frame.add(@vbox)
		vbox5.pack_start(@frame)
	
		vbox6 = Gtk::VBox.new
		vbox7 = Gtk::VBox.new
		vbox6.pack_start(@optgrp2label.set_alignment(0, 1))
		i = 1
		for i in @count2
			vbox7.pack_start(@rb2[i]) if i > 0
			i += 1
		end
		frame2 = Gtk::Frame.new
		frame2.add(vbox7)
		vbox6.pack_start(frame2)
		hbox3 = Gtk::HBox.new(true, 5)
		hbox3.pack_start(vbox5)
		hbox3.pack_start(vbox6)
		@table.attach_defaults(hbox3, 0, 1, 2, 3) # lin3
		
		@table2.attach_defaults(cancelbutton, 0, 1, 0, 1)
		@table2.attach_defaults(okbutton, 2, 3, 0, 1)
		@table.attach(@table2, 0, 2, 3, 4, xopt = Gtk::EXPAND|Gtk::FILL, yopt = Gtk::EXPAND|Gtk::FILL, xpad = 0, ypad = 5) # lin4
	end 
end # class EntryOptWin2Col

end # module Support