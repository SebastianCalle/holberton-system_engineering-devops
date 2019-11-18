#!/usr/bin/env ruby

str = ARGV[0]
str1 = str.scan(/^h.n$/).join
puts str1
