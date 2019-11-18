#!/usr/bin/env ruby

str = ARGV[0]
str1 = str.scan(/[A-Z]/).join
puts str1
