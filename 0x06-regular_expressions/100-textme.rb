#!/usr/bin/env ruby

def extract_message_info(log_line)
	sender = log_line.match(/\[from:([^[\]]+)\]/)[1]
	receiver = log_line.match(/\[to:([^[\]]+)\]/)[1]
	flags = log_line.match(/\[flags:([^[\]]+)\]/)[1]

	"#{sender},#{receiver},#{flags}"
end

if ARGV.empty?
	puts "Usage: #{$PROGRAM_NAME} 'log_line'"
	exit
end

log_line = ARGV[0]
message_info = extract_message_info(log_line)
puts message_info
