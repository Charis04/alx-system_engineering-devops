#!/usr/bin/env ruby

log_line = ARGV[0]
matches = log_line.scan(/\[from:([^[\]]+)\] \[to:([^[\]]+)\] \[flags:([^[\]]+)\]/)

sender = matches[0][0]
receiver = matches[0][1]
flags = matches[0][2]

puts "#{sender},#{receiver},#{flags}"
