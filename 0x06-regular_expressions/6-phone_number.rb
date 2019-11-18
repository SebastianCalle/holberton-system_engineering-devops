#!/usr/bin/env ruby

str = ARGV[0]
str1 = str.scan(/^\d{10}/).join
puts str1
