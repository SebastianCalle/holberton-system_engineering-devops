#!/usr/bin/env ruby

str = ARGV[0]
sender = str.scan(/\[from:(.?\w+)/).join
reciver = str.scan(/\[to:(\+?\d+)/).join
flags = str.scan(/\[flags:(.?\d:.?\d:.?\d:.?\d:.?\d)/).join
puts "#{sender},#{reciver},#{flags}"
